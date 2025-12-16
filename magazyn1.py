import streamlit as st

# Tytuł aplikacji
st.title("📦 Prosty Magazyn")
st.write("Aplikacja do zarządzania listą produktów (w sesji).")

# --- Inicjalizacja stanu (bazy danych w pamięci) ---
# Sprawdzamy, czy lista produktów już istnieje w sesji. Jeśli nie, tworzymy pustą listę.
if 'produkty' not in st.session_state:
    st.session_state.produkty = []

# --- Sekcja 1: Dodawanie produktu ---
st.header("Dodaj produkt")
col1, col2 = st.columns([3, 1])

with col1:
    # Pole tekstowe do wpisania nazwy
    nowy_produkt = st.text_input("Nazwa produktu", key="input_produkt")

with col2:
    # Przycisk dodawania (wyrównany do doła kolumny dla estetyki)
    st.write("") # Pusty odstęp
    st.write("") 
    dodaj_btn = st.button("Dodaj")

if dodaj_btn:
    if nowy_produkt:
        # Dodanie do listy w sesji
        st.session_state.produkty.append(nowy_produkt)
        st.success(f"Dodano: {nowy_produkt}")
    else:
        st.warning("Wpisz nazwę produktu.")

st.divider() # Linia oddzielająca

# --- Sekcja 2: Lista produktów i Usuwanie ---
st.header("Stan Magazynu")

if st.session_state.produkty:
    # Wyświetlenie listy
    for produkt in st.session_state.produkty:
        st.text(f"• {produkt}")

    st.subheader("Usuń produkt")
    # Selectbox pozwala wybrać produkt do usunięcia
    produkt_do_usuniecia = st.selectbox("Wybierz produkt do usunięcia", st.session_state.produkty)
    
    if st.button("Usuń wybrany"):
        st.session_state.produkty.remove(produkt_do_usuniecia)
        st.experimental_rerun() # Odświeżenie strony, aby zaktualizować listę natychmiast
else:
    st.info("Magazyn jest pusty.")
