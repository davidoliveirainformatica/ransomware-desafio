import os
import pyaes

# Nome do arquivo criptografado
encrypted_file_name = "teste.txt.ransomwaretroll"

# Abrir o arquivo criptografado usando o bloco with
with open(encrypted_file_name, "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

# Chave para descriptografia (mantenha sua chave segura e não a compartilhe)
decryption_key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(decryption_key)

# Descriptografar o arquivo
decrypted_data = aes.decrypt(encrypted_data)

# Remover o arquivo criptografado
os.remove(encrypted_file_name)

# Nome do novo arquivo descriptografado
decrypted_file_name = "teste.txt"

# Salvar o arquivo descriptografado usando o bloco with
with open(decrypted_file_name, "wb") as decrypted_file:
    decrypted_file.write(decrypted_data)

