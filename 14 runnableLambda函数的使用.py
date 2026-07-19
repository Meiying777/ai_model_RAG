from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

str_parser = StrOutputParser()
json_parser = JsonOutputParser()

model = ChatTongyi(model='qwen-max')

first_prompt = PromptTemplate.from_template(
    "我的邻居姓{name},他刚生了个{gender},请帮忙取个名字，仅告诉我名字不要额外信息。"
)


second_prompt = PromptTemplate.from_template(
    '姓名是:{name},请帮我解析下名字含义'
)

# 函数的入参 ： AImessage ->dict ({'name':'   '})
my_func = RunnableLambda(lambda ai_msg:{'name':ai_msg.content})

chain = first_prompt|model|my_func|second_prompt|model|str_parser

for chunk in chain.stream({'name':'李','gender':'男孩'}):
    print(chunk,end='',flush=True)