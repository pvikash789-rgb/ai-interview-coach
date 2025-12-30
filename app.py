import streamlit as st

st.set_page_config(page_title="AI Interview Coach", layout="centered")

st.title("AI Interview Coach")
st.subheader("Practice interview answers with structured AI feedback")

st.markdown("""
You can **type your answer** or use **device-level voice dictation** to speak your response.
""")

question_type = st.selectbox(
    "Select question type",
    ["Behavioral (STAR)", "Product Sense"]
)

st.markdown("### Interview Question")
st.info("Tell me about a time you had to influence stakeholders without authority.")

answer = st.text_area(
    "Your Answer",
    height=200,
    placeholder="You can type here or use your device’s voice dictation..."
)

if st.button("Evaluate Answer"):
    st.success("Answer submitted for evaluation (AI coming next).")

