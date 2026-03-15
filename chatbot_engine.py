from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

questions = [
    "When does admission start?",
    "What is the fees structure?",
    "Which courses are available?",
    "Is hostel facility available?",
    "What is the contact number?",
    "Where is the college located?"
]

answers = [
    "Admission starts from June every year.",
    "The annual fees is ₹50,000.",
    "We offer BCA, BBA, B.Tech and MBA programs.",
    "Yes, hostel facility is available for students.",
    "You can call 9876543210 or email info@college.com",
    "The college is located in Bareilly."
]

vectorizer = TfidfVectorizer(stop_words='english')
question_vectors = vectorizer.fit_transform(questions)

def get_ai_response(user_message):
    if not user_message:
        return "Please enter a valid question."

    user_message = user_message.lower().strip()

    user_vector = vectorizer.transform([user_message])
    similarity = cosine_similarity(user_vector, question_vectors)

    best_match_index = np.argmax(similarity)
    best_score = similarity[0][best_match_index]

    if best_score < 0.4:
        return "Sorry, I couldn't clearly understand your question. Please rephrase."

    return answers[best_match_index]
