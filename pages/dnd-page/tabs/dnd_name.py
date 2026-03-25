import streamlit as st

def render():
    st.subheader("Who is it?")
    st.caption("Tell us your heroe's name!")
    st.caption("In the meantime, why not show their face as well? :)")

    st.file_uploader(type=["png", "jpg", "jpeg", "gif", "webp"])
    character_name = st.text_input(placeholder="I am the mighty...")