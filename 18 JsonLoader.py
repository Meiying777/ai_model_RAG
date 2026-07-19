from langchain_community.document_loaders import JSONLoader
"""
.表示整个JSON对象（根）
[门表示数组
.name表示抽取key为name
.hobby表示抽取key为hobby
.hobby[1]或.hobby.[1]表示抽取跳
.other.addr表示抽取key为other下的字典内容key为addr
.[].得到全部字典内容
.[].name得到字典内全部key为name的值
"""
"""
JSoNLoader初始化有4个主要参数：
file_path：文件路径，必填
jq_schema：jq解析语法，必填
text_content：抽取到的是否是字符串，默认True，非必填
json_lines：是否是JsonLines文件，默认False，非必填
·JsonLines文件：每一行都是一个独立的字典（Json对象）
"""
loader = JSONLoader(
    file_path='data/stu_json_lines.json',  # 文件路径
    jq_schema='.',              # （必填）jq schema语法
    text_content=False,         # 告知jsonloader，内容是否为字符串
    json_lines=True,           # 告知jsonloader，内容是否为json_lines
)

document = loader.load()
print(document)