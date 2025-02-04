
import os
from pathlib import Path
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import Canvas, Entry, Button, PhotoImage, Toplevel, Label, messagebox
import tkinter as tk
from ...utilitarios.user_session import USER_SESSION
import sys

class AtualizaCad(ctk.CTkFrame):
    def __init__(self, parent, controlers):
        super().__init__(parent)
        self.parent = parent
        self.controlers = controlers
        self.titulo_font = ctk.CTkFont('Helvetica', 20)

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
        '''
        def show_custom_sucess(title, message):
            error_window = Toplevel()
            error_window.title(title)
            error_window.geometry("400x200")
            error_window.configure(bg="#FFDDDD")

            title_label = Label(error_window, text=title, bg="#74FF33", fg="#FFFFFF", font=("Calibri Bold", 16))
            title_label.pack(pady=10, padx=10)

            message_label = Label(error_window, text=message, bg="#74FF33", fg="#000000", font=("Calibri", 14))
            message_label.pack(pady=20, padx=10)

            ok_button = Button(error_window, text="OK", command=error_window.destroy, bg="#74FF33", fg="#FFFFFF", font=("Calibri", 12), relief="flat")
            ok_button.pack(pady=10)
'''
        if not nome or not sobrenome or not cpf or not nome_empresa or not email or not telefone or not pais_localizacao or not senha or not confirme_senha:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return
        else:
            messagebox.showinfo("Parabéns!", "Usuário atualizado com sucesso!")

        values = self.get_all_entry_values()
        self.controlers['usuario'].update_user(**values)
        self.voltar_funcao()

    def update_name_text(self, name):
        self.canvas.itemconfig(self.name_text_id, text=name)

    def exit_fullscreen(self, event=None):
        self.atualizarcad.destroy()

        #Exclusivamente para o cargo
    def load_and_resize_image(self, image_path, size):
        image = Image.open(self.relative_to_assets(image_path))
        resized_image = image.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(resized_image)


    def relative_to_assets(self,path: str) -> Path:
        # Determine if the script is running as a standalone executable
        if hasattr(sys, '_MEIPASS'):
            # When running from the PyInstaller bundle, use the _MEIPASS attribute
            ASSETS_PATH = Path(sys._MEIPASS) / 'image_files_atl'
        else:
            # When running from the script, use the script's directory
            ASSETS_PATH = Path(os.path.dirname(os.path.abspath(__file__))) / 'assets' / 'frame0'

        final_path = ASSETS_PATH / Path(path)    
        return final_path
        

    def show_cargo_menu(self):
        self.cargo_menu.post(self.cargo_button.winfo_rootx(), self.cargo_button.winfo_rooty() + self.cargo_button.winfo_height())

    def select_cargo(self, cargo):
        self.selected_cargo = cargo
        self.cargo_button.config(text=cargo)

    def voltar_funcao(self):
        self.unbind("<Configure>")
        for widget in self.winfo_children():
            widget.destroy()
        self.parent.show_frame("telaPrincipal")
        self.parent.frames["telaPrincipal"].show_content()


    def show_contentATUALIZAR(self):



        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        centro_x = largura_tela /2
        centro_y = altura_tela / 2


        #criação do canvas
        self.canvas = Canvas(
            self,
            height=altura_tela,
            width=largura_tela,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)

        self.font = ctk.CTkFont('Helvetica',14)

        # Cabeçalho menu personalizado
        cabecalho_menu = {
            "corner_radius": 0,
            "border_width": 0,
            "fg_color": ["#6EC1E4", "#6EC1E4"]
        }

        # Cabeçalho
        self.cabecalho = ctk.CTkFrame(self, height=104, **cabecalho_menu)
        self.cabecalho.pack(fill=ctk.X, pady=(0, 40))

        # Logo
        self.logoJUS = ctk.CTkImage(Image.open('imagens/Logomarca JUS.png'),size = (80,72.54))
        self.logo_cabecalho = ctk.CTkLabel(self.cabecalho, image=self.logoJUS, text = "")
        self.logo_cabecalho.pack(side=ctk.LEFT, padx=(18, 0), pady=7)


        self.canvas.create_text(centro_x, 210.0, text="", fill="#000000", font=("Consolas Bold", 60 * -1))





        #place holder testee
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

        self.voltar = ctk.CTkButton(self.cabecalho, text="Voltar", command=self.voltar_funcao, **voltar_menu)
        self.voltar.pack(side=ctk.RIGHT, padx=(80, 0), pady = 50)


        # Imagens
        #self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        #self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))


        # Criação das imagens no canvas
        #self.canvas.create_image(centro_x, 35.0, image=self.image_image_1)
        #self.canvas.create_image(centro_x, 127.0, image=self.image_image_2)
        self.canvas.create_image(centro_x, centro_y, image=self.image_image_3)


        # Botão
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        button_1 = Button(self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= self.update_user,
            relief="flat"
        )
        button_1.place(x= centro_x + 195.0, y= centro_y + 235.0, width=180.0, height=51.48387145996094)

        # Configuração final da janela
        #self.atualizarcad.resizable(True, False)
        #self.atualizarcad.mainloop()


        # Textos no canvas


        #self.name_text_id = self.canvas.create_text(centro_x, 305.0, text=f"{USER_SESSION.get_user_data().nome} {USER_SESSION.get_user_data().sobrenome}", fill="#000000", font=("Consolas", 22 * -1))
        self.canvas.create_text(centro_x + 110, centro_y - 27, anchor="nw", text="Nome da Empresa", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(centro_x - 300, centro_y + 45, anchor="nw", text="Telefone", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(centro_x - 101, centro_y + 45, anchor="nw", text="País / Localização", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(centro_x + 115, centro_y + 45, anchor="nw", text="CPF", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(centro_x - 301, centro_y + 119.0, anchor="nw", text="Nova Senha", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(centro_x + 90, centro_y + 119.0, anchor="nw", text="Confirme sua Nova Senha", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(centro_x - 300, centro_y - 27, anchor="nw", text="E-mail", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(centro_x + 115, centro_y - 97.0, anchor="nw", text="Sobrenome", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(centro_x - 300, centro_y - 97.0, anchor="nw", text="Nome", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(centro_x, centro_y - 163.0, text="Atualização de dados Cadastro:", fill="#000000", font=("Consolas Bold", 28 * -1))

        # nome
        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(centro_x - 215,centro_y - 50, image=self.entry_image_1)
        self.entry_1 = Entry(self,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_1.place(x= centro_x - 300, y=centro_y - 64, width=174.0, height=29.0)
        self.entry_1.insert(0,USER_SESSION.get_user_data().nome)

        #telefone
        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(centro_x - 221, centro_y +88.0, image=self.entry_image_2)
        self.entry_2 = Entry(self,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_2.place(x= centro_x - 300, y=centro_y + 74.0, width=157.0, height=29.0)
        self.entry_2.insert(0,USER_SESSION.get_user_data().telefone)

        #País
        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(centro_x - 26, centro_y +88.0, image=self.entry_image_3)
        self.entry_3 = Entry(self,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_3.place(x= centro_x - 101, y=centro_y + 74.0, width=157.0, height=29.0)
        self.entry_3.insert(0,USER_SESSION.get_user_data().pais)

        #cpf
        self.entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(centro_x + 202, centro_y +88.0, image=self.entry_image_4)
        self.entry_4 = Entry(self,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=centro_x + 115,y=centro_y + 74.0, width=170.0, height=29.0)
        self.entry_4.insert(0,USER_SESSION.get_user_data().cpf)


        #nova senha
        self.entry_image_5 = PhotoImage(file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(centro_x - 187, centro_y +169.0, image=self.entry_image_5)
        self.entry_5 = Entry(self,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, show='*')
        self.entry_5.place(x= centro_x - 300,y=centro_y +155.0, width=227.0, height=29.0)


        #Confirmar senha
        self.entry_image_6 = PhotoImage(file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(centro_x + 202, centro_y +169.0, image=self.entry_image_6)
        self.entry_6 = Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, show='*')
        self.entry_6.place(x=centro_x + 92,y=centro_y +155.0, width=227.0, height=29.0)


        #Nome Empresa
        self.entry_image_7 = PhotoImage(file=self.relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(centro_x + 202, centro_y + 20, image=self.entry_image_7)
        self.entry_7 = Entry(self,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_7.place(x=centro_x + 115, y= centro_y + 6.0, width=171.0, height=29.0)
        self.entry_7.insert(0,USER_SESSION.get_user_data().nomeEmpresa)

        #Sobrenome
        self.entry_image_8 = PhotoImage(file=self.relative_to_assets("entry_8.png"))
        self.entry_bg_8 = self.canvas.create_image(centro_x + 202, centro_y - 50, image=self.entry_image_8)
        self.entry_8 = Entry(self,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_8.place(x=centro_x + 115, y=centro_y - 64, width=180.0, height=29.0)
        self.entry_8.insert(0,USER_SESSION.get_user_data().sobrenome)


        #E-mail
        self.entry_image_9 = PhotoImage(file=self.relative_to_assets("entry_9.png"))
        self.entry_bg_9 = self.canvas.create_image(centro_x - 110, centro_y + 20, image=self.entry_image_9)
        self.entry_9 = Entry(self,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_9.place(x=centro_x - 300, y= centro_y + 6.0, width=385.0, height=29.0)
        self.entry_9.insert(0,USER_SESSION.get_user_data().email)

