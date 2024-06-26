import boto3

# Configura tu cliente de DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')  # Cambia 'us-west-2' por tu región

# Crear la tabla en modo bajo demanda
table_name = 'tabla-gustavo-velasquez-2'
attribute_definitions = [
    {
        'AttributeName': 'id',
        'AttributeType': 'S'
    }
]
key_schema = [
    {
        'AttributeName': 'id',
        'KeyType': 'HASH'  # Clave de partición
    }
]

# Crear la tabla
response = dynamodb.create_table(
    TableName=table_name,
    AttributeDefinitions=attribute_definitions,
    KeySchema=key_schema,
    BillingMode='PAY_PER_REQUEST'  # Modo de capacidad bajo demanda
)

print(f"Tabla {table_name} creada exitosamente.")


#eliminar la tabla 

table_name = 'tabla-gustavo-velasquez-2'
response = dynamodb.delete_table(TableName=table_name)
print(f"Tabla {table_name} eliminada exitosamente.")
