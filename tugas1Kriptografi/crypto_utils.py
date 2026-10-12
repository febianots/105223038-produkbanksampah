import hashlib
import secrets
import base64
from cryptography.fernet import Fernet

class CryptoService:
    def __init__(self, secret_key: bytes = None):
        """
        Inisialisasi layanan kriptografi.
        Kunci rahasia diambil dari instansiasi atau dibuat acak menggunakan CSPRNG.
        """
        if secret_key is None:
            self.key = Fernet.generate_key()
        else:
            self.key = secret_key
        self.cipher = Fernet(self.key)

    # 1. Hashing Password (PBKDF2-HMAC-SHA256)
    def hash_password(self, password: str, salt: bytes = None) -> tuple[str, bytes]:
        if not password:
            raise ValueError("Password tidak boleh kosong")
        
        if salt is None:
            salt = secrets.token_bytes(16)  # 128-bit CSPRNG salt
            
        iterations = 100_000
        hash_bytes = hashlib.pbkdf2_hmac(
            'sha256', 
            password.encode('utf-8'), 
            salt, 
            iterations
        )
        hash_hex = hash_bytes.hex()
        return hash_hex, salt

    def verify_password(self, password: str, stored_hash: str, salt: bytes) -> bool:
        if not password:
            return False
        computed_hash, _ = self.hash_password(password, salt)
        # Gunakan compare_digest untuk mencegah Timing Attack
        return secrets.compare_digest(computed_hash, stored_hash)

    # 2. Generator Token Kriptografis Aman
    def generate_secure_token(self, nbytes: int = 32) -> str:
        if nbytes < 16:
            raise ValueError("Ukuran token minimum adalah 16 byte untuk keamanan")
        return secrets.token_urlsafe(nbytes)

    # 3. Enkripsi & Dekripsi Simetris (Fernet / AES-128-GCM/CBC + HMAC)
    def encrypt_data(self, plaintext: str) -> str:
        if not plaintext:
            raise ValueError("Data plaintext tidak boleh kosong")
        encrypted_bytes = self.cipher.encrypt(plaintext.encode('utf-8'))
        return encrypted_bytes.decode('utf-8')

    def decrypt_data(self, ciphertext: str) -> str:
        if not ciphertext:
            raise ValueError("Data ciphertext tidak boleh kosong")
        decrypted_bytes = self.cipher.decrypt(ciphertext.encode('utf-8'))
        return decrypted_bytes.decode('utf-8')