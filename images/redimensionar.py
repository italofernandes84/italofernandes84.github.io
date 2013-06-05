# -*- coding: utf-8 -*-

from SimpleCV import Image

nomeImagem = raw_input("Digite o nome da imagem que deseja redimensionar: ")

imgEntrada = Image(nomeImagem)
imgEntrada.resize(1200,300).save(nomeImagem)

print ("Convertendo e redimensionando...")
print ("Done!")