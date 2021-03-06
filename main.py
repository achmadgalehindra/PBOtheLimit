import wx
import restuku
import sqlite3

#bismillah
class cekDB:
    def __init__(self):
        self.conn = sqlite3.connect('restuku.db')
        self.cursor = self.conn.cursor()

    def run(self, query, returnData = False):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.conn.commit()
        if returnData :
            return result

class Main(cekDB, restuku.MyFrame1):
    def __init__(self, parent):
        restuku.MyFrame1.__init__(self, parent)
        self.DM = cekDB()
#objek dibuat maka tombol disesuaikan dengan kondisi
    def button_login( self, event ):
        username = self.m_textCtrl1.GetValue()
        password = self.m_textCtrl2.GetValue()
        self.query = "SELECT * FROM admin where username = '{}' and password = '{}'".format(username, password)
        hasil = self.DM.run(self.query, returnData = True)

        if hasil is not None and len(hasil) > 0 :
            event = Main3(None)
            event.Show()
            self.Destroy()
            self.DM.conn.close()
            return username
        else:
            wx.MessageBox('Wrong Username or Password')


    def klik_daftar( self, event ):
        event = Main2(None)
        event.Show()
        self.Destroy()

class Main2(Main, restuku.MyFrame2):
    def __init__(self, parent):
        restuku.MyFrame2.__init__(self, parent)
        self.DM = cekDB()
        
    def button_daftar( self, event):
        username = self.m_textCtrl3.GetValue()
        nama = self.m_textCtrl4.GetValue()
        email = self.m_textCtrl6.GetValue()
        password = self.m_textCtrl7.GetValue()

        if username != "" and nama != "" and email != "" and password != "":
            self.query = 'INSERT INTO admin (username, nama, email, password) VALUES (\'%s\', \'%s\', \'%s\', \'%s\')'
            self.query= self.query % (username, nama, email, password)
            self.DM.run(self.query)
            event = Main(None)
            wx.MessageBox('Register Successfully')
            event.Show()
            self.Destroy()
            self.DM.conn.close()
        else:
            wx.MessageBox('No empty data')

    def klik_login( self, event ):
        event = Main(None)
        event.Show()
        self.Destroy()

class Main3(Main2, restuku.MyFrame3):
     def __init__(self, parent):
         restuku.MyFrame3.__init__(self, parent)
         self.tabelkeberuntungan.SetColLabelValue(0, "Kode Menu")
         self.tabelkeberuntungan.SetColLabelValue(1, "Nama Menu")
         self.tabelkeberuntungan.SetColLabelValue(2, "Jenis Menu")
         self.tabelkeberuntungan.SetColLabelValue(3, "Harga Menu")
         self.DM = cekDB()
         self.m = Main(self)
         self.tabelcuy()
        
     def tabelcuy(self):    
         self.query = 'SELECT * FROM pilihanMenu'
         hasil = self.DM.run(self.query, returnData=True)
         for a in hasil:
             self.tabelkeberuntungan.AppendRows(1)
         for b in range (4):
             a = 0
             for row in hasil:
                 self.tabelkeberuntungan.SetCellValue(a, b, str(row[b]))
                 a = a + 1

     def button_edit( self, event ):
        event = Main5(None)
        event.Show() 
        self.Destroy()
        self.DM.conn.close()

     def refresh( self, event ):
         event = Main3(None)
         event.Show()
         self.Destroy()


     def button_tambah( self, event ):
         event = Main4(None)
         event.Show()
        
     def button_keluar( self, event ):
         self.DM.conn.close()
         event = Main(None)
         event.Show()
         self.Destroy()

     def button_pesan( self, event ):
         event = Main6(None)
         event.Show()
         self.Destroy()

class Main4(Main3, restuku.MyFrame4):
     def __init__(self, parent):
         restuku.MyFrame4.__init__(self, parent)
         self.DM = cekDB()

     def button_batal( self, event ):
         self.Destroy()
        
     def button_simpan( self, event):
         kode = self.m_textCtrl3.GetValue()
         namaMenu = self.m_textCtrl4.GetValue()
         jenisMenu = self.m_textCtrl6.GetValue()
         hargaMenu = self.m_textCtrl7.GetValue()

         if kode != "" and namaMenu != "" and jenisMenu != "" and hargaMenu != "":
             self.query = 'INSERT INTO pilihanMenu (kodeMenu, namaMenu, jenisMenu, hargaMenu) VALUES (\'%s\', \'%s\', \'%s\', \'%s\')'
             self.query = self.query % (kode, namaMenu, jenisMenu, hargaMenu)
             self.DM.run(self.query)
             wx.MessageBox('Successfully')
             self.Destroy()
             self.DM.conn.close()
         else :
             wx.MessageBox('No empty data')

