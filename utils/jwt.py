from datetime import datetime, timedelta
from jose import JWTError, jwt

from config.settings import get_env

settings = get_env()

class Jwt():
    """
    Encode data to JWT Token and Decode JWT token
    """
    @staticmethod
    def create_token(data: dict, expires_delta: timedelta | None = None):
        """
        Encode data to JWT Token
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
        to_encode.update({"exp": expire})
        encode_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
        return encode_jwt

    @staticmethod
    def decode_token(token: str):
        """
        Decode JWT Token
        """
        try:
            payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        except JWTError:
            return None
        return payload