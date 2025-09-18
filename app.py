import streamlit as st
<<<<<<< HEAD
from auth.signup import show_signup_page 
from auth.login import show_login_page 
st.title("📘NoMoreCheat")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "Login"

# Sidebar Navigation
page = st.sidebar.selectbox("Select Page", ["Signup", "Login", "Exam", "Result"])
index = ["Signup", "Login", "Exam", "Result"].index(st.session_state.page)

# ------------ Signup --------------
if page == "Signup":  
    show_signup_page()
    
#-------------Login------------------    
elif page=="Login":
    show_login_page()
    
elif page=="Exam":
    if not st.session_state.het("logged in",False):
        st.error("⚠️ Please login first to access the exam.")
    
    else:
        st.header("📝 Exam Page")
        st.write(f"welcome **{st.session_state.username}**!")
    

    
=======

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
>>>>>>> 00f9c493df3824ccc3c9382fac3ed20faf10eca6
