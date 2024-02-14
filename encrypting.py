from cryptography.fernet import Fernet
from getpass import getpass

key = b'JFm640lfCqjSXZ8tIAOA3btMLPDJj116lXg0BDM1KDg=' #key = Fernet.generate_key()
agent = Fernet(key)
message = getpass("Enter a message: ")
bytes_message = message.encode()
encrypted_message = agent.encrypt(bytes_message)
print(encrypted_message)