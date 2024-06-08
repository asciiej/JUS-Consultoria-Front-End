import json
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from PyPDF2 import PdfReader, PdfWriter, PageObject
from itertools import islice

def split_string(input_string, chunk_size=65520):
    """
    Divide a string em tuplas de tamanho especificado.

    Args:
    input_string (str): A string a ser dividida.
    chunk_size (int): O tamanho máximo de cada pedaço da string.

    Returns:
    list: Uma lista de tuplas (índice, pedaço da string).
    """
    chunks = []
    for i in range(0, len(input_string), chunk_size):
        chunks.append((i // chunk_size, input_string[i:i + chunk_size]))
    return chunks

def recombine_string(tuples_list):
    """
    Recompoe a string original a partir das tuplas.

    Args:
    tuples_list (list): Lista de tuplas (índice, pedaço da string).

    Returns:
    str: A string recomposta.
    """
    tuples_list.sort()  # Ordena as tuplas pela ordem dos índices
    return ''.join(chunk for _, chunk in tuples_list)



class convertPDF:
    def __init__(self, json_input, papel_timbrado, pdf_com_texto, pdf_saida):
        self.json_input = re.sub(r'[\x00-\x1f\x7f-\x9f]', r"\\n", json_input)
        self.papel_timbrado = papel_timbrado
        self.pdf_com_texto = pdf_com_texto
        self.pdf_saida = pdf_saida
        self.custom_styles = {
            "bold": 'b',
            "italic": 'i',
            "code": 'font face="Courier"',
            "normal size": 'font size="12"',
            "larger size": 'font size="16"',
            "largest size": 'font size="20"',
            "highlight": 'font backColor="yellow"',
            "highlight red": 'font backColor="red"',
            "highlight green": 'font backColor="green"',
            "highlight black": 'font backColor="black"',
            "text white": 'font color="white"',
            "text grey": 'font color="grey"',
            "text blue": 'font color="blue"',
            "text green": 'font color="green"',
            "text red": 'font color="red"'
        }

    def nth_index(self, iterable, value, n):
        if n == 0:
            return 0
        matches = (idx for idx, val in enumerate(iterable) if val == value)
        return next(islice(matches, n-1, n), None)

    def remover_tuplas_vazias(self, lista_tuplas):
        return [tupla for tupla in lista_tuplas if tupla[0] != '']

    def ordenar_tuplas(self, lista_tuplas):
        return sorted(lista_tuplas, key=lambda tupla: (tupla[1], tupla[2]))

    def apply_styles(self, content, styled_text):
        styled_content = content
        offset = 0
        lastStart = 0
        lastEnd = 0
        for styled_item in styled_text:
            text, start, end, style = styled_item
            if lastStart == start:
                styled_start = start
                styled_end = end + offset
            else:
                styled_start = start + offset
                styled_end = end + offset
            lastStart = styled_start
            lastEnd = end
            style = self.custom_styles.get(style)
            styled_content = styled_content[:styled_start] + f"<{style}>" + styled_content[styled_start:]
            offset += len(f"<{style}>")
            styled_content = styled_content[:styled_end + len(f"<{style}>")] + f"</{style}>" + styled_content[styled_end + len(f"<{style}>"):]
            offset += len(f"</{style}>")
        return styled_content

    def parse_json(self):
        data = json.loads(self.json_input)
        return data

    def create_pdf(self, data):
        doc = SimpleDocTemplate(self.pdf_com_texto, pagesize=A4)
        styles = getSampleStyleSheet()
        content = data['content']
        tags = data['tags']
        elements = []

        formatted_text = []

        for tagName in tags:
            for tagStart, tagEnd in tags[tagName]:
                lineStart = int(float(tagStart)) - 1
                wordStart = int(tagStart[tagStart.index('.')+1:])
                lineEnd = int(float(tagEnd)) - 1
                wordEnd = int(tagEnd[tagEnd.index('.')+1:])
                start = self.nth_index(content, '\n', lineStart) + wordStart
                end = self.nth_index(content, '\n', lineEnd) + wordEnd
                if content[end] != '\n':
                    end += 1
                if content[start] == '\n':
                    start += 1
                formatted_text.append((content[start:end], start, end, tagName))

        formatted_text = self.remover_tuplas_vazias(formatted_text)
        formatted_text = self.ordenar_tuplas(formatted_text)
        content = self.apply_styles(content, formatted_text)

        notLineCounter = 0
        for line in content[0:].split('\n'):
            if not line and notLineCounter == 0:
                notLineCounter += 1
                continue
            p = Paragraph(line, styles['Normal'])
            elements.append(p)
            elements.append(Spacer(1, 12))
            notLineCounter = 0

        doc.build(elements)

    def mesclar_pdfs(self):
        leitor_timbrado = PdfReader(self.papel_timbrado)
        leitor_texto = PdfReader(self.pdf_com_texto)
        escritor = PdfWriter()

        pagina_timbrado = leitor_timbrado.pages[0]

        for i in range(len(leitor_texto.pages)):
            pagina_texto = leitor_texto.pages[i]
            pagina_timbrado_copia = PageObject.create_blank_page(width=pagina_timbrado.mediabox.width,
                                                                 height=pagina_timbrado.mediabox.height)
            pagina_timbrado_copia.merge_page(pagina_timbrado)
            pagina_timbrado_copia.merge_page(pagina_texto)
            escritor.add_page(pagina_timbrado_copia)

        with open(self.pdf_saida, "wb") as arquivo_saida:
            escritor.write(arquivo_saida)

    def run(self):
        data = self.parse_json()
        self.create_pdf(data)
        self.mesclar_pdfs()


if __name__ == '__main__':
    # Exemplo de uso:
    json_input = r'''{"content": "\nCONTRATO DE ARRENDAMENTO RURAL\n\nPARTES\n\n\n\nARRENDADOR: Jo\u00e3o Silva, brasileiro, casado, agricultor, portador da c\u00e9dula de identidade RG n\u00ba 12345678 SSP/SP e inscrito no CPF/MF sob n\u00ba 123.456.789-00, residente e domiciliado na Rua das Flores, n\u00ba 100, Bairro Jardim, Cidade de S\u00e3o Paulo, Estado de S\u00e3o Paulo, CEP 01000-000.\nASDFASDFASDF\n\nARRENDAT\u00c1RIO: Maria Oliveira, brasileira, solteira, agricultora, portadora da c\u00e9dula de identidade RG n\u00ba 87654321 SSP/SP e inscrita no CPF/MF sob n\u00ba 987.654.321-00, residente e domiciliada na Rua das Palmeiras, n\u00ba 200, Bairro Centro, Cidade de Campinas, Estado de S\u00e3o Paulo, CEP 13000-000.\n\nCL\u00c1USULA 1 - DO OBJETO\n\nO presente contrato tem como objeto o arrendamento do im\u00f3vel rural denominado \"Fazenda Esperan\u00e7a\", situado na Estrada Rural, km 12, Zona Rural, Munic\u00edpio de Itapetininga, Estado de S\u00e3o Paulo, com \u00e1rea total de 50 hectares, registrado no Cart\u00f3rio de Registro de Im\u00f3veis sob matr\u00edcula n\u00ba 12345.\n\nCL\u00c1USULA 2 - DO PRAZO\n\nO prazo do presente contrato \u00e9 de 5 (cinco) anos, iniciando-se em 01 de julho de 2024 e terminando em 30 de junho de 2029, podendo ser prorrogado por igual per\u00edodo mediante acordo entre as partes.\n\nCL\u00c1USULA 3 - DO VALOR E FORMA DE PAGAMENTO\n\nO valor do arrendamento \u00e9 de R$ 50.000,00 (cinquenta mil reais) anuais, a serem pagos em duas parcelas semestrais de R$ 25.000,00 (vinte e cinco mil reais) cada, vencendo-se a primeira em 01 de janeiro e a segunda em 01 de julho de cada ano.\n\nCL\u00c1USULA 4 - DAS OBRIGA\u00c7\u00d5ES DO ARRENDADOR\n\n4.1. Entregar o im\u00f3vel arrendado em perfeitas condi\u00e7\u00f5es de uso e conserva\u00e7\u00e3o, com todas as benfeitorias necess\u00e1rias ao bom desenvolvimento da atividade agr\u00edcola.\n\n4.2. Garantir ao arrendat\u00e1rio o uso pac\u00edfico do im\u00f3vel durante todo o prazo de vig\u00eancia do contrato.\n\nCL\u00c1USULA 5 - DAS OBRIGA\u00c7\u00d5ES DO ARRENDAT\u00c1RIO\n\n5.1. Utilizar o im\u00f3vel arrendado exclusivamente para atividades agr\u00edcolas, preservando-o e mantendo-o em boas condi\u00e7\u00f5es de uso e conserva\u00e7\u00e3o.\n\n5.2. Pagar pontualmente os valores ajustados na Cl\u00e1usula 3.\n\n5.3. N\u00e3o subarrendar, ceder ou transferir, total ou parcialmente, o im\u00f3vel objeto deste contrato sem a expressa autoriza\u00e7\u00e3o do arrendador.\n\n5.4. Devolver o im\u00f3vel ao t\u00e9rmino do contrato nas mesmas condi\u00e7\u00f5es em que o recebeu, salvo as deteriora\u00e7\u00f5es naturais decorrentes do uso normal.\n\nCL\u00c1USULA 6 - DA RESCIS\u00c3O\n\nO presente contrato poder\u00e1 ser rescindido de pleno direito nas seguintes hip\u00f3teses:\n\n6.1. Inadimplemento de qualquer das cl\u00e1usulas pactuadas.\n\n6.2. Pr\u00e1tica de atos pelo arrendat\u00e1rio que configurem utiliza\u00e7\u00e3o inadequada do im\u00f3vel ou preju\u00edzo \u00e0 sua conserva\u00e7\u00e3o.\n\n6.3. Desinteresse manifestado por qualquer das partes, mediante notifica\u00e7\u00e3o pr\u00e9via por escrito com anteced\u00eancia m\u00ednima de 6 (seis) meses.\n\nCL\u00c1USULA 7 - DAS PENALIDADES\n\nEm caso de rescis\u00e3o antecipada por culpa do arrendat\u00e1rio, este pagar\u00e1 ao arrendador uma multa correspondente a 20% (vinte por cento) do valor anual do arrendamento.\n\nCL\u00c1USULA 8 - DAS DISPOSI\u00c7\u00d5ES GERAIS\n\n8.1. Este contrato obriga n\u00e3o s\u00f3 as partes contratantes, mas tamb\u00e9m seus herdeiros e sucessores.\n\n8.2. Qualquer altera\u00e7\u00e3o no presente contrato somente ter\u00e1 validade se formalizada por escrito e assinada por ambas as partes.\n\n8.3. Fica eleito o foro da Comarca de Itapetininga, Estado de S\u00e3o Paulo, para dirimir quaisquer quest\u00f5es oriundas deste contrato, com ren\u00fancia de qualquer outro, por mais privilegiado que seja.\n\nE, por estarem assim justos e contratados, assinam o presente instrumento em 2 (duas) vias de igual teor e forma, juntamente com duas testemunhas.\n\nItapetininga, 01 de julho de 2024.\n\n___________________________________\nJo\u00e3o Silva\nARRENDADOR\n\n___________________________________\nMaria Oliveira\nARRENDAT\u00c1RIO\n\n___________________________________\nTestemunha 1\n\n___________________________________\nTestemunha 2\n\n\n\n", "tags": {"bold": [["57.10", "57.95"]], "italic": [["13.0", "13.22"]], "code": [["8.0", "8.10"]], "normal size": [], "larger size": [["2.0", "2.30"]], "largest size": [], "highlight": [["63.20", "63.41"]], "highlight red": [], "highlight green": [], "highlight black": [], "text white": [], "text grey": [["23.0", "23.240"]], "text blue": [], "text green": [], "text red": [["23.106", "23.158"], ["61.52", "61.52"]]}}'''

    # Caminho para os arquivos PDF
    papel_timbrado = './pdfs/papelTimbrado.pdf'
    pdf_com_texto = './pdfs/texto.pdf'
    pdf_saida = './pdfs/pdf_final.pdf'

    # Instanciar e executar a classe
    converter = convertPDF(json_input, papel_timbrado, pdf_com_texto, pdf_saida)
    converter.run()
