
import os
from pathlib import Path
from PIL import Image, ImageTk
from tkinter import Canvas, Entry, Button, PhotoImage, Toplevel, Label
import tkinter as tk
from ...utilitarios.user_session import USER_SESSION
import customtkinter

class AtualizaCad:
    def __init__(self, janela, controlers):
        self.atualizarcad = janela
        #self.atualizarcad.configure(bg="#EFEFEF")
        self.controlers = controlers

        cabecalho_menu = {
            "corner_radius": 0,
            "border_width": 0,
            "fg_color": ["#6EC1E4", "#6EC1E4"]
        }
        self.font = customtkinter.CTkFont('Helvetica', 14)
        self.titulo_font = customtkinter.CTkFont('Helvetica', 20)

        # Cabeçalho
        self.cabecalho = customtkinter.CTkFrame(self.atualizarcad, height=104, **cabecalho_menu)
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

        #criação do canvas
        self.canvas = Canvas(
            self.atualizarcad,
            bg="#EFEFEF",
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)

        #place holder testee



        # Imagens
        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))

        # Criação das imagens no canvas
        self.canvas.create_image(578.0, 127.0, image=self.image_image_2)
        self.canvas.create_image(738.0, 401.0, image=self.image_image_3)

        # Textos no canvas


        self.name_text_id = self.canvas.create_text(629.0, 119.0, anchor="nw", text=f"{USER_SESSION.get_user_data().nome} {USER_SESSION.get_user_data().sobrenome}", fill="#000000", font=("Consolas", 22 * -1))
        self.canvas.create_text(880.0, 357.0, anchor="nw", text="Nome da Empresa", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(462.0, 427.0, anchor="nw", text="Telefone", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(667.0, 427.0, anchor="nw", text="País / Localização", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(880.0, 428.0, anchor="nw", text="CPF", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(463.0, 506.0, anchor="nw", text="Nova Senha", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(748.0, 507.0, anchor="nw", text="Confirme sua Nova Senha", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(462.0, 357.0, anchor="nw", text="E-mail", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(669.0, 286.0, anchor="nw", text="Sobrenome", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(462.0, 286.0, anchor="nw", text="Nome", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(516.0, 220.0, anchor="nw", text=" Informações Profissionais:", fill="#000000", font=("Consolas Bold", 28 * -1))

        # nome
        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(551.0, 333.5, image=self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=464.0, y=320.0+ 130, width=174.0, height=29.0)
        self.entry_1.insert(0,USER_SESSION.get_user_data().nome)

        #telefone
        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(545.5, 472.5, image=self.entry_image_2)
        self.entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=467.0, y=459.0+ 130, width=157.0, height=29.0)
        self.entry_2.insert(0,USER_SESSION.get_user_data().telefone)

        #País
        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(747.5, 472.5, image=self.entry_image_3)
        self.entry_3 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=669.0, y=459.0+ 130, width=157.0, height=29.0)
        self.entry_3.insert(0,USER_SESSION.get_user_data().pais)

        #cpf
        self.entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(967.0, 472.5, image=self.entry_image_4)
        self.entry_4 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=882.0, y=459.0+ 130, width=170.0, height=29.0)
        self.entry_4.insert(0,USER_SESSION.get_user_data().cpf)


        #senha
        self.entry_image_5 = PhotoImage(file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(580.5, 552.5, image=self.entry_image_5)
        self.entry_5 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, show='*')
        self.entry_5.place(x=467.0, y=539.0+ 130, width=227.0, height=29.0)


        #Confirmar senha
        self.entry_image_6 = PhotoImage(file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(862.5, 550.5, image=self.entry_image_6)
        self.entry_6 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, show='*')
        self.entry_6.place(x=749.0, y=537.0+ 130, width=227.0, height=29.0)


        #Nome Empresa
        self.entry_image_7 = PhotoImage(file=self.relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(966.5, 401.5, image=self.entry_image_7)
        self.entry_7 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_7.place(x=881.0, y=388.0+ 130, width=171.0, height=29.0)
        self.entry_7.insert(0,USER_SESSION.get_user_data().nomeEmpresa)

        #Sobrenome
        self.entry_image_8 = PhotoImage(file=self.relative_to_assets("entry_8.png"))
        self.entry_bg_8 = self.canvas.create_image(759.0, 332.5, image=self.entry_image_8)
        self.entry_8 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_8.place(x=669.0, y=319.0+ 130, width=180.0, height=29.0)
        self.entry_8.insert(0,USER_SESSION.get_user_data().sobrenome)


        #E-mail
        self.entry_image_9 = PhotoImage(file=self.relative_to_assets("entry_9.png"))
        self.entry_bg_9 = self.canvas.create_image(656.5, 401.5, image=self.entry_image_9)
        self.entry_9 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_9.place(x=464.0, y=388.0+ 130, width=385.0, height=29.0)
        self.entry_9.insert(0,USER_SESSION.get_user_data().email)

        # Botão
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= self.update_user,
            relief="flat"
        )
        button_1.place(x=915.0, y=635.0 + 130, width=180.0, height=51.48387145996094)

        # Configuração final da janela
        self.atualizarcad.resizable(True, False)
        self.atualizarcad.mainloop()


    #funções
    def get_all_entry_values(self):
        entry_values = {
            "cpf": self.entry_4.get(),
            "nome": self.entry_1.get(),
            "sobrenome": self.entry_8.get(),
            "nome_empresa": self.entry_7.get(),
            "cargo": USER_SESSION.get_user_data().cargo,
            "email": self.entry_9.get(),
            "telefone": self.entry_2.get(),
            "pais": self.entry_3.get(),
            "senha_atual": USER_SESSION.get_user_data().senha,
            "nova_senha": self.entry_5.get(),
            "confirme_nova_senha": self.entry_6.get()
        }
        # Para demonstração, vamos imprimir os valores no console
        print("Valores das entradas:", entry_values)
        return entry_values

    def update_user(self):
        nome = self.entry_1.get()
        sobrenome = self.entry_8.get()
        cpf = self.entry_4.get()
        nome_empresa = self.entry_7.get()
        email = self.entry_9.get()
        telefone = self.entry_2.get()
        pais_localizacao = self.entry_3.get()
        senha = self.entry_5.get()
        confirme_senha = self.entry_6.get()

        def show_custom_error(title, message):
            error_window = Toplevel()
            error_window.title(title)
            error_window.geometry("400x200")
            error_window.configure(bg="#FFDDDD")

            title_label = Label(error_window, text=title, bg="#FF3333", fg="#FFFFFF", font=("Calibri Bold", 16))
            title_label.pack(pady=10, padx=10)

            message_label = Label(error_window, text=message, bg="#FFDDDD", fg="#FF0000", font=("Calibri", 14))
            message_label.pack(pady=20, padx=10)

            ok_button = Button(error_window, text="OK", command=error_window.destroy, bg="#FF6666", fg="#FFFFFF", font=("Calibri", 12), relief="flat")
            ok_button.pack(pady=10)

        if not nome or not sobrenome or not cpf or not nome_empresa or not email or not telefone or not pais_localizacao or not senha or not confirme_senha:
            show_custom_error("Erro", "Todos os campos devem ser preenchidos!")
            return
        
        values = self.get_all_entry_values()
        self.controlers['usuario'].update_user(**values)

    def update_name_text(self, name):
        self.canvas.itemconfig(self.name_text_id, text=name)

    def exit_fullscreen(self, event=None):
        self.atualizarcad.destroy()

        #Exclusivamente para o cargo
    def load_and_resize_image(self, image_path, size):
        image = Image.open(self.relative_to_assets(image_path))
        resized_image = image.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(resized_image)


    def relative_to_assets(self, path: str) -> Path:
        ASSETS_PATH = Path(os.path.dirname(os.path.abspath(__file__))) / 'assets' / 'frame0'
        return ASSETS_PATH / Path(path)

    def show_cargo_menu(self):
        self.cargo_menu.post(self.cargo_button.winfo_rootx(), self.cargo_button.winfo_rooty() + self.cargo_button.winfo_height())

    def select_cargo(self, cargo):
        self.selected_cargo = cargo
        self.cargo_button.config(text=cargo)
    
    def voltar_funcao(self):
        pass
