from core.crypto_core import encrypt_text, decrypt_text

print("=== SafeMemo CLI (Text) ===")
print("1. Enkripsi teks")
print("2. Dekripsi teks")

choice = input("Pilih menu: ")

if choice == "1":
    text = input("Masukkan teks: ")
    password = input("Password: ")
    encrypted = encrypt_text(text, password)
    print("\nHasil Enkripsi (bytes):")
    print(encrypted)

elif choice == "2":
    raw = input("Paste data terenkripsi: ")
    password = input("Password: ")
    try:
        result = decrypt_text(raw.encode(), password)
        print("\nHasil Dekripsi:")
        print(result)
    except:
        print("❌ Password salah atau data rusak")


