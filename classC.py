from os import system
class claseC:
    # metodo inicial de la clase clasC
    def __init__(self, subredes, dir_ip):
        # variables de inicializaciń de la clase.
        system("clear")
        self.subredes = subredes
        self.dir_ip = dir_ip
        print('*' * 80)
        # mensaje de salida al utilizar la clase.
        ip_string = '.'.join(map(str, self.dir_ip))
        print('\n\tLa ip ',ip_string,'es clase C su mascara de red es: 255.255.255.0 /24')
        print('\tEl número de subredes requerido son',self.subredes,'\n')
    # comprovación para saber si es viable el desarrollo de subneting.
        # pasar el número de subredes a binario.
        subredes_bin = bin(self.subredes)
        var_subred = (2**(len(subredes_bin) - 2)) - 2
        # creamos una lista para obtener el numero binario del ultimo octeto.
        lista_mascara = []

        for x in range(1, 9):
            if x <= (len(subredes_bin) - 2):
                lista_mascara.append(1)
            else:
                lista_mascara.append(0)
        # los valores de la lista los unimos en un solo valor y los pasamos a int.
        lista_str = ''.join(map(str, lista_mascara))
        # conocer los bits encendidos para la mascara de red clase C.
        encendidos = 24
        for x in range(len(lista_mascara)):
            encendidos += lista_mascara[x]
        # la variable "var_int" almacenara el valor decimal del último octeto.
        var_int = int(lista_str, 2)
        # finalmente comprobamos si es viable el subneteo y mostramos los mensajes.
        if var_subred >= self.subredes:
            print('\tEl desarrollo del subneting es viable.\n \tse comprobo con la formula: 2^#bit - 2 ≥ #subredes')
            print('\t\t\t',var_subred,'>=',self.subredes)
            print('\t\t La nueva mascara es: 255.255.255.' + str(var_int) + ' /' + str(encendidos) + '\n')
            print('*' * 80)
        else:
            print('No es valido el desarrollo de subneting. 2^#bit - 2 !≥ #subredes')
            print('\t\n',var_subred,'!>=',self.subredes)
            print('*' * 80)
    
class ClaseCsubnetting(claseC):
    # inicio de clase para realizar el subnetting.
    def subnetting(self):
        while True:
            try:
                # obtención y verificación del rango ingresado por el usuario.
                n_rangos = int(input('Ingrese el numero de rangos: '))
                if n_rangos <= 0:
                    print('\n\tFavor de ingresar un valor entero mayor a cero.\n')
                elif n_rangos > self.subredes:
                    print('\n\tEl número de rangos no puede ser mayor al número de subredes\n')
                else:
                    break
            except ValueError:
                print('\n\tFavor de ingresar un valor entero mayor a cero.\n')
        # lista para guardar los rangos que indique el usuario.
        lista_rangos = []
        while True:
            try:
                # llenamos la lista de los rangos.
                for x in range(0, n_rangos):
                    in_rango = int(input('\n\tIngresa un rango: '))
                    lista_rangos.append(in_rango)
                break
            except ValueError:
                print('\n\t favor de ingresar un rango correcto debe ser entero, mayor a cero y menor al número de subredes.\n')
                lista_rangos = []
        # lista para lamacenar los rangos en binario
        lista_rangos_bin = []
        for x in range(0, n_rangos):
            lista_rangos_bin.append(bin(lista_rangos[x]))
        # lista para almacenar los numros binarios sin "0b"
        lista_binaria = []
        for x in range(len(lista_rangos_bin)):
            var_binaria = lista_rangos_bin[x]
            lista_binaria.append(var_binaria[2:])
        del lista_rangos_bin
        self.dir_ip.pop()
        # inicio del rango.
        i_lista_binaria = []
        for x in range(len(lista_binaria)):
            lista_aux = []
            var = lista_binaria[x]
            for y in range(len(var)):
                lista_aux.append(var[y])
            while len(lista_aux) < len(bin(self.subredes)) - 2:
                lista_aux.insert(0, '0')
            while (len(lista_aux) + 1) <= 8:
                lista_aux.insert(len(lista_aux ) + 1, '0')
            var = ''.join(map(str, lista_aux))
            i_lista_binaria.append(var)
            lista_aux = []
        # fin del rango.
        f_lista_binaria = []
        for x in range(len(lista_binaria)):
            lista_aux = []
            var = lista_binaria[x]
            for y in range(len(var)):
                lista_aux.append(var[y])
            while len(lista_aux) < len(bin(self.subredes)) - 2:
                lista_aux.insert(0, '0')
            while (len(lista_aux) + 1) <= 8:
                lista_aux.insert(len(lista_aux) + 1, '1')
            var = ''.join(map(str, lista_aux))
            f_lista_binaria.append(var)
            lista_aux = []
        # obtención del inicio y fin del rango en enteros.
        for x in range(len(lista_binaria)):
            i_lista_binaria[x] = int(i_lista_binaria[x], 2)
            f_lista_binaria[x] = int(f_lista_binaria[x], 2)
        
        def ini_fin(rangos, direc_ip, inicio_lis, fin_lis):
            inicio = []
            fin = []
            for x in range(len(rangos)):
                for y in range(0, 3):
                    inicio.append(direc_ip[y])
                    fin.append(direc_ip[y])
                inicio.append(inicio_lis[x])
                fin.append(fin_lis[x])
                i_var = '.'.join(map(str, inicio))
                f_var = '.'.join(map(str, fin))
                print('+' * 80)
                print('\n\tRango:',x + 1,rangos[x])
                print('\n\t\tInicio de rango: ', i_var)
                print('\n\t\tFinal de rango: ', f_var)
                inicio = []
                fin = []
            print('+' * 80)
        
        ini_fin(lista_rangos, self.dir_ip, i_lista_binaria, f_lista_binaria)
        
