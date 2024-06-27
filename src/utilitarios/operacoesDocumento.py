import json
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from PyPDF2 import PdfReader, PdfWriter, PageObject
from itertools import islice
from functools import cmp_to_key

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
    def __init__(self, json_input, papel_timbrado, pdf_com_texto, pdf_saida,substitution:dict = None):
        self.json_input = re.sub(r'[\x00-\x1f\x7f-\x9f]', r"\\n", json_input)
        print(self.json_input)
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
        print(substitution)
        self.substitution = substitution

    def nth_index(self, iterable, value, n):
        if n == 0:
            return 0
        matches = (idx for idx, val in enumerate(iterable) if val == value)
        return next(islice(matches, n-1, n), None)

    def remover_tuplas_vazias(self, lista_tuplas):
        return [tupla for tupla in lista_tuplas if tupla[0] != '']

    def comparar_tuplas(self,a, b):
        inicio_a, fim_a = a[1], a[2]
        inicio_b, fim_b = b[1], b[2]
        
        # Comparar pelos inícios
        if inicio_a < inicio_b:
            return -1
        elif inicio_a > inicio_b:
            return 1
        else:
            # Se os inícios forem iguais, comparar pelos fins (tupla maior primeiro)
            if fim_a > fim_b:
                return -1
            elif fim_a < fim_b:
                return 1
            else:
                return 0
            
    def ordenar_tuplas(self, lista_tuplas):
        return sorted(lista_tuplas, key=cmp_to_key(self.comparar_tuplas))

    def lastCases(self,start,end,lastStart,lastEnd):
        if lastStart <= start and end <= lastEnd:
            return 0 # O atual está entre o último
        else: 
            return 1 # Depois do último, não estão um entre os outros

    def apply_styles(self, content, styled_text):
        styled_content = content
        styled_start = 0
        styled_end = 0
        offset = 0
        lastStartWithoutOffset = 0
        lastStart = 0
        firstIteration = True
        lastOffsetIncrement = 0
        for styled_item in styled_text:
            text, start, end, style = styled_item
            if firstIteration:
                lastStart = start
                lastEnd = end
                lastStartWithoutOffset = start
                lastEndWithoutOffset = end
                firstIteration = False
            
            match self.lastCases(start,end,lastStartWithoutOffset,lastEndWithoutOffset):
                case 0:
                    #print("O atual está entre o último")
                    styled_start = lastStart + lastOffsetIncrement
                    styled_end =   lastEnd + lastOffsetIncrement
                case 1:
                    styled_start = start + offset
                    styled_end =  end + offset
                    #print("Depois do último, não estão um entre os outros")

            lastStartWithoutOffset = start
            lastEndWithoutOffset = end
            
            
            style = self.custom_styles.get(style)
            styled_content = styled_content[:styled_start] + f"<{style}>" + styled_content[styled_start:]
            offset += len(f"<{style}>")
            
            styled_content = styled_content[:styled_end + len(f"<{style}>")] + f"</{style}>" + styled_content[styled_end + len(f"<{style}>"):]
            offset += len(f"</{style}>")

            lastOffsetIncrement = len(f"<{style}>")
            lastStart = styled_start
            lastEnd = styled_end
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
                start = self.nth_index(content, '\n', lineStart) + wordStart + 1
                end = self.nth_index(content, '\n', lineEnd) + wordEnd
                if content[end] != '\n':
                    end += 1
                if lineStart == 0:
                    start -= 1
                checkLineInContent = content[start:end]

                i=1
                while '\n' in checkLineInContent:
                    lineLocation = self.nth_index(content, '\n',lineStart + i)
                    formatted_text.append((content[start:lineLocation], start, lineLocation, tagName))
                    start = lineLocation + 1
                    checkLineInContent = content[start:end]
                    i+=1
        
                formatted_text.append((content[start:end], start, end, tagName))
                
        formatted_text = self.remover_tuplas_vazias(formatted_text)
        formatted_text = self.ordenar_tuplas(formatted_text)
        #print(formatted_text)
        content = self.apply_styles(content, formatted_text)
        notLineCounter = 0

        for line in content[0:].split('\n'):
            if not line and notLineCounter == 0:
                notLineCounter += 1
                continue
            if self.substitution:
                line = self.replaceInformations(line)
            p = Paragraph(line, styles['Normal'])
            
            elements.append(p)
            if '<font size="12">' in line:
                print("teste")
                elements.append(Spacer(1, 8))
            elif '<font size="16">' in line:
                print("teste")
                elements.append(Spacer(1, 10))
            elif '<font size="20">' in line:
                print("teste")
                elements.append(Spacer(1, 12))
            else:
                pass
                elements.append(Spacer(1, 5))
            notLineCounter = 0
        try:
            doc.build(elements)
        except Exception as e:
            raise e

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

    def replaceInformations(self, line):
        startTag = None
        i = 0
        while i < len(line) - 1:
            if line[i] == '$' and line[i+1] == '$':
                if startTag is None:
                    startTag = i
                else:
                    finalTag = i + 2
                    key = line[startTag:finalTag]
                    if key in self.substitution:
                        line = line[:startTag] + self.substitution[key] + line[finalTag:]
                        i = startTag + len(self.substitution[key]) - 1
                    startTag = None
            i += 1
        return line
    


def replaceInformations(self, line):
    startTag = None
    i = 0
    while i < len(line) - 1:
        if line[i] == '$' and line[i+1] == '$':
            if startTag is None:
                startTag = i
            else:
                finalTag = i + 2
                key = line[startTag:finalTag]
                if key in self.substitution:
                    line = line[:startTag] + self.substitution[key] + line[finalTag:]
                    i = startTag + len(self.substitution[key]) - 1
                startTag = None
        i += 1
    return line

if __name__ == "__main__":
    line = "<b>CONTRATANTE</b>: , $$nacionalidadecontratante$$, $$estadocivilcontratante$$, $$profissãocontratante$$, portador(a) da cédula de identidade R.G. nº $$RG contratante$$, inscrito(a) no CPF/MF sob o nº $$cpfoucnpjcontratante$$, residente e domiciliado(a) à $$endereçoresidêncial/comercialcontratante$$, doravante denominado simplesmente CONTRATANTE."
    subs = {'$$nomecompletocontratante$$': '', '$$nacionalidadecontratante$$': '', '$$estadocivilcontratante$$': '', '$$profissãocontratante$$': '', '$$cpfoucnpjcontratante$$': '', '$$endereçoresidêncial/comercialcontratante$$': '', '$$nomecompletocontratado$$': '', '$$nacionalidadecontratado$$': '', '$$estadocivilcontratado$$': '', '$$profissãocontratado$$': '', '$$cpfoucnpjcontratado$$': '', '$$endereçoresidêncial/comercialcontratado$$': '', '$$valor$$': '', '$$formadepagamento$$': '', '$$multademora$$': '', '$$jurosdemora$$': '', '$$correçãomonetária$$': '', '$$prazodeduração$$': ''}
    print(replaceInformations(line,subs))