import customtkinter as ctk
from src.interface.Cadastro_Usuario.cadastroUsuarioo import telaCadastro
from PIL import Image

class TelaLogin:
    def __init__(self,controlers : dict):
        # Configuração inicial da janela
        ctk.set_default_color_theme("lib/temaTkinterCustom.json")
        self.root = ctk.CTk()
        self.root.geometry("800x600")
        self.root.title("Login - Consultorias Arbitragem")

        # Centralizar a janela
        self.center_window(800, 600)

        # Carregar e redimensionar o logotipo
        self.logoJUS = ctk.CTkImage(Image.open('imagens/JUS_Consultoria_Arbitragem.png'), size=(400, 161))
        self.logo_label = ctk.CTkLabel(self.root, text="", image=self.logoJUS)
        self.logo_label.pack(pady=(30, 0))

        # Criar o frame para a área de login
        self.login_frame = ctk.CTkFrame(self.root, width=500, height=450)
        self.login_frame.pack()

        # Campo de entrada para e-mail
        self.email_label = ctk.CTkLabel(self.login_frame, text="e-mail")
        self.email_label.place(relx=0.15, rely=0.1, anchor="w")  # Alinhado à esquerda
        self.email_entry = ctk.CTkEntry(self.login_frame, width=350)
        self.email_entry.place(relx=0.5, rely=0.2, anchor="center")

        # Campo de entrada para senha
        self.senha_label = ctk.CTkLabel(self.login_frame, text="senha")
        self.senha_label.place(relx=0.15, rely=0.33, anchor="w")  # Alinhado à esquerda
        self.senha_entry = ctk.CTkEntry(self.login_frame, show='*', width=350)
        self.senha_entry.place(relx=0.5, rely=0.43, anchor="center")

        # Botão de login
        self.login_button = ctk.CTkButton(self.login_frame, text="Login", command=self.on_login, width=350, height=50)
        self.login_button.place(relx=0.5, rely=0.8, anchor="center")

        # Link para cadastro
        self.register_link = ctk.CTkLabel(self.login_frame, text="Cadastre-se", font=ctk.CTkFont(underline=True), text_color="#EFEFEF", cursor="hand2")
        self.register_link.place(relx=0.5, rely=0.93, anchor="center")
        self.register_link.bind("<Button-1>", lambda e: self.on_register())

        # Iniciar a aplicação
        self.root.mainloop()

    def center_window(self, width, height):
        """Centralizar a janela no meio da tela."""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int(screen_height / 2 - height / 2)
        position_right = int(screen_width / 2 - width / 2)
        self.root.geometry(f'{width}x{height}+{position_right}+{position_top}')

    def on_login(self):
        """Função para o botão de login."""
        email = self.email_entry.get()
        password = self.senha_entry.get()
        # Adicione a lógica de login aqui
        print(f"Email: {email}, Password: {password}")

    def on_register(self):
        """Função para o link de cadastro."""
        self.clear_login_screen()
        telaCadastro(self.root)

    def clear_login_screen(self):
        """Função para limpar a tela de login."""
        # Remove todos os widgets do root
        for widget in self.root.winfo_children():
            widget.destroy()
        
