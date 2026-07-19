from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.prompts import PromptTemplate

str_parser = StrOutputParser()
json_parser = JsonOutputParser()

model = ChatTongyi(model='qwen-max')

first_prompt = PromptTemplate.from_template(
    "我的邻居姓{name},他刚生了个{gender},请帮忙取个名字，你只需要将名字并封装为json模式输出给我，"
    "要求key为name，value就是你起的名字."
)


second_prompt = PromptTemplate.from_template(
    '姓名是:{name},请帮我解析下名字含义'
)


# 构建chain
chain = first_prompt|model|json_parser|second_prompt|model|str_parser

# res = chain.invoke({'name':'张','gender':'女孩'})
# print(res.content)

for chunk in chain.stream({'name':'张','gender':'女孩'}):
    print(chunk,end='',flush=True)