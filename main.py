import pandas as pd
import json
from datetime import datetime

# =========================
# EXTRACT
# =========================

def extract_users():
    try:
        df = pd.read_csv("SDW2023.csv")
        if "id" in df.columns and "name" in df.columns:
            users = df.to_dict(orient="records")
        elif "UserID" in df.columns:
            users = [{"id": int(x), "name": f"Cliente {int(x)}"} for x in df["UserID"].tolist()]
        else:
            raise ValueError("Formato inválido do CSV.")
    except:
        # Caso não exista CSV, usa dados mock
        users = [
            {"id": 1, "name": "Naruto"},
            {"id": 2, "name": "Hinata"},
            {"id": 3, "name": "Sasuke"}
        ]

    for user in users:
        user["news"] = []

    return users


# =========================
# TRANSFORM
# =========================

def generate_message(user):
    messages = [
        f"{user['name']}, investir hoje garante segurança amanhã.",
        f"{user['name']}, faça seu dinheiro trabalhar para você.",
        f"{user['name']}, pequenos investimentos geram grandes resultados.",
        f"{user['name']}, planeje seus investimentos e conquiste liberdade financeira."
    ]
    return messages[user["id"] % len(messages)]


def transform_users(users):
    for user in users:
        message = generate_message(user)
        user["news"].append({
            "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
            "description": message
        })
    return users


# =========================
# LOAD
# =========================

def load_users(users):
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

    rows = []
    for user in users:
        for news in user["news"]:
            rows.append({
                "id": user["id"],
                "name": user["name"],
                "message": news["description"]
            })

    pd.DataFrame(rows).to_csv("output.csv", index=False)

    print("Pipeline executado com sucesso!")


# =========================
# MAIN
# =========================

def main():
    users = extract_users()
    users = transform_users(users)
    load_users(users)


if __name__ == "__main__":
    main()
