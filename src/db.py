import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()  # wczyta zmienne z .env

def get_engine():
    url = (
        f"postgresql+psycopg://{os.getenv('PGUSER')}:{os.getenv('PGPASSWORD')}"
        f"@{os.getenv('PGHOST')}:{os.getenv('PGPORT')}/{os.getenv('PGDATABASE')}"
    )
    return create_engine(url, pool_pre_ping=True)

if __name__ == "__main__":
    eng = get_engine()
    with eng.connect() as conn:
        print(conn.execute(text("select 'DB OK'")).scalar())
