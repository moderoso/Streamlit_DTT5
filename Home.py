# Importação das bibliotecas
import streamlit as st
import pandas as pd

import altair as alt
from plotly.colors import n_colors
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(page_title= 'ONG - Passos Mágicos', layout='wide', page_icon='📊')

# Título da página
st.title('ONG - Passos Mágicos :woman-woman-girl-boy:')


with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Sobre'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected