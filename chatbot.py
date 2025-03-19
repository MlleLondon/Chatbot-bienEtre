import nltk
from nltk.chat.util import Chat, reflections
from transformers import pipeline
import random

# Initialisation du modèle GPT-2
generator = pipeline("text-generation", model="gpt2")

# Mots-clés pour détecter les situations négatives
NEGATIVE_KEYWORDS = {
    "stress": [
        "stress", "stressé", "stressée", "anxiété", "anxieux", "anxieuse", 
        "angoisse", "angoissé", "angoissée", "tension", "tendu", "tendue",
        "pressurisé", "pressurisée", "surmené", "surmenée", "pressurisé",
        "pressurisée", "surchargé", "surchargée", "nerveux", "nerveuse",
        "inquiet", "inquiète", "inquiétude", "panique", "paniqué", "paniquée"
    ],
    "tristesse": [
        "triste", "déprimé", "déprimée", "dépression", "dépressif", "déressive",
        "malheureux", "malheureuse", "mélancolique", "mélancolie", "désespéré",
        "désespérée", "désespoir", "pleurer", "pleurs", "pleure", "chagrin",
        "douleur", "douloureux", "douloureuse", "abattu", "abattue", "morose"
    ],
    "sommeil": [
        "dormir", "insomnie", "fatigué", "fatiguée", "épuisé", "épuisée",
        "sommeil", "dort", "dormir", "réveillé", "réveillée", "cauchemar",
        "cauchemars", "somnolence", "somnolent", "somnolente", "endormi",
        "endormie", "somnambule", "somnambulisme", "apnée", "apnée du sommeil"
    ],
    "mal-être": [
        "mal", "pas bien", "ça va pas", "souffrance", "souffrir", "douleur",
        "difficile", "dur", "compliqué", "malade", "fâché", "fâchée", "mood",
        "humeur", "déséquilibré", "déséquilibrée", "perturbé", "perturbée",
        "confus", "confuse", "perdu", "perdue", "désorienté", "désorientée",
        "mal à l'aise", "inconfortable", "désagréable", "nausée", "nauséeux",
        "nauséeuse", "vertige", "vertiges", "migraine", "migraines", "mal de tête"
    ],
    "solitude": [
        "seul", "seule", "solitude", "isolé", "isolée", "personne", "personnes",
        "abandonné", "abandonnée", "rejeté", "rejetée", "exclu", "exclue",
        "marginalisé", "marginalisée", "séparé", "séparée", "divorcé", "divorcée",
        "veuf", "veuve", "célibataire", "sans ami", "sans amis", "sans famille"
    ],
    "confiance": [
        "confiance", "confiant", "confiante", "peur", "avoir peur", "inquiet",
        "inquiète", "inquiétude", "timide", "timidité", "hésitant", "hésitante",
        "doute", "douter", "douteux", "douteuse", "incertain", "incertaine",
        "anxieux", "anxieuse", "phobie", "phobique", "terrifié", "terrifiée",
        "effrayé", "effrayée", "craintif", "craintive", "méfiant", "méfiante"
    ],
    "motivation": [
        "motivation", "motivé", "motivée", "envie", "désir", "objectif", "but",
        "projet", "démotivé", "démotivée", "lassé", "lassée", "fatigué",
        "fatiguée", "épuisé", "épuisée", "découragé", "découragée", "abandonner",
        "abandonné", "abandonnée", "renoncer", "renoncé", "renoncée", "désespéré",
        "désespérée", "désillusionné", "désillusionnée", "perdre espoir"
    ]
}

