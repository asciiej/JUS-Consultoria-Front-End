import customtkinter as ctk
from src.interface.Cadastro_Usuario.cadastroUsuarioo import telaCadastro
from src.interface.telaPrincipal import telaPrincipal
from src.interface.telaPrincipalAdm import telaPrincipalAdm
from ..utilitarios.user_session import USER_SESSION
from PIL import Image

class TelaLogin(ctk.CTkFrame):
    def __init__(self, parent, controlers: dict):
        super().__init__(parent)
        self.parent = parent

        self.controlers = controlers
        self.added = 0

        # Carregar e redimensionar o logotipo
        self.logoJUS = ctk.CTkImage(Image.open('imagens/JUS_Consultoria_Arbitragem.png'), size=(400, 161))
        self.logo_label = ctk.CTkLabel(self, text="", image=self.logoJUS)
        self.logo_label.pack(pady=(30, 0))

        frameLogin = {
            "corner_radius": 30,
            "border_width": 2,
            "fg_color": ["#6EC1E4", "#6EC1E4"],
            "border_color": ["#00343D", "#00343D"]
        }

        # Criar o frame para a área de login
        self.login_frame = ctk.CTkFrame(self, width=500, height=450,**frameLogin)
        self.login_frame.pack(pady=(30, 0))

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

        # Inicializar a mensagem de erro (será recriada conforme necessário)
        #self.errorMessage = None
        #self.errorText = None

        # Iniciar a aplicação
        #self.root.mainloop()

    def center_window(self, width, height):
        """Centralizar a janela no meio da tela."""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_top = int(screen_height / 2 - height / 2)
        position_right = int(screen_width / 2 - width / 2)
        self.geometry(f'{width}x{height}+{position_right}+{position_top}')

    def on_login(self):
        """Função para o botão de login."""
        email = self.email_entry.get()
        password = self.senha_entry.get()
        # Adicione a lógica de login aqui

        try:
            login = self.controlers["usuario"].login(email, password)
            if login:
                if len(USER_SESSION.get_user_data().roles) <= 1:
                    raise Exception("Voce não possui nenhum cargo, entre em contato com o Admin.")
        except Exception as e:
            self.show_error_message(e)
            return

        if not login:
            self.show_error_message("Usuário ou senha inválidos, tente novamente.")
            return
        print(login)
        self.clear_login_screen()
        if USER_SESSION.is_admin():
            print("admin")
            self.parent.show_frame("telaPrincipalAdm")
            self.parent.frames["telaPrincipalAdm"].show_contentADM()
        else:
            self.parent.show_frame("telaPrincipal")
            self.parent.frames["telaPrincipal"].show_content()
        print(f"Email: {email}, Password: {password}")

    def on_register(self):
        """Função para o link de cadastro."""
        #self.clear_login_screen()
        self.parent.show_frame("telaCadastro")
        #telaCadastro(self,self.controlers)

    def clear_login_screen(self):
        """Função para limpar a tela de login."""
        # Remove todos os widgets do root
        for widget in self.winfo_children():
            widget.destroy()

    def show_error_message(self, message):
        """Função para mostrar uma mensagem de erro."""
        if self.added == 1:
            self.errorMessage.destroy()
        self.errorMessage = ctk.CTkFrame(self, width=500, height=75, fg_color="#D27C7C", border_color="#C23E3E", border_width=2)
        self.errorText = ctk.CTkLabel(self.errorMessage, text=message, font=("Consolas", 17, 'bold'), text_color="#EFEFEF")

        self.logo_label.pack_forget()
        self.login_frame.pack_forget()
        self.logo_label.pack(pady=(30, 0))
        self.errorText.place(relx=0.5, rely=0.5, anchor="center")
        self.errorMessage.pack(pady=(30, 0))
        self.login_frame.pack(pady=(30, 0))
        self.added = 1


