# Importação das bibliotecas
import streamlit as st
import pandas as pd

import altair as alt
from plotly.colors import n_colors
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(page_title= 'ONG - Passos Mágicos', layout='wide', page_icon='📊')

# Título da página
st.title('ONG - Passos Mágicos :woman-woman-girl-boy:')

option = st.selectbox(
...     'How would you like to be contacted?',
...     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)