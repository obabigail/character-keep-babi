import streamlit as st
from PIL import Image

st.set_page_config(
        page_title="DnD Keep",
        page_icon=":material/casino:",
    )
    
st.title("DnD Keep")

dnd_name, dnd_class, dnd_background, dnd_race, dnd_equipment, dnd_stats, dnd_traits, dnd_misc = st.tabs([
    "Name",
    "Class",
    "Background",
    "Race",
    "Equipment",
    "Stats",
    "Traits",
    "Miscelaneous"]
)

with dnd_name:
    st.header("Who is it?")
    st.subheader("Tell us your heroe's name!")
    st.caption("In the meantime, why not show their face as well? :)")

    character_name = st.text_input(placeholder="I am the mighty...", label="Identify yourself!")
    character_profile = st.file_uploader("I look into the mirror...", type=["png", "jpg", "jpeg", "gif", "webp"])

    if character_profile is not None:
        image = Image.open(character_profile)

        if image is not None:
            if image.format == "GIF":
                st.write("It's a GIF!")
            else:
                st.write(f"Image format: {image.format}")
    else:
        st.info("no file")

    st.markdown(f"# I am the mighty :rainbow[{character_name}]!")
    if character_profile is not None:
        st.image(character_profile, width=500)