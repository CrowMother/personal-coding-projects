import json
import pandas as pd
import os
from datetime import datetime
from Bot_App.core.schwab_client import SchwabClient
from Bot_App.core.database import store_orders, get_unposted_orders, mark_as_posted
from Bot_App.services.discord import send_discord_alert
from Bot_App.config.secrets import get_secret, str_to_bool

# Setup
EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

# Initialize client
app_key = get_secret("SCHWAB_APP_KEY", "config/.env")
app_secret = get_secret("SCHWAB_APP_SECRET", "config/.env")
client = SchwabClient(app_key, app_secret)

# Fetch data
orders = client.get_account_positions("FILLED", 168)
if not orders:
    print("No data fetched.")
    exit()

# Convert to DataFrame for CSV/JSON
df = pd.json_normalize(orders)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_path = os.path.join(EXPORT_DIR, f"schwab_orders_{timestamp}.csv")
json_path = os.path.join(EXPORT_DIR, f"schwab_orders_{timestamp}.json")
tree_path = os.path.join(EXPORT_DIR, f"schwab_orders_tree_{timestamp}.txt")

df.to_csv(csv_path, index=False)
df.to_json(json_path, orient="records", indent=2)

# Generate tree structure
def write_tree(obj, file, indent=0):
    prefix = "  " * indent
    if isinstance(obj, dict):
        for k, v in obj.items():
            file.write(f"{prefix}{k}:\n")
            write_tree(v, file, indent + 1)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            file.write(f"{prefix}- item {i}\n")
            write_tree(item, file, indent + 1)
    else:
        file.write(f"{prefix}{obj}\n")

with open(tree_path, "w") as f:
    write_tree(orders, f)

print(f"Exported:\n- CSV: {csv_path}\n- JSON: {json_path}\n- Tree: {tree_path}")
