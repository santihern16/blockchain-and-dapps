# Importamos la biblioteca hashlib que nos permite crear funciones hash criptográficas
import hashlib
# Importamos la biblioteca json para trabajar con datos en formato JSON
import json
# Importamos la funcionalidad RSA de la biblioteca Crypto para criptografía asimétrica
from Crypto.PublicKey import RSA
# Creamos una cadena de texto simple para demostrar el hashing
cadena = "Hola, como estas?" # Creamos la cadena de texto

# Creamos un objeto hash SHA-256 con la cadena convertida a bytes
# encode() convierte la cadena de texto a bytes (necesario para hashlib)
hash_obj = hashlib.sha256(cadena.encode()) # Pasamos la cadena a la funcion sha256

# Convertimos el hash binario a formato hexadecimal legible
# hexdigest() convierte los bytes del hash a una cadena hexadecimal
hash_hex = hash_obj.hexdigest() # es un método que convierte el hash binario (que es una secuencia de bytes) en una representación hexadecimal legible como texto

# Mostramos el hash hexadecimal de la cadena original
print(hash_hex)

# Creamos una lista de transacciones simulando un bloque de blockchain
# Cada transacción es un diccionario con remitente, destinatario y cantidad
transacciones = [
    {"from": "A", "to": "B", "amount": 5},  # Transacción 1: A envía 5 a B
    {"from": "C", "to": "D", "amount": 2},  # Transacción 2: C envía 2 a D
    {"from": "E", "to": "F", "amount": 1}   # Transacción 3: E envía 1 a F
]

# Creamos un diccionario que representa un bloque de blockchain
# Contiene las transacciones, un nonce (número usado en minería) y el hash del bloque anterior
bloque = {
    "transacciones": transacciones,  # Lista de transacciones del bloque
    "nonce": 1234,                   # Número usado en el proceso de minería
    "anterior_hash": "0000000000000000000000000000000000000000000000000000000000000000"  # Hash del bloque anterior (ceros para el primer bloque)
}

# Convertimos el bloque a formato JSON y luego a bytes
# json.dumps() convierte el diccionario a string JSON
# sort_keys=True asegura que las claves estén ordenadas (importante para consistencia)
# encode() convierte el string JSON a bytes
bloque_string = json.dumps(bloque, sort_keys=True).encode()

# Creamos un nuevo objeto hash SHA-256 con los datos del bloque
hash_obj = hashlib.sha256(bloque_string)

# Convertimos el hash del bloque a formato hexadecimal
hash_hex = hash_obj.hexdigest()

# Mostramos el hash hexadecimal del bloque completo
print(hash_hex)

# Creamos una nueva cadena de texto para demostrar otro ejemplo de hashing
mensaje = "Hola, blockchain"

# Creamos un objeto hash SHA-256 con el nuevo mensaje convertido a bytes
# encode() convierte la cadena de texto a bytes (requerido por hashlib)
hash_obj = hashlib.sha256(mensaje.encode())

# Convertimos el hash binario a formato hexadecimal legible
# hexdigest() convierte los bytes del hash a una cadena hexadecimal
hash_resultado = hash_obj.hexdigest()

# Mostramos el mensaje original para comparar
print("Mensaje original:", mensaje)

# Mostramos el hash hexadecimal generado a partir del mensaje
print("Hash generado:", hash_resultado)

# Generamos un par de claves RSA de 2048 bits
# RSA es un algoritmo de criptografía asimétrica que usa dos claves: pública y privada
key = RSA.generate(2048) # Genera un par de claves de 2048 bits

# Extraemos la clave pública del par de claves generado
# La clave pública se puede compartir y se usa para encriptar mensajes
public_key = key.publickey().export_key() # Obtiene la clave pública

# Extraemos la clave privada del par de claves generado
# La clave privada debe mantenerse secreta y se usa para desencriptar mensajes
private_key = key.export_key() # Obtiene la clave privada

# Mostramos la clave pública en formato legible (convertida de bytes a string)
print("Clave pública:", public_key.decode())

# Mostramos la clave privada en formato legible (convertida de bytes a string)
print("Clave privada:", private_key.decode())