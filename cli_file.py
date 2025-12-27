from core.crypto_core import encrypt_text, decrypt_text
from core.utils import save_file, load_file

print("=== SafeMemo CLI (File) ===")
print("1. Enkripsi file")
print("2. Dekripsi file")

choice = input("Pilih menu: ")

if choice == "1":
    path = input("Nama file: ")
    password = input("Password: ")

    with open(path, "r") as f:
        text = f.read()

    encrypted = encrypt_text(text, password)
    save_file(path + ".enc", encrypted)
    print("✔ File berhasil dienkripsi")

elif choice == "2":
    path = input("File .enc: ")
    password = input("Password: ")

    try:
        data = load_file(path)
        text = decrypt_text(data, password)
        with open("decrypted.txt", "w") as f:
            f.write(text)
        print("✔ File berhasil didekripsi (decrypted.txt)")
    except:
        print("❌ Password salah atau file rusak")


