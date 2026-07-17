from langchain_community.embeddings import DashScopeEmbeddings


# 创建模型对象，默认使用text-embddings-v1模型
model = DashScopeEmbeddings()

# 不用invoke，stream
# embred_query,embed_documents
print(model.embed_query('我喜欢你'))  # 单个字符串
print(model.embed_documents(['我喜欢你','我爱你','我讨厌你'])) # 多个数据

