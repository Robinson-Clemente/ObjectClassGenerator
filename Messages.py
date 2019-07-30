import wx

def programMessage(): 
    mensaje = 'El archivo ya existe, eliminelo o cambie de ruta o cambie de posición el archivo'
    wx.MessageBox(mensaje, caption='Mensaje del Programa',
    style= wx.OK|wx.CENTRE|wx.ICON_INFORMATION)

      

