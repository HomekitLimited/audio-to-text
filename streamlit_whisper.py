import streamlit as st
import whisper

st.set_page_config(page_title="Audio to Text Converter" , page_icon=":tada", layout="wide")

st.title("Whisper App")

audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])

model = whisper.load_model("small")
st.text("Whisper Model Loaded")


if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcrbing Audio")
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success("Transcription Complete")
        st.markdown(transcription["text"])
    else:
        st.sidebar.error("Please upload an Audio File")
        
st.sidebar.header("Play Original Audio File")
st.sidebar.audio(audio_file)

