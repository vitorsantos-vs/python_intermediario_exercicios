print("Crie um programa que faça a compressão de uma string usando o algoritmo de compressão RLE (Run-Length Encoding).\n")

def compressao_rle(input_string):
    count = 1
    prev = ""
    lista = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lista.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character, count)
        lista.append(entry)
    return lista

input_string = "AAAABBBCCD"
print(compressao_rle(input_string))
