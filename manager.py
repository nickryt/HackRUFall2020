from cryptography.fernet import Fernet
import random
import string

class Manager:

    keyobject = None
    keytext = None
    loaded = []

    def __init__(self):   
        Manager.generate(self)
        
    def encrypt(self, text):
        token =  Manager.keyobject.encrypt(str.encode(text))
        return token

    def decrypt(self, text):
        token = Manager.keyobject.decrypt(bytes(text,'utf-8'))
        return token

    def generate(self):
        Manager.keytext = Fernet.generate_key()
        Manager.keyobject = Fernet(Manager.keytext)

    def importkey(self, text):
        Manager.keytext = bytes(text,'utf-8')
        Manager.keyobject = Fernet(Manager.keytext)

    def generatepassword(self):
        allcharacters = string.ascii_letters + string.digits
        result = ''.join(random.choice(allcharacters) for i in range(20))
        return result
