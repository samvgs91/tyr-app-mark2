# Sample Streamlit + PostgreSQL App

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Configure `.env` for local dev or use `secrets_template.toml` for Streamlit Cloud.
3. Run PostgreSQL locally with `docker-compose up` (optional).
4. Start the app: `streamlit run app.py`

## Structure
- `app.py`: Main app
- `db/`: DB connection, schema, seed data
- `utils/`: Helper functions
- `data/`: Example data for upload/demo
