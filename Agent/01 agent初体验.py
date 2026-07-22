from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool
# 创建工具
@tool(description='查询天气')
def get_weather() -> str:
    return '晴天'

# 创建智能体
agent = create_agent(
    model=ChatTongyi(model='qwen-max'),   # 大语言模型
    tools=[get_weather],                  # 提供工具
    system_prompt = '你是一个聊天助手，可以回答用户提出的问题。'  # 用户提问
)

res = agent.invoke(
    {
        'messages':[
            {'role':'user','content':'明天昆明的天气怎么样？'}
        ]
    }
)

for message in res['messages']:
    print(type(message).__name__,message.content)