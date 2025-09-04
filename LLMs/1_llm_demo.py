from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables (make sure GOOGLE_API_KEY is in your .env)
load_dotenv()

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

while True:
    question =  input("Enter your questions: ")
    if question.lower() in ['exit', 'quit']:
        break
    result = llm.invoke(question)

    print(result.content)
