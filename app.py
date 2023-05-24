import streamlit as st
from call2llm import get_response
import video_functions
# Function to generate the summaries
def generate_summary(video_url, summary_type, response_placeholder):
    video_id = video_functions.extract_video_id(video_url)
    transcript_url = video_functions.generate_transcript_url(video_id)
    transcript_text = video_functions.extract_text_from_transcript(transcript_url)
    prompt = f"Following is a transcript of youtube video: {transcript_text} Write {summary_type}"
    get_response(prompt, response_placeholder)

# Streamlit UI
st.title("3 Summarize")

# Text box for video ID
video_id = st.text_input("Enter Video URL")

# Button for 3-word summary
if st.button("3-Word Summary"):
    response_placeholder = st.empty()
    generate_summary(video_id, "3-word summary", response_placeholder)

# Button for 3-sentence summary
if st.button("3-Sentence Summary"):
    response_placeholder = st.empty()
    summary = generate_summary(video_id, "3-sentence summary", response_placeholder)
    st.write(summary)

# Button for 3-paragraph summary
if st.button("3-Paragraph Summary"):
    response_placeholder = st.empty()
    summary = generate_summary(video_id, "3-paragraph summary",response_placeholder)
    st.write(summary)

# Button for All notable points summary
if st.button("All Notable Points Summary"):
    response_placeholder = st.empty()
    summary = generate_summary(video_id, "notable-points", response_placeholder)
    st.write(summary)
