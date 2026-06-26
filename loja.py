# Arquivo: loja.py
import streamlit as st
from produtos import lista_de_produtos 

# Configuração da página da Copa
st.set_page_config(page_title="Achadinhos da Copa do Mundo", page_icon="⚽", layout="wide")

# Estilização CSS temática Verde e Amarela
st.markdown("""
    <style>
    .titulo { text-align: center; font-size: 42px; font-weight: bold; color: #2E7D32; margin-bottom: 5px; }
    .subtitulo { text-align: center; font-size: 18px; color: #1565C0; margin-bottom: 30px; }
    .card { background-color: #F8F9FA; padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); text-align: center; min-height: 380px; }
    .nome-produto { font-size: 16px; font-weight: bold; color: #333333; margin-top: 10px; height: 50px; display: flex; align-items: center; justify-content: center; }
    .preco { font-size: 24px; font-weight: bold; color: #2E7D32; margin: 8px 0; }
    .badge-app { background-color: #E8F5E9; color: #2E7D32; font-weight: bold; padding: 4px 12px; border-radius: 20px; font-size: 11px; display: inline-block; margin-bottom: 12px; border: 1px solid #A5D6A7; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='titulo'>🇧🇷 LOJA DOS ACHADINHOS DA COPA</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>Mais de 100 produtos de torcedor pelo menor preço do mercado!</div>", unsafe_allow_html=True)

# --- SISTEMA DE PESQUISA E FILTROS ---
col_busca, col_filtro = st.columns([2, 1])

with col_busca:
    pesquisa = st.text_input("🔍 Digite o que você está procurando (ex: Corneta, Camisa):")

with col_filtro:
    categoria_selecionada = st.selectbox("📂 Filtrar por Categoria:", ["Todos os Produtos", "🏆 Decoração", "🏆 Vestuário", "🏆 Acessórios", "🏆 Festa"])

# Filtrando a lista gigante com base no que o usuário escolheu
produtos_filtrados = []
for prod in lista_de_produtos:
    # Filtro de texto e de categoria ao mesmo tempo
    if pesquisa.lower() in prod["nome"].lower() or pesquisa == "":
        if categoria_selecionada == "Todos os Produtos" or prod["categoria"] == categoria_selecionada:
            produtos_filtrados.append(prod)

st.write(f"Mostrando **{len(produtos_filtrados)}** produtos encontrados.")
st.write("---")

# --- EXIBIÇÃO EM GRADE DE 3 COLUNAS ---
if len(produtos_filtrados) > 0:
    for i in range(0, len(produtos_filtrados), 3):
        grupo = produtos_filtrados[i:i+3]
        colunas = st.columns(3)
        
        for indice, prod in enumerate(grupo):
            with colunas[indice]:
                st.markdown(f"""
                    <div class='card'>
                        <p style='color: #1565C0; font-size: 11px; font-weight: bold; text-transform: uppercase; margin: 0;'>{prod['categoria']}</p>
                        <div class='nome-produto'>{prod['nome']}</div>
                        <div class='preco'>{prod['preco']}</div>
                        <div class='badge-app'>{prod['app_mais_barato']}</div>
                    </div>
                """, unsafe_allow_html=True)
                st.image(prod['imagem'], use_container_width=True)
                st.link_button("🔥 Ver Oferta Barata", prod['link'], use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)
else:
    st.warning("Nenhum produto da Copa encontrado com esse nome. Tente outra palavra!")