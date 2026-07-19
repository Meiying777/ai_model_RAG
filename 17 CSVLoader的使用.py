from langchain_community.document_loaders import CSVLoader


loader = CSVLoader(
    file_path="人员信息.csv",
    encoding="utf-8-sig",
    csv_args={
        "delimiter": ",",  # 指定分隔符
        "quotechar": "“",  # 指定带有分隔符文本的引号是单引号还是双引号
        # "fieldname":[]   # 如果没有表头可以使用fieldname指定表头名称
         }
    )

# 批量加载.load()  -> [documents,documents,………………]
documents = loader.load()
print(documents)

# 懒加载.lazy_load()  迭代器[documents]
for document in loader.lazy_load():
    print(document)