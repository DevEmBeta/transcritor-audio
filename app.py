

import streamlit as st
import whisper
import tempfile

st.set_page_config(page_title="Transcritor de Áudio", layout="centered")

st.title("🎙️ Transcritor de Áudio com Whisper")

uploaded_file = st.file_uploader("Envie um arquivo de áudio (MP3, WAV, OGG)", type=["mp3", "wav", "ogg", "waptt.opus"])

@st.cache_resource
def load_model():
    return whisper.load_model("small") 

if uploaded_file is not None:
    # Salvar temporário
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(uploaded_file.getbuffer())
        temp_path = tmp.name

    st.info("⏳ Transcrevendo, aguarde...")
    model = load_model()
    result = model.transcribe(temp_path, language="pt")

    st.success("✅ Transcrição concluída!")
    st.text_area("Transcrição", result["text"], height=250)

    st.download_button(
        "⬇️ Baixar transcrição em TXT",
        result["text"],
        file_name="transcricao.txt"
    )


