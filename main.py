from subnet.validaIp import ValidarIp as valida
from subnet.mask import KnowMask as mask_class
from errors.validaIp import ErrorsValidarIp as e_valida

def ingresa_ip(opcion):
    # ingreso de la ip.
    lista_ip = input('\n\tIngresa la IP: ')
    str_ip = lista_ip.split(sep = '.')
    valida_ip = valida(str_ip)
    val = valida_ip.validation()

    if val[0]:
        if opcion == 1:
            mascara = mask_class(val[1])
            maskc = mascara.mask()
            print(maskc)

        else:
            pass

    else:
        error = e_valida(val[1])
        fin_error = error.errors_val()
        print(fin_error)

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
        elif opc == 1 or opc == 2:
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
