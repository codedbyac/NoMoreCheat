import streamlit as st

# Title
st.title("ExamAI - Online Exam System")

# Sidebar for navigation
page = st.sidebar.selectbox("Select Page", ["Login", "Exam", "Result"])

# Login Page
if page == "Login":
    st.header("Login")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")
    if st.button("Login"):
        st.success("Login successful (dummy)")  # abhi ke liye demo

# Exam Page
elif page == "Exam":
    st.header("Exam Page")
    st.write("Q1. Example Question: 2 + 2 = ?")
    answer = st.text_input("Your Answer")
    if st.button("Submit Answer"):
        st.success("Answer submitted (dummy)")

# Result Page
elif page == "Result":
    st.header("Result")
    st.write("Your Score: 0 (dummy)")
