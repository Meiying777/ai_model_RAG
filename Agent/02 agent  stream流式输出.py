from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool
# 创建工具
@tool(description='金价查询')
def get_price() ->str:
    return '今天的金价是999元/g。'

# 创建智能体
agent = create_agent(
    model=ChatTongyi(model='qwen-max'),
    tools=[get_price],
    system_prompt= '你是一个智能助手，可以回答用户提出的问题。'
)

# 流式输出
for chunk in  agent.stream(
    {'messages':[
        {
            'role':'user','content':'我想买黄金，你查一下今天的金价告诉我合不合适买。'
        }
    ]},
    stream_mode='values'
):
    least_message = chunk['messages'][-1]
    if least_message.content:
        print(type(least_message).__name__, least_message.content)  # 如果有内容就让输出

    try:
        if least_message.tool_calls:
            print(f'工具调用:{ [tc['name']for tc in least_message.tool_calls]} ')
    except AttributeError as e:
        pass
