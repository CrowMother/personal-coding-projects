import json
import csv
import sqlite3
import os
from typing import Any, Dict, List
import pandas as pd
import Bot_App as bot

# Simulated Schwab JSON data (replace this with live API call in future)
sample_data = {
    "account": {
        "id": 12345678,
        "balance": {
            "cash": 5000,
            "securities": 25000,
            "total": 30000
        },
        "positions": [
            {
                "symbol": "AAPL",
                "quantity": 10,
                "price": 150.0
            },
            {
                "symbol": "TSLA",
                "quantity": 5,
                "price": 700.0
            }
        ]
    },
    "timestamp": "2025-04-03T12:00:00Z"
}


def print_json_tree(data: Any, indent: int = 0):
    spacing = '  ' * indent
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{spacing}{key}:")
            print_json_tree(value, indent + 1)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            print(f"{spacing}- [{i}]")
            print_json_tree(item, indent + 1)
    else:
        print(f"{spacing}{data}")


def print_json_keys(data: Any, indent: int = 0):
    spacing = '  ' * indent
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{spacing}{key}/")
            print_json_keys(value, indent + 1)
    elif isinstance(data, list):
        print(f"{spacing}[]")
        for item in data:
            print_json_keys(item, indent + 1)


def export_to_json(data: Dict, filename: str = "export.json", filepath: str = ".\export"):
    with open(os.path.join(filepath, filename), 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Exported JSON to {filename}")


def flatten_dict(d: Dict, parent_key: str = '', sep: str = '.') -> Dict:
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def export_positions_to_csv(data: List[Dict], filename: str = "positions.csv", filepath: str = ".\export"):
    extracted_rows = []
    for order in data:
        legs = order.get("orderLegCollection", [])
        for leg in legs:
            merged = {**order, **leg, "instrument": leg.get("instrument", {})}
            flat_row = flatten_dict(merged)
            extracted_rows.append(flat_row)

    if not extracted_rows:
        print("No positions found to export.")
        return

    with open(os.path.join(filepath, filename), 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=sorted(extracted_rows[0].keys()))
        writer.writeheader()
        writer.writerows(extracted_rows)
    print(f"Exported positions to {filename}")


def export_to_sqlite(data: List[Dict], db_name: str = "export/schwab_data.db"):
    os.makedirs(os.path.dirname(db_name), exist_ok=True)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    extracted_rows = []
    for order in data:
        legs = order.get("orderLegCollection", [])
        for leg in legs:
            merged = {**order, **leg, "instrument": leg.get("instrument", {})}
            flat_row = flatten_dict(merged)
            extracted_rows.append(flat_row)

    if not extracted_rows:
        print("No positions found to export to SQLite.")
        return

    # Dynamically create table schema based on flattened keys
    columns = sorted(extracted_rows[0].keys())
    columns_sql = ", ".join([f"[{col}] TEXT" for col in columns])
    cursor.execute(f"DROP TABLE IF EXISTS positions")
    cursor.execute(f"CREATE TABLE positions ({columns_sql})")

    for row in extracted_rows:
        placeholders = ", ".join(["?" for _ in columns])
        values = [str(row.get(col, '')) for col in columns]
        cursor.execute(f"INSERT INTO positions ({', '.join(['['+col+']' for col in columns])}) VALUES ({placeholders})", values)

    conn.commit()
    conn.close()
    print(f"Exported positions to SQLite DB: {db_name}")

FILTER = "FILLED"
TIME_DELTA = 168  # 7 days in hours

def menu():
    print("=== Schwab JSON Visualizer ===")
    print("1. use Schwab API")
    print("2. paste sample data")
    print("3. exit")
    choice = input("Enter your choice: ")
    return choice

def run(data):
    print("=== Raw JSON Hierarchy ===")
    print_json_tree(data)

    print("\n=== Key Structure Only ===")
    print_json_keys(data)

    print("\n=== Exporting Data ===")
    export_to_json(data)
    export_positions_to_csv(data)
    export_to_sqlite(data)
def main():
    while True:
        choice = menu()
        if choice == "1":
            client = bot.Schwab_client(
                    bot.util.get_secret("SCHWAB_APP_KEY", "config/.env"),
                    bot.util.get_secret("SCHWAB_APP_SECRET", "config/.env")
                )
            response = client.get_account_positions(FILTER, TIME_DELTA)
            run(response)
        elif choice == "2":
            data = input("Paste your JSON data here: ")
            try:
                data = json.loads(data)
                run(data)
            except json.JSONDecodeError:
                print("Invalid JSON data. Please try again.")
        elif choice == "3":
            print("Goodbye!")
            break
        


if __name__ == "__main__":
    main()
