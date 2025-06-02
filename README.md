# 📊 MindTraderPro

MindTraderPro est une application web responsive conçue pour devenir la **référence absolue dans le domaine du trading**. Elle intègre un **calculateur de lot professionnel**, un **journal de trading intelligent**, ainsi qu’un **assistant IA personnalisé**, le tout dans une interface moderne, fluide et ultra complète.

## 🎯 Objectifs

- Offrir aux traders une **gestion de risque optimale**.
- Permettre une **analyse complète des performances**.
- Intégrer une **IA de soutien psychologique et stratégique**.
- Proposer une interface **admin ultra puissante** pour la gestion des utilisateurs et des contenus.

---

## 🚀 Fonctionnalités clés

### 🔹 Calculateur de lot
- Prix en temps réel (via MetaAPI)
- Gestion des paires, sens, SL/TP en pips ou en prix
- Affichage du lot, R:R, gain/perte potentielle en % et devise
- Historique des calculs, partage, copie rapide

### 🔹 Journal de trading
- Enregistrement détaillé des trades (manuellement ou automatiquement)
- Notes vocales avec transcription IA
- Tags : stratégie, émotion, type d’erreur
- Statistiques automatiques : winrate, drawdown, profit factor…
- Analyse comportementale IA

### 🔹 Assistant IA
- Coach IA dans chaque module
- Analyse des erreurs, conseils sur-mesure
- Plan d’amélioration automatique

### 🔹 Interface utilisateur
- Responsive (Web/Mobile)
- Thèmes clair/sombre
- Avatars, badges, niveaux, personnalisation

### 🔹 Interface administrateur
- Gestion des utilisateurs, historiques, rôles
- Modération des contenus
- Gestion des affiliations, offres partenaires, alertes

### 🔹 Monétisation & parrainage
- Freemium / Premium / Lifetime
- Paiement via Stripe (web) + Apple/Google Pay (mobile)
- Système de parrainage intégré avec tableau de suivi

---

## ⚙️ Stack technique

- **Frontend** : HTML/CSS, JS, React (ou Flask Jinja)
- **Backend** : Flask (Python), API REST
- **Base de données** : PostgreSQL
- **API tiers** : MetaAPI (prix en temps réel), Stripe
- **Hébergement** : Render / GitHub Pages / Firebase (mobile)
- **IA** : OpenAI GPT API / Whisper (transcription audio)

---

## 📁 Structure recommandée

```
/backend
  /routes
  /controllers
  /models
  /services
/frontend
  /components
  /pages
  /styles
/database
/tests
.env
app.py
README.md
```

---

## ✅ Suivi de développement

- [x] Cahier des charges
- [ ] Setup backend Flask
- [ ] Intégration MetaAPI
- [ ] Calculateur 100% fonctionnel
- [ ] Journal + IA
- [ ] Interface admin
- [ ] Système de paiement
- [ ] Déploiement

---

## 📌 Auteur

Développé pour le projet **MindTraderPro**, une application pensée par un trader pour des traders qui veulent devenir inébranlables mentalement et techniquement.
