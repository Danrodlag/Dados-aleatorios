from random import randint


def dado(i):
    resuldado = randint(1, 6)
    posibilidades = {
        1: "\n\n\t*\n\n",
        2: "\n\t\t*\n\n\n\n*\n",
        3: "\n\t\t*\n\n\t*\n\n*\n",
        4: "\n*\t\t*\n\n\n\n*\t\t*\n",
        5: "\n*\t\t*\n\n\t*\n\n*\t\t*\n",
        6: "\n*\t\t*\n\n*\t\t*\n\n*\t\t*\n"
        }
    print(f"\nEl dado número {i + 1} ha generado aleatoriamente un:\n", posibilidades[resuldado])
    return resuldado


def entrada():
    try:
        num = int(input("¿Cuántos dados lanzamos? "))
        return num
    except ValueError:
        print("Eso no es un número...")
        return "Rep"


def salir(set_lista):
    lista_ordenada = sorted(list(set_lista))

    print("Los valores de los dados lanzados fueron: ", ", ".join(str(x) for x in list(set_lista)))
    print("Los porcentajes de salida son: ", "% ".join(str(x) for x in lista_porc), end="%")
    return


def menu():
    print("\033[4;0m" + "PROGRAMA GENERA DADOS")
    with open("resuldados.txt", "w", encoding="utf-8") as fichero:

    estado = True
    resuldados = set()
    while estado:
        num_rep = entrada()
        if num_rep == 0:
            salir(resuldados)
            estado = False
            continue
        elif num_rep == "Rep":
            continue

        for i in range(num_rep):
            resuldado = dado(i)
            resuldados.add(resuldado)
            with open("resuldados.txt", "a", encoding="utf-8") as fichero:
                fichero.write(str(resuldado))


if __name__ == "__main__":
    menu()
