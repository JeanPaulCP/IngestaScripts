import mysql.connector
import pandas as pd
import boto3

host = "98.81.227.242" # IP pública de la instancia EC2
port = 8005
user = "root"
password = "utecmysql"
database = "usuariosdb"

# Conexión a la base de datos
conn = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

query = "SELECT * FROM usuarios"
df = pd.read_sql(query, conn)
conn.close()

csv_filename = "usuarios.csv"
df.to_csv(csv_filename, index=False)

print("Exportación a CSV completa.")

bucket_name = "ingesta-mysql"
s3 = boto3.client('s3')

s3.upload_file(csv_filename, bucket_name, csv_filename)

print("Ingesta completada en S3")