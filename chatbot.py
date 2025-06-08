from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()
api_key = os.getenv('GROQ_API_KEY')
chat = ChatGroq(model='llama-3.3-70b-versatile')

print('Welcome to the chatbot!')
print('Type "exit" or press "X" to end the conversation.\n')

messages = []
def append_message(role, content):
  messages.append({'role': role, 'content': content})

def generate_response(user_input):
  response = chat.invoke(user_input)
  return response.content

while True: 
  user_input = input('You: ')

  if user_input.lower() in ['exit', 'x']:
    print('Chatbot: Goodbye!\n')
    break
  
  append_message('user', user_input)
  response = generate_response(user_input)
  append_message('assistant', response)
  print(f'ChatBot: {response}')

print(f'Messages: {messages}\n')