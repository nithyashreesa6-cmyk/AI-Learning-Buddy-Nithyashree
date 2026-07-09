
import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="AI Learning Buddy Nithyashree",
    page_icon="📚"
)

st.title("📚 AI Learning Buddy Nithyashree")

st.write("Learn any topic with AI!")

topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("Generate"):

    if topic == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple beginner-friendly language."

        elif option == "Real-Life Example":
            prompt = f"Give a real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"Generate 5 multiple-choice questions with answers on {topic}."

        else:
            prompt = topic

        try:
            response = model.generate_content(prompt)
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
