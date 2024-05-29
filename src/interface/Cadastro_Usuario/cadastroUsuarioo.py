import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from src.classes.usuario.usuarioControler import usuarioControler

# entry_1 nome
# entry_2 telefone
# entry_3 senha
# entry_4 confirmeSenha
# entry_5 nomeDaEmpresa
# entry_6 cargo
# entry_7 sobrenome
# entry_8 eMail
# entry_cpf cpf
# entry_paisLocalizacao pais Localização

class telaCadastro:

    def __init__(self):
        print("Rodou")
        self.TkCadastro = Tk()

        self.TkCadastro.geometry("1000x600")
        self.TkCadastro.configure(bg = "#EFEFEF")


        self.canvas = Canvas(
            self.TkCadastro,
            bg = "#EFEFEF",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            484.0,
            363.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            399.0,
            404.0,
            anchor="nw",
            text="Cargo",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.canvas.create_text(
            589.0,
            404.0,
            anchor="nw",
            text="Nome da Empresa",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.canvas.create_text(
            202.0,
            404.0,
            anchor="nw",
            text="Telefone",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.canvas.create_text(
            336.0,
            485.0,
            anchor="nw",
            text="Senha",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.canvas.create_text(
            583.0,
            485.0,
            anchor="nw",
            text="Confirme sua Senha",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.canvas.create_text(
            225.0,
            321.0,
            anchor="nw",
            text="e-mail",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.canvas.create_text(
            460.0,
            243.0,
            anchor="nw",
            text="Sobrenome",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            309.5,
            290.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=210.0,
            y=277.0,
            width=199.0,
            height=29.0
        )

        entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            285.5,
            449.5,
            image=entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=207.0,
            y=436.0,
            width=157.0,
            height=29.0
        )

        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            443.5,
            527.5,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            show='*'
        )
        self.entry_3.place(
            x=330.0,
            y=514.0,
            width=227.0,
            height=29.0
        )

        self.entry_image_4 = PhotoImage(
            file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            690.5,
            527.5,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            show='*'
        )
        self.entry_4.place(
            x=579.0,
            y=514.0,
            width=227.0,
            height=29.0
        )

        self.entry_image_5 = PhotoImage(
            file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            655.5,
            449.5,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(
            x=577.0,
            y=436.0,
            width=157.0,
            height=29.0
        )

        self.entry_image_6 = PhotoImage(
            file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            467.0,
            449.5,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_6.place(
            x=395.0,
            y=436.0,
            width=144.0,
            height=29.0
        )

        self.entry_image_7 = PhotoImage(
            file=self.relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(
            527.5,
            290.5,
            image=self.entry_image_7
        )
        self.entry_7 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_7.place(
            x=428.0,
            y=277.0,
            width=199.0,
            height=29.0
        )

        self.entry_image_cpf = PhotoImage(
            file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_cpf = self.canvas.create_image(
            727.5,
            290.5,
            image=self.entry_image_6
        )
        self.entry_cpf = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_cpf.place(
            x=655.0,
            y=277.0,
            width=144.0,
            height=29.0
        )

        self.entry_image_paisLocalizacao = PhotoImage(
            file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_paisLocalizacao = self.canvas.create_image(
            240.5,
            527.5,
            image=self.entry_image_6
        )
        self.entry_paisLocalizacao = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_paisLocalizacao.place(
            x=170.0,
            y=514.0,
            width=144.0,
            height=29.0
        )

        self.entry_image_8 = PhotoImage(
            file=self.relative_to_assets("entry_8.png"))
        self.entry_bg_8 = self.canvas.create_image(
            485.0,
            368.5,
            image=self.entry_image_8
        )
        self.entry_8 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
        )
        self.entry_8.place(
            x=223.0,
            y=355.0,
            width=524.0,
            height=29.0
        )

        self.canvas.create_text(
            205.0,
            243.0,
            anchor="nw",
            text="Nome",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.canvas.create_text(
            700.0,
            243.0,
            anchor="nw",
            text="CPF",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.canvas.create_text(
            170.0,
            485.0,
            anchor="nw",
            text="País / Localização",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.canvas.create_text(
            154.0,
            183.0,
            anchor="nw",
            text=" Informações Profissionais:",
            fill="#000000",
            font=("Consolas Bold", 28 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonOnClick,
            bg="#6ec1e4",
            relief="flat"
        )
        self.button_1.place(
            x=623.0,
            y=173.0,
            width=180.0,
            height=51.48387145996094
        )

        self.canvas.create_text(
            311.0,
            57.0,
            anchor="nw",
            text="Cadastre-se",
            fill="#000000",
            font=("Consolas Bold", 60 * -1)
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            133.0,
            57.0,
            image=self.image_image_2
        )

        self.TkCadastro.mainloop()

    def relative_to_assets(self,path: str) -> Path:
        ASSETS_PATH = Path(os.path.dirname(os.path.abspath(__file__))) / 'assets' / 'frame0'
        return ASSETS_PATH / Path(path)
    
    def buttonOnClick(self):
        usuarioControler().cadastro(self.entry_1.get(),self.entry_7.get(),self.entry_cpf.get(),self.entry_5.get(),self.entry_6.get(),self.entry_8.get(),self.entry_2.get(),self.entry_paisLocalizacao.get(),self.entry_3.get(),self.entry_4.get())
        
