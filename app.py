
import streamlit as st

from src.screen.home_screen import home_screen
from src.screen.teacher_screen import teacher_screen
from src.screen.student_screen import student_screen
from src.components.dialog_auto_enroll import auto_enroll_dialog


def main():
    if "login_type" not in st.session_state:
        st.session_state["login_type"] = None

    # Join code check
    join_code = st.query_params.get("join-code")

    if join_code and st.session_state.get("login_type") != "student":
        st.session_state["login_type"] = "student"
        st.rerun()

    # Screen selection
    match st.session_state["login_type"]:
        case "teacher":
            teacher_screen()

        case "student":
            student_screen()

        case None:
            home_screen()

    # Show enrollment dialog for logged-in student
    if (
        join_code
        and st.session_state.get("is_logged_in")
        and st.session_state.get("user_role") == "student"
    ):
        auto_enroll_dialog(join_code)


if __name__ == "__main__":
  main()
