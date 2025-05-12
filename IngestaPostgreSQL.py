import psycopg2
import pandas as pd
import boto3

# Configuración de PostgreSQL
host = "98.81.227.242"    # IP pública de la EC2
port = 8006               # Puerto que hayas expuesto (ej. 8006:5432)
user = "postgres"         # Usuario (puede variar, por defecto es "postgres")
password = "utecpostgresql" # Tu contraseña
database = "usuariosdb"   # Nombre de la base de datos

conn = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    dbname=database
)

query = "SELECT * FROM usuarios"
df = pd.read_sql(query, conn)
conn.close()

csv_filename = "usuarios02.csv"
df.to_csv(csv_filename, index=False)
print(" Exportación a CSV completa.")

bucket_name = "ingesta-postgresql"  # Asegurate que el bucket exista
s3 = boto3.client('s3')

s3.upload_file(csv_filename, bucket_name, csv_filename)
print(" Ingesta completada en S3.")
