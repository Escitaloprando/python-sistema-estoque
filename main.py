#Pegar os produtos que foram comprados, exportar os itens que compõem o produto e precisam ser separados e produzidos. Posteriormente adiconar a capacidade de checar com o estoque existente e exportar a quantidade a ser produzida 
import json

componentes = [
    {
        'Código': 0001,
        'Nome': 'Barra Fêmea-Ponteira',
        'Setor de origem': 'Mecânica',
        'Caracteristicas': 'Caracteristicas aqui',
    },
    {
        'Código': 0002,
        'Nome': 'Barra Macho-Fêmea',
        'Setor de origem': 'Mecânica',
        'Caracteristicas': 'Caracteristicas aqui',
    },
    {
        'Código': 0003,
        'Nome': 'Barra Macho-Ponteira',
        'Setor de origem': 'Mecânica',
        'Caracteristicas': 'Caracteristicas aqui',
    },
    {
        'Código': 0004,
        'Nome': 'Kit Suporte Simples',
        'Setor de origem': 'Mecânica',
        'Caracteristicas': '4 buchas, 4 parafusos, suporte lado esquerdo e lado direito',
    },
    {
        'Código': 0000,
        'Nome': 'NOME',
        'Setor de origem': 'Setor',
        'Caracteristicas': 'Caracteristicas aqui',
    },
]



produtos = {
    'Produto': [
        {
            'Código': 3141,
            'Nome': 'Suporte Simples Fundo de Parede D',
            'Componentes': [componentes.index],
        }

    ]
},