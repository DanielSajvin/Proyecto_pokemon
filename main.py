import os 
clear = lambda: os.system('cls')

# En este espacio se le presentara al usuario el menú principal. 
# Donde el entrenador podrá encontrar todas las características del videojuego que su equipo ha desarrollado

while True:
    clear()
    print('---- Menú Principal ----')
    print('1.- Equipo Pokémon.')
    print('2.- Batallas contra Pokémon salvajes')
    print('3.- Pokédex')
    print('4.- Tienda')
    print('5.- Salor del videojuego')
    opcion = int(input('Ingrese una opcion: '))

    # Equipo pokémon
    if opcion == 1:
        pass

    # Batallas contra pokémon salvajes#
    elif opcion == 2:
        pass

    # Pokédex
    elif opcion == 3:
        pass

    # Tienda
    elif opcion == 4:
        pass

    # Salir
    elif opcion == 5:
        clear()
        break

    # De ingresar un numero invalido este seguira reproduciendose.
    else:
        continue