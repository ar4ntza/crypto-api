Proyecto final. Desarrollo de backend criptográfico
Edna Samantha Cortés Carrizosa / Arantza García Vázquez 


~ Instrucciones para montar y ejecutar el proyecto ~

1. Colar el repositorio
    git clone <https://github.com/ar4ntza/crypto-api.git>
    cd <https://github.com/ar4ntza/crypto-api.git>

2. Crear el entorno virtual
    python -m venv venv

3. Activar el entorno
    venv\Scripts\activate

4. Instalar dependencias
    pip install -r requirements.txt

5. Ejecutar servidor
    uvicorn main:app --reload
    main = archivo principal del proyecto (main.py)
    app = instancia FastAPI

6. Acceder a la API
    http://127.0.0.1:8000/docs


~ Pruebas realizadas ~

entrada

{
  "text": "Hola, buen dia :)"
}


salida

{
  "hash": "a31e8c2a8d151ac41312d22058ed131824c9867be26e66735f5e42486cb1609a"
}

------------- ARGON 2 ----------------
Hash de contraseña y verificacion de la misma
Enhashing

entrada:

{
  "password": "iaQliquD"
}

salida

{
  "hash": "$argon2id$v=19$m=65536,t=3,p=4$3vfeHMXieRq5ab+S5wInZg$EWAsheSN8upcFrReMHfcn8AmgTTloc/DamWpqksXzOY"
}

entrada
{
  "password": "iaQliquD",
  "hashed": "$argon2id$v=19$m=65536,t=3,p=4$3vfeHMXieRq5ab+S5wInZg$EWAsheSN8upcFrReMHfcn8AmgTTloc/DamWpqksXzOY"
}

salida

{
  "valid": true
}

-------------- AES-256-CBC --------------
Operación requerida: Cifrar / Descifrar texto
OPERACION SIMETRICA
LLAVES

{
  "key": "QGMOGjP9LCWunlBvF3n/8UmMW13mZGu0RDZP7VHpfVY=",
  "iv": "IokanxIqqfIL+0kbZXtSdg=="
}

Encriptado

Entrada
{
  "key": "QGMOGjP9LCWunlBvF3n/8UmMW13mZGu0RDZP7VHpfVY=",
  "iv": "IokanxIqqfIL+0kbZXtSdg==",
  "plaintext": "Siembra"
}

Salida

{
  "ciphertext": "WU3lmNnRjh7eBVlt9ThXTg=="
}

Desencriptado

Entrada
{
  "key": "QGMOGjP9LCWunlBvF3n/8UmMW13mZGu0RDZP7VHpfVY=",
  "iv": "IokanxIqqfIL+0kbZXtSdg==",
  "ciphertext": "WU3lmNnRjh7eBVlt9ThXTg=="
}

Salida

{
  "plaintext": "Siembra"
}


------------ ChaCha20 ---------------
SIMETRICO
Operación requerida: Cifrar / Descifrar texto
LLAVES

{
  "key": "VRwObsGzPkkIfrsG0HQIaKyQsCLoguuXvPn1WtjL5rU=",
  "nonce": "jhsfKFyp75o+6Ro0"
}

Encriptado

Entrada
{
  "key": "VRwObsGzPkkIfrsG0HQIaKyQsCLoguuXvPn1WtjL5rU=",
  "nonce": "jhsfKFyp75o+6Ro0",
  "plaintext": "Espectador"
}

Salida
{
  "ciphertext": "HnVMcrZbnIurmMYmmRRSOPNf8zqRwEbV2sU="
}

Desencriptado

Entrada
{
  "key": "VRwObsGzPkkIfrsG0HQIaKyQsCLoguuXvPn1WtjL5rU=",
  "nonce": "jhsfKFyp75o+6Ro0",
  "ciphertext": "HnVMcrZbnIurmMYmmRRSOPNf8zqRwEbV2sU="
}

Salida

{
  "plaintext": "Espectador"
}

