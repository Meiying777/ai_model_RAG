from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

model = ChatTongyi(model='qwen-max')

message = [

    SystemMessage(content='你是一名边塞诗人。'),
    AIMessage(content='你需要写一首边塞诗出来')
]
"""
   简写版
   ('system','你是一名边塞诗人'),
   ('ai','你需要写一首边塞诗出来')
   """
# 调用stream流式输出
res = model.stream(input=message)

# for循环迭代打印，通过,content来获取到内容
for chunk in res:
    print(chunk.content,end='',flush=True)