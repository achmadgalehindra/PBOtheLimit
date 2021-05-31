import wx
import modul

#Sub class dengan menginherit MyFrame file modul

class View(modul.MyFrame1):  
    def __init__(self, parent):
        modul.MyFrame1.__init__(self, parent) #dict
        self.database = {"User":"admin"}

    def cek(self):
        self.nama = self.input_nama.GetValue()
        self.nim = self.input_nim.GetValue()

    def btn_registerOnButtonClick(self, event):
        self.cek()
        self.database[self.nama] = self.nim
        wx.MessageBox("Pendaftaran Berhasil")

    def btn_loginOnButtonClick(self, event):
        self.cek()
        try:
            if self.database[self.nama] == self.nim:
                wx.MessageBox("Login Berhasil")
            
                print(self.nama,'\n')
                print(self.nim,'\n')

                b = Pindah(parent=self)
                b.Show()
            else:
                wx.MessageBox("Login Gagal")
        except:
            wx.MessageBox("Login Gagal")
                

class Pindah(modul.MyFrame2):
    def __init__(self, parent):
        modul.MyFrame2.__init__(self, parent)

        self.isi_nama.SetLabelText(str(parent.nama))
        self.isi_nim.SetLabelText(str(parent.nim))

    def btn_ok(self,event):
        a = View(parent=self)
        a.Show()
        
app = wx.App()
frame = View(None)
frame.Show()
app.MainLoop()