---------- RSA-OAEP --------------
ASIMETRICO

Llaves
{
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCtBSFTwvAfXe+C\n3QqWSWxrE+LD9lHUHq918iW29SCVHUBRj5hP7sm5kihXQSTsTCZMY7/PUW4iKNuY\nmxLW1gqUpKHcxkno0FEprwo8wb9aJUfRF7FoBDOdDxzdF+NbVMkKJ1vxMznQtTkK\n/WmNdt5rdZ69ANPtBmag+K/uUzXpCrI0mCgKDNgjRY8ZlXHH+dkplejZV5XvJqGO\n/iESBNMXy4LLM2FWrHwI9JJejzDv6Hs33mu+5KlMNGHeF27BIeIJUqwUnU1iHrw8\ng42HAfDPf/Yr2QPE5tyXvZLuiKYsDSTzhXJm9rDUHC9IRKCFq3vPDVzdGTfcqkMY\nnk3WMrzRAgMBAAECggEAF0dM7BmauAWp72fxADZhvWhgBrCR4uG8BrjtJRgG6bkV\nScPxoLOGdY66Gb88igRW1MlI6cpRcIwhu38Fwlzq8IPT+UG+ePHqMZsI3BLPPYAt\nkO7Ioi+KiDOb1Q1dPBEEuXaBMssLGM8BHT7qICvhkgCxukktukK1tSuwc/bDFpbu\nrqr7h3aRnB6WUc9VcO5QThEBG9miSyjkvqbz4SyjRvgxgzC4I7+w6zAi3EmxAHiP\nVlvEQbOxAJ9Bqvs103awzeJH6oLc+MR89SYeWy1fVKFn4kw7yrjpgbJRK0iXYhk9\nKnguYpczHzmIh9Xnd/CzLXoye+XP6UJ2SiRqnsORjwKBgQDVjPDXRy7ZGA7kz9pT\nmmU89dpUwokLG1kEu1Ap0gb/thdUkZShj7Vq8sfW9J7u86rZYsb1Kx5e0A+cnY/1\nktP2oQXScXyBrgHPqSsytUYpBXqq+3/6809DclDUPDTaXyZc8LQoa8WTyjgI5n3z\nwY45Kb0jOyNivpiGAE+5uoWggwKBgQDPabEm6VVSC0826cWXcSIgId5MDCi6y9BJ\nU34Lr4Wdgeq/umtHO36h3TIO6lnI8PldwIENsiFY+lfjtymKyNGE51UWPEjVPLcZ\nJusldlSYp1kkHmqYz11/BxcZ1+OBZbqDNfp6DWDwfUsm92aCF4HXo4vF9jS5UOyw\n3nPOVDLFGwKBgQCRtYo7iaFolabL7xrsQoPjVWk0vkvd3TofJWPsNRd7cRZ4KKE+\nn5zMrX03qU+sgWxIycIxVMtzLAoK9eNdT2L7fCFJ1w96OG2Z8La98bw+jzOE6PgJ\nFe02exC1z6LMgXHepop2rhpw3eDgCc1U/fN6A4W/PUHGxX+ypxG/C4rT2wKBgQDM\nQE7d/MWyp8R4VTnp6tUqQ2///7FUUkVpEDl+FHlGJJwh9tiSKzqG96bGHW4RfYx0\nEJCGBjbkwpMugj78lsoNUSnvXapzovjEYhkKqT6hnZshAHsExKBT6Y2MO5ek46MK\nd2uUKfyelyQc2WEvFyscScfpSI2fONv9SPNN6oicpQKBgAEWMJkvLNDVaFnFMl+S\n94LeeM2pPz0rMpvHMAAaeis7cDyKNGPI6L4m8aN0VuQUifiXbKntPh1AyMcUMyz1\na4kKABdAkVl9ip/qP6LjZvxnLIE/znBk0Kuhb2ZXkGX7qOhccI+w4N8SRk2S/Dt+\nsv2YiXTSpbxG5u7EaOdbUI+4\n-----END PRIVATE KEY-----\n",
  "public_key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArQUhU8LwH13vgt0Klkls\naxPiw/ZR1B6vdfIltvUglR1AUY+YT+7JuZIoV0Ek7EwmTGO/z1FuIijbmJsS1tYK\nlKSh3MZJ6NBRKa8KPMG/WiVH0RexaAQznQ8c3RfjW1TJCidb8TM50LU5Cv1pjXbe\na3WevQDT7QZmoPiv7lM16QqyNJgoCgzYI0WPGZVxx/nZKZXo2VeV7yahjv4hEgTT\nF8uCyzNhVqx8CPSSXo8w7+h7N95rvuSpTDRh3hduwSHiCVKsFJ1NYh68PIONhwHw\nz3/2K9kDxObcl72S7oimLA0k84VyZvaw1BwvSESghat7zw1c3Rk33KpDGJ5N1jK8\n0QIDAQAB\n-----END PUBLIC KEY-----\n"
}

