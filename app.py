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
    user_message = request.json.get("message")  # Récupérer le message de l'utilisateur envoyé depuis le frontend
    response = process_message(user_message)  # Appel à la fonction qui génère la réponse
    return jsonify({"response": response})  # Retourner la réponse au format JSON

if __name__ == "__main__":
    app.run(debug=True)
