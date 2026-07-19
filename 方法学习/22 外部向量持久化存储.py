from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_chroma import Chroma
# Chroma 向量数据库

vectorstore = Chroma(
    collection_name='test',   # 将存储起名
    embedding_function=DashScopeEmbeddings(),    #  嵌入模型
    persist_directory='data/chroma_db'         #  指定存储文件夹
)

loader = CSVLoader(
    file_path='data/info.csv',
    encoding='utf-8',
    source_column ='source',  # 指定本条数据来源
)

documents = loader.load()

# 向量存储的新增，删除，检索
# 添加
vectorstore.add_documents(
    documents=documents,  # 被添加的文件，类型：list[Document]
    ids=['id'+ str(i) for i in range(1,len(documents)+1)]    #给添加的文档提供id（字符串） list[str]
)

# 删除 传入[id,id,……………]
vectorstore.delete(['id1','id2'])

# 检索
result =vectorstore.similarity_search(
    '学python是不是很简单呀。',   # 检索内容
    3                             # 检索的结果要几个
)

print(result)