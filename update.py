import json

dados = {
    "proximo_jogo": {
        "mandante": "Brasil",
        "visitante": "Marrocos",
        "data": "13/06/2026",
        "hora": "13:00",
        "estadio": "MetLife Stadium"
    },

    "jogos_brasil": [
        {
            "data": "13/06/2026",
            "mandante": "Brasil",
            "visitante": "Marrocos",
            "status": "Agendado"
        },
        {
            "data": "19/06/2026",
            "mandante": "Brasil",
            "visitante": "Haiti",
            "status": "Agendado"
        },
        {
            "data": "24/06/2026",
            "mandante": "Escócia",
            "visitante": "Brasil",
            "status": "Agendado"
        }
    ]
}

with open("dados.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=2)

print("dados.json atualizado")