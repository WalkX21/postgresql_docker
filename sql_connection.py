from sqlalchemy import create_engine, text
# Connection string
conn_string = "postgresql+psycopg2://gitpod:mysecretpassword@172.17.0.2:5432/mydatabase"

# Create an engine
engine = create_engine(conn_string)

# Connect and execute a query
with engine.connect() as connection:
    # Use text() to wrap the raw SQL query
    query = text("SELECT * FROM persons")
    result = connection.execute(query)
    
    # Fetch and print results
    for row in result:
        print(row)