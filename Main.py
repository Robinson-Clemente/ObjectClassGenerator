from ViewTest import *


if __name__ == '__main__':
    app = wx.App()
    frame = ViewTest(None,title='Object Class Generator For Python',size=(900,600))
    frame.Center()
    frame.Show()
    app.MainLoop()    

  