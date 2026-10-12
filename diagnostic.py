import streamlit as st

# Chaque question : thème, énoncé, poids, recommandation si "Non", priorité
QUESTIONS = [
    {"theme": "Mots de passe",
     "q": "Les mots de passe font-ils 12 caractères ou plus, et sont-ils uniques par service ?",
     "poids": 3, "priorite": "Haute",
     "reco": "Imposer des mots de passe longs et uniques via un gestionnaire de mots de passe."},
    {"theme": "Double authentification",
     "q": "La double authentification (MFA) est-elle active sur la messagerie et les comptes admin ?",
     "poids": 3, "priorite": "Haute",
     "reco": "Activer le MFA sur la messagerie, les accès distants et les comptes administrateurs."},
    {"theme": "Mises à jour",
     "q": "Les postes, serveurs et logiciels sont-ils mis à jour régulièrement ?",
     "poids": 3, "priorite": "Haute",
     "reco": "Activer les mises à jour automatiques et suivre les correctifs de sécurité."},
    {"theme": "Sauvegardes",
     "q": "Des sauvegardes sont-elles faites, déconnectées et testées régulièrement ?",
     "poids": 3, "priorite": "Haute",
     "reco": "Appliquer la règle 3-2-1 et tester la restauration au moins une fois par an."},
    {"theme": "Droits d'accès",
     "q": "Les droits sont-ils limités au nécessaire et retirés à chaque départ ?",
     "poids": 2, "priorite": "Moyenne",
     "reco": "Appliquer le moindre privilège et retirer les accès au départ d'une personne."},
    {"theme": "Protection des postes",
     "q": "Un antivirus et un pare-feu sont-ils actifs sur tous les postes ?",
     "poids": 2, "priorite": "Moyenne",
     "reco": "Déployer un antivirus à jour et activer le pare-feu sur chaque poste."},
    {"theme": "Sensibilisation",
     "q": "Les équipes sont-elles sensibilisées au phishing et aux bons réflexes ?",
     "poids": 2, "priorite": "Moyenne",
     "reco": "Former régulièrement les équipes et simuler des campagnes de phishing."},
    {"theme": "Réaction aux incidents",
     "q": "Savez-vous qui contacter et quoi faire en cas d'incident ?",
     "poids": 2, "priorite": "Moyenne",
     "reco": "Rédiger une procédure simple et afficher les contacts (cybermalveillance.gouv.fr)."},
]

st.title("Auto-diagnostic cybersécurité")
st.caption("Pour TPE et associations, inspiré du guide d'hygiène de l'ANSSI.")

reponses = {}
with st.form("diagnostic"):
    for i, item in enumerate(QUESTIONS):
        reponses[i] = st.radio(item["q"], ["Oui", "Non", "Je ne sais pas"],
                               index=2, key=str(i))
    valide = st.form_submit_button("Calculer mon score")

if valide:
    total = sum(item["poids"] for item in QUESTIONS)
    obtenu = sum(QUESTIONS[i]["poids"] for i, rep in reponses.items() if rep == "Oui")
    pourcentage = round(100 * obtenu / total)

    st.header(f"Score : {pourcentage} / 100")
    if pourcentage >= 80:
        st.success("Bon niveau. Maintenir et surveiller.")
    elif pourcentage >= 50:
        st.warning("Niveau moyen. Plusieurs mesures importantes à renforcer.")
    else:
        st.error("Niveau faible. Des mesures prioritaires à mettre en place.")

    ordre = {"Haute": 0, "Moyenne": 1, "Basse": 2}
    manquantes = [QUESTIONS[i] for i, rep in reponses.items() if rep != "Oui"]
    manquantes.sort(key=lambda item: ordre[item["priorite"]])

    if manquantes:
        st.subheader("Recommandations, par priorité")
        lignes = [f"Auto-diagnostic cyber - score {pourcentage}/100", ""]
        for item in manquantes:
            st.markdown(f"**[{item['priorite']}] {item['theme']}** : {item['reco']}")
            lignes.append(f"[{item['priorite']}] {item['theme']} : {item['reco']}")
        st.download_button("Télécharger le rapport", "\n".join(lignes),
                           file_name="diagnostic_cyber.txt")
    else:
        st.write("Toutes les mesures du questionnaire sont couvertes.")