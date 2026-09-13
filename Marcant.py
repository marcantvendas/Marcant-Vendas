import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Configuração da página para ocupar a tela inteira
st.set_page_config(page_title="Portfólio de Vendas", layout="wide")

#Cabeçalho Principal
st.title("🛍️ Catálogo de Produtos")
st.caption("Confira as melhores ofertas e entre em contato direto pelo WhatsApp!")
st.divider()

#Barra Lateral (Filtros)
st.sidebar.header("Marcant Vendas")
st.sidebar.header("Filtros")
categoria = st.sidebar.selectbox("Categoria", ["Todos", "10''", "12''", "Cutelos", "Canivetes", "Mais vendidos ⭐"])
preco_max = st.sidebar.slider("Preço Máximo (R$)", 100, 300, 500)

foto_lateral = Image.open("marcos.jpeg")
st.sidebar.image(foto_lateral, use_container_width=True)

#Dados de exemplo dos produtos
produtos = [
    {"nome": "Faca de clubes 10'' Inox 4mm", "categoria": "10''", "preco": 180, "mais_vendido": True, "img": "https://images-cdn.kyte.site/v0/b/kyte-7c484.appspot.com/o/Mi1P3JDjxoaWcMpELIf35cnXlm82%2FjsEhRNBSPKKS58JxrVBEvg%3D%3D.jpg?alt=media"},
    {"nome": "Picanheira com desenho 10'' inox cabo resina e madeira", "categoria": "10''", "preco": 200, "img": "https://images-cdn.kyte.site/v0/b/kyte-7c484.appspot.com/o/Mi1P3JDjxoaWcMpELIf35cnXlm82%2FPbhTwzNClf21THuCV45Ow%3D%3D.jpg?alt=media"},
    {"nome": "Picanheira 10'' - Cabo com cápsula", "categoria": "10''", "preco": 200, "img": "https://images-cdn.kyte.site/v0/b/kyte-7c484.appspot.com/o/Mi1P3JDjxoaWcMpELIf35cnXlm82%2Fy8rDzjK5OWjg4Sd%2BLFdTJQ%3D%3D.jpg?alt=media"},
    {"nome": "Picanheira 10'' Inox - Cabo pata de cavalo, osso e madeira", "categoria": "10''", "preco": 200, "img": "https://images-cdn.kyte.site/v0/b/kyte-7c484.appspot.com/o/Mi1P3JDjxoaWcMpELIf35cnXlm82%2F6toHoRi1PmX8n4vV4%2BJLtw%3D%3D.jpg?alt=media"},
    {"nome": "Faca Chimango 10'' - Cabo chifre de cervo", "categoria": "10''", "preco": 200, "img": "https://images-cdn.kyte.site/v0/b/kyte-7c484.appspot.com/o/Mi1P3JDjxoaWcMpELIf35cnXlm82%2FOb%2B79iGkOcrjBpXJiI0Kpw%3D%3D.jpg?alt=media"},
    {"nome": "Faca chimango 10'' carbono 5mm - Cabo de madeira", "categoria": "10''", "preco": 150, "mais_vendido": False, "img": "https://images-cdn.kyte.site/v0/b/kyte-7c484.appspot.com/o/Mi1P3JDjxoaWcMpELIf35cnXlm82%2FXlrCYUhjzwcIdvhc0A7pQ%3D%3D.jpg?alt=media"},
    {"nome": "Faca Rambo rústica 10'' Carbono 5mm", "categoria": "10''", "preco": 190, "img": "https://images-cdn.kyte.site/v0/b/kyte-7c484.appspot.com/o/Mi1P3JDjxoaWcMpELIf35cnXlm82%2F%2BzcXayyHw2L8b6chjuqPGw%3D%3D.jpg?alt=media"},
    {"nome": "Facão Bowie fosfatizada 12'' - Cabo osso e madeira 4mm", "categoria": "12''", "preco": 210, "img": "https://images-cdn.kyte.site/v0/b/kyte-7c484.appspot.com/o/Mi1P3JDjxoaWcMpELIf35cnXlm82%2Fa3N17WKoSk7HY0CASRyRTA%3D%3D.jpg?alt=media"},
    {"nome": "Canivete Fosfatizado - Cabo madeira", "categoria": "Canivetes", "preco": 72, "mais_vendido": False, "img": "https://images-cdn.kyte.site/v0/b/kyte-7c484.appspot.com/o/Mi1P3JDjxoaWcMpELIf35cnXlm82%2FaLwkW6JLKnAgTycIrLI0qQ%3D%3D.jpg?alt=media"},
    {"nome": "Canivete Suíço com 17 funções", "categoria": "Canivetes", "preco": 60, "img": "https://images-cdn.kyte.site/v0/b/kyte-7c484.appspot.com/o/Mi1P3JDjxoaWcMpELIf35cnXlm82%2FB%2BUlfkIDx0X88a7fKlWX4w%3D%3D.jpg?alt=media"},

]

#Filtragem dos produtos
produtos_filtrados = [
    p for p in produtos
    if (
        categoria == "Todos"
        or p["categoria"] == categoria
        or (categoria == "Mais vendidos ⭐" and p.get("mais_vendido", False))
    )
    and p["preco"] <= preco_max
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
st.write("📧 marcantvendas@gmail.com")
st.write("💬 (24) 99994-1546")
