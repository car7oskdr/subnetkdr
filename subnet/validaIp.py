# metodo para validar la IP.
class ValidarIp():
    """docstring for ValidarIp to DO
    """
        
    def __init__(self, str_ip):
        self.str_ip = str_ip

    def validation(self):


        final_list = []
        list_ip_int = []

        
        try:
            # convertion of values of the list to int
            list_ip_int = list(map(lambda ip_int: int(ip_int), self.str_ip))

            # check that the octets are within the ranges.
            for x in range(len(list_ip_int)):
                if list_ip_int[x] > 0 and list_ip_int[x] < 256:
                    pass

                else: 
                    final_list.append(False)
                    final_list.append(2)

            # check taht the ip has 4 octetos.
            if len(list_ip_int) == 4:
                final_list.append(True)
                final_list.append(list_ip_int)
            else:
                final_list.append(False)
                final_list.append(3)

        except ValueError:
            final_list.append(False)
            final_list.append(1)

        return final_list
