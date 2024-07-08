import tkinter as tk
import customtkinter as ctk

from src.interface.login import TelaLogin
from src.interface.telaPrincipal import telaPrincipal
from src.interface.Cadastro_Usuario.cadastroUsuarioo import telaCadastro

class MainApp(tk.Tk):
    def __init__(self, controlers):
        super().__init__()
        self.title("Navegação entre Telas")
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        self.geometry(f"{largura_tela}x{altura_tela}")
        #self.geometry("800x600")
        

        # Instanciando os frames
        self.frames = {}

        # Instanciando TelaLogin
        self.tela_login = TelaLogin(self, controlers)
        self.frames["TelaLogin"] = self.tela_login
        self.tela_login.pack(fill="both", expand=True)

        # Instanciando telaRegistro (inicialmente escondida)
        self.tela_cadastro = telaCadastro(self, controlers)
        self.frames["telaCadastro"] = self.tela_cadastro

        # Instanciando telaPrincipal (inicialmente escondida)
        self.tela_principal = telaPrincipal(self, controlers)
        self.frames["telaPrincipal"] = self.tela_principal
        

        # Mostrando a tela inicial
        self.show_frame("TelaLogin")

    def show_frame(self, page_name):
        """Exibe a tela com o nome especificado."""
        # Esconder todas as telas
        for frame_name, frame in self.frames.items():
            frame.pack_forget()

        # Exibir a tela solicitada
        frame = self.frames.get(page_name)
        if frame:
            frame.pack(fill="both", expand=True)
        else:
            print(f"Tela '{page_name}' não encontrada!")

    def show_registro(self):
        """Exibe a tela de registro e esconde a tela de login."""
        self.tela_login.pack_forget()
        self.tela_principal.pack_forget()
        self.tela_cadastro.pack(fill="both", expand=True)

    def show_login(self):
        """Exibe a tela de login e esconde a tela de registro."""
        self.tela_cadastro.pack_forget()
        self.tela_principal.pack_forget()
        self.tela_login.pack(fill="both", expand=True)

    def show_principal(self):
        """Exibe a tela princpal e esconde a tela de login"""
        self.tela_login.pack_forget()
        self.tela_cadastro.pack_forget()
        self.tela_principal.pack(fill="both", expand=True)

        

