from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import ctypes
from functools import partial
from json import loads, dumps
from tkinter import ttk
import customtkinter
from src.utilitarios.visualizadorPDF import PDFReader
from src.classes.contrato.ContractControler import convertPDF
import sys

class telaEdicaoContrato:
    def __init__(self):
        ctypes.windll.shcore.SetProcessDpiAwareness(True)

        # Setup
        self.root = Tk()
        self.root.geometry('800x600')

        # Used to make title of the application
        applicationName = 'Edição de Contrato'
        self.root.title(applicationName)

        # Current File Path
        self.filePath = None

        # initial directory to be the current directory
        self.initialdir = '.'

        # Define File Types that can be choosen
        self.validFileTypes = (
            ("Rich Text File","*.rte"),
            ("all files","*.*")
        )

        # Setting the font and Padding for the Text Area
        fontName = 'Consolas'
        fontSize = 12
        padding = 20

        # Infos about the Document are stored here
        document = None

        # Default content of the File
        self.defaultContent = {
            "content": "",
            "tags": {
                'bold': [(), ()]
            },
        }

        # Add Different Types of Tags that can be added to the document.
        self.tagTypes = {
            # Font Settings
            'Bold': {'font': f'{fontName} {fontSize} bold'},
            'Italic': {'font': f'{fontName} {fontSize} italic'},
            'Code': {'font': f'Consolas {fontSize}', 'background': self.rgbToHex((200, 200, 200))},

            # Sizes
            'Normal Size': {'font': f'{fontName} {fontSize}'},
            'Larger Size': {'font': f'{fontName} {fontSize + 5}'},
            'Largest Size': {'font': f'{fontName} {fontSize + 10}'},

            # Background Colors
            'Highlight': {'background': self.rgbToHex((255, 255, 0))},
            'Highlight Red': {'background': self.rgbToHex((255, 0, 0))},
            'Highlight Green': {'background': self.rgbToHex((0, 255, 0))},
            'Highlight Black': {'background': self.rgbToHex((0, 0, 0))},

            # Foreground / Text Colors
            'Text White': {'foreground': self.rgbToHex((255, 255, 255))},
            'Text Grey': {'foreground': self.rgbToHex((200, 200, 200))},
            'Text Blue': {'foreground': self.rgbToHex((0, 0, 255))},
            'Text Green': {'foreground': self.rgbToHex((0, 255, 0))},
            'Text Red': {'foreground': self.rgbToHex((255, 0, 0))},
        }


        # Frame para os botões à direita com scrollbar
        widithBotoes = 600

        self.frame_botoes_canvas = Canvas(self.root, bg="#6EC1E4", width=widithBotoes)

        self.scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.frame_botoes_canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.frame_botoes_canvas.pack(side=RIGHT, fill=Y , padx=(10,0))



        self.frame_botoes_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.frame_botoes_canvas.bind('<Configure>', lambda e: self.frame_botoes_canvas.configure(scrollregion=self.frame_botoes_canvas.bbox('all')))
        self.frame_botoes_canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

        self.frame_botoes = Frame(self.frame_botoes_canvas, bg="#6EC1E4", highlightbackground="#00343D", highlightthickness=2)
        self.frame_botoes_canvas.create_window((0, 0), window=self.frame_botoes, anchor='nw',width=widithBotoes)


        # Estilo dos botões
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#00343D", foreground="white")
        self.style.map("TButton", background=[('active', '#002831')])

        # Função para criar botões arredondados



        # Format Menu Label
        self.label_format = Label(self.frame_botoes, text="Formatar", bg="#6EC1E4", fg="white", font=(fontName, 20, 'bold'))
        self.label_format.grid(row = 0,column=0,columnspan=2,padx=5,pady=(25,10))

        # Format Menu Buttons
        nrow = 1
        i = 2

        self.tagTranslate = {
            # Configurações de Fonte
            'Bold': 'Negrito',
            'Italic': 'Itálico',
            'Code': 'Código',

            # Tamanhos
            'Normal Size': 'Tamanho Normal',
            'Larger Size': 'Subtítulo',
            'Largest Size': 'Título',

            # Cores de Fundo
            'Highlight': 'Destaque',
            'Highlight Red': 'Destaque Vermelho',
            'Highlight Green': 'Destaque Verde',
            'Highlight Black': 'Destaque Preto',

            # Cores de Texto
            'Text White': 'Texto Branco',
            'Text Grey': 'Texto Cinza',
            'Text Blue': 'Texto Azul',
            'Text Green': 'Texto Verde',
            'Text Red': 'Texto Vermelho',
        }

        self.translateInsertInformation = {
            "Nome": "$$nome$$",
            "Sobrenome": "$$sobrenome$$",
            "CPF": "$$cpf$$",
            "Empresa": "$$empresa$$",
            "Cargo": "$$cargo$$",
            "E-mail": "$$email$$",
            "Telefone": "$$telefone$$",
            "País/Localização": "$$país/localização$$",
            "Nome da empresa": "$$nomedaempresa$$",
            "CNPJ": "$$cnpj$$",
            "CNAE principal": "$$cnaeprincipal$$",
            "CNAE secundário": "$$cnaesecundário$$",
            "CFOP principais produtos": "$$cfopprincipaisprodutos$$",
            "Indústria/Setor": "$$indústria/setor$$",
            "Receita anual": "$$receitaanual$$",
            "Valor": "$$valor$$",
            "Forma de Pagamento": "$$formadepagamento$$",
            "Multa de Mora": "$$multademora$$",
            "Juros de Mora": "$$jurosdemora$$",
            "Correção Monetária": "$$correçãomonetária$$",
            "Prazo de duração": "$$prazodeduração$$",
            "Nome Completocontratante": "$$nomecompletocontratante$$",
            "Nacionalidadecontratante": "$$nacionalidadecontratante$$",
            "Estado Civilcontratante": "$$estadocivilcontratante$$",
            "Profissãocontratante": "$$profissãocontratante$$",
            "CPF ou CNPJcontratante": "$$cpfoucnpjcontratante$$",
            "Endereço Residêncial/Comercialcontratante": "$$endereçoresidêncial/comercialcontratante$$",
            "Nome Completocontratado": "$$nomecompletocontratado$$",
            "Nacionalidadecontratado": "$$nacionalidadecontratado$$",
            "Estado Civilcontratado": "$$estadocivilcontratado$$",
            "Profissãocontratado": "$$profissãocontratado$$",
            "CPF ou CNPJcontratado": "$$cpfoucnpjcontratado$$",
            "Endereço Residêncial/Comercialcontratado": "$$endereçoresidêncial/comercialcontratado$$",
        }

        for tagType in self.tagTypes:
            btn_tag = self.create_rounded_button(self.tagTranslate[tagType], partial(self.tagToggle, tagName=tagType.lower()),"#00343D","#002F37",200)
            btn_tag.grid(row = int(i/2),column = i%2,pady=5, padx=5)
            i += 1

        nrow = int(i/2) + 1

        self.label_format = Label(self.frame_botoes, text="Informações Profissionais", bg="#6EC1E4", fg="white", font=(fontName, 20, 'bold'))
        self.label_format.grid(row = nrow, column=0, columnspan=2, padx=5, pady=(25,10))
        nrow += 1

        # Adding Professional Information Buttons
        info_buttons = [
            "Nome", "Sobrenome", "CPF", "Empresa", "Cargo", "E-mail", "Telefone", "País/Localização"
        ]

        for i, info in enumerate(info_buttons):
            btn_info = self.create_rounded_button(info, partial(self.add_custom_info,self.translateInsertInformation[info]), "#00343D", "#002F37", 200)
            btn_info.grid(row = nrow + int(i/2), column = i%2, pady=5, padx=5)

        nrow += len(info_buttons)//2 + 1

        self.label_format = Label(self.frame_botoes, text="Informações Empresariais", bg="#6EC1E4", fg="white", font=(fontName, 20, 'bold'))
        self.label_format.grid(row = nrow, column=0, columnspan=2, padx=5, pady=(25,10))
        nrow += 1

        # Adding Business Information Buttons
        business_info_buttons = [
            "Nome da empresa", "CNPJ", "CNAE principal", "CNAE secundário", "CFOP principais produtos",
            "Indústria/Setor", "Receita anual"
        ]

        for i, info in enumerate(business_info_buttons):
            btn_info = self.create_rounded_button(info, partial(self.add_custom_info,self.translateInsertInformation[info]), "#00343D", "#002F37", 200)
            btn_info.grid(row = nrow + int(i/2), column = i%2, pady=5, padx=5)

        nrow += len(business_info_buttons)//2 + 1

        self.label_format = Label(self.frame_botoes, text="Informações do Negócio", bg="#6EC1E4", fg="white", font=(fontName, 20, 'bold'))
        self.label_format.grid(row = nrow, column=0, columnspan=2, padx=5, pady=(25,10))
        nrow += 1

        # Adding Business Details Buttons
        business_details_buttons = [
            "Valor", "Forma de Pagamento", "Multa de Mora", "Juros de Mora", "Correção Monetária", "Prazo de duração"
        ]

        for i, detail in enumerate(business_details_buttons):
            btn_detail = self.create_rounded_button(detail, partial(self.add_custom_info,self.translateInsertInformation[detail]), "#00343D", "#002F37", 200)
            btn_detail.grid(row = nrow + int(i/2), column = i%2, pady=5, padx=5)

        nrow += len(business_details_buttons)//2 + 1

        self.label_format = Label(self.frame_botoes, text="Informações do Contratante", bg="#6EC1E4", fg="white", font=(fontName, 20, 'bold'))
        self.label_format.grid(row = nrow, column=0, columnspan=2, padx=5, pady=(25,10))
        nrow += 1

        business_part_information = [
            "Nome Completo", "Nacionalidade", "Estado Civil", "Profissão", "CPF ou CNPJ", "Endereço Residêncial/Comercial"
        ]

        for i, part in enumerate(business_part_information):
            self.btn_part = self.create_rounded_button(part, partial(self.add_custom_info,self.translateInsertInformation[part+'contratante']), "#00343D", "#002F37", 200)
            self.btn_part.grid(row = nrow + int(i/2), column = i%2, pady=5, padx=5)

        nrow += len(business_part_information)//2 + 1

        self.label_format = Label(self.frame_botoes, text="Informações do Contratado", bg="#6EC1E4", fg="white", font=(fontName, 20, 'bold'))
        self.label_format.grid(row = nrow, column=0, columnspan=2, padx=5, pady=(25,10))
        nrow += 1


        for i, part in enumerate(business_part_information):
            btn_part = self.create_rounded_button(part, partial(self.add_custom_info,self.translateInsertInformation[part+'contratado']), "#00343D", "#002F37", 200)
            btn_part.grid(row = nrow + int(i/2), column = i%2, pady=5, padx=5)

        nrow += len(business_part_information)//2 + 1

        self.label_format = Label(self.frame_botoes, text="Informações Personalizadas", bg="#6EC1E4", fg="white", font=(fontName, 20, 'bold'))
        self.label_format.grid(row = nrow, column=0, columnspan=2, padx=5, pady=(25,10))
        nrow += 1

        self.entryInfoPersonalizada = customtkinter.CTkEntry(self.frame_botoes,placeholder_text="Digite a informação que deseja adicionar...",width=400,height=35,font=('Calibri',15,'normal'),fg_color="white",text_color="black",placeholder_text_color="black",border_color="#00343D")
        self.entryInfoPersonalizada.grid(row = nrow, column = 0, columnspan = 2,padx = 5,pady = 10)
        nrow +=1

        self.btn_adicionar = self.create_rounded_button("Adicionar", partial(self.add_custom_info,"customItem"),fg_color="#00343D",hover_color="#002F37",width=300)
        self.btn_adicionar.grid(row = nrow,column = 0,columnspan = 2,pady=(10,40), padx=5)
        nrow += 1


        self.btn_save = customtkinter.CTkButton(self.frame_botoes, text="Salvar", command=partial(self.fileManager,None,'save'), fg_color="#58ABB3", hover_color="#367076", width=400,height=50, font=('Calibri', 25, 'bold'))
        self.btn_save.grid(row = nrow,column = 0,columnspan = 2,pady=10, padx=5)
        nrow += 1

        self.btn_preview =  customtkinter.CTkButton(self.frame_botoes, text="Pré-Visualizar", command=self.preview, fg_color="#58ABB3", hover_color="#367076", width=400,height=50, font=('Calibri', 25, 'bold'))
        self.btn_preview.grid(row = nrow,column = 0,columnspan = 2,pady=10, padx=5)
        nrow += 1

        label_format = Label(self.frame_botoes, text="                                ", bg="#6EC1E4", font=(fontName, 20, 'bold'), fg="white")
        label_format.grid(row = nrow,column=0,columnspan=2,padx=5)
        nrow += 1

        # Frame para o editor de texto à esquerda
        self.frame_texto = Frame(self.root, width=600)
        self.frame_texto.pack(side=LEFT, fill=BOTH, expand=True)

        self.textArea = Text(self.frame_texto, font=f'Consolas {fontSize}', relief=FLAT, wrap=WORD, padx=padding, pady=padding, bd=0, undo=True)  # Enable undo
        self.textArea.pack(fill=BOTH, expand=TRUE)

        # Bind Ctrl+Z to undo
        self.textArea.bind("<Control-z>", lambda event: self.textArea.edit_undo())

        self.textArea.bind("<Key>", self.keyDown)

        self.resetTags()

        self.root.mainloop()


    def resetTags(self):
        for tag in self.textArea.tag_names():
            self.textArea.tag_remove(tag, "1.0", "end")

        for tagType in self.tagTypes:
            self.textArea.tag_configure(tagType.lower(), self.tagTypes[tagType])

    def on_mouse_wheel(self,event):
        self.frame_botoes_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def rgbToHex(self,rgb):
        return "#%02x%02x%02x" % rgb  

    def fileManager(self,event=None, action=None):
        global document, filePath

        # Open
        if action == 'open':
            # ask the user for a filename with the native file explorer.
            filePath = askopenfilename(filetypes=self.validFileTypes, initialdir=self.initialdir)


            with open(filePath, 'r') as f:
                document = loads(f.read())

            # Delete Content
            self.textArea.delete('1.0', END)
            
            # Set Content
            self.textArea.insert('1.0', document['content'])

            # Set Title
            self.root.title(f'{self.applicationName} - {filePath}')

            # Reset all tags
            self.resetTags()

            # Add To the Document
            for tagName in document['tags']:
                for tagStart, tagEnd in document['tags'][tagName]:
                    self.textArea.tag_add(tagName, tagStart, tagEnd)
                    print(tagName, tagStart, tagEnd)

        elif action == 'save':
            document = self.defaultContent
            document['content'] = self.textArea.get('1.0', END)

            for tagName in self.textArea.tag_names():
                if tagName == 'sel': continue

                document['tags'][tagName] = []

                ranges = self.textArea.tag_ranges(tagName)

                for i, tagRange in enumerate(ranges[::2]):
                    document['tags'][tagName].append([str(tagRange), str(ranges[i+1])])

            return dumps(document)
        
    def keyDown(self,event=None):
        self.root.title(f'{self.applicationName} - *{filePath}')


    def tagToggle(self,tagName):
        start, end = "sel.first", "sel.last"

        if tagName in self.textArea.tag_names('sel.first'):
            self.textArea.tag_remove(tagName, start, end)
        else:
            self.textArea.tag_add(tagName, start, end)


    def add_custom_info(self,info):
        if info == "customItem":
            info = f"$${self.entryInfoPersonalizada.get()}$$"
        self.textArea.insert(END, info)


    def preview(self):
        if self.textArea.winfo_ismapped():
            self.textArea.pack_forget()
            # Caminho para os arquivos PDF
            papel_timbrado = './pdfs/papelTimbrado.pdf'
            pdf_com_texto = './pdfs/texto.pdf'
            pdf_saida = './pdfs/pdf_final.pdf'
            json_input = self.fileManager(None,"save")
            # Instanciar e executar a classe
            converter = convertPDF(json_input, papel_timbrado, pdf_com_texto, pdf_saida)
            converter.run()
            PDFReader(self.frame_texto,self.textArea,pdf_saida)


    def create_rounded_button(self,text, command, fg_color, hover_color, width):
        return customtkinter.CTkButton(self.frame_botoes, text=text, command=command, fg_color=fg_color, hover_color=hover_color, width=width, font=('Calibri', 15, 'bold'))
    



