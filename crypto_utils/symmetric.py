import base64
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305


# ---------- AES-256-CBC ----------
def aes_cbc_encrypt(key_b64: str, iv_b64: str, plaintext: str):
    key = base64.b64decode(key_b64)   # llave en bytes
    iv = base64.b64decode(iv_b64)     # iv en bytes

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()

    # Padding PKCS7
    pad_len = 16 - (len(plaintext.encode()) % 16)
    padded = plaintext.encode() + bytes([pad_len] * pad_len)

    ciphertext = encryptor.update(padded) + encryptor.finalize()
    return base64.b64encode(ciphertext).decode()  # ciphertext en base64


def aes_cbc_decrypt(key_b64: str, iv_b64: str, ciphertext_b64: str):
    key = base64.b64decode(key_b64)
    iv = base64.b64decode(iv_b64)
    ciphertext = base64.b64decode(ciphertext_b64)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()

    padded = decryptor.update(ciphertext) + decryptor.finalize()

    # Remover padding PKCS7
    pad_len = padded[-1]
    plaintext = padded[:-pad_len]

    return plaintext.decode()


# ---------- ChaCha20-Poly1305 ----------
def chacha20_encrypt(key_b64: str, nonce_b64: str, plaintext: str):
    key = base64.b64decode(key_b64)
    nonce = base64.b64decode(nonce_b64)

    chacha = ChaCha20Poly1305(key)
    ciphertext = chacha.encrypt(nonce, plaintext.encode(), None)

    return base64.b64encode(ciphertext).decode()


def chacha20_decrypt(key_b64: str, nonce_b64: str, ciphertext_b64: str):
    key = base64.b64decode(key_b64)
    nonce = base64.b64decode(nonce_b64)
    ciphertext = base64.b64decode(ciphertext_b64)

    chacha = ChaCha20Poly1305(key)
    plaintext = chacha.decrypt(nonce, ciphertext, None)

    return plaintext.decode()


# ---------- Generate Keys ----------
def generate_aes_key_iv():
    key = os.urandom(32)   # 256 bits
    iv = os.urandom(16)    # bloque AES
    return base64.b64encode(key).decode(), base64.b64encode(iv).decode()


def generate_chacha_key_nonce():
    key = os.urandom(32)
    nonce = os.urandom(12)  # tamaño estándar ChaCha20
    return base64.b64encode(key).decode(), base64.b64encode(nonce).decode()
