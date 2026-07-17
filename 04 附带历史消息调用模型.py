from openai import OpenAI
# 获取Clint对象，获取openai对象

client = OpenAI(
    base_url='https://ws-75hdpe2iqisptozw.cn-beijing.maas.aliyuncs.com/compatible-mode/v1'
)

response = client.chat.completions.create(
    model='qwen3.7-plus',
    messages=[
        {'role':'system','content':'你是一个AI助手，回答很简洁'},
        {'role':'assistant','content':'好的，我是AI助手，需要什么帮助？'},
        {'role':'user','content':'小红有2条狗'},
        {'role':'assistant','content':'好的'},
        {'role':'user','content':'小红又养了5条狗'},
        {'role':'assistant','content':'好的'},
        {'role':'user','content':'小红总共养了几条狗？'}
    ],
    stream=True
)
# 调用模型

# 处理结果
# print(response.choices[0].message.content)

for chunk in response:
        # 先判断choices是否存在且不为空
    if chunk.choices and len(chunk.choices) > 0:
        delta = chunk.choices[0].delta
            # 再判断content不为空再打印
        if delta.content:
            print(delta.content, end='', flush=True)
print("\n")

