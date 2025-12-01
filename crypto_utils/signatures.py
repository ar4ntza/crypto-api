import base64
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import dsa

# -------------------------------------------------------------------
# Generación de llaves DSA (privada y pública) en formato PEM
# -------------------------------------------------------------------
def generate_dsa_keys():
    # Genera una llave privada DSA de 1024 bits (suficiente para práctica)
    private_key = dsa.generate_private_key(key_size=1024)

    # Obtiene la llave pública correspondiente
    public_key = private_key.public_key()

    # Serializa la llave privada a formato PEM con estándar PKCS8
    pem_private = private_key.private_bytes(
        serialization.Encoding.PEM,                # Formato PEM
        serialization.PrivateFormat.PKCS8,         # Estándar para llaves privadas
        serialization.NoEncryption()               # Sin contraseña
    )

    # Serializa la llave pública a formato PEM
    pem_public = public_key.public_bytes(
        serialization.Encoding.PEM,                # Formato PEM
        serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Regresa las dos llaves como cadenas de texto
    return pem_private.decode(), pem_public.decode()


# -------------------------------------------------------------------
# Firma digital usando DSA + SHA-256
# -------------------------------------------------------------------
def dsa_sign(private_key_pem: str, message: str):
    # Carga la llave privada desde el formato PEM recibido
    private_key = serialization.load_pem_private_key(
        private_key_pem.encode(), 
        password=None
    )

    # Firma el mensaje usando DSA con hash SHA-256
    signature = private_key.sign(
        message.encode(),     # El mensaje debe estar en bytes
        hashes.SHA256()       # Hash usado en el proceso de firma
    )

    # Retorna la firma codificada en base64 para transporte seguro
    return base64.b64encode(signature).decode()


# -------------------------------------------------------------------
# Verificación de firma DSA
# -------------------------------------------------------------------
def dsa_verify(public_key_pem: str, message: str, signature_b64: str):
    # Carga la llave pública desde el PEM recibido
    public_key = serialization.load_pem_public_key(public_key_pem.encode())

    # Decodifica la firma desde base64
    signature = base64.b64decode(signature_b64)

    try:
        # Verifica la firma:
        # - Firma en bytes
        # - Mensaje original en bytes
        # - Algoritmo hash usado
        public_key.verify(signature, message.encode(), hashes.SHA256())
        
        # Si no hay error, la firma es válida
        return True
    except:
        # Si falla la verificación (firma incorrecta o corrupta)
        return False
