import nltk
from nltk.chat.util import Chat, reflections

# Define a more extended set of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, nice to meet you! How can I assist you today?",]
    ],
    [r"hi|hello|hey", ["Hello! How can I assist you today?", "Hi there! What can I do for you?",]],
    [r"my name is (.*)", ["Hello %1, nice to meet you! How can I assist you today?",]],
    [r"what is your name", ["I am a friendly chatbot. People call me ChatMaster. How can I help you?",]],
    [r"how are you", ["I'm doing well, thank you! How about yourself?", "I'm just a computer program, but I'm here and ready to assist you.",]],
    [r"(.*) (help|assist|guide) (.*)", ["Sure, I can help with that. What specific assistance do you need?",]],
    [r"what can you do for me", ["I can provide information, answer questions, or just have a friendly chat. How can I assist you today?",]],
    [r"tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!", "Sure, here's a joke: What do you call fake spaghetti? An impasta!",]],
    [r"(.*) (happy|excited|joyful|good|well)", ["I'm glad to hear that! What brings you joy today?", "That's wonderful! What's making you feel happy?",]],
    [r"(.*) (sad|unhappy|down|not good)", ["I'm sorry to hear that. Is there anything specific you would like to talk about or share?", "I'm here to listen if you need someone to talk to.",]],
    [r"bye|goodbye", ["Goodbye! If you ever need assistance, feel free to reach out. Have a great day.", "It was nice chatting with you. Goodbye!",]],
    [r"how can I contact support", ["You can contact support by emailing support@example.com or calling our helpline at 123-456-7890.",]],
    [r"tell me about yourself", ["I'm just a computer program designed to assist and chat with you. What would you like to know?",]],
    [r"(.*) (weather|forecast) (.*)", ["I can provide you with the current weather. Please specify your location.",]],
    [r"(.*) (recommend|suggest) (.*)", ["I can certainly help with recommendations. What are you looking for suggestions on?",]],
    [r"(.*) (movie|film) (.*)", ["Sure, I can recommend a movie. What genre are you in the mood for?",]],
    [r"(.*) (book|read) (.*)", ["I'd be happy to recommend a book. What genre or author do you prefer?",]],
    # Additional patterns and responses
    [r"what is the meaning of life", ["The meaning of life is a complex philosophical question. It depends on personal beliefs. What's your perspective?",]],
    [r"(.*) (technology|tech) (.*)", ["I can help with technology-related questions. What specific tech topic are you interested in?",]],
    [r"(.*) (learn|learning) (.*)", ["Learning is a wonderful pursuit! What subject or skill are you currently interested in learning?",]],
    [r"(.*) (travel|destination) (.*)", ["Traveling is exciting! Where are you planning to go, or do you need recommendations?",]],
    [r"(.*) (food|cuisine) (.*)", ["Food is great! What type of cuisine are you in the mood for, or do you need a recipe?",]],
    [r"(.*) (music|song) (.*)", ["Music is a fantastic way to unwind. What genre or artist are you into, or do you need a recommendation?",]],
     [r"bye|goodbye", ["Goodbye! If you ever need assistance, feel free to reach out. Have a great day.", "It was nice chatting with you. Goodbye!",]],
    [r"how can I contact support", ["You can contact support by emailing support@example.com or calling our helpline at 123-456-7890.",]],
    [r"tell me about yourself", ["I'm just a computer program designed to assist and chat with you. What would you like to know?",]],
    [r"(.*) (weather|forecast) (.*)", ["I can provide you with the current weather. Please specify your location.",]],
    [r"(.*) (recommend|suggest) (.*)", ["I can certainly help with recommendations. What are you looking for suggestions on?",]],
    [r"(.*) (movie|film) (.*)", ["Sure, I can recommend a movie. What genre are you in the mood for?",]],
    [r"(.*) (book|read) (.*)", ["I'd be happy to recommend a book. What genre or author do you prefer?",]],
    # General knowledge and current affairs
    [r"what is the capital of (.*)", ["The capital of %1 is [Capital Name].", "For %1, the capital is [Capital Name].",]],
    [r"who is the president of (.*)", ["The current president of %1 is [President Name].",]],
    [r"(.*) (latest news|current affairs|recent events)", ["I can provide you with the latest news. What specific topic or category are you interested in?",]],
    [r"(.*) (world leaders|notable personalities)", ["Some notable world leaders include [Leader1], [Leader2], and [Leader3].",]],
    [r"(.*) (sports|athlete) (.*)", ["Sure, I can provide information on sports. What specific sport or athlete are you interested in?",]],
    [r"(.*) (technology|tech) (.*)", ["I can help with technology-related questions. What specific tech topic are you interested in?",]],
    [r"(.*) (learn|learning) (.*)", ["Learning is a wonderful pursuit! What subject or skill are you currently interested in learning?",]],
    [r"(.*) (travel|destination) (.*)", ["Traveling is exciting! Where are you planning to go, or do you need recommendations?",]],
    [r"(.*) (food|cuisine) (.*)", ["Food is great! What type of cuisine are you in the mood for, or do you need a recipe?",]],
    [r"(.*) (music|song) (.*)", ["Music is a fantastic way to unwind. What genre or artist are you into, or do you need a recommendation?",]],
    [r"hi|hello|hey", ["Hello! How can I assist you today?", "Hi there! What can I do for you?",]],
    [r"my name is (.*)", ["Hello %1, nice to meet you! How can I assist you today?",]],
    [r"what is your name", ["I am a friendly chatbot. People call me ByteBuddy. How can I help you?",]],
    [r"how are you", ["I'm doing well, thank you! How about yourself?", "I'm just a computer program, but I'm here and ready to assist you.",]],
    [r"(.*) (help|assist|guide) (.*)", ["Sure, I can help with that. What specific assistance do you need?",]],
    [r"what can you do for me", ["I can provide information, answer questions, or just have a friendly chat. How can I assist you today?",]],
    [r"tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!", "Sure, here's a joke: What do you call fake spaghetti? An impasta!",]],
    [r"(.*) (happy|excited|joyful|good|well)", ["I'm glad to hear that! What brings you joy today?", "That's wonderful! What's making you feel happy?",]],
    [r"(.*) (sad|unhappy|down|not good)", ["I'm sorry to hear that. Is there anything specific you would like to talk about or share?", "I'm here to listen if you need someone to talk to.",]],
    [r"bye|goodbye", ["Goodbye! If you ever need assistance, feel free to reach out. Have a great day.", "It was nice chatting with you. Goodbye!",]],
    # Add more general patterns and responses below
    [r"how can I contact support", ["You can contact support by emailing support@example.com or calling our helpline at 123-456-7890.",]],
    [r"tell me about yourself", ["I'm just a computer program designed to assist and chat with you. What would you like to know?",]],
    [r"(.*) (weather|forecast) (.*)", ["I can provide you with the current weather. Please specify your location.",]],
    [r"(.*) (recommend|suggest) (.*)", ["I can certainly help with recommendations. What are you looking for suggestions on?",]],
    [r"(.*) (movie|film) (.*)", ["Sure, I can recommend a movie. What genre are you in the mood for?",]],
    [r"(.*) (book|read) (.*)", ["I'd be happy to recommend a book. What genre or author do you prefer?",]],
    [r"(.*) (happy|excited|joyful|good|well)", ["I'm glad to hear that! What brings you joy today?", "That's wonderful! What's making you feel happy?",]],
    [r"(.*) (sad|unhappy|down|not good)", ["I'm sorry to hear that. Is there anything specific you would like to talk about or share?", "I'm here to listen if you need someone to talk to.",]],
    [r"(.*) (angry|frustrated|upset|mad)", ["I understand that you're feeling [Emotion]. What's causing you to feel this way?", "I'm here to listen if you want to share what's making you angry or upset.",]],
    [r"(.*) (surprised|shocked|astonished)", ["Wow! That's surprising. What happened to make you feel this way?", "I can sense your surprise. What's the reason behind it?",]],
    [r"(.*) (fear|scared|anxious|worried)", ["It's okay to feel fearful or worried. What's causing these emotions for you?", "I'm here to help you navigate through any fears or concerns you have. What's on your mind?",]],
    [r"(.*) (confused|lost|uncertain)", ["Feeling confused is normal. What's causing the confusion, and how can I assist in clearing things up for you?", "It's okay not to have all the answers. Let's work through the confusion together. What's on your mind?",]],
    [r"(.*) (love|affection|romantic)", ["Love is a beautiful emotion! What's going on in your romantic life, or is there anything specific you'd like to talk about?", "Love is in the air! Anything on your mind related to love or relationships?",]],
    [r"(.*) (bored|boring|uninterested)", ["If you're feeling bored, maybe we can find something interesting to discuss. What topics or activities usually capture your interest?", "Boredom happens to the best of us. Let's find something engaging to chat about. What are you into?",]],
    [r"(.*) (grateful|thankful|appreciative)", ["It's wonderful to feel grateful. What are you thankful for today, or is there something specific you'd like to express gratitude for?", "Expressing gratitude is a great practice. What's making you feel appreciative right now?",]],
    [r"(.*) (embarrassed|shy|awkward)", ["Feeling embarrassed is completely normal. Is there something specific that's making you feel this way, or would you like to talk about it?", "We all experience moments of awkwardness. What happened that's making you feel embarrassed?",]],
    [r"(.*) (proud|accomplished|achievement)", ["Congratulations on your accomplishment! What did you achieve, and how can I celebrate with you?", "Feeling proud is fantastic! What did you accomplish, and how can I support or congratulate you?",]],
    [
        r"what is your name?",
        ["I am a friendly chatbot.", "People call me ChatMaster. How can I help you?",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you! How about yourself?", "I'm just a computer program, but I'm here and ready to assist you.",]
    ],
    [
        r"(.*) (help|assist|guide) (.*)",
        ["Sure, I can help with that. What specific assistance do you need?",]
    ],
    [
        r"what can you do for me?",
        ["I can provide information, answer questions, or just have a friendly chat. How can I assist you today?",]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "Sure, here's a joke: What do you call fake spaghetti? An impasta!"]
    ],
    [
        r"(.*) (happy|excited|joyful|good|well)",
        ["I'm glad to hear that! What brings you joy today?", "That's wonderful! What's making you feel happy?",]
    ],
    [
        r"(.*) (sad|unhappy|down|not good)",
        ["I'm sorry to hear that. Is there anything specific you would like to talk about or share?", "I'm here to listen if you need someone to talk to.",]
    ],
    [
        r"quit",
        ["Goodbye! If you ever need assistance, feel free to reach out. Have a great day.", "It was nice chatting with you. Goodbye!"]
    ],
]
    

# Create a Chat instance
chatbot = Chat(pairs, reflections)

# Simple conversation loop
def chat():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        
        # Exit the loop if the user types 'quit'
        if user_input.lower() == 'quit':
            print("Bot: Goodbye! If you ever need assistance, feel free to reach out. Have a great day.")
            break

        # Get the chatbot's response
        response = chatbot.respond(user_input)
        
        print("Bot:", response)

# Call the chat function
chat()
