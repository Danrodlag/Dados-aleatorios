from random import randint
# Importamos randint para elegir un número aleatorio.
# https://github.com/Danrodlag/PEP1T_4_DRL


def ens_dado(num, it):
    # Creamos un diccionario con los dados, hechos con saltos de línea y tabulaciones para ahorrar líneas
    posibilidades = {
        1: "\n\n\t*\n\n",
        2: "\n\t\t*\n\n\n\n*\n",
        3: "\n\t\t*\n\n\t*\n\n*\n",
        4: "\n*\t\t*\n\n\n\n*\t\t*\n",
        5: "\n*\t\t*\n\n\t*\n\n*\t\t*\n",
        6: "\n*\t\t*\n\n*\t\t*\n\n*\t\t*\n"
    }
    # Enseñamos por pantalla el mensaje con el dado y el número de dado en el que estamos
    print(f"\nEl dado número {it + 1} ha generado aleatoriamente un:\n", posibilidades[num])
    return


# Programa para devolver un número aleatorio
def dado():
    resuldado = randint(1, 6)
    return resuldado


# Función para pedir y comprobar el número de dados que quieren que tiremos
def entrada():
    try:
        num = int(input("¿Cuántos dados lanzamos? "))
        return num
    except ValueError:
        print("Eso no es un número...")
        return "Rep"


# Lo que queremos que haga al salir, enseñando los dados no repetidos que han salido
def salir(caja):
    lista_ordenada = sorted(list(caja))
    # Enseñamos por pantalla la lista ordenada
    print("Los valores de los dados lanzados fueron: ", ", ".join(str(x) for x in lista_ordenada))
    return


# Menú principal con el bucle y toda la salida
def menu():

    # Título
    print("\033[4;0m" + "PROGRAMA GENERA DADOS")

    # Variables que necesitaremos
    estado = True
    resuldados = set()

    # Bucle principal
    while estado:

        # Pedimos el número de repeticiones
        num_rep = entrada()

        # Comprobamos que nos ha devuelto y si quiere salir o es entrada inválida
        if num_rep == 0:
            salir(resuldados)
            estado = False
            continue
        elif num_rep == "Rep":
            continue
        for i in range(num_rep):
            # Bucle que ejecuta todos los dados, y los enseña por pantalla
            resuldado = dado()
            ens_dado(resuldado, i)
            resuldados.add(resuldado)


if __name__ == "__main__":
    # Llamamos a la función menu()
    menu()
