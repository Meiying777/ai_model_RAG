from langchain_community.llms.tongyi import Tongyi
import os
model = Tongyi(model='qwen-max')

# 流式输出Steam方法
res1 = model.stream(input='你是谁呀？')
for chunk in res1:
    print(chunk,end='',flush=True)
# res = model.invoke(input='你是谁呀？')
# print(res)


