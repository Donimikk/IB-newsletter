# 📰 IB Newsletter

> Automatický denný crypto newsletter pre komunitu **Investiční Bohovia**

---

## Čo to je?

Jednoduchý systém, ktorý každý deň:
1. **Stiahne** novinky z crypto zdrojov (API/RSS)
2. **Spracuje** ich cez AI (GPT-4o-mini) - sumarizuje, odstráni duplikáty
3. **Overí** faktickú správnosť (druhé GPT volanie)
4. **Pošle** newsletter emailom cez Brevo

Všetko beží automaticky cez **GitHub Actions** - žiadny server, žiadna údržba.

---

## Ako to funguje? (eli5)

```
⏰ Ráno o 7:00
      ↓
📡 Stiahnem správy z 3 zdrojov
      ↓
🤖 AI to spracuje a napíše pekný text
      ↓
🔍 Druhé AI skontroluje či som neklamal
      ↓
📧 Pošlem email všetkým odberateľom
      ↓
😴 Spím do zajtra
```

---

## Tech Stack

| Čo | Čím |
|----|-----|
| Jazyk | Python 3.11 |
| AI | OpenAI GPT-4o-mini |
| Emaily | Brevo SMTP |
| Scheduler | GitHub Actions (cron) |
| Hosting | Žiadny - serverless |

---

## Štruktúra projektu

```
IB-newsletter/
├── src/                 # Python kód
│   ├── main.py          # Hlavný skript
│   ├── fetcher.py       # Sťahuje dáta z API
│   ├── processor.py     # GPT spracovanie
│   └── sender.py        # Posiela emaily
├── templates/           # HTML šablóna emailu
├── config/              # Nastavenia a prompty
├── specification/       # Dokumentácia projektu
└── .github/workflows/   # GitHub Actions cron job
```

---

## Dokumentácia

- [📋 Projektový plán](specification/project_plan.md)
- [🏗️ Architektúra systému](specification/architecture.md)
- [📝 Špecifikácia](specification/sp.md)

---

## Pre vývojárov

**Potrebuješ Docker/VM?** Nie. GitHub Actions to rieši za teba - proste pushni kód a ono to beží.

**Kde sú API kľúče?** V GitHub Secrets, nie v kóde.

**Ako testovať lokálne?**
```bash
pip install -r requirements.txt
python src/main.py
```

---

## Status

🚧 **V príprave** - zatiaľ len dokumentácia, kód príde čoskoro.

---

*Made with ☕ for [Investiční Bohovia](https://investicnibohovia.sk)*