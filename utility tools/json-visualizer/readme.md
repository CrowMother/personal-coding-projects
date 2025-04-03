# Schwab JSON Visualizer

This Python utility ingests JSON data from the Schwab API (or manually pasted data), then visualizes it in various forms and exports the data for further analysis.

---

## 📦 Features

- ✅ Raw hierarchical JSON visualization in the terminal
- ✅ Key structure explorer (like a JSON sitemap)
- ✅ Export:
  - Pretty-printed `.json`
  - Flattened `.csv` (dynamic fields)
  - Dynamic schema `.sqlite` database
- ✅ Supports real Schwab API access or manual pasted JSON

---

## 🛠 Installation

1. **Clone the repo or copy the script** into a directory.

2. **Install dependencies**:
   ```bash
   pip install pandas 
   ```
3. **Optional Schwab API setup:**
    - create a .env file in a config/ folder
    - Add the following:
    ```ini
    SCHWAB_APP_KEY=your_key_here
    SCHWAB_APP_SECRET=your_secret_here
    ```
## 🚀 How to Use 
Run the program with:
```bash
python visualizer.py
```
You will be prompted with:
```markdown
=== Schwab JSON Visualizer ===
1. use Schwab API
2. paste sample data
3. exit
```
- Option 1 will use your Schwab API credentials to pull recent orders.

- Option 2 lets you paste any JSON (e.g., copied from an API or a file).

- Data will be printed visually, and also exported to the /export folder.

### 📂 Output Files

| File                   | Description                         |
|------------------------|-------------------------------------|
| `export/export.json`   | Raw JSON file (indented)            |
| `export/positions.csv` | Flattened order leg data            |
| `export/schwab_data.db`| SQLite database with all order info |

## 🧩 How to Modify

### 🔍 Want to change the data source?

Modify the `bot.Schwab_client()` or update the `sample_data` structure.

---

### 📊 Want more export formats?

You can add export functions for Excel (`.xlsx`), Parquet, or HTML.

---

### 🗂 Want to adjust fields?

Use the `flatten_dict()` function to modify how nesting is handled.

All exports auto-adapt to new keys — no hardcoded columns.

---

## 🧪 Dev Tips

- You can simulate a run using the `sample_data` object inside the script.
- The SQLite table will be dynamically created and overwritten each run.
- The folder `export/` will be created automatically if it doesn't exist.

---

## ✅ Example Use Case

Paste this JSON into **Option 2** when prompted:

## ✅ Example Use Case

Paste this JSON into **Option 2** when prompted:

```json
{
  "orderLegCollection": [
    {
      "instruction": "BUY_TO_OPEN",
      "quantity": 5,
      "instrument": {
        "symbol": "TSLA",
        "description": "Tesla Inc."
      }
    }
  ],
  "status": "FILLED",
  "price": 700,
  "enteredTime": "2025-04-03T12:00:00Z"
}
```
## 📧 Questions?
Feel free to reach out or modify and adapt the code for your needs.

Built to make Schwab data easier to inspect, search, and use.