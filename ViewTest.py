import wx
import wx.lib.agw.ultimatelistctrl as ULC
from Validaciones import retornar
from Atributo import Atributo
from Generadores import recibir
from Generadores import ejecutar

__autor__ = 'Robinson_Clemente'
string  = 'hola'

#Revisar si al generar un atributo(Property) con solo un setter genera error al usar la clase

class ViewTest(wx.Frame):
    def __init__(self,*args,**kw):
        super(ViewTest,self).__init__(*args,**kw)

        panel = wx.Panel(self)         
        #This list contains allowed numbers or keycodes 
        lista = retornar()
        self.mensaje = ""
        self.path = ""
        # n is the variable that have the count of rows
        self.n=0
        #Metodos especiales
        checked_boxes = []
        
      
#---------------------------------------- SECCIÓN MÉTODO --------------------------------------------------
        #Este es el metodo que se debe ejecutar para mostrar el buscador de carpeta
        def selector(event):            
            dlg.ShowModal()
            self.path = dlg.GetPath()        
            

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
            limite = self.tabla2.GetItemCount()
            validador = False

            for x in range(0,limite,1):
                if nombre==self.tabla2.GetItem(x,col=0).GetText():
                   self.mensaje = 'Por favor digite un atributo no repetido'
                   programMessage()
                   validador = True
                   break

            if validador==False:
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

               self.tcNombreAtributo.SetValue('')


        def read_checkboxes():
            if self.reprcheckbox.IsChecked():
               checked_boxes.append(True)
            else:
                pass     
                   
        def lectorTabla():
            attribute_list = []
            limite = self.tabla2.GetItemCount()
            nombreclase = self.tcNombreClase.GetValue()
            ruta = self.path
                        
            for x in range(0,limite,1):
                col1 = self.tabla2.GetItem(x,col=0).GetText()
                col2 = self.tabla2.GetItem(x,col=1).GetText()
                col3 = self.tabla2.GetItem(x,col=2).IsChecked()
                col4 = self.tabla2.GetItem(x,col=3).IsChecked()
                atributo = Atributo(col1,col2,col3,col4)
                attribute_list.append(atributo)
            read_checkboxes()
            recibir(nombreclase,ruta,checked_boxes,attribute_list)
               
        def mostrarRuta(event):            
            wx.MessageBox(self.path,caption='Path seleccionado',
                style= wx.OK|wx.CENTRE|wx.ICON_INFORMATION) 

        def generar_clase(event):
            if self.tcNombreClase.GetValue()=='' or self.tcNombreClase.GetValue()==None:
                self.mensaje = 'Por favor digite el nombre de la clase'
                programMessage()
            elif self.path =='':
                 self.mensaje = 'Por favor selecciona la ruta de la clase a generar'
                 programMessage()    
            elif self.tabla2.GetItemCount()==0:
                 self.mensaje = 'Por favor agregue almenos 1 atributo'
                 programMessage()
            else:  
                 lectorTabla()
                 ejecutar()            
                 self.mensaje = 'Clase generada con exito'
                 programMessage()


        def eliminarAtributo(event):
            item =  self.tabla2.GetFirstSelected()            
            self.tabla2.DeleteItem(item)
            self.n = self.n - 1
            self.tabla2.Update()
            

#---------------------------------------- SECCIÓN METODO--------------------------------------------------

