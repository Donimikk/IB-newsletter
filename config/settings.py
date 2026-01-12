# ===========================================
# IB Newsletter - Centrálna Konfigurácia
# ===========================================
# Tento súbor obsahuje všetky nastavenia projektu
# Hodnoty sa načítavajú z .env súboru pre bezpečnosť
# ===========================================

import os
from dotenv import load_dotenv

# Načítaj .env súbor (ak existuje)
# Toto hľadá .env v root priečinku projektu
load_dotenv()


# ===========================================
# API Kľúče (z environment variables)
# ===========================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BREVO_API_KEY = os.getenv("BREVO_API_KEY")
BREVO_SENDER_EMAIL = os.getenv("BREVO_SENDER_EMAIL", "newsletter@investicnibohovia.sk")
BREVO_SENDER_NAME = os.getenv("BREVO_SENDER_NAME", "Investiční Bohovia")
BREVO_LIST_ID = int(os.getenv("BREVO_LIST_ID", "1"))


# ===========================================
# Mód aplikácie
# ===========================================

# "development" = posiela len na TEST_EMAIL
# "production" = posiela na celý contact list
MODE = os.getenv("MODE", "development")
TEST_EMAIL = os.getenv("TEST_EMAIL", "")


# ===========================================
# Newsletter Nastavenia
# ===========================================

NEWSLETTER_CONFIG = {
    # Čas odoslania (používa GitHub Actions cron, toto je len pre dokumentáciu)
    "send_time": "07:00",  # CET
    
    # Limity pre obsah
    "min_words": 250,
    "max_words": 350,
    
    # Prefix pre subject line
    # Výsledok bude napr: "Crypto Daily | Bitcoin prelomil 100k"
    "subject_prefix": "Crypto Daily |",
}


# ===========================================
# API Zdroje (MOCK - nahradiť reálnymi)
# ===========================================

# TODO: Nahradiť reálnymi API endpointmi od zákazníka
API_SOURCES = [
    {
        "name": "Zdroj 1 (Mock)",
        "url": "https://api.example.com/crypto-news",
        "type": "api",  # "api" alebo "rss"
        "enabled": True,
    },
    {
        "name": "Zdroj 2 (Mock)",
        "url": "https://example.com/rss/crypto",
        "type": "rss",
        "enabled": True,
    },
    {
        "name": "Zdroj 3 (Mock)",
        "url": "https://api.example.com/market-data",
        "type": "api",
        "enabled": True,
    },
]


# ===========================================
# GPT Nastavenia
# ===========================================

GPT_CONFIG = {
    # Model pre generovanie
    "generator": {
        "model": "gpt-4o-mini",
        "max_tokens": 500,
        "temperature": 0.7,  # Kreatívnejšie, prirodzený jazyk
    },
    # Model pre verifikáciu
    "verifier": {
        "model": "gpt-4o-mini",
        "max_tokens": 200,
        "temperature": 0.2,  # Presnejšie, konzistentné
    },
}


# ===========================================
# Validácia konfigurácie
# ===========================================

def validate_config():
    """
    Skontroluje či sú všetky potrebné premenné nastavené.
    Volá sa pri štarte aplikácie.
    """
    errors = []
    
    if not OPENAI_API_KEY:
        errors.append("OPENAI_API_KEY nie je nastavený")
    
    if not BREVO_API_KEY:
        errors.append("BREVO_API_KEY nie je nastavený")
    
    if MODE == "development" and not TEST_EMAIL:
        errors.append("TEST_EMAIL musí byť nastavený v development móde")
    
    if errors:
        raise ValueError(
            "Chyba konfigurácie:\n" + "\n".join(f"  - {e}" for e in errors)
        )
    
    return True


# Pre debug: vypíš načítanú konfiguráciu
if __name__ == "__main__":
    print("=== IB Newsletter Konfigurácia ===")
    print(f"Mód: {MODE}")
    print(f"OpenAI API: {'✓ nastavené' if OPENAI_API_KEY else '✗ chýba'}")
    print(f"Brevo API: {'✓ nastavené' if BREVO_API_KEY else '✗ chýba'}")
    print(f"Sender: {BREVO_SENDER_NAME} <{BREVO_SENDER_EMAIL}>")
    print(f"Zdroje: {len(API_SOURCES)} definovaných")
