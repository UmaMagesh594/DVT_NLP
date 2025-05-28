import nltk
from nltk.chat.util import Chat, reflections

input_output_patterns = [
    (r'Hi there!', ['Hello!']),
    (r'How are you?', ['I am doing well, thank you. How are you?']),
    (r'What is your name?', ['My name is Chatbot.']),
    (r'Quit|Bye|Thank you', ['Goodbye!', 'Bye! Nice talking to you.'])
]

chatbot = Chat(input_output_patterns, reflections)
chatbot.converse()
chatbot = Chat(input_output_patterns, reflections)
chatbot.converse()
