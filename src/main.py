# ===========================================
# IB Newsletter - Main Entry Point
# ===========================================
# Tento súbor je hlavný vstupný bod aplikácie.
# Spúšťa celý newsletter pipeline:
#   1. Stiahne dáta z API zdrojov
#   2. Spracuje cez GPT
#   3. Vygeneruje HTML email
#   4. Odošle cez Brevo
#
# Spustenie: python src/main.py
# ===========================================

import sys
from datetime import datetime

# Import konfigurácie
# Poznámka: keďže spúšťame z root priečinka, musíme pridať cestu
sys.path.insert(0, ".")
from config.settings import (
    validate_config,
    MODE,
    TEST_EMAIL,
    NEWSLETTER_CONFIG,
)


def run_newsletter_pipeline():
    """
    Hlavná funkcia - spúšťa celý pipeline.
    
    Kroky:
    1. Validácia konfigurácie
    2. Fetch dát z API zdrojov
    3. GPT spracovanie (generátor + verifikátor)
    4. Renderovanie HTML šablóny
    5. Odoslanie emailu
    """
    
    print("=" * 50)
    print("🚀 IB Newsletter Pipeline - Štart")
    print(f"📅 Dátum: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
    print(f"🔧 Mód: {MODE}")
    print("=" * 50)
    
    # --- Krok 1: Validácia ---
    print("\n[1/5] Validujem konfiguráciu...")
    try:
        validate_config()
        print("      ✓ Konfigurácia OK")
    except ValueError as e:
        print(f"      ✗ Chyba: {e}")
        return False
    
    # --- Krok 2: Fetch dát ---
    print("\n[2/5] Sťahujem dáta z API zdrojov...")
    # TODO: Implementovať v src/fetcher.py
    # articles = fetch_all_sources()
    articles = _mock_fetch_articles()  # Zatiaľ mock
    print(f"      ✓ Stiahnutých {len(articles)} článkov")
    
    # --- Krok 3: GPT spracovanie ---
    print("\n[3/5] Spracúvam cez GPT...")
    # TODO: Implementovať v src/processor.py
    # content = process_articles(articles)
    content = _mock_process_articles(articles)  # Zatiaľ mock
    print(f"      ✓ Vygenerovaný obsah ({len(content.split())} slov)")
    
    # --- Krok 4: Renderovanie HTML ---
    print("\n[4/5] Generujem HTML email...")
    # TODO: Implementovať v src/formatter.py
    # html = render_email(content, subject)
    subject = f"{NEWSLETTER_CONFIG['subject_prefix']} {datetime.now().strftime('%d.%m.%Y')}"
    html = _mock_render_html(content, subject)  # Zatiaľ mock
    print(f"      ✓ HTML vygenerované ({len(html)} znakov)")
    
    # --- Krok 5: Odoslanie ---
    print("\n[5/5] Odosielam email...")
    # TODO: Implementovať v src/sender.py
    # success = send_newsletter(html, subject)
    success = _mock_send_email(html, subject)  # Zatiaľ mock
    
    if success:
        print("      ✓ Email odoslaný!")
    else:
        print("      ✗ Chyba pri odosielaní")
        return False
    
    print("\n" + "=" * 50)
    print("✅ Pipeline dokončený úspešne!")
    print("=" * 50)
    
    return True


# ===========================================
# MOCK FUNKCIE (dočasné, kým nie sú implementované moduly)
# ===========================================

def _mock_fetch_articles():
    """
    Mock funkcia - vráti falošné články pre testovanie.
    Bude nahradená reálnym src/fetcher.py
    """
    return [
        {
            "title": "Bitcoin prelomil 100 000 USD",
            "content": "Bitcoin dnes prvýkrát v histórii prekročil hranicu 100 000 dolárov. Analytici hovoria o novej ére pre kryptomeny.",
            "source": "Mock API 1",
            "date": datetime.now().isoformat(),
        },
        {
            "title": "Ethereum 2.0 upgrade naplánovaný",
            "content": "Ethereum Foundation oznámila dátum ďalšieho major upgradu siete. Očakáva sa zníženie poplatkov.",
            "source": "Mock API 2", 
            "date": datetime.now().isoformat(),
        },
        {
            "title": "Solana zaznamenala rekordný objem",
            "content": "Solana blockchain spracoval najviac transakcií za posledných 24 hodín, čo signalizuje rastúci záujem.",
            "source": "Mock RSS",
            "date": datetime.now().isoformat(),
        },
    ]


def _mock_process_articles(articles):
    """
    Mock funkcia - vráti falošný spracovaný obsah.
    Bude nahradená reálnym src/processor.py s GPT integráciou.
    """
    return """
🔥 HLAVNÁ SPRÁVA DŇA

Bitcoin dnes prvýkrát v histórii prelomil magickú hranicu 100 000 dolárov. 
Toto je historický moment pre celý crypto svet - od prvého Bitcoinu v roku 2009 
to trvalo 15 rokov, kým sme sa dostali sem.

📰 V SKRATKE

• Ethereum chystá ďalší veľký upgrade - očakáva sa zníženie gas fees
• Solana láme rekordy v počte transakcií - sieť zvláda záťaž bez problémov  
• Celková trhová kapitalizácia crypto prekročila 3.5 bilióna USD

Dnes je dobrý deň byť súčasťou Investičných Bohov! 🚀
    """.strip()


def _mock_render_html(content, subject):
    """
    Mock funkcia - vráti jednoduchý HTML.
    Bude nahradená reálnym src/formatter.py s Jinja2 šablónou.
    """
    return f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{subject}</title>
</head>
<body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
    <h1 style="color: #1a1a1a;">📰 Investiční Bohovia</h1>
    <p style="color: #666;">Denný crypto prehľad</p>
    <hr>
    <div style="white-space: pre-line;">
{content}
    </div>
    <hr>
    <footer style="color: #999; font-size: 12px;">
        © 2026 Investiční Bohovia | <a href="{{{{unsubscribe}}}}">Odhlásiť sa</a>
    </footer>
</body>
</html>
    """.strip()


def _mock_send_email(html, subject):
    """
    Mock funkcia - simuluje odoslanie emailu.
    Bude nahradená reálnym src/sender.py s Brevo integráciou.
    """
    print(f"      [MOCK] Subject: {subject}")
    print(f"      [MOCK] Mód: {MODE}")
    if MODE == "development":
        print(f"      [MOCK] Príjemca: {TEST_EMAIL}")
    else:
        print("      [MOCK] Príjemcovia: celý contact list")
    return True


# ===========================================
# Spustenie
# ===========================================

if __name__ == "__main__":
    # Spusti pipeline
    success = run_newsletter_pipeline()
    
    # Exit code pre GitHub Actions
    # 0 = úspech, 1 = chyba
    sys.exit(0 if success else 1)
