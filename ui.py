import wx
import os
from elements import taiko_elements

class Window(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.InitUI()
    
    def InitUI(self):

        self.panel = wx.Panel(self)
        self.result = wx.StaticText(self.panel, label = "")
        self.result.SetForegroundColour(wx.RED)
        self.path = wx.TextCtrl(self.panel, size = (400, -1))
        self.button = wx.Button(self.panel, label="Browse")
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)

        # Set sizer for frame
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)

        # Set sizer for panel content
        self.sizer = wx.GridBagSizer(2, 2)
        self.sizer.Add(self.button, (0, 2), (1, 2), flag = wx.EXPAND)
        self.sizer.Add(self.path, (0 ,0))

        # Border
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)        

        # Use the sizers
        self.panel.SetSizerAndFit(self.border)
        self.SetSizerAndFit(self.windowSizer)

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

        self.SetSize((600, 600))
        self.SetTitle('Simple menu')
        self.Centre()

    def OnQuit(self, e):
        self.Close()
    
    def OnButton(self, e):
        path = self.path.GetValue()
        skin_list = s.get_skins(path)

        # Makes dropdown appear
        self.combo = wx.ComboBox(self.panel, choices = skin_list)
        self.sizer2 = wx.GridBagSizer(2, 2)
        self.sizer2.Add(self.combo, (0, 5))
        self.border2 = wx.BoxSizer()
        self.border2.Add(self.sizer2, 2, wx.ALL | wx.EXPAND, 5)
        self.panel.SetSizerAndFit(self.border2)

class Skin():

    def get_skins(self, path):
        skins = []
        skin_folder = path + "\\Skins"
        for folder in os.listdir(skin_folder):
            skins.append(folder)
        return skins

s = Skin()

def main():

    app = wx.App()
    w = Window(None)
    w.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
