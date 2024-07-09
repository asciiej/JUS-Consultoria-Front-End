import tkinter as tk
import customtkinter as ctk

from src.interface.login import TelaLogin
from src.interface.telaPrincipal import telaPrincipal
from src.interface.telaPrincipalAdm import telaPrincipalAdm
from src.interface.Cadastro_Usuario.cadastroUsuarioo import telaCadastro
from src.interface.alterarAcesso import alterarAcesso
from src.interface.edicaoContratos import telaEdicaoContrato
from src.interface.Atualizar_dados.atualizarinform import AtualizaCad

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

        # Instanciando telaPrincipal (inicialmente escondida)
        self.tela_principalADM = telaPrincipalAdm(self, controlers)
        self.frames["telaPrincipalAdm"] = self.tela_principalADM

        # Instanciando alterarAcesso (inicialmente escondida)
        self.tela_alterarAcesso = alterarAcesso(self, controlers)
        self.frames["alterarAcesso"] = self.tela_alterarAcesso
        
        # Instanciando edicaoContratos (inicialmente escondida)
        self.tela_edicaoContratos = telaEdicaoContrato(self, controlers)
        self.frames["telaEdicaoContrato"] = self.tela_edicaoContratos

        # Instanciando AtualizaCad (inicialmente escondida)
        self.tela_atualizaInform = AtualizaCad(self, controlers)
        self.frames["AtualizaCad"] = self.tela_atualizaInform
        

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

        self.tela_cadastro.pack(fill="both", expand=True)

    def show_login(self):
        """Exibe a tela de login e esconde a tela de registro."""
        self.tela_cadastro.pack_forget()

        self.tela_login.pack(fill="both", expand=True)

    def show_principal(self):
        """Exibe a tela princpal e esconde a tela de login"""
        self.tela_login.pack_forget()

        self.tela_principal.pack(fill="both", expand=True)

    def show_principal_Adm(self):
        """Exibe a tela princpal e esconde a tela de login"""
        self.tela_login.pack_forget()
        self.tela_alterarAcesso.pack_forget()

        self.tela_principalADM.pack(fill="both", expand=True)

    def show_alterarAcesso(self):
        """Exibe a tela alterar acesso e esconde a tela principal ADM"""
        self.tela_principalADM.pack_forget()

        self.tela_alterarAcesso.pack(fill="both", expand=True)

    def show_edicaoContratos(self):
        """Exibe a tela edicao Contratos e esconde a tela principal ADM"""
        self.tela_principalADM.pack_forget()

        self.tela_edicaoContratos.pack(fill="both", expand=True)

    def show_atualizaInform(self):
        """Exibe a tela atualizar dados e esconde a tela principal"""
        self.tela_principal.pack_forget()

        self.tela_atualizaInform.pack(fill="both", expand=True)

        

