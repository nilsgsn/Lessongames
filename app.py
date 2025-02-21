import streamlit as st
import random

# Farben definieren
primary_color = "rgb(0, 171, 215)"  # Schulfarbe Blau
secondary_color = "rgb(59, 135, 156)"  # Sanftes Blaugrün
tertiary_color = "rgb(187, 102, 165)"  # Sanftes Lila
background_color = "rgb(240, 240, 240)"  # Hellgrau

# Stile anpassen
st.markdown(
    f"""
    <style>
        body {{ background-color: {background_color}; }}
        .stApp {{ color: black; }}
        .sidebar .sidebar-content {{ background-color: {secondary_color}; }}
        .stButton>button {{ background-color: {primary_color}; color: white; }}
        .stSelectbox>div {{ background-color: white; }}
        .footer {{ position: fixed; bottom: 0; width: 100%; background-color: {tertiary_color}; text-align: center; padding: 10px; }}
    </style>
    """,
    unsafe_allow_html=True
)

# Datenbanken für die Fächer
exercises = {
    "Englisch": [
        {"name": "20 Questions", "category": "Speaking", "grade": "7-10", "instructions": "One student thinks of a word, others ask yes/no questions to guess it."},
        {"name": "Word Association", "category": "Vocabulary", "grade": "5-9", "instructions": "Students say words related to a given topic in a circle."},
        # Weitere Englisch-Übungen...
    ],
    "Mathe": [
        {"name": "Zahlen-Bingo", "category": "Rechnen", "grade": "5-7", "instructions": "Lehrkraft nennt Aufgaben, Schüler markieren Ergebnisse auf Bingo-Karten."},
        {"name": "Peng", "category": "Kopfrechnen", "grade": "6-8", "instructions": "Zahlenreihe vorgeben, falsche Zahlen müssen erkannt werden."},
        # Weitere Mathe-Übungen...
    ],
    "Deutsch": [],
    "Naturwissenschaften": [],
    "Geschichte": [],
    "Geographie": [],
    "Sport": [],
    "Informatik": []
}

# Sidebar für Fächerauswahl
st.sidebar.title("Fach auswählen")
selected_subject = st.sidebar.selectbox("", list(exercises.keys()))

# Dropdowns für Kategorie und Klassenstufe
categories = list(set(ex["category"] for ex in exercises[selected_subject]))
grades = list(set(ex["grade"] for ex in exercises[selected_subject]))

selected_category = st.sidebar.selectbox("Kategorie wählen", categories)
selected_grade = st.sidebar.selectbox("Klassenstufe wählen", grades)

# Gefilterte Übungen anzeigen
filtered_exercises = [ex for ex in exercises[selected_subject] if ex["category"] == selected_category and ex["grade"] == selected_grade]

if filtered_exercises:
    exercise = random.choice(filtered_exercises)
    st.write(f"### {exercise['name']}")
    st.write(f"**Kategorie:** {exercise['category']}")
    st.write(f"**Klassenstufe:** {exercise['grade']}")
    st.write(f"**Anleitung:** {exercise['instructions']}")
else:
    st.write("Keine Übungen für diese Auswahl gefunden.")

# Footer mit Schullogo und Name
st.markdown(
    f"""
    <div class='footer'>
        <img src=school_logo.png' width='100'>
        <p>Created by Mr Übach in collaboration with ChatGPT</p>
    </div>
    """,
    unsafe_allow_html=True
)
