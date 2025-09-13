import streamlit as st

st.title("📘 ExamAI Online System")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "Login"

# Sidebar navigation (controlled by session_state)
page = st.sidebar.selectbox(
    "Select Page", ["Login", "Exam", "Result"],
    index=["Login", "Exam", "Result"].index(st.session_state.page)
)

# ---------------- Login Page ---------------- #
if page == "Login":
    st.header("🔑 Login to ExamAI")

    username = st.text_input("👤 Username")
    password = st.text_input("🔒 Password", type="password")

    if st.button("Login"):
        if username == "" or password == "":
            st.error("⚠️ Username and Password are required!")
        else:
            st.success("✅ Login Successful (demo)")
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.page = "Exam"   # Redirect to Exam
            st.rerun()

# ---------------- Exam Page ---------------- #
elif page == "Exam":
    
    if not st.session_state.logged_in:
        st.error("⚠️ Please login first to access the exam.")
        st.session_state.page = "Login"
        st.rerun()
    else:
        st.header("📝 Exam Page")
        st.write(f"👋 Welcome **{st.session_state.username}**!")
        st.write("Q1. Example Question: 2 + 2 = ?")
        answer = st.text_input("Your Answer")
        if st.button("Submit Answer"):
            st.success("Answer submitted (dummy)")

# ---------------- Result Page ---------------- #
elif page == "Result":
    if not st.session_state.logged_in:
        st.error("⚠️ Please login first to view results.")
        st.session_state.page = "Login"
        st.rerun()
    else:
        st.header("📊 Result")
        st.write("Your Score: 0 (dummy)")
