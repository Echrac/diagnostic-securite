# Auto-diagnostic cybersécurité

Application web (Streamlit) qui aide une TPE ou une association à évaluer son niveau d'hygiène informatique. L'utilisateur répond à un court questionnaire, l'application calcule un score et renvoie des recommandations classées par priorité, puis un rapport téléchargeable.

C'est un **outil de sensibilisation**, inspiré du guide d'hygiène informatique de l'ANSSI — pas un audit certifié.

## Fonctionnalités

- Questionnaire couvrant les mesures de sécurité essentielles (mots de passe, double authentification, mises à jour, sauvegardes…).
- Score pondéré selon l'importance de chaque mesure.
- Recommandations affichées des plus prioritaires aux moins urgentes.
- Rapport téléchargeable au format texte.

## Prérequis

- Python 3.9 ou plus récent
- Streamlit

## Installation

```bash
git clone https://github.com/<utilisateur>/<depot>.git
cd <depot>
python -m venv .venv

# Windows (PowerShell) :
.\.venv\Scripts\Activate.ps1
# macOS / Linux :
# source .venv/bin/activate

pip install -r requirements.txt
```

## Lancer

```bash
streamlit run diagnostic.py
```

Le navigateur s'ouvre sur `http://localhost:8501`. Répondre au questionnaire, puis cliquer sur « Calculer mon score ».

## Structure

```
.
├── diagnostic.py       # l'application Streamlit
├── requirements.txt    # dépendances
├── .gitignore
└── README.md
```

## À propos

Projet d'apprentissage réalisé dans le cadre d'un portfolio (cybersécurité, gestion du risque). Outil de sensibilisation ; pour un accompagnement sérieux, se référer au guide de l'ANSSI et à cybermalveillance.gouv.fr.

## Licence

MIT
