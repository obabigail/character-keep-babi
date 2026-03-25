import streamlit as st

from .tabs import dnd_name, dnd_class, dnd_background, dnd_race, dnd_equipment, dnd_stats, dnd_traits, dnd_misc

def render_page() -> None:
    """Renderiza a Page Configurações do Projeto."""
    st.title("DnD Keep")

    tab_labels = [
        "Name",
        "Class",
        "Background",
        "Race",
        "Equipment",
        "Stats",
        "Traits",
        "Miscellaneous",
    ]
    tabs = st.tabs(tab_labels)

    with tabs[0]:
        dnd_name.render()

    with tabs[1]:
        dnd_class.render()

    with tabs[2]:
        dnd_background.render()

    with tabs[3]:
        dnd_equipment.render()

    with tabs[4]:
        dnd_stats.render()

    with tabs[5]:
        dnd_traits.render()

    with tabs[6]:
        dnd_misc.render()