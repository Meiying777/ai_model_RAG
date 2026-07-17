from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate,ChatPromptTemplate


template = PromptTemplate.from_template('我的名字是:{name},最喜欢{hobby}')
res = template.format(name='林俊杰',hobby='钓鱼')
print(res,type(res)) # format方法本质是进行纯字符串替换{}占位符

res1 = template.invoke({'name':'周杰伦','hobby':'唱歌'})
print(res1,type(res1)) # invoke方法是返回一个类对象