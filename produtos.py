# Arquivo: produtos.py
import random

# Listas de base para criar as combinações da Copa
categorias_copa = ["Decoração", "Vestuário", "Acessórios", "Festa"]
aplicativos = ["Shopee", "Mercado Livre", "AliExpress", "Amazon"]

links_apps = {
    "Shopee": "https://shopee.com.br",
    "Mercado Livre": "https://www.mercadolivre.com.br",
    "AliExpress": "https://www.aliexpress.com",
    "Amazon": "https://www.amazon.com.br"
}

# Imagens reais do Unsplash sobre futebol/torcida
imagens_copa = [
    "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=500&auto=format&fit=crop&q=60", # Bola de futebol
    "https://images.unsplash.com/photo-1518091043644-c1d4457512c6?w=500&auto=format&fit=crop&q=60", # Estádio/Torcida
    "https://images.unsplash.com/photo-1579952362874-468f71ba3a77?w=500&auto=format&fit=crop&q=60", # Futebol em campo
    "https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=500&auto=format&fit=crop&q=60"  # Jogador/Gramado
]

itens_base = [
    ("Bandeira Oficial do Brasil 1,50m", "Decoração"),
    ("Corneta Barulhenta do Brasil Vuvuzela", "Acessórios"),
    ("Kit Pintura Facial Verde e Amarelo", "Festa"),
    ("Camisa Torcedor Brasil Retrô", "Vestuário"),
    ("Caneca de Chopp Seleção Brasileira", "Festa"),
    ("Chapeu Cartola Verde e Amarelo", "Vestuário"),
    ("Balões Decorativos Copo do Mundo (Kit 50x)", "Decoração"),
    ("Mini Craque Colecionável de Jogador", "Acessórios"),
    ("Adesivos de Rosto Estrela do Brasil", "Festa"),
    ("Cachecol do Brasil Verde e Amarelo", "Vestuário")
]

lista_de_produtos = []

# Loop para gerar 104 produtos diferentes da Copa de forma automática!
for x in range(1, 11): # Repete o ciclo para criar variações
    for nome_base, categoria in itens_base:
        app_sorteado = random.choice(aplicativos)
        precio_sorteado = round(random.uniform(9.90, 39.90), 2) # Sempre menor que R$ 40
        
        lista_de_produtos.append({
            "nome": f"{nome_base} Edição #{x*10 + random.randint(1,9)}",
            "categoria": f"🏆 {categoria}",
            "imagem": random.choice(imagens_copa),
            "preco": f"R$ {precio_sorteado:.2f}".replace('.', ','),
            "app_mais_barato": f"🔰 Menor preço no app: {app_sorteado}",
            "link": links_apps[app_sorteado]
        })