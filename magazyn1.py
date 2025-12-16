import streamlit as st

# Konfiguracja strony (dodaje ikonkę i tytuł na karcie przeglądarki)
st.set_page_config(page_title="Magazyn", page_icon="🏭")

# Tytuł aplikacji z emoji
st.title("🏭 Prosty Magazyn")
st.write("Aplikacja do zarządzania listą produktów (dane w sesji).")

# --- Inicjalizacja stanu ---
if 'produkty' not in st.session_state:
    st.session_state.produkty = []

# --- Sekcja 1: Dodawanie produktu ---
st.header("📝 Dodaj nowy produkt")
col1, col2 = st.columns([3, 1])

with col1:
    # Emoji przy etykiecie pola
    nowy_produkt = st.text_input("🏷️ Nazwa produktu", key="input_produkt")

with col2:
    st.write("") 
    st.write("") 
    # Emoji na przycisku
    dodaj_btn = st.button("➕ Dodaj")

if dodaj_btn:
    if nowy_produkt:
        st.session_state.produkty.append(nowy_produkt)
        # Komunikat sukcesu z "checkiem"
        st.success(f"✅ Dodano pomyślnie: **{nowy_produkt}**")
    else:
        # Ostrzeżenie
        st.warning("⚠️ Proszę wpisać nazwę produktu.")

st.divider()

# --- Sekcja 2: Lista produktów i Usuwanie ---
st.header("📦 Stan Magazynu")

if st.session_state.produkty:
    # Wyświetlenie licznika produktów
    st.caption(f"Liczba produktów w magazynie: {len(st.session_state.produkty)}")

    # Wyświetlenie listy z ikonami pudełek
    for produkt in st.session_state.produkty:
        st.text(f"📦 {produkt}")

    st.markdown("---") # Lekki separator
    st.subheader("🗑️ Usuń produkt")
    
    # Wybór produktu do usunięcia
    produkt_do_usuniecia = st.selectbox("🔍 Wybierz produkt do usunięcia", st.session_state.produkty)
    
    # Czerwony przycisk (type="primary" wyróżnia go kolorem w Streamlit)
    if st.button(f"❌ Usuń {produkt_do_usuniecia}", type="primary"):
        st.session_state.produkty.remove(produkt_do_usuniecia)
        st.rerun() # Odświeżenie aplikacji (nowa komenda zamiast experimental_rerun)
else:
    # Komunikat, gdy lista jest pusta
    st.info("📭 Magazyn jest obecnie pusty.")
