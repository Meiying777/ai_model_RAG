"""
RunnablewithMessageHistory是LangChain内Runnable接
口的实现，主要用于：
.
创建一个带有历史记忆功能的Runnable实例（链）
它在创建的时候需要提供一个BaseChatMessageHistory的具体
实现（用来存储历史消息）
.
InMemoryChatMessageHistory可以实现在内存中存储历史
额外的，如果想要在invoke或stream执行链的同时，将提示词
print出来，可以在链中加入自定义函数实现。
。
注意：函数的输入应原封不动返回出去，避免破坏原有业务，
仅在return之前，print所需信息即可。
"""


from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model = ChatTongyi(model='qwen-max')
prompt = PromptTemplate.from_template(
    '你需要根据回话历史回复用户问题，对话历史为:{chat_message},用户提问为:{input},请回答。'
)

str_parser = StrOutputParser()
base_chain = prompt|model|str_parser

# 通过实现会话id获取InMemoryChatMessageHistory类对象
story = {}  # Key为session Id，value就是InMemoryChatMessageHistory类对象
def get_history(session_id):
    if session_id not in story:
        story[session_id] = InMemoryChatMessageHistory()

    return story[session_id]
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
    res = con_chain.invoke({'input':"小明有两只猫。"},session_config)
    print("第一次执行：",res)
    res = con_chain.invoke({'input': "小刚有3只狗。"}, session_config)
    print("第二次执行：", res)
    res = con_chain.invoke({'input': "总共有几只宠物？"}, session_config)
    print("第三次执行：", res)
