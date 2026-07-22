"""
ReAct是一种工作范式，定义了大模型的工作流程。
思考：分析需求，考虑下一步
行动：工具调用获取信息
观察：分析获取的信息
思考→行动观察→思考>……结束
LangChain的Agent对象，就是按ReAct模式运行。
"""


from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool
# 创建工具
@tool(description='体重查询')
def get_weight() ->int :
    return 90

@tool(description='获取身高')
def get_heigth() -> int :
    return 170

# 创建智能体
agent = create_agent(
    model=ChatTongyi(model='qwen-max'),
    tools=[get_weight, get_heigth],
    system_prompt="""你是严格遵循ReAct框架的智能体，必须按「思考→行动一观察→再思考」的流程解决问题，
    且**每轮仅能思考并调用1个工具**，禁止单次调用多个工具。
    并告知我你的思考过程，工具的调用原因，按思考、行动、观察三个结构告知我"""
)

# 流式输出
for chunk in  agent.stream(
    {'messages':[
        {
            'role':'user','content':'计算一下我的BMI.'
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
