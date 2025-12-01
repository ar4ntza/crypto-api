import base64
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# --------------------------- GENERACIÓN DE LLAVES RSA ---------------------------

# Función para generar llaves RSA (privada y pública) en formato PEM
def generate_rsa_keys():
    # Genera una llave privada RSA de 2048 bits con exponente público estándar 65537
    private = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Obtiene la llave pública asociada a la llave privada
    public = private.public_key()

    # Serializa la llave privada al formato PEM (PKCS8)
    # No se agrega contraseña (NoEncryption)
    pem_private = private.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Serializa la llave pública al formato PEM
    pem_public = public.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Regresa ambas llaves como strings (decodificando de bytes a texto)
    return pem_private.decode(), pem_public.decode()


# --------------------------- CIFRADO RSA ---------------------------

# Función para cifrar usando RSA-OAEP
def rsa_encrypt(public_key_pem: str, plaintext: str):
    # Carga la llave pública desde un string PEM
    public_key = serialization.load_pem_public_key(public_key_pem.encode())

    # Cifra el mensaje usando RSA con padding OAEP y SHA-256
    ciphertext = public_key.encrypt(
        plaintext.encode(),   # Se convierte el texto plano a bytes
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Generación de máscara MGF1 con SHA-256
            algorithm=hashes.SHA256(),                    # Hash principal para OAEP
            label=None                                    # No se usa etiqueta
        )
    )

    # Codifica el resultado en base64 para facilitar transporte en JSON
    return base64.b64encode(ciphertext).decode()


# --------------------------- DESCIFRADO RSA ---------------------------

# Función para descifrar usando RSA-OAEP
def rsa_decrypt(private_key_pem: str, ciphertext_b64: str):
    # Carga la llave privada desde el PEM proporcionado
    private_key = serialization.load_pem_private_key(private_key_pem.encode(), password=None)

    # Decodifica el texto cifrado desde base64 a bytes
    ciphertext = base64.b64decode(ciphertext_b64)

    # Descifra usando RSA-OAEP con SHA-256 (debe coincidir exactamente con el cifrado)
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Mismo MGF1
            algorithm=hashes.SHA256(),                    # Mismo hash
            label=None                                    # Misma etiqueta (ninguna)
        )
    )

    # Regresa el texto ya descifrado como string
    return plaintext.decode()
