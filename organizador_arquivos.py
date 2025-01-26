"""Programa para organizar arquivos
Após a seleção da pasta que será organizada, o programa cria pastas e organiza os arquivos por tipo"""

# Importando módulos
import os
from tkinter.filedialog import askdirectory

# Selecionando uma pasta e salvando o caminho
caminho = askdirectory(title='Selecione uma pasta')
print(caminho)

# Vamos listar os arquivos presentes na pasta selecionada
lista_arquivos = os.listdir(caminho)
print(lista_arquivos)

# Vamos criar um dicionário para armazenar as extensões que deverão ficar em cada pasta
# {pasta: extensão}
locais = {
    'Imagens': ['.jpg', '.png'],
    'Arquivos de Texto': ['.txt'],
    'PDFs': ['.pdf'],
    'Planilhas': ['.xlsx', '.csv']
}

# Loop para percorrer os arquivos
for arquivo in lista_arquivos:

    # Separa o caminho+nome_arquivo da extensão (que é o que queremos) 
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}')

    # Loop para verificar para qual pasta um arquivo deve ir
    for pasta in locais:
        if extensao in locais[pasta]:

            # Verificando se a pasta existe, caso contrário, será criada
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho}/{pasta}')

            # Movendo os arquivos para as pastas apropriadas    
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')
            