Encriptado

{
  "public_key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArQUhU8LwH13vgt0Klkls\naxPiw/ZR1B6vdfIltvUglR1AUY+YT+7JuZIoV0Ek7EwmTGO/z1FuIijbmJsS1tYK\nlKSh3MZJ6NBRKa8KPMG/WiVH0RexaAQznQ8c3RfjW1TJCidb8TM50LU5Cv1pjXbe\na3WevQDT7QZmoPiv7lM16QqyNJgoCgzYI0WPGZVxx/nZKZXo2VeV7yahjv4hEgTT\nF8uCyzNhVqx8CPSSXo8w7+h7N95rvuSpTDRh3hduwSHiCVKsFJ1NYh68PIONhwHw\nz3/2K9kDxObcl72S7oimLA0k84VyZvaw1BwvSESghat7zw1c3Rk33KpDGJ5N1jK8\n0QIDAQAB\n-----END PUBLIC KEY-----\n",
  "plaintext": "Lealtad"
}

Salida

{
  "ciphertext": "V5ztxPguOnY0vPPNHrlZ3DCY+YKlBolnEUMlAbawblFEUQUEp8V9A1txB12K4xy9kC+Wrm2PjN6Oyr7SykjJeovANts39XEwWzCPa+vA4RJdkdyikMKkJcSB5rWhoudGj7nSa9v/AW4Gxww5vG+ATlLhceNlL+Gv/BBtjWQyL33PEp6+xiLlDpYldtVpliubAZLpmU8Ly1KNg5rEccYU7+enWIAN/WZUqKQSLvN+uHskFzlLpmSuP+G2SSav6w3NWYlI4mhQrqz6lBOr0nTPMlEZkg1b3UXXQdOnegTYyHeL80rSSZ6zN6upE2qgIfCaFteysVj4hD7PMh6HjDIp6g=="
}

Desencriptado

