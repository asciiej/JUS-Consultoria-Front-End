import tkinter as tk
import customtkinter
from PIL import Image
import webbrowser
from tkinter import filedialog
import shutil
#from ..utilitarios.user_session import USER_SESSION


class redirecionaGOV:
    def __init__(self):
        customtkinter.set_default_color_theme("lib/temaTkinterCustom.json")

        self.janela = customtkinter.CTk()
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        self.janela.geometry(f"{largura_tela}x{altura_tela}-10+0")
        self.janela.title('JUS Consultorias')
        self.font = customtkinter.CTkFont('Helvetica', 14)
        self.titulo_font = customtkinter.CTkFont('Helvetica', 20)

        # Cabeçalho menu personalizado
        cabecalho_menu = {
            "corner_radius": 0,
            "border_width": 0,
            "fg_color": ["#6EC1E4", "#6EC1E4"]
        }

        # Cabeçalho
        self.cabecalho = customtkinter.CTkFrame(self.janela, height=104, **cabecalho_menu)
        self.cabecalho.pack(fill=customtkinter.X)

        # Logo
        self.logoJUS = customtkinter.CTkImage(Image.open('imagens/Logomarca JUS.png'), size=(80, 72.54))
        self.logo_cabecalho = customtkinter.CTkLabel(self.cabecalho, image=self.logoJUS, text="")
        self.logo_cabecalho.pack(side=customtkinter.LEFT, padx=(18, 0), pady=7)

        # Usuario foto
        self.userPic = customtkinter.CTkImage(Image.open('imagens/User Male Black.png'), size=(90, 90))
        self.userPic_cabecalho = customtkinter.CTkLabel(self.cabecalho, image=self.userPic, text="")
        self.userPic_cabecalho.pack(side=customtkinter.RIGHT, padx=(0, 18), pady=7)

        # Botão menu personalizado
        voltar_menu = {
            "corner_radius": 0,
            "border_width": 0,
            "fg_color": ["#6EC1E4", "#6EC1E4"],
            "hover_color": ["#6EC1E4", "#6EC1E4"],
            "border_color": ["#6EC1E4", "#6EC1E4"],
            "text_color": "#000000",
            "text_color_disabled": ["#6EC1E4", "#6EC1E4"]
        }

        # Texto menu e Botão de VOLTAR
        self.h1_titulo = customtkinter.CTkLabel(self.cabecalho, text="Assinatura de um Documento", font=self.titulo_font)
        self.h1_titulo.pack(side=customtkinter.LEFT, padx=(25, 0))

        self.voltar = customtkinter.CTkButton(self.cabecalho, text="Voltar \u2192", command=self.voltar_funcao, **voltar_menu)
        self.voltar.pack(side=customtkinter.LEFT, padx=(700, 0))

         # Nome do usuario no cabeçalho
        self.nome_usuario_label = customtkinter.CTkLabel(self.cabecalho, text="Lucas Simoni", font=self.font)
        #self.nome_usuario_label = customtkinter.CTkLabel(self.cabecalho, text=f"{USER_SESSION.get_user_data().nome} {USER_SESSION.get_user_data().sobrenome}", font=self.font)
        self.nome_usuario_label.pack(side=customtkinter.RIGHT, padx=(0, 25))

        # Calcular a altura do "body"
        self.janela.update_idletasks()
        window_height = self.janela.winfo_height()
        header_height = self.cabecalho.winfo_height()
        body_height = window_height - header_height

        # Body
        self.canvas = tk.Canvas(self.janela, height=body_height)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Frame
        self.frame = customtkinter.CTkFrame(self.canvas, height=460, width=750)
        self.frame.pack(pady=(100, 0))
        self.frame.pack_propagate(False)

        # Texto
        self.h2 = customtkinter.CTkLabel(self.frame, text="Obrigado por escolher a JUS Consultorias e arbitragens, sua\nminuta está pronta para ser assinada digitalmente.", font=("Helvetica", 25))
        self.h2.pack(side=customtkinter.TOP, padx=(0, 0), pady=(100, 50))
        #self.h2.place(x=120, y=120)

        baixar = {
                "corner_radius": 13,
                "border_width": 0,
                "width": 200,
                "height": 50,
                "fg_color": ["#58ABB3", "#58ABB3"],
                "hover_color": ["#167F89", "#167F89"],
                "border_color": ["#6EC1E4", "#6EC1E4"],
                "text_color": "#EFEFEF",
                "text_color_disabled": ["#EFEFEF", "#EFEFEF"],
                "font": ("Helvetica", 20)
            }
        
        GOV = {
                "corner_radius": 13,
                "border_width": 0,
                "width": 200,
                "height": 50,
                "fg_color": ["#325564", "#325564"],
                "hover_color": ["#183E4F", "#183E4F"],
                "border_color": ["#6EC1E4", "#6EC1E4"],
                "text_color": "#EFEFEF",
                "text_color_disabled": ["#EFEFEF", "#EFEFEF"],
                "font": ("Helvetica", 20)
            }

        # Baixar PDF
        botao_baixar = customtkinter.CTkButton(self.frame, text="Baixar a minuta em formato PDF",command=self.func_baixar, **baixar)
        botao_baixar.pack(side=customtkinter.TOP, padx=(0, 0), pady=(0, 30))

        # Redireciona GOV
        botao_gov = customtkinter.CTkButton(self.frame, text="Acesse o GOV.br para a assinatura digital",command=self.func_gov, **GOV)
        botao_gov.pack(side=customtkinter.TOP, padx=(0, 0), pady=(0, 0))

        self.janela.mainloop()

    def voltar_funcao(self):

        pass
    def func_baixar(self):
        
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")]) # Selecionar onde salvar arquivo
        if file_path:
            try:
                
                shutil.copy('./pdfs/pdf_final.pdf', file_path) # Copiar o arquivo pdf_final.pdf para o local escolhido pelo usuário
            except Exception as e:
                print(f"Erro ao copiar o arquivo: {e}")
                
    def func_gov(self):

        webbrowser.open("http://assinador.iti.br/")
        

if __name__ == "__main__":
    app = redirecionaGOV()