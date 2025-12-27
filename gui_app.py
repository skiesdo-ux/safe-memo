import tkinter as tk
from core.crypto_core import encrypt_text, decrypt_text

def encrypt():
    try:
        data = encrypt_text(text.get("1.0", tk.END), password.get())
        output.delete("1.0", tk.END)
        output.insert(tk.END, data)
    except:
        output.insert(tk.END, "Error")

def decrypt():
    try:
        result = decrypt_text(output.get("1.0", tk.END).encode(), password.get())
        text.delete("1.0", tk.END)
        text.insert(tk.END, result)
    except:
        output.insert(tk.END, "Password salah")

root = tk.Tk()
root.title("SafeMemo")

tk.Label(root, text="Password").pack()
password = tk.Entry(root, show="*")
password.pack()

tk.Label(root, text="Text").pack()
text = tk.Text(root, height=6)
text.pack()

tk.Button(root, text="Encrypt", command=encrypt).pack()
tk.Button(root, text="Decrypt", command=decrypt).pack()

output = tk.Text(root, height=6)
output.pack()

root.mainloop()
