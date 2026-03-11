print("🤖 AI Chatbot Started")
print("Type 'bye' to exit\n")

# Question-Answer Dictionary
responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm fine 😊 How about you?",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning is a subset of AI that learns from data.",
    "who created you": "I was created using Python programming.",
    "your name": "I am a simple AI Chatbot.",
    "bye": "Goodbye! Have a nice day 😊"
}

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot:", responses["bye"])
        break

    found = False
    for question in responses:
        if question in user_input:
            print("Bot:", responses[question])
            found = True
            break

    if not found:
        print("Bot: Sorry, I don't understand that question.")
