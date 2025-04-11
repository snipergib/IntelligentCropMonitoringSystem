from sqlalchemy import create_engine

# 🔐 Direct credentials (Supabase PostgreSQL connection)
DB_USER = "postgres"
DB_PASS = "759243168"
DB_HOST = "db.ohoxmyshkdvctgilxdca.supabase.co"
DB_PORT = "5432"
DB_NAME = "postgres"

# ✅ Full connection URL (with SSL required by Supabase)
DATABASE_URL = f"postgresql://postgres:759243168@db.ohoxmyshkdvctgilxdca.supabase.co:5432/postgres?sslmode=require"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

def get_engine():
    return engine