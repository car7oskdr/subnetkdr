from os import system

class KnowMask:
    
    def __init__(self, list_ip):
        """ to Do """
        self.list_ip = list_ip

        # mascarade de red de la ip
        system("clear")
        print('*' * 80)
        ip_string = '.'.join(map(str, self.list_ip))
        if self.list_ip[0] >= 0 and self.list_ip[0] < 128:
            print('\n\tLa IP',ip_string,'es clase A la mascara ',
                  'de red es 255.0.0.0 /8\n')
        elif self.list_ip < 192:
            print('\n\tLa IP',ip_string,'es clase B la mascara ',
                  'de red es 255.255.0.0 /16\n')
        elif self.list_ip < 224:
            print('\n\tLa IP',ip_string,'es clase C la mascara ',
                  'de red es 255.255.255.0 /24\n')
        else:
            pass
        print('*' * 80)
        
