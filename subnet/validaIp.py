# metodo para validar la IP.
class ValidarIp():
    """docstring for ValidarIp to DO
    """
        
    def __init__(self, str_ip, final_list = []):
        self.str_ip = str_ip
    

    def validation(self):

        list_ip_int = []
        final_list = []
        
        try:
            # convertion of values of the list to int
            list_ip_int = list(map(lambda ip_int: int(ip_int), self.str_ip))

            # check taht the ip has 4 octetos.
            if len(list_ip_int) == 4:
                # check that the octets are within the ranges.
                if len(list(filter(lambda x: x > 0 and x < 256, list_ip_int), 2)) == 4:
                    final_list.append(True)
                    final_list.append(list_ip_int)
                else:
                    final_list.append(False)
                    final_list.append(3)        
            else:
                final_list.append(False)
                final_list.append(2)

        except ValueError:
            final_list.append(False)
            final_list.append(1)

        return final_list