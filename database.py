from sqlalchemy import create_engine

# 🔐 Direct credentials (Supabase PostgreSQL connection)
DB_USER = "USERNAME"
DB_PASS = "PASS"
DB_HOST = "SUPABASE-LINK"
DB_PORT = "PORT-NO"
DB_NAME = "postgres"

# ✅ Full connection URL (with SSL required by Supabase)
DATABASE_URL = "DATABASE-URL"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

def get_engine():

    return engine
