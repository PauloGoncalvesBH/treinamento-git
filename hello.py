import datetime

print("Finalmente ne!")

#Comentario simples

"""

Comentario Teoricamente de Multi Linhas

"""
espaco = "momento                               rapaz            numero       5       "
NOME = "MATHEUS FELIPE"
nome = "matheus felipe"
name = "Matheus Felipe"
age = 22
diferenca = 4
frase = name + "tem {} anos de idade é {} anos mais novo q sua irmã"
lista = ["Gangplank", "Veigar", "Norra", "Sejuani", "Twisted Fate"]
tupla = ("Matheus Felipe", 22, "Cariacica", "Santa Barbara", 130)
personagensFavoritos = {"Veigar", "Ziggs", "Vex"}


print(name)
print(age)

print(type(name))
print(type(age))

print(name[0:5])
print(name[:7])
print(name[5:])
print(name[-1:-5])

print(frase.format(age, diferenca))

print(NOME.lower())
print(nome.upper())
print(espaco.strip())
print(nome.title())
print(name.replace('e', 'i'))


print(type(lista))
print(lista)
lista.pop()
print(lista)
lista.append("Twisted Fate")
print(lista)
lista.insert(0, "Senna")
print(lista)
lista.remove("Gangplank")
print(lista)
lista.append("Aphelios")
print(lista)
lista.pop(3)
print(lista)

print(tupla)
print(len(tupla))
print(type(tupla))
print(tupla[0])
print(tupla[-1])
print(tupla[0:1])
print(tupla[1:])
print(tupla[:1])
print(tupla[-1:-2])
print(tupla[-1:])
print(tupla[:-1])


if "Matheus Felipe" in tupla:
    print("Oia o homi ai o")

(namae, idade, *lugar) = tupla

print(namae)
print(lugar)

lista.append(personagensFavoritos)
print(lista)
personagensFavoritos.add("Fizz")
print(lista)
personagensFavoritos.remove("Vex")
personagensFavoritos.discard("Fizz")

dicionario = {
  "nome": "Matheus Felipe",
  "mae": "Maria Aparecida",
  "pai": "Moacir Soares"
}
if "mae" in dicionario:
  print("Sim, Matheus é filho de Maria e Moacir")


data = datetime.datetime.now()
print(data)