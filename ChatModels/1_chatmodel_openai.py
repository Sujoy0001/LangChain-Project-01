from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

while True:
    question =  input("Enter your questions: ")
    if question.lower() in ['exit', 'quit']:
        break
    result = model.invoke(question)

    print(result.content)