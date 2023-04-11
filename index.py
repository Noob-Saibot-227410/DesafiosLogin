import tkinter as tk
from tkinter import messagebox

class TelaLogin:
    def __init__(self, master):
        self.master = master
        self.master.title("Tela de Login")
        self.master.geometry("300x150")
        self.master.resizable(False, False)
        self.master.configure(background="#F0F0F0")

        self.lbl_usuario = tk.Label(self.master, text="Usuário:", font=("Arial", 12), bg="#F0F0F0")
        self.lbl_usuario.place(x=10, y=10)

        self.txt_usuario = tk.Entry(self.master, font=("Arial", 12), width=25)
        self.txt_usuario.place(x=100, y=10)

        self.lbl_senha = tk.Label(self.master, text="Senha:", font=("Arial", 12), bg="#F0F0F0")
        self.lbl_senha.place(x=10, y=40)

        self.txt_senha = tk.Entry(self.master, font=("Arial", 12), show="*", width=25)
        self.txt_senha.place(x=100, y=40)

        self.btn_entrar = tk.Button(self.master, text="Entrar", font=("Arial", 12), command=self.validar_login)
        self.btn_entrar.place(x=110, y=80)

    def validar_login(self):
        usuario = self.txt_usuario.get()
        senha = self.txt_senha.get()

        if usuario == "admin" and senha == "123":
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Nome de usuário ou senha inválidos")

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaLogin(root)
    root.mainloop()
