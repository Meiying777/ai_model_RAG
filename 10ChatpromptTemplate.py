from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi

model = ChatTongyi(model='qwen-max')


chat_compot = ChatPromptTemplate.from_messages(
    [
        ('system','你是一个生活小助手，可以给出生活小妙招'),
        MessagesPlaceholder('history'),
        ('ai','您好，我是您的生活小助手，你有什么需要吗？'),
        ('human','我不知道鸡蛋怎么煮，你可以给我提示吗？'),
    ]
)

history_data =  [
        ('human','土豆别名叫什么？'),
        ('ai','土豆的别名叫做马铃薯。'),
        ('human','茄子可以怎么吃？'),
        ('ai','茄子可以蒸，可以煮，可以炒，可以烤。'),
]

# 将history注入到MessagePlaceholder里面
# 需要用to_string()转换为字符串
chat_text = chat_compot.invoke({'history':history_data}).to_string()
print(chat_text)

res = model.invoke(chat_text)
# 使用.content转换为纯字符串
print(res.content)