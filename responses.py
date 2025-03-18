PREDEFINED_RESPONSES = {
    # Questions sur le bien-être général
    "comment aller mieux": "Pour aller mieux, je vous suggère plusieurs approches :\n- Pratiquer la méditation quotidienne\n- Faire de l'exercice régulièrement\n- Bien dormir\n- Maintenir une alimentation équilibrée\n- Parler à des proches ou à un professionnel",
    
    "je me sens stressé": "Je comprends que vous vous sentiez stressé. Voici quelques techniques pour gérer le stress :\n- Respirez profondément pendant 5 minutes\n- Faites une pause et sortez prendre l'air\n- Écrivez ce qui vous préoccupe\n- Pratiquez une activité relaxante\n- N'hésitez pas à demander de l'aide",
    
    "je n'arrive pas à dormir": "Pour améliorer votre sommeil, essayez ces conseils :\n- Établissez une routine du coucher\n- Évitez les écrans 1h avant de dormir\n- Créez un environnement calme et sombre\n- Pratiquez des exercices de relaxation\n- Évitez la caféine en soirée",
    
    # Questions sur l'anxiété
    "comment gérer l'anxiété": "Pour gérer l'anxiété, voici des techniques efficaces :\n- Pratiquez la respiration 4-7-8\n- Faites de l'exercice physique\n- Limitez la caféine et l'alcool\n- Maintenez un journal d'anxiété\n- Consultez un professionnel si nécessaire",
    
    # Questions sur la méditation
    "comment méditer": "Pour débuter la méditation :\n- Trouvez un endroit calme\n- Asseyez-vous confortablement\n- Concentrez-vous sur votre respiration\n- Commencez par 5-10 minutes\n- Utilisez des applications guidées comme Headspace ou Petit Bambou",
    
    # Questions sur l'alimentation
    "alimentation et bien-être": "Une bonne alimentation pour le bien-être mental :\n- Mangez des aliments riches en oméga-3\n- Privilégiez les fruits et légumes\n- Hydratez-vous suffisamment\n- Limitez le sucre et la caféine\n- Maintenez des repas réguliers",
    
    # Questions sur l'exercice physique
    "exercices pour le bien-être": "Exercices recommandés pour le bien-être :\n- Marche quotidienne de 30 minutes\n- Yoga doux\n- Étirements matinaux\n- Exercices de respiration\n- Activité physique modérée régulière",
    
    # Questions sur la motivation
    "manque de motivation": "Pour retrouver la motivation :\n- Fixez-vous des objectifs réalistes\n- Divisez vos tâches en petites étapes\n- Récompensez-vous pour vos succès\n- Entourez-vous de personnes positives\n- Visualisez vos objectifs",
    
    # Questions sur la confiance en soi
    "améliorer la confiance en soi": "Pour développer votre confiance :\n- Célébrez vos petites victoires\n- Pratiquez l'auto-compassion\n- Sortez de votre zone de confort progressivement\n- Apprenez de vos erreurs\n- Entourez-vous de personnes bienveillantes",
    
    # Questions sur la gestion des émotions
    "gérer ses émotions": "Pour mieux gérer vos émotions :\n- Identifiez vos déclencheurs\n- Acceptez vos émotions sans jugement\n- Exprimez-vous de manière saine\n- Pratiquez la pleine conscience\n- Prenez du recul avant de réagir",
    
    # Questions sur le développement personnel
    "comment s'améliorer": "Pour votre développement personnel :\n- Lisez régulièrement\n- Apprenez de nouvelles compétences\n- Fixez-vous des objectifs\n- Sortez de votre zone de confort\n- Entourez-vous de personnes inspirantes"
}

def get_response(user_input):
    """
    Recherche une réponse prédéfinie pour l'entrée utilisateur.
    Retourne None si aucune correspondance n'est trouvée.
    """
    # Convertir l'entrée en minuscules pour la comparaison
    user_input = user_input.lower().strip()
    
    # Rechercher une correspondance exacte
    if user_input in PREDEFINED_RESPONSES:
        return PREDEFINED_RESPONSES[user_input]
    
    # Rechercher une correspondance partielle
    for key in PREDEFINED_RESPONSES:
        if key in user_input:
            return PREDEFINED_RESPONSES[key]
    
    # Aucune correspondance trouvée
    return None 