class Main5(Main2, restuku.MyFrame5):
    def __init__(self, parent):
         restuku.MyFrame5.__init__(self, parent)
         self.tabelkeberuntungan.SetColLabelValue(0, "Kode Menu")
         self.tabelkeberuntungan.SetColLabelValue(1, "Nama Menu")
         self.tabelkeberuntungan.SetColLabelValue(2, "Jenis Menu")
         self.tabelkeberuntungan.SetColLabelValue(3, "Harga Menu")
         self.DM = cekDB()
         self.m = Main(self)
         self.tabelcuy()
        
    def tabelcuy(self):    
         self.query = 'SELECT * FROM pilihanMenu'
         hasil = self.DM.run(self.query, returnData=True)
         for a in hasil:
             self.tabelkeberuntungan.AppendRows(1)
         for b in range (4):
             a = 0
             for row in hasil:
                 self.tabelkeberuntungan.SetCellValue(a, b, str(row[b]))
                 a = a + 1

    def tabelkeberuntunganOnGridCmdSelectCell( self, event ):
        row = event.GetRow()
        self.TabelIsi(row) 

    def TabelIsi(self, row):
        kode = self.tabelkeberuntungan.GetCellValue(row, 0)
        namaMenu = self.tabelkeberuntungan.GetCellValue(row, 1)
        jenisMenu = self.tabelkeberuntungan.GetCellValue(row, 2)
        hargaMenu = self.tabelkeberuntungan.GetCellValue(row, 3)

        self.m_textCtrl3.SetValue(kode)
        self.m_textCtrl4.SetValue(namaMenu)
        self.m_textCtrl6.SetValue(jenisMenu)
        self.m_textCtrl7.SetValue(hargaMenu)
                 
    def button_simpanEdit(self, event):
        kodeMenu = self.m_textCtrl3.GetValue()
        namaMenu = self.m_textCtrl4.GetValue()
        jenisMenu = self.m_textCtrl6.GetValue()
        hargaMenu = self.m_textCtrl7.GetValue()

        self.query = "UPDATE pilihanMenu set namaMenu = \'%s\', jenisMenu = \'%s\', hargaMenu = \'%s\' WHERE kodeMenu = \'%s\'"
        self.query = self.query % (namaMenu, jenisMenu, hargaMenu, kodeMenu)
        self.DM.run(self.query)
        if kodeMenu != "":
            wx.MessageBox('Successfully')
            self.button_Refresh2(event)
        else :
            wx.MessageBox('Failed')

    def button_hapus( self, event ):
         kodeMenu = self.m_textCtrl3.GetValue()
         self.query = "DELETE From pilihanMenu WHERE kodeMenu = \'%s\'"
         self.query = self.query % (kodeMenu)
         self.DM.run(self.query)
         if kodeMenu != "":
             wx.MessageBox('Successfully Deleted')
             self.button_Refresh2(event)
         else :
             wx.MessageBox('Failed')

    def button_kembali( self, event ):
         event = Main3(None)
         event.Show()
         self.Destroy()
         self.DM.conn.close()

    def button_Refresh2( self, event ):
         event = Main5(None)
         event.Show()
         self.Destroy()

class Main6(Main3, restuku.MyFrame6):
    def __init__(self, parent):
         restuku.MyFrame6.__init__(self, parent)
         self.tabelkeberuntungan.SetColLabelValue(0, "Kode Menu")
         self.tabelkeberuntungan.SetColLabelValue(1, "Nama Menu")
         self.tabelkeberuntungan.SetColLabelValue(2, "Jenis Menu")
         self.tabelkeberuntungan.SetColLabelValue(3, "Harga Menu")
         self.DM = cekDB()
         self.m = Main(self)
         self.tabelcuy()
        
    def tabelcuy(self):    
         self.query = 'SELECT * FROM pilihanMenu'
         hasil = self.DM.run(self.query, returnData=True)
         for a in hasil:
             self.tabelkeberuntungan.AppendRows(1)
         for b in range (4):
             a = 0
             for row in hasil:
                 self.tabelkeberuntungan.SetCellValue(a, b, str(row[b]))
                 a = a + 1

    def tabelkeberuntunganOnGridCmdSelectCell( self, event ):
        row = event.GetRow()
        self.TabelIsi(row) 

    def TabelIsi(self, row):
        kode = self.tabelkeberuntungan.GetCellValue(row, 0)
        namaMenu = self.tabelkeberuntungan.GetCellValue(row, 1)
        jenisMenu = self.tabelkeberuntungan.GetCellValue(row, 2)
        totalBiaya = self.tabelkeberuntungan.GetCellValue(row, 3)

        self.m_textCtrl31.SetValue(kode)
        self.m_textCtrl45.SetValue(namaMenu)
        self.m_textCtrl61.SetValue(jenisMenu)
        self.m_textCtrl7.SetValue(totalBiaya)
                 
    def button_tambah( self, event ):
        nama = self.m_textCtrl3.GetValue()
        tanggal = self.m_datePicker1.GetValue()
        noMeja = self.m_textCtrl6.GetValue()
        kodeMenu = self.m_textCtrl31.GetValue()
        namaMenu = self.m_textCtrl45.GetValue()
        jenisMenu = self.m_textCtrl61.GetValue()
        totalBiaya = self.m_textCtrl7.GetValue()

        if nama != "" and tanggal != "" and noMeja != "" and kodeMenu != "" and namaMenu != "" and jenisMenu != "" and totalBiaya != "":
             self.query = 'INSERT INTO pemesanan (nama, tanggal, noMeja, kodeMenu, namaMenu, jenisMenu, totalBiaya) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')'
             self.query = self.query % (nama, tanggal, noMeja, kodeMenu, namaMenu, jenisMenu, totalBiaya)
             self.DM.run(self.query)
             wx.MessageBox('Successfully')
        else :
             wx.MessageBox('No empty data')


    def button_hapus( self, event ):
         event = Main3(None)
         event.Show()
         self.Destroy()
         self.DM.conn.close()

    def button_Refresh2( self, event ):
         event = Main6(None)
         event.Show()
         self.Destroy()
 
    def klik_rincian(self, event):
        event = Main7(None)
        event.Show()
        self.Destroy()

    def button_simpanEdit(self, event):
        event = Main8(None)
        event.Show()
        self.Destroy()

