# auth/signup.py
import streamlit as st

def show_signup_page():
    st.header("Signup Page")
    username=st.text_input("Username/Email")
    password=st.text_input("Password",type="password")
    btn=st.button("Sign up")
    
    if(btn):
        if username=="" or password=="":
            st.error("⚠️ Username and Password required!")
        else:
            st.success(f"✅ Account created for {username} (demo)")


