


import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


ASSETS_PATH = Path(os.path.dirname(os.path.abspath(__file__))) / 'assets' / 'frame0'


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#EFEFEF")


canvas = Canvas(
    window,
    bg = "#EFEFEF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    731.0,
    584.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    731.0,
    584.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    731.0,
    584.0,
    image=image_image_3
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    735.0,
    721.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=608.0,
    y=699.0,
    width=254.0,
    height=43.0
)

canvas.create_text(
    603.0,
    658.0,
    anchor="nw",
    text="Cargo",
    fill="#000000",
    font=("Calibri", 24 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1055.5,
    721.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=910.0,
    y=699.0,
    width=291.0,
    height=43.0
)

canvas.create_text(
    905.0,
    658.0,
    anchor="nw",
    text="Nome da Empresa",
    fill="#000000",
    font=("Calibri", 24 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    411.0,
    721.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=238.0,
    y=699.0,
    width=346.0,
    height=43.0
)

canvas.create_text(
    233.0,
    658.0,
    anchor="nw",
    text="Telefone",
    fill="#000000",
    font=("Calibri", 24 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    461.0,
    850.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=243.0,
    y=828.0,
    width=436.0,
    height=43.0
)

canvas.create_text(
    233.0,
    787.0,
    anchor="nw",
    text="Senha",
    fill="#000000",
    font=("Calibri", 24 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    988.5,
    850.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=763.0,
    y=828.0,
    width=451.0,
    height=43.0
)

canvas.create_text(
    745.0,
    787.0,
    anchor="nw",
    text="Confirme sua Senha",
    fill="#000000",
    font=("Calibri", 24 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    719.5,
    608.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=238.0,
    y=586.0,
    width=963.0,
    height=42.0
)

canvas.create_text(
    233.0,
    537.0,
    anchor="nw",
    text="e-mail",
    fill="#000000",
    font=("Calibri", 24 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    904.5,
    483.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=608.0,
    y=458.0,
    width=593.0,
    height=49.0
)

canvas.create_text(
    603.0,
    406.0,
    anchor="nw",
    text="Sobrenome",
    fill="#000000",
    font=("Calibri", 24 * -1)
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    406.0,
    483.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=238.0,
    y=458.0,
    width=336.0,
    height=49.0
)

canvas.create_text(
    233.0,
    406.0,
    anchor="nw",
    text="Nome",
    fill="#000000",
    font=("Calibri", 24 * -1)
)

canvas.create_text(
    154.0,
    315.0,
    anchor="nw",
    text=" Informações Profissionais:",
    fill="#000000",
    font=("Consolas Bold", 48 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=947.0,
    y=301.0,
    width=293.0,
    height=80.0
)

canvas.create_text(
    441.0,
    100.0,
    anchor="nw",
    text="Cadastre-se",
    fill="#000000",
    font=("Consolas Bold", 85 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    206.0,
    105.0,
    image=image_image_4
)
window.resizable(False, False)
window.mainloop()
