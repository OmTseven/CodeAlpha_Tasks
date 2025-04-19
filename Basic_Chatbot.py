import spacy


nlp = spacy.load("en_core_web_sm")

def chatbot():
    print("Hi! I'm your friendly chatbot. Type 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break

        
        doc = nlp(user_input)
        
        
        if "weather" in user_input:
            print("Chatbot: The weather is unpredictable these days! Stay prepared.")
        elif "name" in user_input:
            print("Chatbot: You can call me ChatBoticus! What's yours?")
        elif any(token.pos_ == "VERB" for token in doc):
            print("Chatbot: I love talking about actions! Tell me more.")
        else:
            print("Chatbot: That's interesting! Can you tell me more?")
        
        