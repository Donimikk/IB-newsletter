1. Predmet a Rozsah Riešenia
Predmetom dodávky je plne automatizovaný backendový systém, ktorý zabezpečuje denný zber, inteligentné spracovanie a distribúciu spravodajského obsahu formou emailového newslettera. Systém funguje autonómne na cloudovej infraštruktúre bez potreby manuálneho zásahu prevádzkovateľa.

2. Architektonické Rozhodnutia a Technológie
Systém je navrhnutý ako Serverless architektúra s dôrazom na minimalizáciu prevádzkových nákladov a maximalizáciu spoľahlivosti doručenia.

Jadro systému (Backend): Python skript vykonávaný v cloudovom prostredí.

Hosting a Plánovanie: GitHub Actions (Cron Scheduler) – zabezpečuje spúšťanie v presne stanovený čas bez nutnosti dedikovaného servera.

AI Engine (Spracovanie): OpenAI GPT-4o-mini – zvolený pre optimálny pomer cena/výkon pre úlohy sumarizácie a formátovania textu.

Emailová Infraštruktúra: Brevo (Transactional SMTP) – zvolené pre zabezpečenie reputácie domény, DKIM/SPF podpisovanie a manažment odhlásení (Unsubscribe).

3. Funkčné Požiadavky
3.1 Modul: Zber Dát (Input)
Systém sa automaticky aktivuje 1x denne v stanovený čas (napr. 07:00 CET).

Systém vykoná dopyt na 3 definované externé zdroje (API alebo RSS feedy).

Resiliencia: V prípade nedostupnosti jedného zo zdrojov systém nesmie zlyhať, ale musí vygenerovať obsah zo zvyšných dostupných zdrojov.

3.2 Modul: AI Spracovanie a Syntéza
Systém agreguje surové textové dáta zo všetkých zdrojov.

Vykoná sémantickú analýzu a syntézu obsahu do jedného koherentného textu (nie len kopírovanie odstavcov).

Transformuje výstup do validného HTML formátu vhodného pre emailových klientov (nadpisy, odstavce, zvýraznenie kľúčových informácií).

Zabezpečuje konzistentný tón komunikácie (definovaný "Tone of Voice").

3.3 Modul: Distribúcia a Správa (Output)
Odoslanie vygenerovaného HTML obsahu na zoznam príjemcov.

Dynamické generovanie predmetu emailu (Subject line) na základe obsahu daného dňa.

Automatické vloženie povinnej pätičky s odkazom na odhlásenie z odberu.

4. Systémové Obmedzenia a Limity
4.1 Frekvencia a Reálny čas
Systém pracuje v dávkovom režime (Batch processing), nie v reálnom čase.

Spustenie prebieha 1x denne. Akákoľvek mimoriadna správa vydaná po spustení skriptu bude zahrnutá až v nasledujúcom cykle (na ďalší deň).

4.2 Dátová pamäť (Statelessness)
Systém je navrhnutý ako bezstavový. Neuchováva históriu predošlých newsletterov ani kontext udalostí starších ako aktuálny beh (pokiaľ nie je explicitne napojený na externú databázu, čo nie je v rozsahu verzie 1.0).



5. Správa Dát a Bezpečnosť (GDPR)
Rola dodávateľa: Sprostredkovateľ (Data Processor).

Uloženie kontaktov: Emailové adresy sú uložené výhradne v zabezpečenej databáze poskytovateľa emailových služieb (Brevo). Backendový skript kontakty neukladá, len iniciuje rozosielku.

Ochrana súkromia: Obsah komunikácie (newsletter) je verejný, neobsahuje personalizované údaje o príjemcovi (okrem technických hlavičiek pre odhlásenie).

6. Vylúčenia z rozsahu (Out of Scope)
Nasledujúce položky nie sú súčasťou tejto špecifikácie:

Automatizované postovanie na sociálne siete (Instagram/Facebook).

Vývoj a správa webovej stránky pre registráciu/zber emailov (klient dodáva existujúcu databázu alebo API prístup k zoznamu).

Archivácia starších vydaní newslettera na webe.

Grafické práce a dizajn loga (použije sa jednoduchá, čistá HTML šablóna).