# Réponses prédéfinies pour chaque catégorie
RESPONSES = {
    "stress": [
        "Je comprends que vous vous sentiez stressé. Voici quelques techniques pour gérer le stress :\n"
        "- Respirez profondément pendant 5 minutes\n"
        "- Faites une pause et sortez prendre l'air\n"
        "- Écrivez ce qui vous préoccupe\n"
        "- Pratiquez une activité relaxante\n"
        "- N'hésitez pas à demander de l'aide",
        
        "Le stress peut être très difficile à gérer. Essayez ces exercices :\n"
        "- Pratiquez la respiration 4-7-8 (inspirez sur 4, retenez sur 7, expirez sur 8)\n"
        "- Faites une promenade de 10 minutes\n"
        "- Écoutez de la musique relaxante\n"
        "- Faites des étirements doux\n"
        "- Parlez à quelqu'un de confiance",
        
        "Pour réduire votre stress, je vous suggère :\n"
        "- Limitez votre consommation de caféine\n"
        "- Établissez une routine quotidienne\n"
        "- Prenez des pauses régulières\n"
        "- Pratiquez la méditation de pleine conscience\n"
        "- Faites de l'exercice physique régulièrement"
    ],
    "tristesse": [
        "Je suis là pour vous écouter. Voici quelques suggestions pour aller mieux :\n"
        "- Parlez à un proche ou un professionnel\n"
        "- Pratiquez une activité qui vous fait plaisir\n"
        "- Sortez prendre l'air et marcher\n"
        "- Écrivez vos sentiments dans un journal\n"
        "- N'oubliez pas que vous n'êtes pas seul(e)",
        
        "La tristesse est une émotion naturelle. Essayez de :\n"
        "- Vous entourer de personnes positives\n"
        "- Faire quelque chose qui vous fait rire\n"
        "- Vous exprimer à travers l'art ou la musique\n"
        "- Prendre soin de vous (sommeil, alimentation)\n"
        "- Vous rappeler que les moments difficiles sont temporaires",
        
        "Pour surmonter la tristesse, je vous conseille :\n"
        "- Pratiquer la gratitude quotidienne\n"
        "- Aider quelqu'un d'autre\n"
        "- Passer du temps dans la nature\n"
        "- Écouter de la musique positive\n"
        "- Consulter un professionnel si nécessaire"
    ],
    "sommeil": [
        "Pour améliorer votre sommeil, essayez ces conseils :\n"
        "- Établissez une routine du coucher\n"
        "- Évitez les écrans 1h avant de dormir\n"
        "- Créez un environnement calme et sombre\n"
        "- Pratiquez des exercices de relaxation\n"
        "- Évitez la caféine en soirée",
        
        "Pour un meilleur sommeil, je vous suggère :\n"
        "- Faites de l'exercice régulièrement mais pas en soirée\n"
        "- Maintenez une température confortable dans votre chambre\n"
        "- Évitez les repas lourds avant de dormir\n"
        "- Utilisez des techniques de relaxation\n"
        "- Limitez les siestes pendant la journée",
        
        "Pour lutter contre les problèmes de sommeil :\n"
        "- Créez un rituel du coucher apaisant\n"
        "- Évitez l'alcool et la nicotine\n"
        "- Gardez votre chambre uniquement pour dormir\n"
        "- Pratiquez la méditation avant de dormir\n"
        "- Maintenez des horaires de sommeil réguliers"
    ],
    "mal-être": [
        "Je comprends que vous ne vous sentiez pas bien. Voici quelques suggestions :\n"
        "- Parlez à quelqu'un de confiance\n"
        "- Pratiquez la méditation ou le yoga\n"
        "- Faites une activité qui vous fait du bien\n"
        "- N'hésitez pas à consulter un professionnel\n"
        "- Rappelez-vous que ça va passer",
        
        "Pour aller mieux, essayez de :\n"
        "- Identifier la source de votre malaise\n"
        "- Prendre soin de votre corps (sommeil, alimentation)\n"
        "- Pratiquer des exercices de respiration\n"
        "- Vous exprimer de manière saine\n"
        "- Demander de l'aide si nécessaire",
        
        "Pour surmonter ce moment difficile :\n"
        "- Écrivez vos sentiments dans un journal\n"
        "- Faites une activité qui vous distrait positivement\n"
        "- Parlez à un professionnel de santé\n"
        "- Pratiquez l'auto-compassion\n"
        "- Rappelez-vous que vous n'êtes pas seul(e)"
    ],
    "solitude": [
        "La solitude peut être difficile. Voici quelques idées :\n"
        "- Rejoignez un club ou une association\n"
        "- Appelez un ami ou un membre de la famille\n"
        "- Participez à des activités de groupe\n"
        "- Utilisez des applications de rencontre amicale\n"
        "- N'oubliez pas que vous êtes important(e)",
        
        "Pour surmonter la solitude, essayez de :\n"
        "- Participer à des événements communautaires\n"
        "- Pratiquer une activité de groupe\n"
        "- Maintenir des contacts réguliers\n"
        "- Faire du bénévolat\n"
        "- Rejoindre des groupes en ligne",
        
        "Pour lutter contre la solitude :\n"
        "- Créez une routine sociale\n"
        "- Pratiquez des activités en groupe\n"
        "- Utilisez les réseaux sociaux de manière positive\n"
        "- Participez à des cours ou ateliers\n"
        "- N'hésitez pas à demander de l'aide"
    ],
    "confiance": [
        "Pour développer votre confiance en vous :\n"
        "- Célébrez vos petites victoires\n"
        "- Pratiquez l'auto-compassion\n"
        "- Sortez de votre zone de confort progressivement\n"
        "- Apprenez de vos erreurs\n"
        "- Entourez-vous de personnes bienveillantes",
        
        "Pour renforcer votre confiance, je vous conseille :\n"
        "- Identifiez vos forces et vos talents\n"
        "- Fixez-vous des objectifs réalistes\n"
        "- Pratiquez l'affirmation positive\n"
        "- Prenez soin de votre apparence\n"
        "- Apprenez à dire non quand nécessaire",
        
        "Pour améliorer votre confiance en vous :\n"
        "- Pratiquez la visualisation positive\n"
        "- Développez vos compétences\n"
        "- Acceptez les compliments\n"
        "- Prenez des initiatives\n"
        "- Entourez-vous de personnes positives"
    ],
    "motivation": [
        "Pour retrouver la motivation :\n"
        "- Fixez-vous des objectifs réalistes\n"
        "- Divisez vos tâches en petites étapes\n"
        "- Récompensez-vous pour vos succès\n"
        "- Entourez-vous de personnes positives\n"
        "- Visualisez vos objectifs",
        "Pour booster votre motivation, essayez de :\n"
        "- Créer un tableau de vision\n"
        "- Établir une routine quotidienne\n"
        "- Célébrer vos progrès\n"
        "- Trouver un partenaire de responsabilité\n"
        "- Vous rappeler votre pourquoi"
        "Pour maintenir votre motivation :\n"
        "- Commencez par de petites actions\n"
        "- Créez un environnement propice\n"
        "- Éliminez les distractions\n"
        "- Pratiquez l'auto-motivation\n"
        "- Restez focalisé sur vos objectifs"
    ] ,
}

def process_message(message):
    """
    Analyse le message et retourne une réponse appropriée
    """
    message = message.lower()
    
    # Vérifier chaque catégorie de mots-clés
    for category, keywords in NEGATIVE_KEYWORDS.items():
        for keyword in keywords:
            if keyword in message:
                # Retourner une réponse aléatoire de la catégorie
                return random.choice(RESPONSES[category])
    
    # Si aucun mot-clé n'est trouvé, retourner None pour indiquer qu'il faut utiliser Chatbase
    return None
