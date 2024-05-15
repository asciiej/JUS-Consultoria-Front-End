import tkinter as tk
from PIL import Image, ImageTk
import customtkinter

class telaCadastro:
    def __init__(self):

        self.janela = tk.Tk()
        self.janela.geometry("1000x600")
        self.janela.title('JUS Consultorias')
        self.janela.configure(bg="#efefef") 
        
       
        imagem_logo = Image.open('imagens/JUS_Consultoria_Arbitragem.png')
        imagem_logo = imagem_logo.resize((306, 110)) 
        self.logoJUS = ImageTk.PhotoImage(imagem_logo)

        
      
        self.label_logo = tk.Label(self.janela, image=self.logoJUS, bg="#efefef")
        self.label_logo.pack(pady=20,padx= 0, anchor=tk.W)


        titulo = tk.Label(self.janela, text="Cadastre - se", font=("Calibri", 50), width=10, height=20)
        titulo.pack(pady=0, padx= 32)
        titulo.place(relx=0.5, rely=0.2, anchor=tk.CENTER)


        wid = tk.Label(self.janela, bg="#6EC1E4", width=130, height=683)
        wid.pack(pady=70)

  

        


        self.janela.mainloop()

    def clique(self):
        print("Clicou")










