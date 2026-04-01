import streamlit as st
from PIL import Image
from spire.pdf import *

sheet = "../character-keep-babi/data/5E_CharacterSheet_Fillable.pdf"

st.set_page_config(
        page_title="DnD Keep",
        page_icon=":material/casino:",
    )
    
st.title("DnD Keep")

dnd_name, dnd_class, dnd_background, dnd_race, dnd_equipment, dnd_stats, dnd_traits, dnd_misc, dnd_export = st.tabs([
    "Name",
    "Class",
    "Background",
    "Race",
    "Equipment",
    "Stats",
    "Traits",
    "Miscelaneous",
    "Export"]
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

with dnd_export:
    if character_name is not (None or ""):
        st.header("Behold...")
        st.subheader("You're ready to export your sheet!")
        st.caption("Adventure awaits. HUZZAH!")

        dnd_sheet = PdfDocument()
        dnd_sheet.LoadFromFile(sheet)

        first_page = dnd_sheet.Pages[0]

        font = PdfTrueTypeFont("Arial", 12.0, 0 , False)
        brush = PdfBrushes.get_Black()

        first_page.Canvas.DrawString(character_name, font, brush, 60.0, 65.0)
        dnd_sheet.SaveToFile(f"../character-keep-babi/data/{character_name}_D&D5E_Sheet.pdf")
        dnd_sheet.Close()

        with open(f"../character-keep-babi/data/{character_name}_D&D5E_Sheet.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(
            "Download character sheet",
            data=PDFbyte,
            file_name=f"{character_name}_D&D5E_Sheet.pdf",
            mime="application/pdf"
            )
    else:
        st.write("You need to finish you character's creation before exporting it!")
        st.caption("'Hey, I'm not even alive yet!'")