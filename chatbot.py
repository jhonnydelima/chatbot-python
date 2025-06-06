print('Welcome to the chatbot!')
print('Type "exit" or press "X" to end the conversation.\n')

while True: 
  user_input = input('You: ')

  if user_input.lower() in ['exit', 'x']:
    print('Chatbot: Goodbye!')
    break
  
  # Here you would typically process the user input and generate a response.
  # For demonstration, we'll just echo the input.
  print(f'Chatbot: You said "{user_input}"')