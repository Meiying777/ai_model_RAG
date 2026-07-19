"""
StroutputParser是LangChain内置的简单字符串解析器。
.
可以将AIMessage类型转换为基础字符串
.
可以加入chain作为组件存在（Runnable接口子类）
"""


from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import PromptTemplate
model = ChatTongyi(model='qwen-max')

prompt = PromptTemplate.from_template(
    '我叫{name}，我喜欢{hobby},请问你的名字和爱好是什么？'
)

# chain = prompt | model
# res = chain.invoke({'name':'林俊杰','hobby':'钓鱼'})
# print(res)

parser = StrOutputParser()
chain = prompt | model | parser | model
res1 = chain.invoke({'name':'周杰伦','hobby':'唱歌'})
print(res1.content)
