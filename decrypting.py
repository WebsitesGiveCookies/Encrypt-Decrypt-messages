from cryptography.fernet import Fernet

key = input("Enter the key: ")
bytes_key = key.encode()
agent = Fernet(bytes_key)
encrypted_message = input("Enter a message: ")
message = agent.decrypt(encrypted_message)
print(message)