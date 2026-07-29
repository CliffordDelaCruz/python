from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:Bacteria01!@127.0.0.1:3306/world_layoffs")

with engine.connect() as conn:
    result = conn.execute("SELECT * FROM layoffs LIMIT 10")
    for row in result:
        print(row)