import streamlit as st
import random

# --- Konfiguracja strony ---
st.set_page_config(page_title="Magazyn Gablotka", page_icon="🏭", layout="wide")

st.title("🏭 Magazyn z Gablotką")
st.write("Dodaj produkt, a system wylosuje mu unikalne emoji na podstawie pierwszej litery!")

# --- Funkcja pomocnicza: Losowanie emoji ---
def dobierz_emoji(nazwa_produktu):
    if not nazwa_produktu:
        return "📦"
    
    # Pobieramy pierwszą literę (małą)
    litera = nazwa_produktu[0].lower()
    
    # Słownik z pulą emoji dla popularnych liter (możesz go rozbudować)
    baza_emoji = {
        'a': ['🍎', '🥑', '🚑', '✈️', '🦍', '🎨'],
        'b': ['🍌', '💣', '🎈', '🏀', '🚲', '🥦'],
        'c': ['🍪', '🍫', '🚜', '🧢', '🌵', '🕯️'],
        'd': ['🍩', '🚪', '🦕', '🎲', '🥁', '💎'],
        'e': ['📧', '🔌', '🦅', '🍆', '🧪', '💶'],
        'k': ['🥝', '🔑', '🌵', '👑', '💻', '📷'],
        'l': ['🍋', '🔦', '🦁', '🍭', '💻', '🥬'],
        'm': ['🍈', '🚗', '🛵', '🐒', '🎙️', '🗺️'],
        'p': ['🍍', '🍕', '🍟', '🐼', '🖊️', '💊'],
        's': ['🍓', '🥪', '🥗', '🐍', '☀️', '👖'],
        't': ['🌮', '🍅', '🐅', '🚌', '🎾', '🔭'],
        'w': ['🍇', '🌊', '🐺', '⌚', '🔩', '🛀'],
        'z': ['🦓', '⌚', '🥔', '🏰', '🧩', '🦗']
    }
    
    # Domyślna pula dla liter, których nie ma w słowniku
    inne = ['📦', '🛒', '✨', '🏭', '🔖', '🧸', '⚙️', '🧱']
    
    # Wybierz listę pasującą do litery lub domyślną
    mozliwe_emoji = baza_emoji.get(litera, inne)
    
    # Wylosuj jeden element z listy
    return random.choice(mozliwe_emoji)

# --- Inicjalizacja stanu (Pamięć sesji) ---
if 'produkty' not in st.session_state:
    st.session_state.produkty = [] 
    # Teraz lista będzie przechowywać słowniki: {'nazwa': '...', 'emoji': '...'}

# --- Sekcja 1: Dodawanie produktu ---
with st.container(border=True):
    st.header("📝 Przyjęcie towaru")
    col1, col2 = st.columns([4, 1])

    with col1:
        nowy_produkt_nazwa = st.text_input("Nazwa produktu", key="input_produkt", placeholder="np. Banan, Cegła, Mleko")

    with col2:
        st.write("")
        st.write("")
        dodaj_btn = st.button("➕ Do gabloty", use_container_width=True)

    if dodaj_btn:
        if nowy_produkt_nazwa:
            # 1. Losujemy emoji
            wylosowane_emoji = dobierz_emoji(nowy_produkt_nazwa)
            
            # 2. Tworzymy obiekt produktu
            nowy_obiekt = {
                'nazwa': nowy_produkt_nazwa,
                'emoji': wylosowane_emoji
            }
            
            # 3. Dodajemy do listy
            st.session_state.produkty.append(nowy_obiekt)
            st.success(f"Dodano do gabloty: {wylosowane_emoji} {nowy_produkt_nazwa}")
        else:
            st.warning("⚠️ Wpisz nazwę produktu.")

st.divider()

# --- Sekcja 2: Gablotka (Wyświetlanie) ---
st.header("📦 Gablotka Magazynowa")

if st.session_state.produkty:
    # Licznik
    st.caption(f"Stan magazynowy: {len(st.session_state.produkty)} szt.")

    # TWORZENIE SIATKI (GRID) - 4 kolumny
    cols = st.columns(4)
    
    for i, produkt in enumerate(st.session_state.produkty):
        # Wybierz kolumnę cyklicznie (0, 1, 2, 3, 0, 1...)
        col = cols[i % 4]
        
        with col:
            # Wyświetlamy produkt w ramce (container border)
            with st.container(border=True):
                # Duże emoji na środku
                st.markdown(f"<h1 style='text-align: center;'>{produkt['emoji']}</h1>", unsafe_allow_html=True)
                # Nazwa produktu pod spodem
                st.markdown(f"<p style='text-align: center;'><b>{produkt['nazwa']}</b></p>", unsafe_allow_html=True)
                
                # Przycisk usuwania (mały)
                if st.button("Usuń", key=f"del_{i}", use_container_width=True):
                    st.session_state.produkty.pop(i)
                    st.rerun()

else:
    st.info("📭 Gablotka jest pusta. Dodaj coś powyżej!")
