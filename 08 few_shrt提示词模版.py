from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model='qwen-max')

# 示例模版
example_prompt = PromptTemplate.from_template('单词:{word},反义词:{anto}')

# 示例的动态数据注入，list套dict
example_data = [
    {'word':'上','anto':'下'},
    {'word':'黑','anto':'白'},
    {'word':'凸','anto':'凹'},
]


few_shot_temp = FewShotPromptTemplate(
    example_prompt=example_prompt, # 实例模版
    examples = example_data,     # 示例数据（用来注入动态数据），list内套字典
    prefix = '告知我单词的反义词，我提供以下示例：',       # 示例之前的提示词
    suffix = '基于前面的示例告诉我，单词{input_word}的反义词是：',       # 示例之后的提示词
    input_variables=['input_word']   # 声明在前缀或后缀中所需要注入的变量名
)

prmt_text = few_shot_temp.invoke(input={'input_word':'笑'}).to_string()
print(prmt_text)

print(model.invoke(input=prmt_text))