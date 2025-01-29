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
st.set_page_config(page_title= 'ONG - Passos Mágicos', layout='wide', page_icon=':gem:📊')

# Título da página
st.title('ONG - Passos Mágicos :woman-woman-girl-boy:✨')

page_bg_img = """
<style>
body {{
background-image: url("images/pm.png");
background-size: cover;
}}
</style>
"""

# Display the background image
st.markdown(page_bg_img, unsafe_allow_html=True)