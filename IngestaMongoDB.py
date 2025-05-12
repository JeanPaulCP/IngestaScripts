from pymongo import MongoClient
import boto3
import json

host = "98.81.227.242"       # IP pública de la EC2 donde corre Mongo
port = 27017                 # Puerto de Mongo
user = "root"
password = "utecmongodb"
database_name = "usuariosdb"
collection_name = "usuarios"

mongo_uri = f"mongodb://{user}:{password}@{host}:{port}/"
client = MongoClient(mongo_uri)
db = client[database_name]
collection = db[collection_name]

documentos = list(collection.find({}, {"_id": 0}))
json_filename = "usuarios.json"

with open(json_filename, "w") as f:
    json.dump(documentos, f, indent=4)

print("✅ Exportación a JSON completa.")

bucket_name = "ingesta-mongodb"
s3 = boto3.client("s3")

s3.upload_file(json_filename, bucket_name, json_filename)

print("Ingesta completada en S3.")
