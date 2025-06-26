import pyodbc

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost,1433;"
    "DATABASE=CorrespondenciaDB;"
    "UID=django_user;"
    "PWD=Django2024!;"
)
try:
    with pyodbc.connect(conn_str, timeout=5) as conn:
        print("✅ Conexión a SQL Server exitosa.")
except Exception as e:
    print("❌ Error al conectar:", e)
