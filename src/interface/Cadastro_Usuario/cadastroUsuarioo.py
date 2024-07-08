import os
import re
import customtkinter as ctk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox, Toplevel, Label, Menu
from PIL import Image, ImageTk

class telaCadastro(ctk.CTkFrame):
    def __init__(self, parent, controlers):
        super().__init__(parent)
        self.parent = parent
        self.controlers = controlers
        self.titulo_font = ctk.CTkFont('Helvetica', 20)

        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        self.canvas = Canvas(
            self,
            height=altura_tela,
            width=largura_tela,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.pack_propagate(False)

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

        self.voltar = ctk.CTkButton(self.canvas, text="Voltar \u2192", command=self.voltar_funcao, **voltar_menu)
        self.voltar.pack(side=ctk.TOP, padx=(700, 0))

        self.canvas.place(x=0, y=0)
        #self.retangulo_vermelho = self.canvas.create_rectangle(441, 80, 300, 200, fill="red")
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(720.0, 378.0, image=self.image_image_1)

        self.canvas.create_text(859.0, 265.0, anchor="nw", text="Cargo", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(862.0, 334.0, anchor="nw", text="Nome da Empresa", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(444.0, 404.0, anchor="nw", text="Telefone", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(649.0, 404.0, anchor="nw", text="País / Localização", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(862.0, 405.0, anchor="nw", text="CPF", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(445.0, 483.0, anchor="nw", text="Senha", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(730.0, 484.0, anchor="nw", text="Confirme sua Senha", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(444.0, 334.0, anchor="nw", text="E-mail", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(651.0, 263.0, anchor="nw", text="Sobrenome", fill="#000000", font=("Calibri", 18 * -1))

        def on_focus_in(event):
            if self.entry_1.get() == "ex: nome":
                self.entry_1.delete(0, "end")
                self.entry_1.config(fg="#000716")

        def on_focus_out(event):
            if self.entry_1.get() == "":
                self.entry_1.insert(0,"ex: nome")
                self.entry_1.config(fg="gray")

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(533.0, 310.5, image=self.entry_image_1)
        self.entry_1 = Entry(self,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=446.0, y=297.0, width=174.0, height=29.0)  # Nome
        self.entry_1.insert(0,"ex: nome")
        self.entry_1.config(fg="gray")
        self.entry_1.bind("<FocusIn>", on_focus_in)
        self.entry_1.bind("<FocusOut>", on_focus_out)

        def on_focus_in(event):
            if self.entry_2.get() == "+55 DD 9....-....":
                self.entry_2.delete(0, "end")
                self.entry_2.config(fg="#000716")

        def on_focus_out(event):
            if self.entry_2.get() == "":
                self.entry_2.insert(0,"+55 DD 9....-....")
                self.entry_2.config(fg="gray")

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(527.5, 449.5, image=self.entry_image_2)
        self.entry_2 = Entry(self,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=449.0, y=436.0, width=157.0, height=29.0)  # Telefone
        self.entry_2.insert(0,"+55 DD 9....-....")
        self.entry_2.config(fg="gray")
        self.entry_2.bind("<FocusIn>", on_focus_in)
        self.entry_2.bind("<FocusOut>", on_focus_out)


        self.entry_image_paisLocalizacao = PhotoImage(file=self.relative_to_assets("entry_paisLocalizacao.png"))
        self.entry_bg_paisLocalizacao = self.canvas.create_image(729.5, 449.5, image=self.entry_image_paisLocalizacao)
        self.entry_paisLocalizacao = Entry(self,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_paisLocalizacao.place(x=651.0, y=436.0, width=157.0, height=29.0)  # País

        def on_focus_in(event):
            if self.entry_cpf.get() == " 000.000.000-00":
                self.entry_cpf.delete(0, "end")
                self.entry_cpf.config(fg="#000716")

        def on_focus_out(event):
            if self.entry_cpf.get() == "":
                self.entry_cpf.insert(0," 000.000.000-00")
                self.entry_cpf.config(fg="gray")

        self.entry_image_cpf = PhotoImage(file=self.relative_to_assets("entry_cpf.png"))
        self.entry_bg_cpf = self.canvas.create_image(949.0, 449.5, image=self.entry_image_cpf)
        self.entry_cpf = Entry(self,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_cpf.place(x=864.0, y=436.0, width=170.0, height=29.0)  # CPF
        self.entry_cpf.insert(0," 000.000.000-00")
        self.entry_cpf.config(fg="gray")
        self.entry_cpf.bind("<FocusIn>", on_focus_in)
        self.entry_cpf.bind("<FocusOut>", on_focus_out)

        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(562.5, 529.5, image=self.entry_image_3)
        self.entry_3 = Entry(self,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, show='*')
        self.entry_3.place(x=449.0, y=516.0, width=227.0, height=29.0)  # Senha


        self.entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(844.5, 527.5, image=self.entry_image_4)
        self.entry_4 = Entry(self,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, show='*')
        self.entry_4.place(x=731.0, y=514.0, width=227.0, height=29.0)  # Confirmar Senha


        def on_focus_in(event):
            if self.entry_5.get() == "ex: nome empresa":
                self.entry_5.delete(0, "end")
                self.entry_5.config(fg="#000716")

        def on_focus_out(event):
            if self.entry_5.get() == "":
                self.entry_5.insert(0,"ex: nome empresa")
                self.entry_5.config(fg="gray")

        self.entry_image_5 = PhotoImage(file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(948.5, 378.5, image=self.entry_image_5)
        self.entry_5 = Entry(self,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_5.place(x=863.0, y=365.0, width=171.0, height=29.0)  # Nome da Empresa
        self.entry_5.insert(0,"ex: nome empresa")
        self.entry_5.config(fg="gray")
        self.entry_5.bind("<FocusIn>", on_focus_in)
        self.entry_5.bind("<FocusOut>", on_focus_out)

        # Cargo
        self.image_image_2 = self.load_and_resize_image("image_2.png", (200, 30))
        self.cargo_button = Button(
            self,
            image=self.image_image_2,
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
        self.cargo_button.place(x=860, y=295, width=200, height=30)

        self.cargo_menu = Menu(self, tearoff=0, background="#FFFFFF", foreground="#000000")
        cargos = [
    "Diretor de Conformidade e Regulação",
    "Gerente de Contratos e Licitações",
    "Especialista em Propriedade Intelectual e Patentes",
    "Consultor de Fusões e Aquisições",
    "Diretor de Relações Trabalhistas",
    "Gestor de Compliance Financeiro",
    "Coordenador de Projetos de Infraestrutura",
    "Diretor de Privacidade e Proteção de Dados",
    "Gerente de Compliance Ambiental",
    "Consultor de Segurança e Conformidade em Tecnologia",
    "Diretor de Governança Corporativa",
    "Coordenador de Relações Governamentais e Assuntos Públicos",
    "Especialista em Comércio Internacional e Regulações Aduaneiras",
    "Gerente de Ética e Compliance",
    "Consultor de Investimentos e Conformidade Financeira",
    "Outro"
]
        for cargo in cargos:
            self.cargo_menu.add_command(label=cargo, command=lambda c=cargo: self.select_cargo(c))

        self.selected_cargo = "Cargos"

        self.entry_image_7 = PhotoImage(file=self.relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(741.0, 309.5, image=self.entry_image_7)
        self.entry_7 = Entry(self,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_7.place(x=651.0, y=296.0, width=180.0, height=29.0)  # Sobrenome

        self.entry_image_8 = PhotoImage(file=self.relative_to_assets("entry_8.png"))
        self.entry_bg_8 = self.canvas.create_image(638.5, 378.5, image=self.entry_image_8)
        self.entry_8 = Entry(self,bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_8.place(x=446.0, y=365.0, width=385.0, height=29.0)  # E-mail

        self.canvas.create_text(444.0, 263.0, anchor="nw", text="Nome", fill="#000000", font=("Calibri", 18 * -1))
        self.canvas.create_text(390.0, 203.0, anchor="nw", text=" Informações Profissionais:", fill="#000000", font=("Consolas Bold", 28 * -1))

        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0, command=self.buttonOnClick, bg="#6ec1e4", activebackground="#6ec1e4")
        self.button_1.place(x=859.0, y=195.0, width=180.0, height=51.48387145996094)

        self.canvas.create_text(441.0, 71.0, anchor="nw", text="Cadastro Usuário", fill="#000000", font=("Consolas Bold", 60 * -1))


        self.image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(126.0, 57.0, image=self.image_image_3)


        #self.TkCadastro.mainloop()

    #Exclusivamente para o cargo
    def load_and_resize_image(self, image_path, size):
        image = Image.open(self.relative_to_assets(image_path))
        resized_image = image.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(resized_image)

    def relative_to_assets(self, path: str) -> Path:
        ASSETS_PATH = Path(os.path.dirname(os.path.abspath(__file__))) / 'assets' / 'frame0'
        return ASSETS_PATH / Path(path)

    def buttonOnClick(self):
        nome = self.entry_1.get()
        sobrenome = self.entry_7.get()
        cpf = self.entry_cpf.get()
        nome_empresa = self.entry_5.get()
        email = self.entry_8.get()
        telefone = self.entry_2.get()
        pais_localizacao = self.entry_paisLocalizacao.get()
        cargo = self.selected_cargo
        senha = self.entry_3.get()
        confirme_senha = self.entry_4.get()

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

        if not nome or not sobrenome or not cpf or not nome_empresa or not email or not telefone or not pais_localizacao or not cargo or not senha or not confirme_senha:
            show_custom_error("Erro", "Todos os campos devem ser preenchidos!")
            return

        if not self.validar_cpf(cpf):
            messagebox.showerror("Erro", "CPF inválido!")
            return

        if not self.validar_email(email):
            messagebox.showerror("Erro", "E-mail inválido!")
            return

        if senha != confirme_senha:
            messagebox.showerror("Erro", "As senhas não coincidem!")
            return



        #print(cargo.encode('utf-8'))
        retorno = self.controlers['usuario'].register(nome = nome, sobrenome = sobrenome,cpf = cpf,nome_empresa=  nome_empresa,email= email,telefone= telefone,pais= pais_localizacao,cargo= cargo,senha= senha,confirme_senha= confirme_senha)

    def validar_cpf(self, cpf):
        cpf = re.sub(r'\D', '', cpf)
        if len(cpf) != 11 or not cpf.isdigit():
            return False
        return True

    def validar_email(self, email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def show_cargo_menu(self):
        self.cargo_menu.post(self.cargo_button.winfo_rootx(), self.cargo_button.winfo_rooty() + self.cargo_button.winfo_height())

    def select_cargo(self, cargo):
        self.selected_cargo = cargo
        self.cargo_button.config(text=cargo)

    def voltar_funcao(self):
      #self.clear_fields()
        self.parent.show_frame("TelaLogin")
      