entrada
{
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCtBSFTwvAfXe+C\n3QqWSWxrE+LD9lHUHq918iW29SCVHUBRj5hP7sm5kihXQSTsTCZMY7/PUW4iKNuY\nmxLW1gqUpKHcxkno0FEprwo8wb9aJUfRF7FoBDOdDxzdF+NbVMkKJ1vxMznQtTkK\n/WmNdt5rdZ69ANPtBmag+K/uUzXpCrI0mCgKDNgjRY8ZlXHH+dkplejZV5XvJqGO\n/iESBNMXy4LLM2FWrHwI9JJejzDv6Hs33mu+5KlMNGHeF27BIeIJUqwUnU1iHrw8\ng42HAfDPf/Yr2QPE5tyXvZLuiKYsDSTzhXJm9rDUHC9IRKCFq3vPDVzdGTfcqkMY\nnk3WMrzRAgMBAAECggEAF0dM7BmauAWp72fxADZhvWhgBrCR4uG8BrjtJRgG6bkV\nScPxoLOGdY66Gb88igRW1MlI6cpRcIwhu38Fwlzq8IPT+UG+ePHqMZsI3BLPPYAt\nkO7Ioi+KiDOb1Q1dPBEEuXaBMssLGM8BHT7qICvhkgCxukktukK1tSuwc/bDFpbu\nrqr7h3aRnB6WUc9VcO5QThEBG9miSyjkvqbz4SyjRvgxgzC4I7+w6zAi3EmxAHiP\nVlvEQbOxAJ9Bqvs103awzeJH6oLc+MR89SYeWy1fVKFn4kw7yrjpgbJRK0iXYhk9\nKnguYpczHzmIh9Xnd/CzLXoye+XP6UJ2SiRqnsORjwKBgQDVjPDXRy7ZGA7kz9pT\nmmU89dpUwokLG1kEu1Ap0gb/thdUkZShj7Vq8sfW9J7u86rZYsb1Kx5e0A+cnY/1\nktP2oQXScXyBrgHPqSsytUYpBXqq+3/6809DclDUPDTaXyZc8LQoa8WTyjgI5n3z\nwY45Kb0jOyNivpiGAE+5uoWggwKBgQDPabEm6VVSC0826cWXcSIgId5MDCi6y9BJ\nU34Lr4Wdgeq/umtHO36h3TIO6lnI8PldwIENsiFY+lfjtymKyNGE51UWPEjVPLcZ\nJusldlSYp1kkHmqYz11/BxcZ1+OBZbqDNfp6DWDwfUsm92aCF4HXo4vF9jS5UOyw\n3nPOVDLFGwKBgQCRtYo7iaFolabL7xrsQoPjVWk0vkvd3TofJWPsNRd7cRZ4KKE+\nn5zMrX03qU+sgWxIycIxVMtzLAoK9eNdT2L7fCFJ1w96OG2Z8La98bw+jzOE6PgJ\nFe02exC1z6LMgXHepop2rhpw3eDgCc1U/fN6A4W/PUHGxX+ypxG/C4rT2wKBgQDM\nQE7d/MWyp8R4VTnp6tUqQ2///7FUUkVpEDl+FHlGJJwh9tiSKzqG96bGHW4RfYx0\nEJCGBjbkwpMugj78lsoNUSnvXapzovjEYhkKqT6hnZshAHsExKBT6Y2MO5ek46MK\nd2uUKfyelyQc2WEvFyscScfpSI2fONv9SPNN6oicpQKBgAEWMJkvLNDVaFnFMl+S\n94LeeM2pPz0rMpvHMAAaeis7cDyKNGPI6L4m8aN0VuQUifiXbKntPh1AyMcUMyz1\na4kKABdAkVl9ip/qP6LjZvxnLIE/znBk0Kuhb2ZXkGX7qOhccI+w4N8SRk2S/Dt+\nsv2YiXTSpbxG5u7EaOdbUI+4\n-----END PRIVATE KEY-----\n",
  "ciphertext": "V5ztxPguOnY0vPPNHrlZ3DCY+YKlBolnEUMlAbawblFEUQUEp8V9A1txB12K4xy9kC+Wrm2PjN6Oyr7SykjJeovANts39XEwWzCPa+vA4RJdkdyikMKkJcSB5rWhoudGj7nSa9v/AW4Gxww5vG+ATlLhceNlL+Gv/BBtjWQyL33PEp6+xiLlDpYldtVpliubAZLpmU8Ly1KNg5rEccYU7+enWIAN/WZUqKQSLvN+uHskFzlLpmSuP+G2SSav6w3NWYlI4mhQrqz6lBOr0nTPMlEZkg1b3UXXQdOnegTYyHeL80rSSZ6zN6upE2qgIfCaFteysVj4hD7PMh6HjDIp6g=="
}

salida

{
  "plaintext": "Lealtad"
}


----------- DSA --------------
ASIMETRICO

