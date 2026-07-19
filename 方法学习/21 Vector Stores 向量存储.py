"""
Langchain内提供向量存储功能，可以基于：
。
InMemoryvectorStore，完成内存向量存储
Chroma，外部数据库向量存储
向量存储类均提供3个通用API接口：
。
add_document，添加文档到向量存储
.
delete，从向量存储中删除文档
·
similarity_search:相似度搜索
"""
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

vectorstore = InMemoryVectorStore(
    embedding=DashScopeEmbeddings(),
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