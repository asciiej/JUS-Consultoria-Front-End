import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


ASSETS_PATH = Path(os.path.dirname(os.path.abspath(__file__))) / 'assets' / 'frame0'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


TkCadastro = Tk()

TkCadastro.geometry("1000x600")
TkCadastro.configure(bg = "#EFEFEF")

def buttonOnClick():
    print("Clicou")

canvas = Canvas(
    TkCadastro,
    bg = "#EFEFEF",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    484.0,
    363.0,
    image=image_image_1
)

canvas.create_text(
    399.0,
    404.0,
    anchor="nw",
    text="Cargo",
    fill="#000000",
    font=("Calibri", 18 * -1)
)

canvas.create_text(
    589.0,
    404.0,
    anchor="nw",
    text="Nome da Empresa",
    fill="#000000",
    font=("Calibri", 18 * -1)
)

canvas.create_text(
    202.0,
    404.0,
    anchor="nw",
    text="Telefone",
    fill="#000000",
    font=("Calibri", 18 * -1)
)

canvas.create_text(
    206.0,
    485.0,
    anchor="nw",
    text="Senha",
    fill="#000000",
    font=("Calibri", 18 * -1)
)

canvas.create_text(
    523.0,
    485.0,
    anchor="nw",
    text="Confirme sua Senha",
    fill="#000000",
    font=("Calibri", 18 * -1)
)

canvas.create_text(
    205.0,
    321.0,
    anchor="nw",
    text="e-mail",
    fill="#000000",
    font=("Calibri", 18 * -1)
)

canvas.create_text(
    460.0,
    243.0,
    anchor="nw",
    text="Sobrenome",
    fill="#000000",
    font=("Calibri", 18 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    309.5,
    290.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=210.0,
    y=277.0,
    width=199.0,
    height=29.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    285.5,
    449.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=207.0,
    y=436.0,
    width=157.0,
    height=29.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    323.5,
    527.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    show='*'
)
entry_3.place(
    x=210.0,
    y=514.0,
    width=227.0,
    height=29.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    622.5,
    527.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    show='*'
)
entry_4.place(
    x=509.0,
    y=514.0,
    width=227.0,
    height=29.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    655.5,
    449.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=577.0,
    y=436.0,
    width=157.0,
    height=29.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    467.0,
    449.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=395.0,
    y=436.0,
    width=144.0,
    height=29.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    527.5,
    290.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=428.0,
    y=277.0,
    width=199.0,
    height=29.0
)

entry_image_cpf = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_cpf = canvas.create_image(
    727.5,
    290.5,
    image=entry_image_6
)
entry_cpf = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_cpf.place(
    x=655.0,
    y=277.0,
    width=144.0,
    height=29.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    465.0,
    368.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=203.0,
    y=355.0,
    width=524.0,
    height=29.0
)

canvas.create_text(
    205.0,
    243.0,
    anchor="nw",
    text="Nome",
    fill="#000000",
    font=("Calibri", 18 * -1)
)

canvas.create_text(
    700.0,
    243.0,
    anchor="nw",
    text="CPF",
    fill="#000000",
    font=("Calibri", 18 * -1)
)

canvas.create_text(
    154.0,
    183.0,
    anchor="nw",
    text=" Informações Profissionais:",
    fill="#000000",
    font=("Consolas Bold", 28 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=buttonOnClick,
    bg="#6ec1e4",
    relief="flat"
)
button_1.place(
    x=623.0,
    y=173.0,
    width=180.0,
    height=51.48387145996094
)

canvas.create_text(
    311.0,
    57.0,
    anchor="nw",
    text="Cadastre-se",
    fill="#000000",
    font=("Consolas Bold", 60 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    133.0,
    57.0,
    image=image_image_2
)

TkCadastro.mainloop()