Keys

{
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIBSwIBADCCASwGByqGSM44BAEwggEfAoGBAOkkh2d/3JjdcZzx54REWkyorffS\nubrIp2lamHS0JE5aeYxJVglArQy/zTsBuRegvhFrbBRk57BDxIJnQnBBqH+pssK8\no0SkOm9P5ocTtyFNYrjoCTuYvyUuE37bxk8Isieii4Wnt7V0L+dr6k8nKdDshWaX\nbimc8uVpBrsYjbnBAhUAk4AnJffHtmRhd4Yr/+OcAVbD6skCgYEA165KKDARY17s\n9ZJ2CO1hWvxfOi8chbcmatzEikV/TzV/ez7zA/qx2lLJ0g1s9YabtYMkwTDZiaCf\nM30yZIrXpdUn7Kw1rHDuzN8+SP4IuxhN1gn1t6uw2klrRyr69Wdj03hgMJ/836Ur\ngqXN4SWNfvyNvLi/4HCrpWEpezie4HgEFgIUcTl3D4uUy1MzdkhRa6v5J0nj3J0=\n-----END PRIVATE KEY-----\n",
  "public_key": "-----BEGIN PUBLIC KEY-----\nMIIBtzCCASwGByqGSM44BAEwggEfAoGBAOkkh2d/3JjdcZzx54REWkyorffSubrI\np2lamHS0JE5aeYxJVglArQy/zTsBuRegvhFrbBRk57BDxIJnQnBBqH+pssK8o0Sk\nOm9P5ocTtyFNYrjoCTuYvyUuE37bxk8Isieii4Wnt7V0L+dr6k8nKdDshWaXbimc\n8uVpBrsYjbnBAhUAk4AnJffHtmRhd4Yr/+OcAVbD6skCgYEA165KKDARY17s9ZJ2\nCO1hWvxfOi8chbcmatzEikV/TzV/ez7zA/qx2lLJ0g1s9YabtYMkwTDZiaCfM30y\nZIrXpdUn7Kw1rHDuzN8+SP4IuxhN1gn1t6uw2klrRyr69Wdj03hgMJ/836UrgqXN\n4SWNfvyNvLi/4HCrpWEpezie4HgDgYQAAoGAfMtNRsn3DCQh560O1KAGGH2D6GqR\nVXp5B5jpHzltO1Z0tsnsIzk/gauCeKwFitozqyI38P/rPm0FebgsXhsOpgFfPuJL\nge5mr266qJrddKjiQxag2sDppQe2GAOXIZx+prpwPpGd14M4+YNpuPlQT3coLlvi\nPOllkixH28h8f8s=\n-----END PUBLIC KEY-----\n"
}

Firma 

Entrada
{
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIBSwIBADCCASwGByqGSM44BAEwggEfAoGBAOkkh2d/3JjdcZzx54REWkyorffS\nubrIp2lamHS0JE5aeYxJVglArQy/zTsBuRegvhFrbBRk57BDxIJnQnBBqH+pssK8\no0SkOm9P5ocTtyFNYrjoCTuYvyUuE37bxk8Isieii4Wnt7V0L+dr6k8nKdDshWaX\nbimc8uVpBrsYjbnBAhUAk4AnJffHtmRhd4Yr/+OcAVbD6skCgYEA165KKDARY17s\n9ZJ2CO1hWvxfOi8chbcmatzEikV/TzV/ez7zA/qx2lLJ0g1s9YabtYMkwTDZiaCf\nM30yZIrXpdUn7Kw1rHDuzN8+SP4IuxhN1gn1t6uw2klrRyr69Wdj03hgMJ/836Ur\ngqXN4SWNfvyNvLi/4HCrpWEpezie4HgEFgIUcTl3D4uUy1MzdkhRa6v5J0nj3J0=\n-----END PRIVATE KEY-----\n",
  "message": "Pues ya saben que la prueba de su fe produce perseverancia"
}