class Main7(Main2, restuku.MyFrame7):
     def __init__(self, parent):
         restuku.MyFrame7.__init__(self, parent)
         self.tabelkeberuntungan.SetColLabelValue(0, "id")
         self.tabelkeberuntungan.SetColLabelValue(1, "Nama Pelanggan")
         self.tabelkeberuntungan.SetColLabelValue(2, "Tanggal Pesan")
         self.tabelkeberuntungan.SetColLabelValue(3, "No Meja")
         self.tabelkeberuntungan.SetColLabelValue(4, "Nama Menu")
         self.tabelkeberuntungan.SetColLabelValue(5, "Jenis Menu")
         self.tabelkeberuntungan.SetColLabelValue(6, "Harga Menu")
         self.DM = cekDB()
         self.m = Main(self)
         self.tabelcuy()
        
     def tabelcuy(self):    
         self.query = 'SELECT * FROM pemesanan'
         hasil = self.DM.run(self.query, returnData=True)
         for a in hasil:
             self.tabelkeberuntungan.AppendRows(1)
         for b in range (7):
             a = 0
             for row in hasil:
                 self.tabelkeberuntungan.SetCellValue(a, b, str(row[b]))
                 a = a + 1

     def refresh( self, event ):
         event = Main7(None)
         event.Show()
         self.Destroy()
        
     def button_keluar( self, event ):
         event = Main6(None)
         event.Show()
         self.Destroy()
         self.DM.conn.close()

class Main8(Main2, restuku.MyFrame8):
     def __init__(self, parent):
         restuku.MyFrame8.__init__(self, parent)
         self.tabelkeberuntungan.SetColLabelValue(0, "id")
         self.tabelkeberuntungan.SetColLabelValue(1, "Nama Pelanggan")
         self.tabelkeberuntungan.SetColLabelValue(2, "Tanggal Pesan")
         self.tabelkeberuntungan.SetColLabelValue(3, "No Meja")
         self.tabelkeberuntungan.SetColLabelValue(4, "Kode Menu")
         self.tabelkeberuntungan.SetColLabelValue(5, "Nama Menu")
         self.tabelkeberuntungan.SetColLabelValue(6, "Jenis Menu")
         self.tabelkeberuntungan.SetColLabelValue(7, "Harga Menu")
         self.DM = cekDB()
         self.m = Main(self)
         self.tabelcuy()
        
     def tabelcuy(self):    
         self.query = 'SELECT * FROM pemesanan'
         hasil = self.DM.run(self.query, returnData=True)
         for a in hasil:
             self.tabelkeberuntungan.AppendRows(1)
         for b in range (8):
             a = 0
             for row in hasil:
                 self.tabelkeberuntungan.SetCellValue(a, b, str(row[b]))
                 a = a + 1

     def tabelkeberuntunganOnGridCmdSelectCell( self, event ):
        row = event.GetRow()
        self.TabelIsi(row) 

     def TabelIsi(self, row):
        namaPelanggan = self.tabelkeberuntungan.GetCellValue(row, 1)

        self.m_staticText3711.SetLabelText(namaPelanggan)

    #  def total(self):
    #     self.query = 'SELECT SUM totalBiaya FROM pemesanan'
    #     namaPelanggan = self.DM.run(self.query, returnData=True)

    #     self.m_staticText481.SetLabelText(namaPelanggan)

     def refresh( self, event ):
         event = Main7(None)
         event.Show()
         self.Destroy()
        
     def button_keluar( self, event ):
         event = Main6(None)
         event.Show()
         self.Destroy()
         self.DM.conn.close()

run = wx.App()
frame = Main(parent=None)
frame.Show()
run.MainLoop()
