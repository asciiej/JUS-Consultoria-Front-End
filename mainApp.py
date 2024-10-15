import tkinter as tk
import customtkinter as ctk
import os

from src.interface.login import TelaLogin
from src.interface.telaPrincipal import telaPrincipal
from src.interface.telaPrincipalAdm import telaPrincipalAdm
from src.interface.Cadastro_Usuario.cadastroUsuarioo import telaCadastro
from src.interface.alterarAcesso import alterarAcesso
from src.interface.edicaoContratos import telaEdicaoContrato
from src.interface.Atualizar_dados.atualizarinform import AtualizaCad
from src.interface.checagemInformacoes import checagemInformacoes
from src.interface.assinaturaDocumento import telaAssinaturaDocumento
from src.interface.redirecionaGOV import redirecionaGOV
from src.classes.contrato.ContratoPesudoPreenchido import ContratoPseudoPreenchido
from src.classes.contrato.ContractControler import Controler

class MainApp(tk.Tk):
    ContratosPseudoPreenchidos = []
    def __init__(self, controlers):
        super().__init__()
        self.title("JUS Consultorias e Arbitragem")
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        self.geometry(f"{largura_tela}x{altura_tela}")
        self.iconbitmap("imagens/Logomarca-JUS.ico")
        # Determine the base path for assets

        # Example of loading an image
        caminho_absoluto = os.path.abspath("lib/temaTkinterCustom.json")
        ctk.set_default_color_theme(caminho_absoluto)
        ctk.set_appearance_mode("light")
        

        # Instanciando os frames
        self.frames = {}

        # Instanciando TelaLogin
        self.tela_login = TelaLogin(self, controlers)
        self.frames["TelaLogin"] = self.tela_login
        self.tela_login.pack(fill="both", expand=True)

        # Instanciando outras telas (inicialmente escondida)
        self.tela_cadastro = telaCadastro(self, controlers)
        self.frames["telaCadastro"] = self.tela_cadastro

        self.tela_principal = telaPrincipal(self, controlers)
        self.frames["telaPrincipal"] = self.tela_principal

        self.tela_principalADM = telaPrincipalAdm(self, controlers)
        self.frames["telaPrincipalAdm"] = self.tela_principalADM

        self.tela_alterarAcesso = alterarAcesso(self, controlers)
        self.frames["alterarAcesso"] = self.tela_alterarAcesso
        
        self.tela_edicaoContratos = telaEdicaoContrato(self, controlers)
        self.frames["telaEdicaoContrato"] = self.tela_edicaoContratos
        
        self.tela_atualizaInform = AtualizaCad(self, controlers)
        self.frames["AtualizaCad"] = self.tela_atualizaInform

        self.tela_checaInfo = checagemInformacoes(self, controlers)
        self.frames["checagemInformacoes"] = self.tela_checaInfo

        self.tela_assinaDoc = telaAssinaturaDocumento(self, controlers)
        self.frames["telaAssinaturaDocumento"] = self.tela_assinaDoc

        self.tela_GOV = redirecionaGOV(self, controlers)
        self.frames["redirecionaGOV"] = self.tela_GOV

        # Mostrando a tela inicial
        self.show_frame("TelaLogin")

    def show_frame(self, page_name):
        """Exibe a tela com o nome especificado."""
        # Esconder todas as telas
        for frame_name, frame in self.frames.items():
            frame.pack_forget()

        # Exibir a tela solicitada
        frame = self.frames.get(page_name)
        print(f"Frames: {self.frames}")
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
        self.tela_checaInfo.pack_forget()
        

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

    def show_checaInfo(self):
        """Exibe a tela checagem infos e esconde a tela principal"""
        self.tela_principal.pack_forget()
        self.tela_assinaDoc.pack_forget()

        self.tela_checaInfo.pack(fill="both", expand=True)

    def show_assinaDoc(self):
        """Exibe a tela atualizar dados e esconde a tela principal"""
        self.tela_checaInfo.pack_forget()
        self.tela_GOV.pack_forget()

        self.tela_assinaDoc.pack(fill="both", expand=True)

    def show_GOV(self):
        """Exibe a tela atualizar dados e esconde a tela principal"""
        self.tela_assinaDoc.pack_forget()

        self.tela_GOV.pack(fill="both", expand=True)

    def setContrato(self,contract : Controler):
        self.contract = contract
    
    def getContrato(self) -> Controler:
        return self.contract 
    
    def addContratoPseudoPreenchido(self,contratoPseudo: ContratoPseudoPreenchido):
        if contratoPseudo not in self.ContratosPseudoPreenchidos: 
            self.ContratosPseudoPreenchidos.append(contratoPseudo)

    def getContratoPseudoPreenchido(self,titulo:str) -> ContratoPseudoPreenchido:
        for contrato in self.ContratosPseudoPreenchidos:
            if contrato.titulo == titulo:
                return contrato
        return None 

