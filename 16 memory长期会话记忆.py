import os,json
from typing import Sequence
from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory
# message_to_dict:单个消息对象（BaseMessage类对象）-> 字典
# messages_from_dict :[字典，字典……]—>[消息，消息，…………]
# AIMessage,HumanMessage,SystemMessage都是BaseMessage的子类
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory

class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self,session_id,storage_path):
        self.session_id = session_id  # 会话ID
        self.storage_path = storage_path # 不同ID会话文件的存储位置
        # 完整的文件路径
        self.file_path = os.path.join(self.storage_path,self.session_id)
        # 确保文件路径存在
        os.makedirs(os.path.dirname(self.file_path),exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        # Sequence :序列 类似list
        all_message = list(self.messages) # 已有的消息列表
        all_message.extend(messages)    # 新的和已有的消息列表融合为一个list

        # 将数据同步写入到本地文件中
        # 类对象写入文件 -> 一堆二进制
        # 为了方便，可以将BaseMessage消息转为字典（借助json模块以json字符串写入文件）
        # 官方message_to_dict:单个消息转换为字典
        new_messages = []
        for message in all_message:
            d = message_to_dict(message)
            new_messages.append(d)

        # 将数据写入文件
        with open(self.file_path,'w') as f:
            json.dump(new_messages,f)

    @property   # 装饰器将messages方法变成成员属性使用
    def messages(self) -> list[BaseMessage]:
        # 当前文件内：list[字典]
            try:
                with open(self.file_path,'r') as f:
                    messsages_data = json.load(f)   # 返回值是：list[字典]
                    return messages_from_dict(messsages_data)
            except FileNotFoundError:
                return []


    def clear(self)->None:
        with open(self.file_path,'w') as f:
            json.dump([],f)




model = ChatTongyi(model='qwen-max')
prompt = PromptTemplate.from_template(
    '你需要根据回话历史回复用户问题，对话历史为:{chat_message},用户提问为:{input},请回答。'
)

str_parser = StrOutputParser()
base_chain = prompt|model|str_parser


def get_history(session_id):
    return FileChatMessageHistory(session_id,'./chat_history')
# 创建新的链，对原有链增强功能，自动附加历史消息
con_chain = RunnableWithMessageHistory(
    base_chain,  # 被增强的原有Chain
    get_history, # 通过会话id获取InMemoryChatMessageHistory
    input_messages_key='input',  # 表示用户输入在模版中的占位符
    history_messages_key='chat_message', # 表示对话历史在模版中的占位符
 )


if __name__ == '__main__':
    # 固定格式，添加Langchain的配置，为当前程序配置所属的session_id:
    session_config={
        "configurable":{
            "session_id":'user_001'
                        }
    }
    # res = con_chain.invoke({'input':"小明有两只猫。"},session_config)
    # print("第一次执行：",res)
    # res = con_chain.invoke({'input': "小刚有3只狗。"}, session_config)
    # print("第二次执行：", res)
    res = con_chain.invoke({'input': "总共有几只宠物？"}, session_config)
    print("第三次执行：", res)
