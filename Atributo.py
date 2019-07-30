
class Atributo(): 

    def __init__(self,nombre,tipo,get,sett):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__get = get
        self.__sett = sett


    @property
    def nombre(self):
        return self.__nombre

    @property
    def tipo(self):
        return self.__tipo

    @property
    def get(self):
        return self.__get

    @property
    def sett(self):
        return self.__sett

    @nombre.setter
    def nombre(self,nombre):
        if isinstance(nombre,str):
           self.__nombre = nombre
        else:
            raise TypeError('Tipo invalido para el atributo') 

    @tipo.setter
    def tipo(self,tipo):
        if isinstance(tipo,str):
           self.__tipo = tipo
        else:
            raise TypeError('Tipo invalido para el atributo') 

    @get.setter
    def get(self,get):
        if isinstance(get,bool):
           self.__get = get
        else:
            raise TypeError('Tipo invalido para el atributo') 

    @sett.setter
    def sett(self,sett):
        if isinstance(sett,bool):
           self.__sett = sett
        else:
            raise TypeError('Tipo invalido para el atributo') 


