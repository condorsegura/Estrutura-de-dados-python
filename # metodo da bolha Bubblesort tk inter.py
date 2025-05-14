import tkinter as tk
from tkinter import messagebox

# Função para trocar dois elementos em uma lista
def troca(lista, i):
    lista[i], lista[i + 1] = lista[i + 1], lista[i]

# Função Bubble Sort
def bubblesort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                troca(lista, j)

# Lista global para armazenar os números
seg = []

# Função para executar o Bubble Sort e exibir o resultado
def executar_bubblesort():
    try:
        if not seg:
            messagebox.showwarning("Aviso", "A lista está vazia. Adicione números antes de ordenar.")
            return
        bubblesort(seg)
        messagebox.showinfo("Resultado", f"Números ordenados: {seg}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função para adicionar números à lista
def adicionar_numero():
    try:
        numero = int(entry_numero.get())
        seg.append(numero)
        entry_numero.delete(0, tk.END)
        messagebox.showinfo("Sucesso", f"Número {numero} adicionado!")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Interface Bubble Sort")

# Campo para adicionar números
frame_adicionar = tk.Frame(root)
frame_adicionar.pack(pady=10)

label_numero = tk.Label(frame_adicionar, text="Número:")
label_numero.pack(side=tk.LEFT, padx=5)

entry_numero = tk.Entry(frame_adicionar)
entry_numero.pack(side=tk.LEFT, padx=5)

btn_adicionar = tk.Button(frame_adicionar, text="Adicionar Número", command=adicionar_numero)
btn_adicionar.pack(side=tk.LEFT, padx=5)

# Botão para executar o Bubble Sort
btn_ordenar = tk.Button(root, text="Ordenar Números", command=executar_bubblesort)
btn_ordenar.pack(pady=10)

# Inicia o loop da interface
root.mainloop()