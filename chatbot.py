import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

api_key = os.getenv('GROQ_API_KEY')
chat = ChatGroq(model='llama-3.3-70b-versatile')
loader = WebBaseLoader('https://www.wikipedia.org')
documents_list = loader.load()

document = ''
for doc in documents_list:
  document += doc.page_content + '\n'

def append_message(role, content):
  messages.append((role, content))

def generate_response(user_input):
  template = ChatPromptTemplate.from_messages([
    ('system', 'You are a friendly helpful assistant called Chatty. You have access to the following information to provide answers: {documents}'),
    ('user', '{input}')
  ])
  chain = template | chat
  response = chain.invoke({'documents': document, 'input': user_input})
  return response.content

print('Welcome to the chatbot!')
print('Type "exit" or press "X" to end the conversation.\n')

messages = []

while True: 
  user_input = input('You: ')

  if user_input.lower() in ['exit', 'x']:
    print('Chatbot: Goodbye!\n')
    break
  
  append_message('user', user_input)
  response = generate_response(user_input)
  append_message('assistant', response)
  print(f'ChatBot: {response}\n')

print(f'Messages: {messages}\n')