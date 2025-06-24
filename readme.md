# 🪙 Crypto History CLI App

This is a Python-based CLI tool to fetch historical cryptocurrency data from the [CoinGecko API](https://www.coingecko.com/en/api) and optionally persist it into a local PostgreSQL database.

## 📦 Requirements

* Python **<= 3.12**
* Docker & Docker Compose
* `pip` (Python package installer)

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Create a Virtual Environment

Make sure you are using Python 3.12 or lower:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Configure API Token

This application requires a CoinGecko API token. Add the following line to your `.env` file:

```env
export API_TOKEN=your_token_here
```

### 4. Start Services & Install Dependencies

Use the provided `init.sh` script to:

* Spin up the PostgreSQL database using Docker Compose
* Install Python dependencies
* Load environment variables
* Run the app

```bash
chmod +x init.sh
./init.sh
```

## 🛠 How It Works

The app takes **4 CLI arguments**:

```bash
python app/main.py <coin> <start_date> <end_date> <persist>
```

### Example

```bash
python app/main.py bitcoin 2024-05-01 2024-05-31 y
```

### Arguments

| Argument       | Description                                                                  |
| -------------- | ---------------------------------------------------------------------------- |
| `<coin>`       | A valid CoinGecko coin ID (e.g., `bitcoin`, `ethereum`)                      |
| `<start_date>` | The start date in `YYYY-MM-DD` format (max 1 year in the past)               |
| `<end_date>`   | The end date in `YYYY-MM-DD` format (must be within one month of start date) |
| `<persist>`    | `y` to persist data into PostgreSQL, any thing else to skip persistence      |

### Output

* Raw API data is saved to `app/data/` as JSON files.
* If `persist=true`, data is saved into two tables:

  * `coin_history`
  * `coin_aggregates`

## 💃 Database

The PostgreSQL database is managed via Docker Compose. It's automatically started by `init.sh`.

* Database: `crypto`
* Tables: `coin_history`, `coin_aggregates`

Ensure your `.env` file contains the correct database credentials and your API token.

## 🔪 Testing

You can run your CLI app with test arguments to verify everything works as expected.

```bash
python app/main.py ethereum 2024-06-01 2024-06-30 y
```

## 📁 File Structure

```
├── app/
│   ├── data/
│   ├── sql/                 
│       |── ddl/
│       |   ├── coin_aggregates.sql
│       |   ├── coin_history.sql
│       └── update_aggregates.sql
│   ├── cli_app.py
│   ├── db_uploader.py
│   ├── extractor.py
│   ├── main.py
│   ├── models.py
│   └── utils.py
│ 
├── requirements.txt
├── docker-compose.yml
├── .gitignore
├── .env
├── init.sh
└── README.md
```