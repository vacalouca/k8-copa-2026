import json

dados = {
    "proximo_jogo": {
        "mandante": "Brasil",
        "visitante": "Marrocos",
        "data": "2026-06-13",
        "hora": "13:00",
        "estadio": "MetLife Stadium"
    }
}

with open("dados.json", "w", encoding="utf-8") as f:
    json.dump(
        dados,
        f,
        ensure_ascii=False,
        indent=2
    )

print("dados.json atualizado")