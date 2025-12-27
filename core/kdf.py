import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

ITERATIONS = 100000
KEY_LENGTH = 32  # 256-bit

def derive_key(password: str, salt: bytes) -> bytes:
    """
    Menghasilkan kunci AES dari password menggunakan PBKDF2
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_LENGTH,
        salt=salt,
        iterations=ITERATIONS
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))
