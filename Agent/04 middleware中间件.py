from langchain.agents import create_agent, AgentState
from langgraph.runtime import Runtime
from langchain.agents.middleware import before_agent, after_agent, before_model, wrap_model_call, wrap_tool_call, \
    after_model
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool
# 创建工具
@tool(description='查询天气,传入城市名称字符串，返回天气字符串')
def get_weather(city:str) -> str:
    return f'{city}天气：晴天'

"""
1.agent执行前
2.model执行前
3.tool执行时
4.模型调用中
5.model执行后
6.agent执行后
"""

@before_agent
def log_before_agent(state:AgentState,runtime:Runtime) -> None:
    # agent执行前会调用函数并传入state和runtime两个对象
    print(f'[before agent]agent启动，并附带{len(state['messages'])}消息')

@after_agent
def log_after_agent(state:AgentState,runtime:Runtime) ->None:
    print(f'[after agent]agent结束，并附带{len(state['messages'])}消息')

@before_model
def log_before_model(state:AgentState,runtime:Runtime) ->None:
    print(f'[before model]model开始，并附带{len(state['messages'])}消息')

@after_model
def log_after_model(state:AgentState,runtime:Runtime) ->None:
    print(f'[after model]model结束，并附带{len(state['messages'])}消息')

# 模型调用中
@wrap_model_call
def model_call_hook(request,handler):
    print('模型正在调用中')
    return handler(request)

# 工具调用中
@wrap_tool_call
def toll_call_hook(request,handler):
    print(f'工具正在调用中:{request.tool_call["name"]}')
    print(f'工具执行传入参数:{request.tool_call["args"]}')
    return handler(request)

agent = create_agent(
    model=ChatTongyi(model='qwen-max'),
    tools=[get_weather],
    middleware=[log_before_agent,log_after_agent,log_before_model,log_after_model,toll_call_hook,model_call_hook],
    system_prompt= '你是一个智能助手，可以回答用户提出的问题。'
)

res  = agent.invoke({'messages':[
    {
        'role':'user','content':'今天昆明的天气如何，出门穿什么衣服'
    }
]})
print('**********\n',res)
