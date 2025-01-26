"""Programa para mesclar PDFs 
Inserir os PDFs que serão mesclados na pasta 'arquivos', organizados por numeração."""

# Carregando os módulos
import PyPDF2
import os

# Mesclador de PDFs
merger = PyPDF2.PdfMerger()

# Objeto para listar os arquivos na pasta
lista_arquivos = os.listdir('arquivos')

# Ordena os arquivos na pasta, para que sejam mesclados na ordem correta
lista_arquivos.sort()

# Verificando se os arquivos estão ordenados
print(lista_arquivos)

# Vamos mesclar os arquivos
for arquivo in lista_arquivos:

    # Verificando se há arquivo que não é PDF na pasta
    if '.pdf' in arquivo:
        merger.append(f'arquivos/{arquivo}')

# Criando o novo arquivo mesclado
merger.write('PDF_mesclado.pdf')