# manejo de errores al ingresar la ip.
class ErrorsValidarIp():
    """docstring for ErrorsValidarIp
        
        requiere: la opcion del mensaje de error a mostrar.
        
        retorna: el mensaje de error. 
    """

    def __init__(self, error):
        self.error = error

    def errors_val(self):

        var = ""

        if self.error == 1:
            var = "El número de octetos es incorrecto"

        elif self.error == 2:
            var = "No puedes ingresar caracteres"

        else:
            var = ("Los octetos no pueden ser negativos, ni mayores "+
                   "a 256.")
            
        return var
