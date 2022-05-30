from distutils.file_util import copy_file
import wx
import os
import tkinter as tk
from tkinter import filedialog
from elements import taiko_elements
from elements import standard_elements
from elements import mania_elements
from elements import ctb_elements

class Window(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.InitUI()
    
    def InitUI(self):

        self.panel = wx.Panel(self)
        self.foldermessage = wx.StaticText(self.panel, label = "Input the path of your osu! folder:")
        self.path = wx.TextCtrl(self.panel, size = (400, -1))
        self.button = wx.Button(self.panel, label="Submit")
        self.button2 = wx.Button(self.panel, label="Browse")
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)
        self.button2.Bind(wx.EVT_BUTTON, self.OnBrowse)

        # Set sizer for frame
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)

        # Set sizer for panel content
        self.sizer = wx.GridBagSizer(2, 2)
        self.sizer.Add(self.button, (0, 2), (0, 10), flag = wx.EXPAND)
        self.sizer.Add(self.foldermessage, (0, 0))
        self.sizer.Add(self.path, (1 ,0))
        self.sizer.Add(self.button2, (1, 2),  (0, 10), flag = wx.EXPAND)

        # Border
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)        

        # Use the sizers
        self.panel.SetSizerAndFit(self.border)
        self.SetSizerAndFit(self.windowSizer)

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        deleteFile = fileMenu.Append(wx.ID_DELETE, 'Delete log', 'Delete log')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)
        self.Bind(wx.EVT_MENU, s.delete_log(), deleteFile)

        self.SetSize((500, 117))
        self.SetTitle('Gamemode Copier')
        self.Centre()

    def OnQuit(self, e):
        self.Close()
    
    def OnButton(self, e):
        self.path = self.path.GetValue()
        if self.path:
            self.skin_list = s.get_skins(self.path)

        # Makes dropdown appear
        self.text = wx.StaticText(self.panel, label = "Choose the skin you will copy from", pos = (5, 57))
        self.combo = wx.ComboBox(self.panel, choices = self.skin_list, pos=(5, 77))
        self.text2 = wx.StaticText(self.panel, label = "Choose the skin you will copy to", pos = (5, 102))
        self.combo2 = wx.ComboBox(self.panel, choices = self.skin_list, pos=(5, 122))
        self.submit = wx.Button(self.panel, label = "Submit", pos = (430, 100))
        self.standard = wx.CheckBox(self.panel, -1, 'Standard', pos = (315, 74))
        self.taiko = wx.CheckBox(self.panel, -1, 'Taiko', pos = (315, 94))
        self.mania = wx.CheckBox(self.panel, -1, 'Mania', pos = (315, 114))
        self.ctb = wx.CheckBox(self.panel, -1, 'Catch the Beat', pos = (315, 134))
        self.submit.Bind(wx.EVT_BUTTON, self.OnSubmit)
        self.SetSize((500, 218))
    
    def OnSubmit(self, e):
        source_skin = self.combo.GetValue()
        dest_skin = self.combo2.GetValue()
        source_path = f"{self.path}\\Skins\\{source_skin}"
        destination_path = f"{self.path}\\Skins\\{dest_skin}"
        standard_value = self.standard.GetValue()
        taiko_value = self.taiko.GetValue()
        mania_value = self.mania.GetValue()
        ctb_value = self.ctb.GetValue()
        s.determine_copy(source_path, destination_path, standard_value, taiko_value, ctb_value, mania_value)
    
    def OnBrowse(self, e):
        folder_path = filedialog.askdirectory()
        self.path.SetValue(folder_path)
        self.OnButton(e)
        

class Skin():

    def get_skins(self, path):
        skins = []
        skin_folder = path + "\\Skins"
        for folder in os.listdir(skin_folder):
            skins.append(folder)
        return skins
    def determine_copy(self, source_path, destination_path, standard_value, taiko_value, ctb_value, mania_value):
        if standard_value:
            self.copy_files(source_path, destination_path, standard_elements)
            standard_value = False
        if taiko_value:
            self.copy_files(source_path, destination_path, taiko_elements)
            taiko_value = False
        if ctb_value:
            self.copy_files(source_path, destination_path, ctb_elements)
            ctb_value = False
        if mania_value:
            self.copy_files(source_path, destination_path, mania_elements)
            mania_value = False


    def copy_files(self, source_path, destination_path, elements):
        self.delete_log()
        for file in os.listdir(source_path):
            for element in elements:
                file = file.replace(".png", "").strip()
                element = element.replace(".png", "").strip()
                if file.startswith(element):
                    file = file + ".png"
                    s_path = f"{source_path}\\{file}"
                    in_file = open(s_path, "rb")
                    data = in_file.read()

                    d_path = f"{destination_path}\\{file}"
                    with open(d_path, "wb") as out:
                        out.write(data)
                    print(f"Copied {file}")
                    with open('log.txt', 'a') as f:
                        f.write(f"\n{file} and {element} match!")
                else:
                    with open('log.txt', 'a') as f:
                        f.write(f"\n{file} and {element} dont match!")
                    continue
    
    def delete_log(self):
        if os.path.exists("log.txt"):
            os.remove("log.txt")

s = Skin()

root = tk.Tk()
root.withdraw()

def main():

    app = wx.App()
    w = Window(None)
    w.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
