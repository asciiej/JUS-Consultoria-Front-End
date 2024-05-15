import customtkinter
from PIL import Image

class telaLogin:
    def __init__(self):
        customtkinter.set_default_color_theme("lib/temaTkinterCustom.json")

        self.janela = customtkinter.CTk()
        self.janela.geometry("1000x600")
        self.janela.title('JUS Consultorias')
        self.font = customtkinter.CTkFont('Helvetica',14)
        
        self.logoJUS = customtkinter.CTkImage(Image.open('imagens/LogoBicolor.png'),size = (243,189))
        self.lable = customtkinter.CTkLabel(self.janela,text = "",image = self.logoJUS)
        self.lable.pack(pady = 20)
        
        self.emailText = customtkinter.CTkLabel(self.janela,text="e-mail",font=self.font)
        self.emailText.pack()
        self.email = customtkinter.CTkEntry(self.janela,placeholder_text="...",width=386,height=37)
        self.email.pack(pady=10)
        
        self.senhaText = customtkinter.CTkLabel(self.janela,text="senha",font=self.font)
        self.senhaText.pack()
        self.senha = customtkinter.CTkEntry(self.janela,placeholder_text="...",show='*',width=386,height=37)
        self.senha.pack(pady = 10)

        self.login = customtkinter.CTkButton(self.janela,text="Login",command = self.clique,width=200,height=42)
        self.login.pack(pady=20)

        self.janela.mainloop()

    def clique(self):
        print("Clicou")



