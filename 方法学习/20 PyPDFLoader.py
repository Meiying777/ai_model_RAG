"""
from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader(
file_path="",
#文件路径必填
mode='page'，#读取模式，可选page（按页面划分不同Document）和single（单个Document）
password='password'，#文件密码
"""

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path="data/pdf1.pdf",  # 文件路径
    mode='page',                # 默认page，每个页面形成一个Document对象
                                # single模式，不管有多少页都只返回一个Document对象
)
i = 0
for chunk in loader.lazy_load():
    i +=1
    print(chunk)
    print('='*30,f'当前打印的页码是第%d页'%i)