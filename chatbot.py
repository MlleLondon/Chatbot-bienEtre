import nltk
from nltk.chat.util import Chat, reflections
from transformers import pipeline

# Initialisation du modèle GPT-2 (ou un modèle plus avancé comme ChatGPT si dispo)
generator = pipeline("text-generation", model="gpt2")

# Fonction de génération de réponse avec GPT-2
def generate_response(message):
    response = generator(message, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']

# Définition des paires de questions/réponses
pairs = [
    (r"Comment te sens-tu aujourd'hui\?", ["Je me sens bien, merci de demander. Et toi, comment te sens-tu ?"]),
    (r"Je me sens (.*)", ["C'est normal de se sentir %1 parfois. Que puis-je faire pour t'aider à te sentir mieux ?"]),
    (r"(.*) stressé(.*)", ["Respire profondément, inspire pendant 4 secondes, retiens pendant 4 secondes, puis expire pendant 4 secondes."]),
    (r"(.*) triste(.*)", ["C'est ok de se sentir triste parfois. Laisse-moi te lire une citation motivante."]),
    (r"(.*)", ["Je ne suis pas sûr de comprendre, mais je suis là pour t'aider."])
]

def process_message(message):
    # Recherche de la correspondance dans les paires définies
    for pattern, responses in pairs:
        if nltk.re.search(pattern, message):
            return responses[0]
    # Si aucun modèle n'est trouvé, utiliser GPT-2
    return generate_response(message)
