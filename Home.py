# Importação das bibliotecas
import streamlit as st
import pandas as pd

import altair as alt
from plotly.colors import n_colors
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar

# Configuração da página
st.set_page_config(page_title= 'ONG - Passos Mágicos', layout='wide', page_icon='📊')

# Título da página
st.title('ONG - Passos Mágicos :woman-woman-girl-boy:')


import streamlit as st
from streamlit_navigation_bar import st_navbar


st.set_page_config(initial_sidebar_state="collapsed")

pages = ["Home", "Library", "Tutorials", "Development", "Download"]
styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

page = st_navbar(pages, styles=styles)
st.write(page)

with st.sidebar:
    st.write("Sidebar")