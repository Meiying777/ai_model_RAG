from openai import OpenAI
import os
from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate,ChatPromptTemplate
"""
PromptTemplate：通用提示词模板，支持动态注入信息。
FewShotPromptTemplate：支持基于模板注入任意数量的示例信息。
ChatPromptTemplate：支持注入任意数量的历史会话信息。
"""
client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    base_url="https://ws-75hdpe2iqisptozw.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)

messages = [{"role": "user", "content": "你可以做什么"}]
completion = client.chat.completions.create(
    model="qwen3.7-plus",  # 您可以按需更换为其它深度思考模型
    messages=messages,
    extra_body={"enable_thinking": True},
    stream=True
)
is_answering = False  # 是否进入回复阶段
print("\n" + "=" * 20 + "思考过程" + "=" * 20)
for chunk in completion:
    if not chunk.choices:
        continue
    delta = chunk.choices[0].delta
    if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None:
        if not is_answering:
            print(delta.reasoning_content, end="", flush=True)
    if hasattr(delta, "content") and delta.content:
        if not is_answering:
            print("\n" + "=" * 20 + "完整回复" + "=" * 20)
            is_answering = True
        print(delta.content, end="", flush=True)