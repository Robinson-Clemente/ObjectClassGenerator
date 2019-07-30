import wx
import wx.lib.agw.ultimatelistctrl as ULC
from Validaciones import retornar
from Atributo import *
from Generadores import get_data

__autor__ = 'Robinson_Clemente'
string  = 'hola'



class ViewTest(wx.Frame):
    def __init__(self,*args,**kw):
        super(ViewTest,self).__init__(*args,**kw)

        panel = wx.Panel(self)
        self.path = '' 
        #This list contains allowed numbers or keycodes 
        lista = retornar()
        self.mensaje = ""
        # n is the variable that have the count of rows
        self.n=0
        #Metodos especiales
        lista_metodos = []
        checked_list = []
        

#---------------------------------------- SECCIÓN MÉTODO --------------------------------------------------
        #Este es el metodo que se debe ejecutar para mostrar el buscador de carpeta
        def selector(event):
            self.path
            dlg.ShowModal()
            self.path = dlg.GetPath()
            self.ruta.SetLabel(self.path)
            panel.Update()

        def programMessage(): 
            wx.MessageBox(self.mensaje, caption='Mensaje del Programa',
                style= wx.OK|wx.CENTRE|wx.ICON_INFORMATION)    
    
        def validador_letras(event):
            keycode = event.GetKeyCode()            
                 
            if keycode in lista:
               event.Skip()

        def validador_atributo(event):            
            if self.tcNombreAtributo.GetValue() =='':
               self.mensaje = 'Llene la casilla de nombre de atributo, por favor'              
               programMessage()
            else:
                add_attribute()

        def add_attribute():            
            nombre = self.tcNombreAtributo.GetValue()
            tipo = self.cbTipo.GetStringSelection()

            #We create a row                
            self.item = ULC.CreateListItem(self.n,2)
            fonte = wx.Font()
            self.item.SetFont(fonte)
            self.item.SetKind(1) 
            self.item._format = ULC.ULC_FORMAT_LEFT
            self.tabla2.InsertItem(self.item)
            
            self.item2 = ULC.CreateListItem(self.n,3)            
            self.item2.SetFont(fonte)
            self.item2.SetKind(1) 
            self.item2._format = ULC.ULC_FORMAT_LEFT
            self.tabla2.SetItem(self.item2)

            self.tabla2.SetStringItem(self.n,0,nombre)
            self.tabla2.SetStringItem(self.n,1,tipo)
                        
                           
            self.n=self.n+1 
                   
        def lectorTabla():
            attribute_list = []
            limite = self.tabla2.GetItemCount()

            for x in range(0,limite,1):
                col1 = self.tabla2.GetItem(x,col=0).GetText()
                col2 = self.tabla2.GetItem(x,col=1).GetText()
                col3 = self.tabla2.GetItem(x,col=2).IsChecked()
                col4 = self.tabla2.GetItem(x,col=1).IsChecked()
                atributo = Atributo(col1,col2,col3,col4)
                attribute_list.append(atributo)
                
            

    
    

       


           
            

#---------------------------------------- SECCIÓN METODO--------------------------------------------------

#---------------------------------------- SECCIÓN CREACIÓN --------------------------------------------------
       
        
        #Creamos la tabla
        self.tabla2 = wx.lib.agw.ultimatelistctrl.UltimateListCtrl(panel,pos=(150,240),size=(600,300),agwStyle=ULC.ULC_REPORT)
        self.tabla2.InsertColumn(0,'Attribute Name',format=ULC.ULC_FORMAT_LEFT,width=150)
        self.tabla2.InsertColumn(1,'Type',format=ULC.ULC_FORMAT_LEFT,width=150)
        self.tabla2.InsertColumn(2,'Set Method',format=ULC.ULC_FORMAT_LEFT,width=150)
        self.tabla2.InsertColumn(3,'Get Method',format=ULC.ULC_FORMAT_LEFT,width=150)

       
       
       
       
        #Creamos el modal para seleccionar la carpeta destino
        dlg = wx.DirDialog(panel, message='Selecione la carpeta destino', defaultPath="/home/inspiron",
        style=wx.DD_DIR_MUST_EXIST, pos=(400,300), size=(200,100),name='Seleccione la carpeta')
        
        self.boton = wx.Button(panel,label='Seleccionar ruta',size=(120,30),pos=(80,100))
        self.ruta = wx.StaticText(panel,label=self.path,pos=(220,106),size=(680,30))

        self.stnombre = wx.StaticText(panel,label='Nombre de la Clase',pos=(80,50),size=(200,30))
        self.tcNombreClase = wx.TextCtrl(panel,pos=(220,45),size=(120,26))
        self.stAdvertencia = wx.StaticText(panel,label='(Sin Extensión)',pos=(345,50),size=(150,80))
        
        #Creamos un checkbox para el primer metodo especial repr
        self.sttitulo2 = wx.StaticText(panel,label='Metodos Especiales',pos=(10,240),size=(80,80))
        self.reprcheckbox = wx.CheckBox(panel,label='repr',pos=(10,300))
        lista_metodos.append(self.reprcheckbox)

        self.stTitulo3 = wx.StaticText(panel,label='Agregue atributos :',pos=(80,160),size=(200,30))

        self.stTitulo4 = wx.StaticText(panel,label='Nombre Atributo',pos=(220,160),size=(200,30))
        self.tcNombreAtributo = wx.TextCtrl(panel,pos=(350,160),size=(140,22))

        self.stTitulo5 = wx.StaticText(panel,label='Tipo del Atributo',pos=(220,200),size=(200,30))
        self.cbTipo= wx.ComboBox(panel,pos=(350,200),value='str',size=(120,30),
        choices=['str','int','bool','long','float'],style=wx.CB_READONLY)

        self.btAddAtributte = wx.Button(panel,label='Agregar Atributo',size=(120,30),pos=(500,190))

#---------------------------------------- SECCIÓN CREACIÓN --------------------------------------------------

 


#---------------------------------------- SECCIÓN BIND --------------------------------------------------

        self.boton.Bind(wx.EVT_BUTTON, selector)
        self.tcNombreClase.Bind(wx.EVT_CHAR, validador_letras)
        self.tcNombreAtributo.Bind(wx.EVT_CHAR, validador_letras)
        self.btAddAtributte.Bind(wx.EVT_BUTTON, validador_atributo)

#---------------------------------------- SECCIÓN BIND --------------------------------------------------           


    def mostrar_mensaje(self):
        print("Se importó este código")
     
        


        

       