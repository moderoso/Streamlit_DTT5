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
st.set_page_config(page_title= 'ONG - Passos Mágicos', layout='wide', page_icon=':gem:')

# Título da página
st.title('ONG - Passos Mágicos :woman-woman-girl-boy:✨')



st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
    )
side_bg_ext = 'pm.png'
sidebar_bg(side_bg)