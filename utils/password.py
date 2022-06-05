import bcrypt

class PasswordUtils():
    @staticmethod
    def hash(password: str):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    
    @staticmethod
    def compare(hash_password: str, password: str):
        hash_password = bytes(hash_password, 'utf-8')
        password = bytes(password, 'utf-8')
        return bcrypt.checkpw(password, hash_password)