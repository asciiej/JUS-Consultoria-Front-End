import tkinter as tk
import customtkinter
from PIL import Image
from functools import partial
from ..utilitarios.user_session import USER_SESSION
#from ..utilitarios.user_session import USER_SESSION


class alterarAcesso:
    def __init__(self,janela, controlers):
        customtkinter.set_default_color_theme("lib/temaTkinterCustom.json")

        self.janela = janela
        self.font = customtkinter.CTkFont('Helvetica', 14)
        self.titulo_font = customtkinter.CTkFont('Helvetica', 20)
        self.controlers = controlers

        # Cabeçalho menu personalizado
        cabecalho_menu = {
            "corner_radius": 0,
            "border_width": 0,
            "fg_color": ["#6EC1E4", "#6EC1E4"]
        }

        # Cabeçalho
        self.cabecalho = customtkinter.CTkFrame(self.janela, height=104, **cabecalho_menu)
        self.cabecalho.pack(fill=customtkinter.X)

        # Logo
        self.logoJUS = customtkinter.CTkImage(Image.open('imagens/Logomarca JUS.png'), size=(80, 72.54))
        self.logo_cabecalho = customtkinter.CTkLabel(self.cabecalho, image=self.logoJUS, text="")
        self.logo_cabecalho.pack(side=customtkinter.LEFT, padx=(18, 0), pady=7)

        # Usuario foto
        self.userPic = customtkinter.CTkImage(Image.open('imagens/User Male Black.png'), size=(90, 90))
        self.userPic_cabecalho = customtkinter.CTkLabel(self.cabecalho, image=self.userPic, text="")
        self.userPic_cabecalho.pack(side=customtkinter.RIGHT, padx=(0, 18), pady=7)

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
        self.h1_titulo = customtkinter.CTkLabel(self.cabecalho, text="Mudar nível de acesso de usuário", font=self.titulo_font)
        self.h1_titulo.pack(side=customtkinter.LEFT, padx=(25, 0))

        self.voltar = customtkinter.CTkButton(self.cabecalho, text="Voltar \u2192", command=self.voltar_funcao, **voltar_menu)
        self.voltar.pack(side=customtkinter.LEFT, padx=(700, 0))

         # Nome do usuario no cabeçalho
        self.nome_usuario_label = customtkinter.CTkLabel(self.cabecalho, text=f"{USER_SESSION.get_user_data().nome} {USER_SESSION.get_user_data().sobrenome}", font=self.font)
        self.nome_usuario_label.pack(side=customtkinter.RIGHT, padx=(0, 25))

        # Calcular a altura do "body"
        self.janela.update_idletasks()
        window_height = self.janela.winfo_height()
        header_height = self.cabecalho.winfo_height()
        body_height = window_height - header_height

        # Body
        self.canvas = tk.Canvas(self.janela, height=body_height)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Frame
        self.frame = customtkinter.CTkScrollableFrame(self.canvas, height=480, width=900)
        self.frame.pack(pady=(100, 0))

        caixa_busca = {
            "corner_radius": 40,  # Raio dos cantos
            "font": ("Helvetica", 17),
            "width": 800,
            "height": 45
        }

        # Caixa de busca
        self.caixa_busca = customtkinter.CTkEntry(self.frame, **caixa_busca, placeholder_text="Pesquise o nome de um usuário")
        self.caixa_busca.pack(padx=20, pady=20, side=tk.TOP)

        user_frame = {
            "corner_radius": 28,
            "width": 800,
            "height": 85,
            "fg_color": ["#D9D9D9", "#D9D9D9"]
        }

        self.frame_usuarios = []

        usuarios = controlers['usuario'].get_all_users()

        for usuario in usuarios:
            novo_frame = customtkinter.CTkFrame(self.frame, **user_frame)
            novo_frame.pack(pady=(10, 0))
            novo_frame.pack_propagate(False)


            # Usuario foto
            self.foto = customtkinter.CTkImage(Image.open('imagens/User Male Black.png'), size=(70, 70))
            self.foto_usuario = customtkinter.CTkLabel(novo_frame, image=self.foto, text="")
            self.foto_usuario.pack(side=customtkinter.LEFT, anchor=customtkinter.NW, padx=(20, 0), pady=(10, 0))

            # Labels para exibir nome e CPF do usuário
            nome = customtkinter.CTkLabel(novo_frame, text=f"{usuario.nome}", font=self.titulo_font)
            nome.pack(side=customtkinter.LEFT, anchor=customtkinter.NW, padx=(10, 0), pady=(30, 0))

            cpf = customtkinter.CTkLabel(novo_frame, text=f"CPF: {usuario.cpf}", font=self.font)
            cpf.pack(side=customtkinter.LEFT, anchor=customtkinter.NW, padx=(15, 0), pady=(32, 0))

            checkbox = {
                "corner_radius": 5,
                "border_width": 2,
                "border_color": "#325564",
                "fg_color": ["#6EC1E4", "#183E4F"],
                "hover_color": ["#6EC1E4", "#183E4F"],
                "text_color": "#000000",
                "text_color_disabled": ["#6EC1E4", "#183E4F"],
                "font": ("Helvetica", 14)
            }


            self.cb_consultoria_empresarial = customtkinter.CTkCheckBox(novo_frame, text="Consultoria Empresarial", **checkbox)

            self.cb_consultoria_tributaria = customtkinter.CTkCheckBox(novo_frame, text="Consultoria Tributária", **checkbox)

            self.cb_camara_arbitragem = customtkinter.CTkCheckBox(novo_frame, text="Câmara de Arbitragem", **checkbox)

            alterar = {
                "corner_radius": 20,
                "border_width": 0,
                "width": 160,
                "height": 36,
                "fg_color": ["#325564", "#325564"],
                "hover_color": ["#183E4F", "#183E4F"],
                "border_color": ["#6EC1E4", "#6EC1E4"],
                "text_color": "#EFEFEF",
                "text_color_disabled": ["#EFEFEF", "#EFEFEF"]
            }

            submeter = {
                "corner_radius": 20,
                "border_width": 0,
                "width": 190,
                "height": 36,
                "fg_color": ["#325564", "#325564"],
                "hover_color": ["#183E4F", "#183E4F"],
                "border_color": ["#6EC1E4", "#6EC1E4"],
                "text_color": "#EFEFEF",
                "text_color_disabled": ["#EFEFEF", "#EFEFEF"]
            }

            cancelarr = {
                "corner_radius": 20,
                "border_width": 0,
                "width": 160,
                "height": 36,
                "fg_color": ["#941111", "#941111"],
                "hover_color": ["#4F1818", "#4F1818"],
                "border_color": ["#E46E6E", "#E46E6E"],
                "text_color": "#EFEFEF",
                "text_color_disabled": ["#EFEFEF", "#EFEFEF"]
            }

            botao_alterar_acesso = customtkinter.CTkButton(novo_frame, text="Alterar Acesso", **alterar)
            botao_alterar_acesso.pack(side=customtkinter.RIGHT, anchor=customtkinter.NE, padx=(0, 20), pady=(30, 0))

            botao_submeter = customtkinter.CTkButton(novo_frame, text="Submeter Alterações", **submeter)
            # botao_cancelar.pack(side=customtkinter.RIGHT, anchor=customtkinter.SE,padx=(0, 20), pady = (0,20))

            botao_cancelar = customtkinter.CTkButton(novo_frame, text="Cancelar", **cancelarr)
            # botao_cancelar.pack(side=customtkinter.RIGHT, anchor=customtkinter.SE,padx=(0, 20), pady = (0,20))

            # Função dos botões
            botao_alterar_acesso.configure(command=partial(self.toggle_frame_expansion, novo_frame, novo_frame.winfo_height(), usuario, botao_alterar_acesso, botao_cancelar, botao_submeter,self.cb_consultoria_empresarial, self.cb_consultoria_tributaria, self.cb_camara_arbitragem))

            botao_cancelar.configure(command=partial(self.toggle_frame_expansion, novo_frame, novo_frame.winfo_height(), usuario, botao_alterar_acesso, botao_cancelar, botao_submeter,self.cb_consultoria_empresarial, self.cb_consultoria_tributaria, self.cb_camara_arbitragem))

            self.frame_usuarios.append(novo_frame)



        # Pesquisar usuarios
        self.caixa_busca.bind("<KeyRelease>", self.pesquisar_usuarios)

        self.janela.mainloop()

    def toggle_frame_expansion(self, frame, initial_height, usuario, botao_alterar, botao_cancelar, botao_submeter,cb_consultoria_empresarial, cb_consultoria_tributaria, cb_camara_arbitragem):
        current_height = frame.winfo_height()
        print(f"Current frame height: {current_height}")
        if frame.winfo_height() == current_height:
            #print(f"Expandindo ! {usuario['cpf']}")
            frame.configure(height=285)
            botao_alterar.pack_forget()

            cb_consultoria_empresarial.place(x=42, y=100)
            cb_consultoria_tributaria.place(x=42, y=150)
            cb_camara_arbitragem.place(x=42, y=200)

            botao_submeter.pack(side=customtkinter.RIGHT, anchor=customtkinter.SE,padx=(0, 20), pady = (0,20))
            botao_cancelar.pack(side=customtkinter.RIGHT, anchor=customtkinter.SE, padx=(0, 20), pady=(0, 20))
        else:
           #print(f"Fechando !{usuario['nome']}")
            frame.configure(height=current_height-80)
            botao_cancelar.pack_forget()
            botao_submeter.pack_forget()

            self.cb_consultoria_empresarial.pack_forget()
            self.cb_consultoria_tributaria.pack_forget()
            self.cb_camara_arbitragem.pack_forget()

            botao_alterar.pack(side=customtkinter.RIGHT, anchor=customtkinter.NE, padx=(0, 20), pady=(30, 0))

    def pesquisar_usuarios(self, event):

        termo_busca = self.caixa_busca.get().lower()

        for frame in self.frame_usuarios:

            nome_usuario = frame.winfo_children()[1].cget("text").lower()  # recebe o nome dos usuarios
            if termo_busca in nome_usuario:
                frame.pack(pady=(10, 0))
            else:
                frame.pack_forget()

        if not termo_busca:
            for i, frame in enumerate(self.frame_usuarios):
                frame.pack(pady=(10, 0))

    def voltar_funcao(self):
        pass

if __name__ == "__main__":
    app = alterarAcesso()