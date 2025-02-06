# Importação da biblioteca streamlit
import streamlit as st
from auxiliar import apply_custom_style


if __name__ == '__main__':
        apply_custom_style()
		
#### Menu Superior
cols = st.columns(5, gap="large")
with cols[0]:
    st.image("images/pme.png")
with cols[1]:
    if st.button("Home"):
        st.switch_page("Home.py")
with cols[2]:
    if st.button("Estudo"):
        st.switch_page("pages/02 Estudo.py")
with cols[3]:
    if st.button("MVP"):
        st.switch_page("pages/03 MVP.py")
with cols[4]:
    if st.button("Conclusão"):
        st.switch_page("pages/05 Conclusao.py")
##with cols[5]:
    ##if st.button("Referências"):
        ##st.switch_page("pages/Referencias.py")
st.header("", divider="gray")

# Título da página
st.title('Dashboard e Storytelling')