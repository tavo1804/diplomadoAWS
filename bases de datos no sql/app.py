import boto3

#crear cliente para dynamodb

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')
tabla = dynamodb.Table('tabla-gustavo-velasquez')

#Leer un elemento de la tabla 
response = tabla.get_item(Key={'id':'2'})
print(response['Item'])

#Leer todos los elementos de la tabla 
response = tabla.scan()
print(response['Items'])


# Insertar nuevo registro
nuevo_item = {
    
    "id": "3",
    "ciudad": "Cali",
    "nombre": "juan"
}

# Insertar el nuevo registro en la tabla
tabla.put_item(Item=nuevo_item)

print("Nuevo registro insertado exitosamente.")


#Actualizar el atributo sin utilizar tabla.put_item 

# Parámetros para identificar el elemento y actualizar el atributo
key = {
    "id": "3"
}
update_expression = "SET ciudad = :val"
expression_attribute_values = {
    ":val": "medellin"
}

# Actualizar el atributo
response = tabla.update_item(
    Key=key,
    UpdateExpression=update_expression,
    ExpressionAttributeValues=expression_attribute_values
)

print("Atributo actualizado exitosamente.")
