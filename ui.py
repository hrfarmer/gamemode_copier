import wx
import os
import re
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
        self.SetTitle('Gamemode Copier')
        self.Centre()

    def OnQuit(self, e):
        self.Close()
    
    def OnButton(self, e):
        self.path = self.path.GetValue()
        self.skin_list = s.get_skins(self.path)

        # Makes dropdown appear
        self.text = wx.StaticText(self.panel, label = "Choose the skin you will copy from", pos = (5, 35))
        self.combo = wx.ComboBox(self.panel, choices = self.skin_list, pos=(5, 55))
        self.text2 = wx.StaticText(self.panel, label = "Choose the skin you will copy to", pos = (5, 80))
        self.combo2 = wx.ComboBox(self.panel, choices = self.skin_list, pos=(5, 100))
        self.submit = wx.Button(self.panel, label = "Submit", pos = (5, 135))
        self.submit.Bind(wx.EVT_BUTTON, self.OnSubmit)
    
    def OnSubmit(self, e):
        source_skin = self.combo.GetValue()
        dest_skin = self.combo2.GetValue()
        source_path = f"{self.path}\\Skins\\{source_skin}"
        destination_path = f"{self.path}\\Skins\\{dest_skin}"
        s.copy_files(source_path, destination_path)
        

class Skin():

    def get_skins(self, path):
        skins = []
        skin_folder = path + "\\Skins"
        for folder in os.listdir(skin_folder):
            skins.append(folder)
        return skins
    
    def copy_files(self, source_path, destination_path):
        for file in os.listdir(source_path):
            if file in taiko_elements:
                s_path = f"{source_path}\\{file}"
                in_file = open(s_path, "rb")
                data = in_file.read()

                d_path = f"{destination_path}\\{file}"
                with open(d_path, "wb") as out:
                    out.write(data)
                print(f"Copied {file}")

s = Skin()

def main():

    app = wx.App()
    w = Window(None)
    w.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
