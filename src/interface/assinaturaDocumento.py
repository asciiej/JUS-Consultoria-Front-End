from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import ctypes
from functools import partial
from json import loads, dumps
from tkinter import ttk
import customtkinter
from src.utilitarios.visualizadorPDF import PDFReader
from src.utilitarios.operacoesDocumento import convertPDF

class telaAssinaturaDocumento:
    def __init__(self,root,json_input,substitutions : dict):
        #self.contractControler = contractControler
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
        pdf_saida = './pdfs/pdf_final.pdf'
        papel_timbrado = './pdfs/papelTimbrado.pdf'
        pdf_com_texto = './pdfs/output.pdf'
        try:
            convertPDF(json_input, papel_timbrado, pdf_com_texto, pdf_saida,substitutions).run()
        except Exception as e:
            print("Excessão na abertura do arquivo: ",e)

        fontName = 'Consolas'
        fontSize = 12
        padding = 20

        # Setup
        self.root = root

        # Used to make title of the application
        self.applicationName = 'Assinatura documento'
        self.root.title(self.applicationName)


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
        nrow = 0

        while nrow < 4:
            self.framePreenchimento = customtkinter.CTkFrame(self.frame_botoes,fg_color="#6EC1E4",border_width = 0)
            self.framePreenchimento.grid(row = nrow,column = 0,columnspan = 2,pady=3, padx=5)
            nrow +=1

        self.btn_save = customtkinter.CTkButton(self.frame_botoes, text="Alterar seus dados", command=None, fg_color="#58ABB3", hover_color="#367076", width=400,height=50, font=('Calibri', 25, 'bold'))
        self.btn_save.grid(row = nrow,column = 0,columnspan = 2,pady=10, padx=5)
        nrow += 1

        self.btn_preview =  customtkinter.CTkButton(self.frame_botoes, text="Assinar", command=None, fg_color="#58ABB3", hover_color="#367076", width=400,height=50, font=('Calibri', 25, 'bold'))
        self.btn_preview.grid(row = nrow,column = 0,columnspan = 2,pady=10, padx=5)
        nrow += 1

        label_format = Label(self.frame_botoes, text="                                ", bg="#6EC1E4", font=(fontName, 20, 'bold'), fg="white")
        label_format.grid(row = nrow,column=0,columnspan=2,padx=5)
        nrow += 1

        # Frame para o editor de texto à esquerda
        self.frame_texto = Frame(self.root, width=600)
        self.frame_texto.pack(side=LEFT, fill=BOTH, expand=True)

        self.textArea = Text(self.frame_texto, font=f'Consolas {fontSize}', relief=FLAT, wrap=WORD, padx=padding, pady=padding, bd=0, undo=True)  # Enable undo
        # self.textArea.pack(fill=BOTH, expand=TRUE)

        # Bind Ctrl+Z to undo
        # self.textArea.bind("<Control-z>", lambda event: self.textArea.edit_undo())
        
        pdf_saida = './pdfs/pdf_final.pdf'
        PDFReader(self.frame_texto,None,pdf_saida)



        self.root.mainloop()


    def on_mouse_wheel(self,event):
        self.frame_botoes_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
