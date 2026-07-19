from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader('../data/Python基础语法.txt', encoding='utf-8')

docus = loader.load()
# print(docus)
# print(len(docus))

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,    # 分段的最大字符数
    chunk_overlap=50,  # 分段之间允许重叠的字符数
    separators=['\n\n','\n','。','！','？','.','!','?',' ',''],  # 文本自然分段的依据符号
    length_function=len # 统计字符的依据函数
)

split_docs = splitter.split_documents(docus)
print(len(split_docs))
for i in split_docs:
    print('='*20)
    print(i)
    print('='*20)