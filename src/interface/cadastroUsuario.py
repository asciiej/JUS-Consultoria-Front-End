import tkinter as tk
from PIL import Image, ImageTk
import customtkinter

class telaCadastro:
    def __init__(self):

        self.janela = tk.Tk()
        self.janela.geometry("1000x600") #1920x1080
        self.janela.title('JUS Consultorias')
        #self.box = customtkinter.CTkCheckBox(fg_color="#6EC1E4") 
        
       
        imagem_logo = Image.open('imagens/JUS_Consultoria_Arbitragem.png')
        imagem_retangulo = Image.open('imagens/cadastro/retangulo_cadastro.png')
        imagem_retangulo = imagem_retangulo.resize((1090, 440)) 
        imagem_logo = imagem_logo.resize((306, 100)) 
        self.logoJUS = ImageTk.PhotoImage(imagem_logo)
        self.retangulo = ImageTk.PhotoImage(imagem_retangulo)
        
      
        self.label_logo = tk.Label(self.janela, image=self.logoJUS, bg="#efefef")
        self.label_logo.pack(pady=20,padx= 0, anchor=tk.W)


        self.titulo = tk.Label(self.janela, text="Cadastre-se", font=("Consolas", 50), width=18, height=0)
        self.titulo.pack(pady=0)
        self.titulo.place(relx=0.5, rely=0.23, anchor=tk.CENTER)

        #retangulo azul
        self.wid = tk.Label(self.janela, image=self.retangulo)
        self.wid.pack(pady= 0)
        self.wid.place(relx=0.1, rely= 0.36)

        self.wid = tk.Label(self.janela, text="Informações Profissionais: ", font=("Consolas", 30), width=30, bg="#6EC1E4")
        self.wid.place(relx=0.18, rely=0.40)

        #botão
        self.bot = customtkinter.CTkButton(self.janela,text="Finalizar",command = self.clique,width=293,height=60, fg_color="#325564")
        self.bot.pack(pady=20)
        self.bot.place(relx=0.66, rely=0.40)


        self.janela.mainloop()

    def clique(self):
        print("Clicou")












