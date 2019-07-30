from Atributo import *  
from Messages import programMessage

nombreclase = ""
ruta = ""
checkedlist = []
#Data list contains objects of Atributo class
data =[]

def recibir(nombre,rut,checkboxes,attribute):
    global nombreclase
    global ruta
    global checkedlist
    global data    
    nombreclase = nombre
    ruta = rut
    checkedlist =checkboxes
    data = attribute



def openFile_a():
    file = open(f"{ruta}/{nombreclase}.py","a")
    return file


def generador_archivo():    
    try:
        file = open(f"{ruta}/{nombreclase}.py","x")
        file.close()
    except Exception:
         programMessage()
    


def class_constructor():
    file = openFile_a()
    file.write(f"\nclass {nombreclase}(): ")
    file.write("\n")
    
    string = listar_variables_horizontal()
    file.write(f"\n    def __init__(self{string}):")
    file.close()
    listar_variables_vertical()

    file.close()
        

def listar_variables_horizontal():    
    cadena = ""  

    for atributo in data:
        cadena = cadena+f",{atributo.nombre}"

    return cadena

def listar_variables_vertical():

    file = openFile_a()

    #Por ahora por defecto hago los atributos 'privados' debido a que si
    #Vas a crear una clase con get and set los atributos deben ser privados(get-set)
    for atributo in data:
        file.write(f"\n        self.__{atributo.nombre} = {atributo.nombre}")

    file.close()        


def getter_setter():
    comilla = "'"
    
    file = openFile_a()
    file.write("\n")
    file.write("\n")   

    #Getter Methods   
    for atributo in data:
        if atributo.get:
           file.write("\n    @property")
           file.write(f"\n    def {atributo.nombre}(self):")
           file.write(f"\n        return self.__{atributo.nombre}")
           file.write("\n") 
                
    #Setter Methods
    for atributo in data:
        if atributo.sett:
           file.write(f"\n    @{atributo.nombre}.setter")        
           file.write(f"\n    def {atributo.nombre}(self,{atributo.nombre}):")
           file.write(f"\n        if isinstance({atributo.nombre},{atributo.tipo}):")    
           file.write(f"\n           self.__{atributo.nombre} = {atributo.nombre}")
           file.write(f"\n        else:")
           file.write(f"\n            raise TypeError({comilla}Tipo invalido para el atributo{comilla}) ")     
           file.write("\n") 

  
    file.close()        


def repr_method_generator():        
    file = openFile_a()
    cadena = ""
    comilla = "'"
    llave_a = "{"
    llave_b = "}"
    for atributo in data:
        if cadena == "":
           cadena = cadena + f"{llave_a}self.{atributo.nombre}{llave_b}" 
        else:
            cadena = cadena + f":{llave_a}self.{atributo.nombre}{llave_b}"
    
    file.write("\n    def __repr__(self):")
    file.write(f"\n       return f{comilla}{cadena}{comilla}  ")
    file.close()    

def lector_checkboxes():
    n=0
    for checked in checkedlist:
        if checked:
           if n==0:           
              repr_method_generator() 
        
        n=n+1


def ejecutar():
    generador_archivo()
    class_constructor()
    getter_setter()
    lector_checkboxes()
    
