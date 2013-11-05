import wx
def load(event):
    file=open(text_filename.GetValue())
    text_filecontent.SetValue(file.read())
    file.close()

def save(event):
    file=open(text_filename.GetValue(),'w')
    file.write(text_filecontent.GetValue())
    file.close

app=wx.App()
win=wx.Frame(None,title="python GUI",size=(500,400))

pnl_bkg=wx.Panel(win)

btn_load=wx.Button(pnl_bkg,label='Open',pos=(300,5),size=(50,30))
btn_load.Bind(wx.EVT_BUTTON,load)
btn_save=wx.Button(pnl_bkg,label='Save',pos=(400,5),size=(50,30))
btn_save.Bind(wx.EVT_BUTTON,save)
text_filename=wx.TextCtrl(pnl_bkg, pos=(5,10),size=(280,20))
text_filecontent=wx.TextCtrl(pnl_bkg,pos=(5,40),size=(475,300),
                             style=wx.TE_MULTILINE|wx.HSCROLL)

hbox=wx.BoxSizer()
hbox.Add(text_filename,proportion=1,flag=wx.EXPAND)
hbox.Add(btn_load,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(btn_save,proportion=0,flag=wx.RIGHT,border=5)

vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
vbox.Add(text_filecontent,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)

pnl_bkg.SetSizer(vbox)
win.Show()
app.MainLoop()

