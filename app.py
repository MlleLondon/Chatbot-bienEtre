from flask import Flask, request, jsonify, render_template
from chatbot import process_message  # Importer la fonction de traitement du message

app = Flask(__name__)

# Route pour la page d'accueil (index.html)
@app.route("/")
def home():
    return render_template("index.html")  # Assure-toi que le fichier index.html existe dans le dossier templates

# Route pour afficher la page de chat
@app.route("/chat")
def chat():
    return render_template("chat.html")  # Cette route sert à afficher le chat (chat.html)

# Route pour recevoir les messages du chat (via POST)
@app.route("/chat", methods=["POST"])
def chat_message():
    data = request.get_json()
    user_message = data.get('message', '')
    
    # Traiter le message avec notre système de mots-clés
    response = process_message(user_message)
    
    # Si aucune réponse n'est trouvée ou si c'est une réponse d'erreur, rediriger vers Chatbase
    if response is None or "Je ne peux pas répondre" in response:
        return jsonify({
            'redirect_to_chatbase': True,
            'response': "Je ne peux pas répondre à votre question. Je vais vous rediriger vers notre assistant IA plus avancé."
        })
    
    return jsonify({
        'redirect_to_chatbase': False,
        'response': response
    })

if __name__ == "__main__":
    app.run(debug=True)
