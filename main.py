your spacy
import random

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Define a dictionary for responses
responses = {
    'greeting': ['Hi! How are you doing today?', 'Hello! How can I assist you today?'],
    'name': ['I am a chatbot created by CodeAlpha.', 'I don’t have a personal name, but you can call me Assistant.'],
    'help': ['Of course! What do you need assistance with?', 'Sure! What can I help you with today?'],
    'projects': ['Great! Which domain interests you?'],
    'resume': ['Focus on highlighting your key achievements and skills relevant to the job you’re applying for.'],
    'relax': ['Try taking a walk or reading a book to unwind.'],
    'stress': ['Consider breaking your tasks into smaller, manageable steps and prioritizing them to reduce overwhelm.'],
    'default': ['Sorry, I didn’t understand that. Could you please rephrase?', 'I’m not sure how to respond to that. Can you ask something else?']
}

def get_response(user_input):
    doc = nlp(user_input.lower())
    if any(token.text in ['hi', 'hello'] for token in doc):
        return random.choice(responses['greeting'])
    elif 'name' in user_input.lower():
        return random.choice(responses['name'])
    elif 'help' in user_input.lower():
        return random.choice(responses['help'])
    elif 'project' in user_input.lower():
        return random.choice(responses['projects'])
    elif 'resume' in user_input.lower():
        return random.choice(responses['resume'])
    elif 'relax' in user_input.lower():
        return random.choice(responses['relax'])
    elif 'stressed' in user_input.lower() or 'stress' in user_input.lower():
        return random.choice(responses['stress'])
    else:
        return random.choice(responses['default'])

def start_chat():
    print("Hello! I am a chatbot.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_chat()