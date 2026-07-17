from langchain_ollama import OllamaLLM

model =OllamaLLM(model='qwen3.5:4b')
res = model.invoke(input='你是谁？你可以干什么，给我一个简短的回答。')
print(res)
