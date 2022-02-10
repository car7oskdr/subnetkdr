from subnet.validaIp import ValidarIp as valida
from subnet.mask import KnowMask as mask
from errors.validaIp import ErrorsValidarIp as e_valida

def ingresa_ip(opcion):
    # ingreso de la ip.
    lista_ip = list(input('\n\tIngresa la IP: '))
    #print(lista_ip)
    valida_ip = valida(lista_ip)
    val = valida_ip.validation()
    print("yes, here index.py/1")

    if val[0]:
        if opcion == 1:
            #print(mask(valida_ip))
            mascara = mask(val)
            print(mascara)
        else:
            pass
    else:
        e_valida(valida_ip[1])

while True:
    #menu de subnetting
    print("""\n\t\t\=======>SUBNETTING<=======/
            1.-Conocer la clase y mascara de red de una IP.
            2.-Realizar subenetting.
            3.-Salir\n""")

    try:
        opc = int(input('Favor de eligir una opción: '))
        print('\n\n')

        if opc <= 0:
            print('=' * 85)
            print('\n\t\tHas ingresado un cero o un numero negativo')
            print('\t\tElegir un numero entero de la lista.\n')
            print('=' * 85)
        elif opc == 1:
            ingresa_ip(opc)
        elif opc == 2:
            ingresa_ip(opc)
        elif opc == 3:
            print('=' * 85)
            print('\n\t\t "Gracias por usar la app"\n')
            print('=' * 85)
            exit()
        else:
            print('=' * 85)
            print(f'\n\t El numero ingresado {opc} esta fuera',
                   'del rango de la lista, elige otra opción.\n\n')
            print('=' * 85)

    except (ValueError, TypeError):
        print('=' * 85)
        print('\n\tHas escogido un carater o ingresaste un numero',
              ' con punto decimal.')
        print('\t\tFavor de elegir un numero entero de la lista.\n')
        print('=' * 85)
