from random import randint


def dado(i):
    resuldado = randint(1, 6)
    posibilidades = {
        1: "\n\n\t*\n\n",
        2: "\n\t\t*\n\n*\n",
        3: "\n\t\t*\n\t*\n*\n",
        4: "\n*\t\t*\n\n*\t\t*\n",
        5: "\n*\t\t*\n\t*\n*\t\t*\n",
        6: "\n*\t\t*\n*\t\t*\n*\t\t*\n"
        }
    print(f"\nEl dado número {i} ha generado aleatoriamente un:\n", posibilidades[resuldado])
    return resuldado


def entrada():
    try:
        num = int(input("¿Cuántos dados lanzamos?"))
        return num
    except ValueError:
        print("Eso no es un número...")
        return "Rep"


def salir(lista):
    pass


def menu():
    print("\033[4;0m" + "PROGRAMA GENERA DADOS")
    estado = True
    resuldados = []
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
            resuldados.append(resuldado)


if __name__ == "__main__":
    menu()
