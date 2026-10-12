import pytest
import secrets
from crypto_utils import CryptoService

@pytest.fixture
def crypto():
    # Menggunakan kunci sintetis untuk lingkungan pengujian
    test_key = CryptoService.generate_key() if hasattr(CryptoService, 'generate_key') else None
    return CryptoService()

# UJI POSITIF 1: Verifikasi Hashing Password yang Valid
def test_password_hashing_success(crypto):
    password = "KataSandiNasabah123!"
    hash_hex, salt = crypto.hash_password(password)
    
    assert hash_hex is not None
    assert len(salt) == 16
    assert crypto.verify_password(password, hash_hex, salt) is True

# UJI POSITIF 2: Verifikasi Generasi Token Unik dan Panjang Berkelayakan
def test_generate_secure_token_success(crypto):
    token1 = crypto.generate_secure_token(32)
    token2 = crypto.generate_secure_token(32)
    
    assert len(token1) > 0
    assert token1 != token2  # Memastikan token unik (CSPRNG)

# UJI POSITIF 3: Enkripsi dan Dekripsi Data Sensitif
def test_encrypt_decrypt_data_success(crypto):
    nik_nasabah = "3171012304950001"
    ciphertext = crypto.encrypt_data(nik_nasabah)
    plaintext_restored = crypto.decrypt_data(ciphertext)
    
    assert ciphertext != nik_nasabah
    assert plaintext_restored == nik_nasabah


# UJI NEGATIF 1 (Batas/Exception): Password Kosong
def test_hash_password_empty_raises_value_error(crypto):
    with pytest.raises(ValueError, match="Password tidak boleh kosong"):
        crypto.hash_password("")

# UJI NEGATIF 2 (Batas/Exception): Ukuran Token Kurang dari 16 Byte
def test_token_under_minimum_length_raises_value_error(crypto):
    with pytest.raises(ValueError, match="Ukuran token minimum adalah 16 byte"):
        crypto.generate_secure_token(8)