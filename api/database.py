from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

dotenv_path = "/Users/houleyeanne/Documents/FinSent/api/FINSENT_DB_PASSWORD.env"  # ou "../FINSENT_DB_PASSWORD.env" selon dossier
loaded = load_dotenv(dotenv_path=dotenv_path)
password = os.getenv("FINSENT_DB_PASSWORD")
engine = create_engine(f"mysql+pymysql://root:{password}@127.0.0.1/finsent_db")