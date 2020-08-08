
import sys
import numpy as np
import math

# Checando os argumentos de linha de comando
if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f'Argument:{i}: {arg}')


# Abrir os arquivos de entrada e de saída
entrada = open(sys.argv[1], "r+")
saida = open(sys.argv[2], "w+")

linha = entrada.readline() #P2
linha = entrada.readline() #Comentário
linha = entrada.readline() #Dimensões
dimensoes = linha.split()
largura = int(dimensoes[0])
altura = int(dimensoes[1])
linha = entrada.readline() #Valar fixo
linha = entrada.readlines() #Ler o restante do arquivo e gravar como lista

#converter de lista para array
imagem = np.asarray(linha, dtype=int)
#reshape
imagem = np.reshape(imagem, (altura, largura))


#Edge Detection
kernel = [[1, 0, -1], [0, 0, 0], [-1, 0, 1]]
kernel = np.asarray(kernel)

#kernel = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
#kernel = np.asarray(kernel)

#kernel = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
#kernel = np.asarray(kernel)

print(kernel)

ks = int((len(kernel) - 1) / 2)

#escrevendo a imagem cópia
saida.write("P2\n")
saida.write("#Criado por Thais\n")
saida.write(str(largura-(ks*2)))
saida.write(" ")
saida.write(str(altura-(ks*2)))
saida.write("\n")
saida.write("255\n")

#fazer a transformação
for i in range(ks, len(imagem)-ks):
    for j in range(ks, len(imagem[1])-ks):
        sum = 0
        for ki in range(len(kernel)):
            for kj in range(len(kernel[1])):
                sum = sum + (imagem[i - ks + ki][j - ks + kj] * kernel[ki][kj])
        sum = int(sum)
        sum = str(sum)
        saida.write(sum)
        saida.write("\n")

#fechar os dois arquivos
entrada.close()
saida.close()
