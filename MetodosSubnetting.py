from os import system
from IPclaseC import claseC as c
from IPclaseC import ClaseCsubnetting as subC

class metodosSub:
    
    def __init__(self, ip_int, opc_metodo):
        
        self.ip_int = ip_int
        self.opc_metodo = opc_metodo

        # mascarade de red de la ip
        def mascara_de_red(octeto_uno):
            system("clear")
            print('*' * 80)
            ip_string = '.'.join(map(str, self.ip_int))
            if octeto_uno >= 0 and octeto_uno < 128:
                print('\n\tLa IP',ip_string,'es clase A la mascara de red es 255.0.0.0 /8\n')
            elif octeto_uno < 192:
                print('\n\tLa IP',ip_string,'es clase B la mascara de red es 255.255.0.0 /16\n')
            elif octeto_uno < 224:
                print('\n\tLa IP',ip_string,'es clase C la mascara de red es 255.255.255.0 /24\n')
            else:
                pass
            print('*' * 80)
        
        # validar desarrollo de subnetting.
        def validar_desarrollo(octeto_uno):

            while True:
                if octeto_uno >= 0 and octeto_uno < 128:
                    pass
                elif octeto_uno < 192:
                    pass
                elif octeto_uno < 224:
                    try:
                        var_sub = int(input('\tIngrese el número de subredes: '))
                        if var_sub > 0 and self.opc_metodo == 2:
                            c(var_sub, self.ip_int)
                            break
                        elif var_sub > 0 and self.opc_metodo == 3:
                            var_tem = subC(var_sub, self.ip_int)
                            var_tem.subnetting()
                            break
                        else:
                            print('\n\tFavor de introducir un número de subredes mayor a cero.')
                    except ValueError:
                        print('\n\tFavor de verificar que el número ingresado sea un entero mayor a cero.')

        if self.opc_metodo == 1:
            mascara_de_red(self.ip_int[0])

        elif self.opc_metodo == 2:
            validar_desarrollo(self.ip_int[0])
        else:
            validar_desarrollo(self.ip_int[0])
