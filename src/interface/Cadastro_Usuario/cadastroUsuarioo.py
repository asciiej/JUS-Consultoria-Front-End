
import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from src.classes.usuario.usuarioControler import usuarioControler

# entry_1 nome
# entry_2 telefone
# entry_3 senha
# entry_4 confirmeSenha
# entry_5 nomeDaEmpresa
# image_image_2  cargo
# entry_7 sobrenome
# entry_8 eMail
# entry_paisLocalizacao pais Localização
# entry_cpf cpf




class telaCadastro:
    def __init__(self):
        self.TkCadastro = Tk()


        self.TkCadastro.geometry("1400x720")

        #self.TkCadastro.attributes('-fullscreen', True)
        
        self.TkCadastro.configure(bg = "#EFEFEF")


        self.canvas = Canvas(
            self.TkCadastro,
            bg = "#EFEFEF",
            height = 720,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            720.0,
            378.0,
            image=self.image_image_1
        )


        self.canvas.create_text(
            859.0,
            265.0,
            anchor="nw",
            text="Cargo",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.canvas.create_text(
            862.0,
            334.0,
            anchor="nw",
            text="Nome da Empresa",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.canvas.create_text(
            444.0,
            404.0,
            anchor="nw",
            text="Telefone",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.canvas.create_text(
            649.0,
            404.0,
            anchor="nw",
            text="País / Localização",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.canvas.create_text(
            862.0,
            405.0,
            anchor="nw",
            text="CPF",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.canvas.create_text(
            445.0,
            483.0,
            anchor="nw",
            text="Senha",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.canvas.create_text(
            730.0,
            484.0,
            anchor="nw",
            text="Confirme sua Senha",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.canvas.create_text(
            444.0,
            334.0,
            anchor="nw",
            text="E-mail",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.canvas.create_text(
            651.0,
            263.0,
            anchor="nw",
            text="Sobrenome",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            533.0,
            310.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place( #nome
            x=446.0,
            y=297.0,
            width=174.0,
            height=29.0
        )

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            527.5,
            449.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place( #telefone
            x=449.0,
            y=436.0,
            width=157.0,
            height=29.0
        )

        self.entry_image_paisLocalizacao = PhotoImage(
            file=self.relative_to_assets("entry_paisLocalizacao.png"))
        self.entry_bg_paisLocalizacao = self.canvas.create_image(
            729.5,
            449.5,
            image=self.entry_image_paisLocalizacao
        )
        self.entry_paisLocalizacao = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_paisLocalizacao.place( #país
            x=651.0,
            y=436.0,
            width=157.0,
            height=29.0
        )

        self.entry_image_cpf = PhotoImage(
            file= self.relative_to_assets("entry_cpf.png"))
        self.entry_bg_cpf = self.canvas.create_image(
            949.0,
            449.5,
            image=self.entry_image_cpf
        )
        self.entry_cpf = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_cpf.place( #cpf
            x=864.0,
            y=436.0,
            width=170.0,
            height=29.0
        )

        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            562.5,
            529.5,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place( #senha
            x=449.0,
            y=516.0,
            width=227.0,
            height=29.0
        )

        self.entry_image_4 = PhotoImage(
            file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            844.5,
            527.5,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place( #confirmar_senha
            x=731.0,
            y=514.0,
            width=227.0,
            height=29.0
        )

        self.entry_image_5 = PhotoImage(
            file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            948.5,
            378.5,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place( #nome_empresa
            x=863.0,
            y=365.0,
            width=171.0,
            height=29.0
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            949.0,
            309.0,
            image=self.image_image_2 #cargo
        )

        self.entry_image_7 = PhotoImage(
            file=self.relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(
            741.0,
            309.5,
            image=self.entry_image_7
        )
        self.entry_7 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_7.place( #sobrenome
            x=651.0,
            y=296.0,
            width=180.0,
            height=29.0
        )

        self.entry_image_8 = PhotoImage(
            file=self.relative_to_assets("entry_8.png"))
        self.entry_bg_8 = self.canvas.create_image(
            638.5,
            378.5,
            image=self.entry_image_8
        )
        self.entry_8 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_8.place( #email
            x=446.0,
            y=365.0,
            width=385.0,
            height=29.0
        )

        self.canvas.create_text(
            444.0,
            263.0,
            anchor="nw",
            text="Nome",
            fill="#000000",
            font=("Calibri", 18 * -1)
        )

        self.canvas.create_text(
            390.0,
            203.0,
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
            x=859.0,
            y=195.0,
            width=180.0,
            height=51.48387145996094
        )

        self.canvas.create_text(
            441.0,
            71.0,
            anchor="nw",
            text="Cadastro Usuário",
            fill="#000000",
            font=("Consolas Bold", 60 * -1)
        )

        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            126.0,
            57.0,
            image=self.image_image_3
        )
        self.TkCadastro.resizable(False, False)
        self.TkCadastro.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        ASSETS_PATH = Path(os.path.dirname(os.path.abspath(__file__))) / 'assets' / 'frame0'
        return ASSETS_PATH / Path(path)

    def buttonOnClick(self):
        usuarioControler().cadastro(self.entry_1.get(),self.entry_7.get(),self.entry_cpf.get(),self.entry_5.get(),self.entry_8.get(),self.entry_2.get(),self.entry_paisLocalizacao.get(),self.entry_3.get(),self.entry_4.get())