Salida
{
  "signature": "MC0CFFt+5hgCGZ9WnyxiVPkGcaQoImMBAhUAgdeHxVmsp1w9uG5WlySB/KGtun8="
}

Verificación

Entrada
{
  "public_key": "-----BEGIN PUBLIC KEY-----\nMIIBtzCCASwGByqGSM44BAEwggEfAoGBAOkkh2d/3JjdcZzx54REWkyorffSubrI\np2lamHS0JE5aeYxJVglArQy/zTsBuRegvhFrbBRk57BDxIJnQnBBqH+pssK8o0Sk\nOm9P5ocTtyFNYrjoCTuYvyUuE37bxk8Isieii4Wnt7V0L+dr6k8nKdDshWaXbimc\n8uVpBrsYjbnBAhUAk4AnJffHtmRhd4Yr/+OcAVbD6skCgYEA165KKDARY17s9ZJ2\nCO1hWvxfOi8chbcmatzEikV/TzV/ez7zA/qx2lLJ0g1s9YabtYMkwTDZiaCfM30y\nZIrXpdUn7Kw1rHDuzN8+SP4IuxhN1gn1t6uw2klrRyr69Wdj03hgMJ/836UrgqXN\n4SWNfvyNvLi/4HCrpWEpezie4HgDgYQAAoGAfMtNRsn3DCQh560O1KAGGH2D6GqR\nVXp5B5jpHzltO1Z0tsnsIzk/gauCeKwFitozqyI38P/rPm0FebgsXhsOpgFfPuJL\nge5mr266qJrddKjiQxag2sDppQe2GAOXIZx+prpwPpGd14M4+YNpuPlQT3coLlvi\nPOllkixH28h8f8s=\n-----END PUBLIC KEY-----\n",
  "message": "Pues ya saben que la prueba de su fe produce perseverancia",
  "signature": "MC0CFFt+5hgCGZ9WnyxiVPkGcaQoImMBAhUAgdeHxVmsp1w9uG5WlySB/KGtun8="
}

Salida

{
  "valid": true
}



~ Explicación sobre la seguridad de cada algoritmo ~



* Hashing seguro*

1. SHA-256
- Es un hash criptográfico fuerte.
- Excelente para integridad de datos.
- No es seguro para contraseñas, porque es rápido → fácil de atacar con fuerza bruta.

2. Argon2id
- Diseñado específicamente para contraseñas.
- Ganador del Password Hashing Competition.
- Es lento, configurable y resistente a GPUs/ASICs.
- Protege de ataques de fuerza bruta y diccionario.
- Se prefiere sobre SHA-256 para almacenamiento de contraseñas.


* Cifrado simétrico *

3. AES (Advanced Encryption Standard)
- Estándar mundial para cifrado seguro.
- Utiliza claves de 128, 192 o 256 bits.
- AES-256-CBC es seguro y ampliamente utilizado.
- Mucho más seguro que DES (que tiene solo 56 bits de llave y está obsoleto).


¿Por qué AES en lugar de DES?
- DES puede romperse en horas.
- AES es resistente a ataques actuales.
- AES está aprobado por NIST y se usa en banca, gobierno y empresas.


4. ChaCha20-Poly1305
- Algoritmo moderno, rápido y seguro.
- Ideal para dispositivos móviles.
- Incluye autenticación (AEAD), detecta alteraciones.
- Alternativa segura a AES, especialmente donde no hay aceleración por hardware.


* Cifrado asimétrico *


5. RSA-OAEP
- Utiliza pares de llaves (pública/privada).
- OAEP agrega seguridad contra ataques de padding.
- Ideal para intercambio de claves, no para grandes cantidades de datos.

6. Firmas digitales (DSA)
- Permiten validar autenticidad e integridad.
- DSA + SHA-256 ofrece un nivel adecuado para demostración académica.
- En producción se prefieren ECDSA o Ed25519, pero DSA es válido para comprender el concepto.