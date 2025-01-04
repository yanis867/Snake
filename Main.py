import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

root = tk.Tk()
root.title("Analyseur Snake")
root.geometry("680x770")
root.resizable(False, False)

file_content = ""

# Panel for file selection
selection_fichier = ttk.Frame(root)
selection_fichier.place(x=10, y=10, width=664, height=90)

def charger_fichier():
    global file_content
    file_path = filedialog.askopenfilename()
    if file_path:
        text_field.delete(0, tk.END)
        text_field.insert(0, file_path)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier: {e}")

btn_charger = ttk.Button(selection_fichier, text="Charger un fichier", command=charger_fichier)
btn_charger.pack(side=tk.LEFT, padx=5, pady=5)

text_field = ttk.Entry(selection_fichier, width=50)
text_field.pack(side=tk.LEFT, padx=5, pady=5)

# Panel for analysis
analyse = ttk.Frame(root)
analyse.place(x=10, y=111, width=664, height=639)

tab_control = ttk.Notebook(analyse)
tab_control.place(x=10, y=10, width=642, height=573)

tab_code_source = ttk.Frame(tab_control)
tab_control.add(tab_code_source, text="Code Source")
scroll_code_source = ttk.Scrollbar(tab_code_source)
scroll_code_source.pack(side=tk.RIGHT, fill=tk.Y)
text_code_source = tk.Text(tab_code_source, wrap=tk.WORD, yscrollcommand=scroll_code_source.set)
text_code_source.pack(expand=1, fill=tk.BOTH, padx=5, pady=5)
scroll_code_source.config(command=text_code_source.yview)

tab_lexicale = ttk.Frame(tab_control)
tab_control.add(tab_lexicale, text="Analyse Lexicale")
scroll_lexicale = ttk.Scrollbar(tab_lexicale)
scroll_lexicale.pack(side=tk.RIGHT, fill=tk.Y)
text_lexicale = tk.Text(tab_lexicale, wrap=tk.WORD, yscrollcommand=scroll_lexicale.set, state=tk.DISABLED)
text_lexicale.pack(expand=1, fill=tk.BOTH, padx=5, pady=5)
scroll_lexicale.config(command=text_lexicale.yview)

tab_syntaxique = ttk.Frame(tab_control)
tab_control.add(tab_syntaxique, text="Analyse Syntaxique")
scroll_syntaxique = ttk.Scrollbar(tab_syntaxique)
scroll_syntaxique.pack(side=tk.RIGHT, fill=tk.Y)
text_syntaxique = tk.Text(tab_syntaxique, wrap=tk.WORD, yscrollcommand=scroll_syntaxique.set, state=tk.DISABLED)
text_syntaxique.pack(expand=1, fill=tk.BOTH, padx=5, pady=5)
scroll_syntaxique.config(command=text_syntaxique.yview)

tab_semantique = ttk.Frame(tab_control)
tab_control.add(tab_semantique, text="Analyse Sémantique")
scroll_semantique = ttk.Scrollbar(tab_semantique)
scroll_semantique.pack(side=tk.RIGHT, fill=tk.Y)
text_semantique = tk.Text(tab_semantique, wrap=tk.WORD, yscrollcommand=scroll_semantique.set, state=tk.DISABLED)
text_semantique.pack(expand=1, fill=tk.BOTH, padx=5, pady=5)
scroll_semantique.config(command=text_semantique.yview)

def analyser():
    global file_content
    if file_content:
        text_code_source.delete(1.0, tk.END)
        text_code_source.insert(tk.END, file_content)
        
        text_lexicale.config(state=tk.NORMAL)
        text_lexicale.delete(1.0, tk.END)
        text_lexicale.insert(tk.END, file_content)
        text_lexicale.config(state=tk.DISABLED)

        text_syntaxique.config(state=tk.NORMAL)
        text_syntaxique.delete(1.0, tk.END)
        text_syntaxique.insert(tk.END, file_content)
        text_syntaxique.config(state=tk.DISABLED)

        text_semantique.config(state=tk.NORMAL)
        text_semantique.delete(1.0, tk.END)
        text_semantique.insert(tk.END, file_content)
        text_semantique.config(state=tk.DISABLED)

btn_analyser = ttk.Button(analyse, text="Analyser", command=analyser)
btn_analyser.place(x=516, y=595, width=136, height=33)

root.mainloop()
