from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model='qwen-max')

prompt_tem = PromptTemplate.from_template(
    "我喜欢吃{fruit},我还喜欢吃{vegetable},你喜欢吃什么？"
)

# # 调用.format方法注入信息
# prompt_text = prompt_tem.format(fruit='西瓜',vegetable='白菜')
#
# res = model.invoke(input=prompt_text)
#
# print(res)

# 构建执行链条
chain = prompt_tem | model
res1 = chain.invoke(input={'fruit':'西瓜','vegetable':'白菜'})
print(res1)