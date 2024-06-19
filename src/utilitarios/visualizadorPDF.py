import fitz  # PyMuPDF
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

class PDFReader:
    def __init__(self, root,textArea,file_path):
        self.root = root
        self.textArea = textArea
        self.file_path = file_path

        self.pdf_document = None
        self.page_count = 0
        self.current_page = 0

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill=tk.BOTH, expand=1)

        self.toolbar = tk.Frame(self.root)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.open_pdf()

        self.open_button = ctk.CTkButton(self.toolbar, text="Voltar", command=self.voltar,fg_color="#00343D",hover_color="#002F37", width=200, font=('Calibri', 15, 'bold'))
        if self.textArea: self.open_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.next_button = ctk.CTkButton(self.toolbar, text="Próxima Página", command=self.next_page,fg_color="#00343D",hover_color="#002F37", width=200, font=('Calibri', 15, 'bold'))
        self.next_button.pack(side=tk.RIGHT, padx=2, pady=2)

        self.prev_button = ctk.CTkButton(self.toolbar, text="Página Anterior", command=self.prev_page,fg_color="#00343D",hover_color="#002F37", width=200, font=('Calibri', 15, 'bold'))
        self.prev_button.pack(side=tk.RIGHT, padx=2, pady=2)

    def open_pdf(self):
        if self.file_path:
            self.pdf_document = fitz.open(self.file_path)
            self.page_count = self.pdf_document.page_count
            self.current_page = 0
            self.display_page(self.current_page)

    def display_page(self, page_number):
        page = self.pdf_document[page_number]
        pix = page.get_pixmap()

        # Convert pixmap to image
        mode = "RGB" if pix.alpha == 0 else "RGBA"
        img = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
        photo = ImageTk.PhotoImage(image=img)

        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo  # Keep a reference to prevent garbage collection

    def next_page(self):
        if self.pdf_document and self.current_page < self.page_count - 1:
            self.current_page += 1
            self.display_page(self.current_page)

    def prev_page(self):
        if self.pdf_document and self.current_page > 0:
            self.current_page -= 1
            self.display_page(self.current_page)

    def voltar(self):
        self.toolbar.pack_forget()
        self.canvas.pack_forget()
        self.textArea.pack(fill=tk.BOTH, expand=True)

