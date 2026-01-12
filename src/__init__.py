# ===========================================
# IB Newsletter - Source Package
# ===========================================
# Tento súbor označuje priečinok src/ ako Python package
# Umožňuje importovať moduly ako: from src.fetcher import ...
# ===========================================

# Verzia projektu
__version__ = "0.1.0"

# Čo sa exportuje pri "from src import *"
__all__ = [
    "fetcher",
    "processor", 
    "formatter",
    "sender",
]
