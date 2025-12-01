import base64
from hashlib import sha256
from argon2 import PasswordHasher

# Se crea una instancia de PasswordHasher, que aplica Argon2id con parámetros seguros por defecto.
ph = PasswordHasher()


# ----------------------- SHA-256 -----------------------

# Función que genera un hash SHA-256 a partir de un texto.
def sha256_hash(text: str) -> str:
    # sha256() recibe bytes, por eso se usa encode().
    # hexdigest() convierte el hash binario a una cadena hexadecimal legible.
    return sha256(text.encode()).hexdigest()


# ----------------------- ARGON2: HASH -----------------------

# Función que genera el hash seguro de una contraseña usando Argon2id.
def argon2_hash(password: str) -> str:
    # ph.hash() administra parámetros como memoria, tiempo y paralelismo de Argon2.
    # Devuelve un string que incluye el algoritmo, parámetros, salt y hash final.
    return ph.hash(password)


# ----------------------- ARGON2: VERIFICACIÓN -----------------------

# Función que verifica si una contraseña coincide con un hash Argon2 almacenado.
def argon2_verify(password: str, hashed: str) -> bool:
    try:
        # verify() compara automáticamente:
        # - la contraseña ingresada
        # - el salt contenido en el hash
        # - los parámetros usados para generar el hash
        ph.verify(hashed, password)
        return True

    # Si la contraseña no coincide o el formato del hash es inválido, genera excepción.
    except:
        return False
