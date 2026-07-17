from openai import OpenAI
# 获取Clint对象，获取openai对象

client = OpenAI(
    base_url='https://ws-75hdpe2iqisptozw.cn-beijing.maas.aliyuncs.com/compatible-mode/v1'
)

# 调用模型
response = client.chat.completions.create(
    model='qwen3.7-plus',
    messages=[
        {'role':'system','content':'你是一个python专家，并且喜欢说话。'},
        {'role':'assistant','content':'好的，我是编程专家，并且喜欢说话，你要问什么？'},
        {'role':'user','content':'输出1-10的数字，使用python代码'}
    ],
    stream=True
)

# 处理结果
# print(response.choices[0].message.content)

for chunk in response:
    print(
        chunk.choices[0].delta.content,
        end='',  # 每一段之间用空格分隔
        flush=True  # 立即刷新缓冲区
    )

