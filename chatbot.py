import spacy

# Load English tokenizer, POS tagger, parser, NER
nlp = spacy.load("en_core_web_sm")

# Predefined FAQs
FAQS = {
    "what are your hours": "We are open from 9am to 5pm, Monday through Friday.",
    "where are you located": "We are located at 123 Main Street, Anytown.",
    "how can i contact support": "You can contact support via email at support@example.com.",
}

# Session context
session_context = {
    "user_name": None
}

def process_input(user_input):
    doc = nlp(user_input.lower())
    
    # Greeting detection
    greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
    if any(token.text in greetings for token in doc):
        if session_context["user_name"]:
            return f"Hello again, {session_context['user_name']}! How can I help you today?"
        else:
            return "Hello! What is your name?"
    
    # Name detection (simple heuristic: if sentence starts with "my name is")
    if "my name is" in user_input.lower():
        name = user_input.split("is")[-1].strip().split()[0]
        session_context["user_name"] = name.capitalize()
        return f"Nice to meet you, {session_context['user_name']}! How can I help you?"
    
    # Answer FAQs
    for question, answer in FAQS.items():
        if question in user_input.lower():
            return answer
    
    # Default fallback
    return "I'm sorry, I didn't quite understand that. Could you please rephrase?"

