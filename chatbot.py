import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

load_dotenv()
api_key = os.getenv('GROQ_API_KEY')
chat = ChatGroq(model='llama-3.3-70b-versatile')

def append_message(role, content):
  messages.append((role, content))

def generate_response(messages):
  chat_prompts = [('system', 'You are a friendly helpful assistant called Chatty.')]
  chat_prompts += messages
  template = ChatPromptTemplate.from_messages(chat_prompts)
  chain = template | chat
  response = chain.invoke({})
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
  response = generate_response(messages)
  append_message('assistant', response)
  print(f'ChatBot: {response}\n')

print(f'Messages: {messages}\n')