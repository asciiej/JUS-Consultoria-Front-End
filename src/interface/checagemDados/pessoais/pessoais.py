
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Documentos\Estudos\ASCII\FrontJUS\Tkinter-Designer-master\build\assets\frame0")


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
canvas.create_rectangle(
    0.0,
    0.0,
    1440.0,
    104.0,
    fill="#6EC1E4",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    107.0,
    52.0,
    image=image_image_1
)

canvas.create_text(
    205.0,
    18.0,
    anchor="nw",
    text="Checagem de Dados:",
    fill="#FFFFFF",
    font=("JostRoman Regular", 48 * -1)
)

canvas.create_text(
    1068.0,
    42.0,
    anchor="nw",
    text="Gustavo Janot",
    fill="#FFFFFF",
    font=("Calibri", 28 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1357.0,
    52.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    720.0,
    519.0,
    image=image_image_3
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    481.0,
    683.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EFEFEF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=278.0,
    y=663.0,
    width=406.0,
    height=43.0
)

canvas.create_text(
    273.0,
    620.0,
    anchor="nw",
    text="Senha",
    fill="#000000",
    font=("JostRoman Regular", 24 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    939.0,
    683.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EFEFEF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=738.0,
    y=663.0,
    width=402.0,
    height=43.0
)

canvas.create_text(
    744.0,
    620.0,
    anchor="nw",
    text="Confirme sua Senha",
    fill="#000000",
    font=("JostRoman Regular", 24 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    880.0,
    559.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#EFEFEF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=619.0,
    y=536.0,
    width=522.0,
    height=46.0
)

canvas.create_text(
    626.0,
    491.0,
    anchor="nw",
    text="Cargo",
    fill="#000000",
    font=("JostRoman Regular", 24 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    433.0,
    559.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#EFEFEF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=278.0,
    y=536.0,
    width=310.0,
    height=46.0
)

canvas.create_text(
    282.0,
    491.0,
    anchor="nw",
    text="Telefone",
    fill="#000000",
    font=("JostRoman Regular", 24 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    709.0,
    437.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#EFEFEF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=278.0,
    y=416.0,
    width=862.0,
    height=45.0
)

canvas.create_text(
    290.0,
    364.0,
    anchor="nw",
    text="E-mail",
    fill="#000000",
    font=("JostRoman Regular", 24 * -1)
)

canvas.create_text(
    273.0,
    281.0,
    anchor="nw",
    text=" Informações Pessoais:",
    fill="#000000",
    font=("JostRoman Regular", 48 * -1)
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
    x=979.0,
    y=827.0,
    width=270.0,
    height=80.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    725.0,
    178.0,
    image=image_image_4
)
window.resizable(False, False)
window.mainloop()
