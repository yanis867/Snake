import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Analyseur Snake")
        self.geometry("680x770")
        self.resizable(False, False)

        # Panel for file selection
        self.selection_fichier = ttk.Frame(self)
        self.selection_fichier.place(x=10, y=10, width=664, height=90)

        self.btn_charger = ttk.Button(self.selection_fichier, text="Charger un fichier", command=self.charger_fichier)
        self.btn_charger.pack(side=tk.LEFT, padx=5, pady=5)

        self.text_field = ttk.Entry(self.selection_fichier, width=50)
        self.text_field.pack(side=tk.LEFT, padx=5, pady=5)

        # Panel for analysis
        self.analyse = ttk.Frame(self)
        self.analyse.place(x=10, y=111, width=664, height=639)

        self.tab_control = ttk.Notebook(self.analyse)
        self.tab_control.place(x=10, y=10, width=642, height=573)

        self.tab_code_source = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_code_source, text="Code Source")
        self.scroll_code_source = ttk.Scrollbar(self.tab_code_source)
        self.scroll_code_source.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_code_source = tk.Text(self.tab_code_source, wrap=tk.WORD, yscrollcommand=self.scroll_code_source.set)
        self.text_code_source.pack(expand=1, fill=tk.BOTH, padx=5, pady=5)
        self.scroll_code_source.config(command=self.text_code_source.yview)
        
        self.tab_lexicale = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_lexicale, text="Analyse Lexicale")
        self.scroll_lexicale = ttk.Scrollbar(self.tab_lexicale)
        self.scroll_lexicale.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_lexicale = tk.Text(self.tab_lexicale, wrap=tk.WORD, yscrollcommand=self.scroll_lexicale.set, state=tk.DISABLED)
        self.text_lexicale.pack(expand=1, fill=tk.BOTH, padx=5, pady=5)
        self.scroll_lexicale.config(command=self.text_lexicale.yview)

        self.tab_syntaxique = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_syntaxique, text="Analyse Syntaxique")
        self.scroll_syntaxique = ttk.Scrollbar(self.tab_syntaxique)
        self.scroll_syntaxique.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_syntaxique = tk.Text(self.tab_syntaxique, wrap=tk.WORD, yscrollcommand=self.scroll_syntaxique.set, state=tk.DISABLED)
        self.text_syntaxique.pack(expand=1, fill=tk.BOTH, padx=5, pady=5)
        self.scroll_syntaxique.config(command=self.text_syntaxique.yview)

        self.tab_semantique = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_semantique, text="Analyse Sémantique")
        self.scroll_semantique = ttk.Scrollbar(self.tab_semantique)
        self.scroll_semantique.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_semantique = tk.Text(self.tab_semantique, wrap=tk.WORD, yscrollcommand=self.scroll_semantique.set, state=tk.DISABLED)
        self.text_semantique.pack(expand=1, fill=tk.BOTH, padx=5, pady=5)
        self.scroll_semantique.config(command=self.text_semantique.yview)
        

        self.btn_analyser = ttk.Button(self.analyse, text="Analyser", command=self.analyser)
        self.btn_analyser.place(x=516, y=595, width=136, height=33)

        self.file_content = ""  # To store file content

    def charger_fichier(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.text_field.delete(0, tk.END)
            self.text_field.insert(0, file_path)

            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    self.file_content = file.read()
            except Exception as e:
                print(f"Erreur lors de la lecture du fichier: {e}")

    def analyser(self):
        if self.file_content:
            self.text_code_source.delete(1.0, tk.END)
            self.text_code_source.insert(tk.END, self.file_content)
            
            self.text_lexicale.config(state=tk.NORMAL)
            self.text_lexicale.delete(1.0, tk.END)
            self.text_lexicale.insert(tk.END, self.file_content)
            self.text_lexicale.config(state=tk.DISABLED)

            self.text_syntaxique.config(state=tk.NORMAL)
            self.text_syntaxique.delete(1.0, tk.END)
            self.text_syntaxique.insert(tk.END, self.file_content)
            self.text_syntaxique.config(state=tk.DISABLED)

            self.text_semantique.config(state=tk.NORMAL)
            self.text_semantique.delete(1.0, tk.END)
            self.text_semantique.insert(tk.END, self.file_content)
            self.text_semantique.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
