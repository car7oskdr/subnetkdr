# metodo para validar la IP.
class ValidarIp():
    """docstring for ValidarIp
        
        requiere: Una lista con los cuatro octetos en formato string
                  puede ser ['255.255.255.2555'] o 
                            ['255','255','255','255']
        retorna: Una lista con:
                    pos[0] valor voleano dependiendo si la ip 
                    ingresada es correcta,
                    pos[1] si la ip es incorrecta retorna un valor
                    entero que indica el error a mostrar por 
                    errors/validaIp,
                    si la ip es correcta retornara una lista con los
                    octetos en formato type int [A, B, C, D]
    """
        
    def __init__(self, str_ip):
        self.str_ip = str_ip

    def validation(self):
        
        lista_ip_int = []
        final_list = []

        # verificar el numero de elementos dentro de la lista.
        if len(self.str_ip) == 1:
            print("subnet/valida.py/1")
            pass
        # verificar que sean cuatro elementos en la lista.
        elif len(self.str_ip) == 4:
            print(self.str_ip)
            self.str_ip = self.str_ip.split(sep = '.')
        else:
            print("yes, here subnet/valida.py/2")
            final_list.append(False)
            final_list.append(1)
            print(final_list)
        # conversión de valores de la lista a enteros.
        print("yes, here subnet/valida.py/3")
        try:
            print("yes, here subnet/valida.py/4")
            print(self.str_ip)
            for x in range(len(self.str_ip)):
                print(x)
                lista_ip_int.append(int(self.str_ip[x]))
            print("yes, here subnet/valida.py/5")
        except ValueError:
            final_list.append(False)
            final_list.append(2)

        # comprobar que los octetos esten dentro de los rangos.
        for x in range(len(lista_ip_int)):
            if lista_ip_int[x] < 0 and lista_ip_int[x] >= 256:
               pass
            else: 
                final_list.append(False)
                final_list.append(3)
    
        final_list.append(True)
        final_list.append(lista_ip_int)
        print(final_list)
        print("yes, here subnet/valida.py/6")

        return final_list
