from fastapi import FastAPI
from pydantic import BaseModel

# Se importan utilidades criptográficas personalizadas organizadas por módulo.
# hashing        → funciones de hashing seguro (SHA-256, Argon2)
# symmetric      → cifrado simétrico (AES-CBC, ChaCha20)
# asymmetric     → cifrado asimétrico (RSA)
# signatures     → firma y verificación digital (DSA)

from crypto_utils.hashing import sha256_hash, argon2_hash, argon2_verify
from crypto_utils.symmetric import (
    aes_cbc_encrypt, aes_cbc_decrypt,
    chacha20_encrypt, chacha20_decrypt,
    generate_aes_key_iv, generate_chacha_key_nonce
)
from crypto_utils.asymmetric import (
    generate_rsa_keys, rsa_encrypt, rsa_decrypt
)
from crypto_utils.signatures import (
    generate_dsa_keys, dsa_sign, dsa_verify
)

# Se crea la aplicación FastAPI.
app = FastAPI()

# ------------------ MODELOS DE DATOS ------------------
# Cada clase define un esquema que la API recibirá en formato JSON.

class SHA256Req(BaseModel):
    text: str

class Argon2Req(BaseModel):
    password: str

class Argon2VerifyReq(BaseModel):
    password: str
    hashed: str

class AESCBCReq(BaseModel):
    key: str
    iv: str
    plaintext: str

class AESCBCDecReq(BaseModel):
    key: str
    iv: str
    ciphertext: str

class ChaChaReq(BaseModel):
    key: str
    nonce: str
    plaintext: str

class ChaChaDecReq(BaseModel):
    key: str
    nonce: str
    ciphertext: str

class RSAEncryptReq(BaseModel):
    public_key: str
    plaintext: str

class RSADecryptReq(BaseModel):
    private_key: str
    ciphertext: str

class DSASignReq(BaseModel):
    private_key: str
    message: str

class DSAVerifyReq(BaseModel):
    public_key: str
    message: str
    signature: str

# ------------------ RUTAS ------------------

# Ruta raíz de prueba para verificar que la API está funcionando.
@app.get("/")
def root():
    return {"msg": "API cryptography utilities is running."}

# ---------- HASH ----------
# Recibe texto y devuelve su hash con SHA-256.
@app.post("/api/hash/sha256")
def sha256_route(data: SHA256Req):
    return {"hash": sha256_hash(data.text)}

# Aplica Argon2 para generar un hash de contraseña.
@app.post("/api/hash/argon2")
def argon2_route(data: Argon2Req):
    return {"hash": argon2_hash(data.password)}

# Verifica si una contraseña coincide con un hash Argon2.
@app.post("/api/hash/argon2/verify")
def argon2_verify_route(data: Argon2VerifyReq):
    return {"valid": argon2_verify(data.password, data.hashed)}

# ---------- AES ----------
# Genera una llave AES y un vector de inicialización (IV).
@app.get("/api/keys/symmetric/aes")
def get_aes_keys():
    key, iv = generate_aes_key_iv()
    return {"key": key, "iv": iv}

# Cifra texto usando AES en modo CBC.
@app.post("/api/encrypt/aes_cbc")
def aes_encrypt_route(data: AESCBCReq):
    ciphertext = aes_cbc_encrypt(data.key, data.iv, data.plaintext)
    return {"ciphertext": ciphertext}

# Descifra un ciphertext AES-CBC.
@app.post("/api/decrypt/aes_cbc")
def aes_decrypt_route(data: AESCBCDecReq):
    plaintext = aes_cbc_decrypt(data.key, data.iv, data.ciphertext)
    return {"plaintext": plaintext}

# ---------- ChaCha20 ----------
# Genera clave y nonce para ChaCha20.
@app.get("/api/keys/symmetric/chacha20")
def get_chacha_keys():
    key, nonce = generate_chacha_key_nonce()
    return {"key": key, "nonce": nonce}

# Cifra texto con ChaCha20.
@app.post("/api/encrypt/chacha20")
def chacha_encrypt_route(data: ChaChaReq):
    ciphertext = chacha20_encrypt(data.key, data.nonce, data.plaintext)
    return {"ciphertext": ciphertext}

# Descifra texto cifrado con ChaCha20.
@app.post("/api/decrypt/chacha20")
def chacha_decrypt_route(data: ChaChaDecReq):
    plaintext = chacha20_decrypt(data.key, data.nonce, data.ciphertext)
    return {"plaintext": plaintext}

# ---------- RSA (asimétrico) ----------
# Genera llaves privadas y públicas RSA.
@app.get("/api/rsa/keys")
def rsa_keys():
    private, public = generate_rsa_keys()
    return {"private_key": private, "public_key": public}

# Cifra datos con la llave pública RSA.
@app.post("/api/encrypt/rsa")
def rsa_encrypt_route(data: RSAEncryptReq):
    return {"ciphertext": rsa_encrypt(data.public_key, data.plaintext)}

# Descifra datos con la llave privada RSA.
@app.post("/api/decrypt/rsa")
def rsa_decrypt_route(data: RSADecryptReq):
    return {"plaintext": rsa_decrypt(data.private_key, data.ciphertext)}

# ---------- DSA (firmas digitales) ----------
# Genera llaves DSA.
@app.get("/api/dsa/keys")
def dsa_keys():
    private, public = generate_dsa_keys()
    return {"private_key": private, "public_key": public}

# Firma un mensaje usando DSA.
@app.post("/api/sign/dsa")
def sign_dsa_route(data: DSASignReq):
    return {"signature": dsa_sign(data.private_key, data.message)}

# Verifica una firma digital DSA.
@app.post("/api/verify/dsa")
def verify_dsa_route(data: DSAVerifyReq):
    return {"valid": dsa_verify(data.public_key, data.message, data.signature)}