#---------------------------------------- SECCIÓN CREACIÓN --------------------------------------------------
        #Creamos lineas utilizando paneles
        self.line1 = wx.StaticBox(panel,label='',pos=(1,350),size=(900,3))
        self.line1.SetBackgroundColour((8,8,8))

        self.line2 = wx.StaticBox(panel,label='',pos=(450,353),size=(3,150))
        self.line2.SetBackgroundColour((8,8,8))      
        
      
       

        #Creamos la tabla
        self.tabla2 = wx.lib.agw.ultimatelistctrl.UltimateListCtrl(panel,pos=(150,40),size=(600,300),agwStyle=ULC.ULC_REPORT)
        self.tabla2.InsertColumn(0,'Attribute Name',format=ULC.ULC_FORMAT_LEFT,width=150)
        self.tabla2.InsertColumn(1,'Type',format=ULC.ULC_FORMAT_LEFT,width=150)
        self.tabla2.InsertColumn(2,'Get Method',format=ULC.ULC_FORMAT_LEFT,width=150)
        self.tabla2.InsertColumn(3,'Set Method',format=ULC.ULC_FORMAT_LEFT,width=150)


       
        self.stTitulo = wx.StaticText(panel,label=('Lista de Atributos'),pos=(400,10),size=(200,30))
        font1 = wx.Font(12,wx.DECORATIVE,wx.ITALIC,wx.BOLD)
        self.stTitulo.SetFont(font1)
       
       
        #Creamos el modal para seleccionar la carpeta destino
        dlg = wx.DirDialog(panel, message='Selecione la carpeta destino', defaultPath="/home/inspiron",
        style=wx.DD_DIR_MUST_EXIST, pos=(400,300), size=(200,100),name='Seleccione la carpeta')
        
        self.boton = wx.Button(panel,label='Seleccionar ruta',size=(120,30),pos=(10,435))       
        self.btnRuta = wx.Button(panel,label='Ver Ruta',pos=(150,435),size=(120,30))

        self.stnombre = wx.StaticText(panel,label='Nombre de la Clase',pos=(10,393),size=(200,30))
        self.tcNombreClase = wx.TextCtrl(panel,pos=(150,390),size=(120,30))
        self.stAdvertencia = wx.StaticText(panel,label='(Sin Extensión)',pos=(275,395),size=(150,80))
        
        #Creamos un checkbox para el primer metodo especial repr
        self.sttitulo2 = wx.StaticText(panel,label='Metodos \nEspeciales',pos=(12,40),size=(80,80))
        self.sttitulo2.SetFont(font1)
        self.reprcheckbox = wx.CheckBox(panel,label='repr',pos=(10,80))
        

        self.stTitulo4 = wx.StaticText(panel,label='Nombre Atributo',pos=(460,393),size=(200,30))
        self.tcNombreAtributo = wx.TextCtrl(panel,pos=(585,388),size=(140,30))

        self.stTitulo5 = wx.StaticText(panel,label='Tipo del Atributo',pos=(460,435),size=(200,30))
        self.cbTipo= wx.ComboBox(panel,pos=(585,430),value='str',size=(140,32),
        choices=['str','int','bool','long','float'],style=wx.CB_READONLY)

        self.btAddAtributte = wx.Button(panel,label='Agregar Atributo',size=(120,30),pos=(750,410))

        self.stTitulo6 = wx.StaticText(panel,label='Nombre y Ruta de la Clase',pos=(140,355),size=(200,30))
        self.stTitulo6.SetFont(font1)

        self.stTitulo6 = wx.StaticText(panel,label='Atributos',pos=(650,355),size=(200,30))
        self.stTitulo6.SetFont(font1)

        self.btnGenerar = wx.Button(panel,label='Generar Clase',size=(140,50),pos=(381,505))

        self.botonEliminar = wx.Button(panel,label='Eliminar Atributo',size=(120,30),pos=(760,42))
      
#---------------------------------------- SECCIÓN CREACIÓN --------------------------------------------------

 


#---------------------------------------- SECCIÓN BIND --------------------------------------------------

        self.boton.Bind(wx.EVT_BUTTON, selector)
        self.tcNombreClase.Bind(wx.EVT_CHAR, validador_letras)
        self.tcNombreAtributo.Bind(wx.EVT_CHAR, validador_letras)
        self.btAddAtributte.Bind(wx.EVT_BUTTON, validador_atributo)
        self.btnRuta.Bind(wx.EVT_BUTTON, mostrarRuta)
        self.btnGenerar.Bind(wx.EVT_BUTTON, generar_clase)
        self.botonEliminar.Bind(wx.EVT_BUTTON, eliminarAtributo)

#---------------------------------------- SECCIÓN BIND --------------------------------------------------           



        

       