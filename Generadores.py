from ViewTest import mostrar_mensaje



nombreclase = "Atributo"
ruta = "/home/inspiron/Escritorio"
checkedlist = ['repr']
atributos = []
atributos_getter = []
atributos_setter = []
tipos = []


#itemtest =tabla.GetItem(0,col=0)
#itemtest2 =tabla.GetItem(0,col=1)
#itemtest3 =tabla.GetItem(0,col=2) 
#itemtest4 =tabla.GetItem(0,col=3)    
                


def generador_archivo(nombreclase,ruta):
    file = open(f"{ruta}/{nombreclase}.py","x")
    file.close()

def definir_atributos(tabla):
    limite=tabla.GetItemCount()
    for y in range(0,limite,1):
      variable = tabla.GetItem(y,col=0)
      atributos.append(variable.GetText())

    for y in range(0,limite,1):
        tipo = tabla.GetItem(y,col=1)
        tipos.append(tipo.GetText())  

def get_data(data_list):
    pass

def class_constructor(nombreclase,ruta,tabla):
    

    file = open(f"{ruta}/{nombreclase}.py","a")
    file.write(f"\nclass {nombreclase}(): ")
    file.write("\n")
    
    string = listar_variables_horizontal(tabla)
    file.write(f"\n    def __init__(self{string}):")
    file.close()
    listar_variables_vertical(nombreclase,ruta)

    file.close()
        

def listar_variables_horizontal(tabla):
   
    x=0
    cadena = ""
    
    definir_atributos(tabla)

    for atributo in atributos:
        cadena = cadena+f",{atributo}"

    return cadena

def listar_variables_vertical(nombreclase,ruta):

    file = open(f"{ruta}/{nombreclase}.py","a")

    #Por ahora por defecto hago los atributos 'privados' debido a que si
    #Vas a crear una clase con get and set los atributos deben ser privados(get-set)
    for atributo in atributos:
        file.write(f"\n        self.__{atributo} = {atributo}")

    file.close()        


def getter_setter(nombreclase,ruta):
    comilla = "'"
    
    #Getter Method
    file = open(f"{ruta}/{nombreclase}.py","a")
    file.write("\n")
    file.write("\n")    

    for atributo in atributos:
        file.write("\n    @property")
        file.write(f"\n    def {atributo}(self):")
        file.write(f"\n        return self.__{atributo}")
        file.write("\n")    

    #Setter Method
    n=0
    for atributo in atributos:
        file.write(f"\n    @{atributo}.setter")        
        file.write(f"\n    def {atributo}(self,{atributo}):")
        file.write(f"\n        if isinstance({atributo},{tipos[n]}):")    
        file.write(f"\n           self.__{atributo} = {atributo}")
        file.write(f"\n        else:")
        file.write(f"\n            raise TypeError({comilla}Tipo invalido para el atributo{comilla}) ")     
        file.write("\n")
        n+=1    
    file.close()        


def repr_method_generator(nombreclase,ruta):
        
    file = open(f"{ruta}/{nombreclase}.py","a")
    cadena = ""
    comilla = "'"
    llave_a = "{"
    llave_b = "}"
    for atributo in atributos:
        if cadena == "":
           cadena = cadena + f"{llave_a}self.{atributo}{llave_b}" 
        else:
            cadena = cadena + f":{llave_a}self.{atributo}{llave_b}"
    
    file.write("\n    def __repr__(self):")
    file.write(f"\n       return f{comilla}{cadena}{comilla}  ")
    file.close()    
            

generador_archivo(nombreclase,ruta)
class_constructor(nombreclase,ruta,tabla)
getter_setter(nombreclase,ruta)
