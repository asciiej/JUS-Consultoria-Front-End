
import re
import os
from pathlib import Path
from PIL import Image, ImageTk
from tkinter import Tk, Canvas, Entry, Button, PhotoImage,Menu
from src.classes.usuario.usuarioControler import usuarioControler
# Configuração dos caminhos


# Configuração da janela principal
class AtualizaCad:
    def __init__(self):
        self.atualizarcad = Tk()
        self.atualizarcad.geometry("1400x700")
        self.atualizarcad.configure(bg="#EFEFEF")
        #self.TkCadastro.attributes('-fullscreen', True)
        # Criação do canvas
        self.canvas = Canvas(
            self.atualizarcad,
            bg="#EFEFEF",
            height=700,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Imagens
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))

        # Criação das imagens no canvas
        self.canvas.create_image(720.0, 35.0, image=self.image_image_1)
        self.canvas.create_image(578.0, 127.0, image=self.image_image_2)
        self.canvas.create_image(738.0, 401.0, image=self.image_image_3)
    

        # Textos no canvas
        self.canvas.create_text(629.0, 119.0, anchor="nw", text="Gustavo Sabbatini Janot", fill="#000000", font=("Consolas", 22 * -1))
        self.canvas.create_text(877.0, 288.0, anchor="nw", text="Cargo", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(880.0, 357.0, anchor="nw", text="Nome da Empresa", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(462.0, 427.0, anchor="nw", text="Telefone", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(667.0, 427.0, anchor="nw", text="País / Localização", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(880.0, 428.0, anchor="nw", text="CPF", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(463.0, 506.0, anchor="nw", text="Senha", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(748.0, 507.0, anchor="nw", text="Confirme sua Senha", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(462.0, 357.0, anchor="nw", text="E-mail", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(669.0, 286.0, anchor="nw", text="Sobrenome", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(462.0, 286.0, anchor="nw", text="Nome", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(516.0, 220.0, anchor="nw", text=" Informações Profissionais:", fill="#000000", font=("Consolas Bold", 28 * -1))

        # Entradas de texto (Entry)
        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(551.0, 333.5, image=self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=464.0, y=320.0, width=174.0, height=29.0)

        #telefone
        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(545.5, 472.5, image=self.entry_image_2)
        self.entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=467.0, y=459.0, width=157.0, height=29.0)

        #País
        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(747.5, 472.5, image=self.entry_image_3)
        self.entry_3 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=669.0, y=459.0, width=157.0, height=29.0)

        #cpf
        self.entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(967.0, 472.5, image=self.entry_image_4)
        self.entry_4 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=882.0, y=459.0, width=170.0, height=29.0)

        #senha
        self.entry_image_5 = PhotoImage(file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(580.5, 552.5, image=self.entry_image_5)
        self.entry_5 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_5.place(x=467.0, y=539.0, width=227.0, height=29.0)

        #Confirmar senha
        self.entry_image_6 = PhotoImage(file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(862.5, 550.5, image=self.entry_image_6)
        self.entry_6 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_6.place(x=749.0, y=537.0, width=227.0, height=29.0)

        #Nome Empresa
        self.entry_image_7 = PhotoImage(file=self.relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(966.5, 401.5, image=self.entry_image_7)
        self.entry_7 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_7.place(x=881.0, y=388.0, width=171.0, height=29.0)

        #Sobrenome
        self.entry_image_8 = PhotoImage(file=self.relative_to_assets("entry_8.png"))
        self.entry_bg_8 = self.canvas.create_image(759.0, 332.5, image=self.entry_image_8)
        self.entry_8 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_8.place(x=669.0, y=319.0, width=180.0, height=29.0)

        #E-mail
        self.entry_image_9 = PhotoImage(file=self.relative_to_assets("entry_9.png"))
        self.entry_bg_9 = self.canvas.create_image(656.5, 401.5, image=self.entry_image_9)
        self.entry_9 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_9.place(x=464.0, y=388.0, width=385.0, height=29.0)

        # Cargo
        self.image_image_4 = self.load_and_resize_image("image_4.png", (200, 30))
        self.cargo_button = Button(
            self.atualizarcad,
            image=self.image_image_4,
            borderwidth=0,
            command=self.show_cargo_menu,
            compound="center",
            text="Cargos",
            fg="#000716",
            bg="#6ec1e4",
            activebackground="#6ec1e4", 
            activeforeground="#000000",
            font=("Calibri", 11)
        )
        self.cargo_button.place(x=869, y=318, width=200, height=30)
        
        self.cargo_menu = Menu(self.atualizarcad, tearoff=0, background="#FFFFFF", foreground="#000000")
        cargos = ["Cargo 1 ddff", "Cargo 2", "Cargo 3"]
        for cargo in cargos:
            self.cargo_menu.add_command(label=cargo, command=lambda c=cargo: self.select_cargo(c))

        self.selected_cargo = "Cargos"



        # Botão
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("clicou"),
            relief="flat"
        )
        button_1.place(x=915.0, y=635.0, width=180.0, height=51.48387145996094)

        # Configuração final da janela
        self.atualizarcad.resizable(False, False)
        self.atualizarcad.mainloop()

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