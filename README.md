
# 🌐 Orbita – Bot Discord communautaire

**Orbita** est un bot Discord polyvalent conçu pour gérer les communautés autour du gaming, du sport, du divertissement et plus encore.  
Il facilite l’accueil des membres, la modération et l’organisation de votre serveur.

---

## ✨ Fonctionnalités principales

- ✅ Rôle automatique après acceptation du règlement
- 👋 Messages de bienvenue personnalisés
- 🛠️ Commandes de modération (mute, kick, ban, purge...)
- 🧾 Attribution de rôles via boutons ou réactions
- 📢 Annonces programmées ou manuelles
- 📊 Logs (arrivées, suppressions, modifications...)
- 🎮 Fonctions communautaires à venir (quiz, sondages, jeux...)

---

## 🚀 Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/ton-utilisateur/orbita-bot.git
cd orbita-bot
```

2. Créez et activez un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. Configurez votre fichier `.env` :
```
DISCORD_TOKEN=your_token_here
GUILD_ID=1234567890
```

5. Lancez le bot :
```bash
python main.py
```

---

## 🧰 Dépendances principales

- [`discord.py`](https://pypi.org/project/discord.py/)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)

Installez-les avec :
```bash
pip install discord.py python-dotenv
```

---

## 📁 Arborescence conseillée

```
orbita-bot/
│
├── main.py
├── cogs/
│   ├── welcome.py
│   ├── roles.py
│   └── moderation.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ✅ À venir

- 🎲 Commandes de mini-jeux communautaires
- 📅 Système d’événements programmés
- 🧠 Auto-modération intelligente
- 📈 Dashboard web (facultatif)

---

## 📜 Licence

Ce projet est open source et distribué sous licence **MIT**.

---

## 🤝 Contribuer

Pull requests bienvenues ! Si vous avez des idées ou des bugs à signaler, ouvrez une *issue*.

---

## 📩 Contact

Créé avec ❤️ par **Milou-code**  
[Discord du projet](à venir) • [GitHub](https://github.com/Milou-code)
