import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Configuração da página para ocupar a tela inteira
st.set_page_config(page_title="Portfólio de Vendas", layout="wide")

#Cabeçalho Principal
st.title("🛍️ Catálogo de Produtos - Marcant")
st.caption("Confira as melhores ofertas e entre em contato direto pelo WhatsApp!")
st.divider()

#Barra Lateral (Filtros)
st.sidebar.header("Filtros")
categoria = st.sidebar.selectbox("Categoria", ["Todos", "10''", "12''", "Cutelos"])
preco_max = st.sidebar.slider("Preço Máximo (R$)", 100, 300, 500)

#Dados de exemplo dos produtos
produtos = [
    {"nome": "Cervinho língua de chimango chifre de cervo legítimo importado 10", "categoria": "10''", "preco": 200, "img": "https://images-cdn.kyte.site/v0/b/kyte-7c484.appspot.com/o/Mi1P3JDjxoaWcMpELIf35cnXlm82%2FOb%2B79iGkOcrjBpXJiI0Kpw%3D%3D.jpg?alt=media"},
    {"nome": "Chimango carbono 5mm 10 cabo madeira", "categoria": "10''", "preco": 150, "img": "https://images-cdn.kyte.site/v0/b/kyte-7c484.appspot.com/o/Mi1P3JDjxoaWcMpELIf35cnXlm82%2FXlrCYUhjzwcIdvhc0A7pQ%3D%3D.jpg?alt=media"},
    {"nome": "Faca de clubes linha nova 10 Inox 4mm", "preco": 180, "img": "https://images-cdn.kyte.site/v0/b/kyte-7c484.appspot.com/o/Mi1P3JDjxoaWcMpELIf35cnXlm82%2FjsEhRNBSPKKS58JxrVBEvg%3D%3D.jpg?alt=media"},
    {"nome": "Faca Rambo rústica 10 Carbono 5mm", "preco": 190, "img": "https://images-cdn.kyte.site/v0/b/kyte-7c484.appspot.com/o/Mi1P3JDjxoaWcMpELIf35cnXlm82%2F%2BzcXayyHw2L8b6chjuqPGw%3D%3D.jpg?alt=media"},
    {"nome": "Bowie fosfatizada cabo osso e madeira 4mm 12", "preco": 210, "img": "https://images-cdn.kyte.site/v0/b/kyte-7c484.appspot.com/o/Mi1P3JDjxoaWcMpELIf35cnXlm82%2Fa3N17WKoSk7HY0CASRyRTA%3D%3D.jpg?alt=media"},

]

#Filtragem dos produtos
produtos_filtrados = [
    p for p in produtos
    if (categoria == "Todos" or p["categoria"] == categoria) and p["preco"] <= preco_max
]
#Produtos em Grid (4 Colunas)
cols = st.columns(4)

for idx, prod in enumerate(produtos_filtrados):
    with cols[idx % 4]:
        st.image(prod["img"])
        st.subheader(prod["nome"])
        st.write(f"**R$ {prod['preco']:.2f}**")

        # Link dinâmico para mensagem no WhatsApp
        msg_wa = f"Olá, tenho interesse no produto: {prod['nome']}"
        link_wa = f"https://wa.me/5524999941546?text={msg_wa.replace(' ', '%20')}"

        st.link_button("💬 Encomendar via WhatsApp", link_wa)
        st.divider()

#Rodapé / Contato
st.markdown("---")
st.subheader("📬 Fale Conosco")
st.write("Dúvidas sobre entregas ou pagamento? Envie uma mensagem diretamente para nossa equipe.")
