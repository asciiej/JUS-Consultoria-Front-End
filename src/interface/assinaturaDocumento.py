from tkinter import *
from PIL import Image
import ctypes
from tkinter import ttk
import customtkinter
from src.utilitarios.visualizadorPDF import PDFReader
from src.interface.redirecionaGOV import redirecionaGOV
from src.utilitarios.user_session import USER_SESSION

class telaAssinaturaDocumento:
    def __init__(self,root):
        #self.contractControler = contractControler
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
        self.root = root

        cabecalho_menu = {
            "corner_radius": 0,
            "border_width": 0,
            "fg_color": ["#6EC1E4", "#6EC1E4"]
        }
        self.font = customtkinter.CTkFont('Helvetica', 14)
        self.titulo_font = customtkinter.CTkFont('Helvetica', 20)

        # Cabeçalho
        self.cabecalho = customtkinter.CTkFrame(self.root, height=104, **cabecalho_menu)
        self.cabecalho.pack(fill=customtkinter.X)

        # Logo
        self.logoJUS = customtkinter.CTkImage(Image.open('imagens/Logomarca JUS.png'), size=(80, 72.54))
        self.logo_cabecalho = customtkinter.CTkLabel(self.cabecalho, image=self.logoJUS, text="")
        self.logo_cabecalho.pack(side=customtkinter.LEFT, padx=(18, 0), pady=7)

        # Usuario foto
        self.userPic = customtkinter.CTkImage(Image.open('imagens/User Male Black.png'), size=(90, 90))
        self.userPic_cabecalho = customtkinter.CTkLabel(self.cabecalho, image=self.userPic, text="")
        self.userPic_cabecalho.pack(side=customtkinter.RIGHT, padx=(0, 18), pady=7)

        # Texto menu e Botão de VOLTAR
        self.h1_titulo = customtkinter.CTkLabel(self.cabecalho, text=f"Assinatura do documento", font=self.titulo_font)
        self.h1_titulo.pack(side=customtkinter.LEFT, padx=(25, 0))

        self.voltar = customtkinter.CTkButton(self.cabecalho, text="Voltar \u2192", command=self.voltar_funcao,width=200)
        self.voltar.pack(side=customtkinter.LEFT, padx=(700, 40))

         # Nome do usuario no cabeçalho
        self.nome_usuario_label = customtkinter.CTkLabel(self.cabecalho, text=f"{USER_SESSION.get_user_data().nome} {USER_SESSION.get_user_data().sobrenome}", font=self.font)
        self.nome_usuario_label.pack(side=customtkinter.RIGHT, padx=(0, 25))

        # Frame para os botões à direita com scrollbar
        widithBotoes = 600

        self.frame_botoes = Frame(self.root, bg="#6EC1E4", highlightbackground="#00343D", highlightthickness=2,width=widithBotoes)
        self.frame_botoes.pack(side=RIGHT, fill=Y , padx=(10,0))


        # Estilo dos botões
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#00343D", foreground="white")
        self.style.map("TButton", background=[('active', '#002831')])


        self.btn_save = customtkinter.CTkButton(self.frame_botoes, text="Alterar seus dados", command=None, fg_color="#58ABB3", hover_color="#367076", width=400,height=50, font=('Calibri', 25, 'bold'))
        self.btn_save.pack(padx = 40,pady = 40,side = 'bottom') 


        self.btn_preview =  customtkinter.CTkButton(self.frame_botoes, text="Assinar", command=self.assinar, fg_color="#58ABB3", hover_color="#367076", width=400,height=50, font=('Calibri', 25, 'bold'))
        self.btn_preview.pack(padx = 40,pady = 10,side = 'bottom')

        # Frame para o editor de texto à esquerda
        self.frame_texto = Frame(self.root, width=600)
        self.frame_texto.pack(side=LEFT, fill=BOTH, expand=True)

        
        pdf_saida = './pdfs/pdf_final.pdf'
        PDFReader(self.frame_texto,None,pdf_saida)



        self.root.mainloop()

    def voltar_funcao(self):
        pass

    def assinar(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        redirecionaGOV(self.root)
