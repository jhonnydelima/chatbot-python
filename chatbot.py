from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('GROQ_API_KEY')

print('Welcome to the chatbot!')
print('Type "exit" or press "X" to end the conversation.\n')

messages = []
def add_message(role, content):
  messages.append({'role': role, 'content': content})

def generate_response():
  # This function would typically generate a response based on the messages.
  # For demonstration, we'll just return a placeholder response.
  return "This is a placeholder response."

while True: 
  user_input = input('You: ')

  if user_input.lower() in ['exit', 'x']:
    print('Chatbot: Goodbye!\n')
    break
  
  add_message('user', user_input)
  response = generate_response()
  add_message('assistant', response)
  print(f'ChatBot: {response}')

print(f'Messages: {messages}\n')