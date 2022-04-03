import bcrypt

class PaswwordUtils():
    def hash(self, password: str):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed
        
    def compare(self, hash_password: str, password: str):
        return bcrypt.checkpw(password, hash_password)