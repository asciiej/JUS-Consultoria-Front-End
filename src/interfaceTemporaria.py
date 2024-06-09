import tkinter as tk
from tkinter import ttk, filedialog

class ContractApp:
    def __init__(self, root, controlers):
        self.root = root
        self.root.title("Contract Management")
        self.controlers = controlers

        # Notebook widget for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True)

        self.create_arbitragem_tab()
        self.create_tributaria_tab()
        self.create_empresarial_combined_tab()

    def create_arbitragem_tab(self):
        self.arbitragem_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.arbitragem_frame, text="Arbitragem Contract")

        self.create_entry(self.arbitragem_frame, "Contract Type")
        self.create_entry(self.arbitragem_frame, "Nome Empresa")
        self.create_entry(self.arbitragem_frame, "CNPJ")
        self.create_entry(self.arbitragem_frame, "CNAE Principal")
        self.create_entry(self.arbitragem_frame, "CNAE Secundario")
        self.create_entry(self.arbitragem_frame, "CFOP Principais")
        self.create_entry(self.arbitragem_frame, "Industria Setor")
        self.create_entry(self.arbitragem_frame, "Receita Anual")

        self.create_button(self.arbitragem_frame, "Create Arbitragem Contract", self.create_contract, 'arbitragem').pack(pady=10)

    def create_tributaria_tab(self):
        self.tributaria_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.tributaria_frame, text="Tributaria Contract")

        self.create_entry(self.tributaria_frame, "Contract Type")
        self.create_entry(self.tributaria_frame, "Nome Empresa")
        self.create_entry(self.tributaria_frame, "CNPJ")
        self.create_entry(self.tributaria_frame, "CNAE Principal")
        self.create_entry(self.tributaria_frame, "CNAE Secundario")
        self.create_entry(self.tributaria_frame, "CFOP Principais")
        self.create_entry(self.tributaria_frame, "Industria Setor")
        self.create_entry(self.tributaria_frame, "Receita Anual")

        self.create_button(self.tributaria_frame, "Create Tributaria Contract", self.create_contract, 'tributaria').pack(pady=10)

    def create_empresarial_combined_tab(self):
        self.empresarial_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.empresarial_frame, text="Empresarial Contract")

        self.create_empresarial_contratante_section()
        self.create_empresarial_contratado_section()
        self.create_empresarial_remuneracao_section()

    def create_empresarial_contratante_section(self):
        self.contratante_frame = ttk.LabelFrame(self.empresarial_frame, text="Contratante")
        self.contratante_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.create_entry(self.contratante_frame, "Qualificacao")
        self.create_entry(self.contratante_frame, "Nome Completo")
        self.create_entry(self.contratante_frame, "Nacionalidade")
        self.create_entry(self.contratante_frame, "Estado Civil")
        self.create_entry(self.contratante_frame, "Profissao")
        self.create_entry(self.contratante_frame, "CPF_CNPJ")

    def create_empresarial_contratado_section(self):
        self.contratado_frame = ttk.LabelFrame(self.empresarial_frame, text="Contratado")
        self.contratado_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.create_entry(self.contratado_frame, "Qualificacao")
        self.create_entry(self.contratado_frame, "Nome Completo")
        self.create_entry(self.contratado_frame, "Nacionalidade")
        self.create_entry(self.contratado_frame, "Estado Civil")
        self.create_entry(self.contratado_frame, "Profissao")
        self.create_entry(self.contratado_frame, "CPF_CNPJ")
        self.create_entry(self.contratado_frame, "Objeto Contrato")

    def create_empresarial_remuneracao_section(self):
        self.remuneracao_frame = ttk.LabelFrame(self.empresarial_frame, text="Remuneração")
        self.remuneracao_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.create_grid_entry(self.remuneracao_frame, "Contract Type", 0, 0)
        self.create_grid_entry(self.remuneracao_frame, "Valor", 0, 0)
        self.create_grid_entry(self.remuneracao_frame, "Forma Pagamento", 0, 1)
        self.create_grid_entry(self.remuneracao_frame, "Multa Mora", 1, 0)
        self.create_grid_entry(self.remuneracao_frame, "Juros Mora", 1, 1)
        self.create_grid_entry(self.remuneracao_frame, "Correcao Monetaria", 2, 0)
        self.create_grid_entry(self.remuneracao_frame, "Prazo Duracao", 2, 1)

        self.create_button(self.remuneracao_frame, "Create Empresarial Remuneracao", self.create_contract, 'empresarial').grid(row=3, columnspan=2, pady=10)
        self.create_button(self.remuneracao_frame, "GET Empresarial Remuneracao", self.get_contract_by_id, 'empresarial', 2).grid(row=3, columnspan=3, pady=10)

    def create_entry(self, parent, text):
        label = ttk.Label(parent, text=text)
        label.pack()
        entry = ttk.Entry(parent)
        entry.pack()
        setattr(self, text.replace(" ", "_").lower(), entry)

    def create_grid_entry(self, parent, text, row, column):
        label = ttk.Label(parent, text=text)
        label.grid(row=row, column=column * 2, padx=5, pady=5, sticky="e")
        entry = ttk.Entry(parent)
        entry.grid(row=row, column=column * 2 + 1, padx=5, pady=5, sticky="w")
        setattr(self, text.replace(" ", "_").lower(), entry)

    def create_button(self, parent, text, command, *args):
        button = ttk.Button(parent, text=text, command=lambda: command(*args))
        return button

    def create_contract(self, button_type):
        if button_type == 'arbitragem':
            contract_data = {attr: getattr(self, attr).get() for attr in ["contract_type", "nome_empresa", "cnpj", "cnae_principal", "cnae_secundario", "cfop_principais", "industria_setor", "receita_anual"]}
            self.controlers['contract'].arbitragem(contract_data).create()

        elif button_type == 'tributaria':
            contract_data = {attr: getattr(self, attr).get() for attr in ["contract_type", "nome_empresa", "cnpj", "cnae_principal", "cnae_secundario", "cfop_principais", "industria_setor", "receita_anual"]}
            self.controlers['contract'].tributaria(contract_data).create()

        elif button_type == 'empresarial':
            contract_data = {attr: getattr(self, attr).get() for attr in ["contract_type", "valor", "forma_pagamento", "multa_mora", "juros_mora", "correcao_monetaria", "prazo_duracao"]}
            contract_data["contratante"] = {attr: getattr(self, attr).get() for attr in ["qualificacao", "nome_completo", "nacionalidade", "estado_civil", "profissao", "cpf_cnpj"]}
            contract_data["contratado"] = {attr: getattr(self, attr).get() for attr in ["qualificacao", "nome_completo", "nacionalidade", "estado_civil", "profissao", "cpf_cnpj", "objeto_contrato"]}
            self.controlers['contract'].empresarial(contract_data).create()

    def get_contract_by_id(self ,contract_type, contract_id):
        retorno = getattr(self.controlers['contract'], contract_type)().get_by_id(contract_id)
        print(retorno)

def interface(controlers):
    root = tk.Tk()
    app = ContractApp(root, controlers)
    root.mainloop()
