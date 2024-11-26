import streamlit as st
from streamlit_option_menu import option_menu
import ogd_map

# https://icons.getbootstrap.com/?q=image
menu_icons = ["house", "table", "graph-up", "chat-dots"]

__version__ = "0.2.3"
__author__ = "Lukas Calmbach"
__author_email__ = "lcalmbach@gmail.com"
VERSION_DATE = "2024-11-22"
APP_NAME = "ODS-Maps"
GIT_REPO = "https://github.com/lcalmbach/ods-maps"


APP_INFO = f"""<div style="background-color:#34282C; padding: 10px;border-radius: 15px; border:solid 1px white;">
    <small>App von <a href="mailto:{__author_email__}">{__author__}</a><br>
    Version: {__version__} ({VERSION_DATE})<br>
    Quelle: <a href=https://data.bs.ch>data.bs</a><br>
    <a href="{GIT_REPO}">git-repo</a></small></div>
    """


def init():
    st.set_page_config(
        page_title=APP_NAME,
        page_icon="🗺️",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def main():
    init()
    if "map" not in st.session_state:
        with st.spinner("Daten werden geladen..."):
            st.session_state.map = ogd_map.Map()
    map = st.session_state.map
    with st.sidebar:
        st.title(f"{APP_NAME}")
        st.image("./map.png")
    map.layer_menu()
    

    st.sidebar.markdown(APP_INFO, unsafe_allow_html=True)


if __name__ == "__main__":
    main()


