from core.crypto_core import encrypt_text, decrypt_text

encrypted = encrypt_text("Pesan rahasia", "password123")

print("Uji password salah:")
try:
    decrypt_text(encrypted, "salah")
except:
    print("✔ Password salah / tampering terdeteksi")
