"""
通过|链接提示词模板对象和模型对象
返回值chain对象是RunnableSerializable对象
·是Runnable接口的直接子类
·也是绝大多数组件的父类
·通过invoke或stream进行阻塞执行或流式执行
组成的链在执行上有：上一个组件的输出作为下一个组件
的输入的特性。
"""
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
chat_prompt_template = ChatPromptTemplate.from_messages(
    [
            ("system","你是一个边塞诗人,可以作诗。"),
            MessagesPlaceholder("history"),
            ("human","请再来一首唐诗"),
    ]
)

history_data=[
        ("human","你来写一个唐诗"),
        ("ai","床前明月光,疑是地上霜,举头望明月,低头思故乡"),
        ("human","好诗再来一个"),
        ("ai","锄禾日当午,汗滴禾下锄,谁知盘中餐,粒粒皆辛苦"),
    ]


# 正常方法
# prompt_value = chat_prompt_template.invoke({'history': history_data}).to_string()
# print(prompt_value)

model = ChatTongyi(model='qwen-max')

# chain方法
chain = chat_prompt_template| model

# 通过调用链去调用invoke|stream
res = chain.invoke({'history':history_data})
print(res.content)

