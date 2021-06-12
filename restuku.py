# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import wx.adv

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"==========================================", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Login Restuku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 28, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Carda Bold Italic" ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer1.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl1.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		self.m_textCtrl2.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )


		bSizer1.Add( fgSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.m_button4.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_button4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer3.Add( self.m_button4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		fgSizer4 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Don't have a account yet?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer4.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		fgSizer4.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer3.Add( fgSizer4, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( bSizer3, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"==========================================", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_staticText12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer1.Add( self.m_staticText12, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button4.Bind( wx.EVT_BUTTON, self.button_login )
		self.m_staticText7.Bind( wx.EVT_LEFT_UP, self.klik_daftar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def button_login( self, event ):
		event.Skip()

	def klik_daftar( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"REGISTRASI RESTUKU", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 28, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Carda" ) )
		self.m_staticText101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5.SetMinSize( wx.Size( -1,170 ) )
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl3.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Nama Lengkap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl4.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL )
		self.m_textCtrl6.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText15.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		self.m_textCtrl7.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl7, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Daftar", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer5.Add( self.m_button5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		fgSizer51 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer51.SetFlexibleDirection( wx.BOTH )
		fgSizer51.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Try another way?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText16.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer51.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		self.m_staticText17.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText17.SetForegroundColour( wx.Colour( 5, 109, 224 ) )

		fgSizer51.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer5.Add( fgSizer51, 1, wx.EXPAND, 5 )


		bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.button_daftar )
		self.m_staticText17.Bind( wx.EVT_LEFT_UP, self.klik_login )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def button_daftar( self, event ):
		event.Skip()

	def klik_login( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer102 = wx.BoxSizer( wx.VERTICAL )

		bSizer102.SetMinSize( wx.Size( -1,50 ) )
		self.m_staticText371 = wx.StaticText( self, wx.ID_ANY, u"Daftar Pilihan Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText371.Wrap( -1 )

		self.m_staticText371.SetFont( wx.Font( 22, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText371.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer102.Add( self.m_staticText371, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer7.Add( bSizer102, 0, wx.EXPAND, 5 )

		fgSizer7 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		bSizer7.Add( fgSizer7, 0, wx.ALL, 5 )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.m_panel6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.tabelkeberuntungan = wx.grid.Grid( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,320 ), 0 )

		# Grid
		self.tabelkeberuntungan.CreateGrid( 0, 10 )
		self.tabelkeberuntungan.EnableEditing( False )
		self.tabelkeberuntungan.EnableGridLines( True )
		self.tabelkeberuntungan.EnableDragGridSize( False )
		self.tabelkeberuntungan.SetMargins( 0, 35 )

		# Columns
		self.tabelkeberuntungan.SetColSize( 0, 80 )
		self.tabelkeberuntungan.SetColSize( 1, 241 )
		self.tabelkeberuntungan.SetColSize( 2, 159 )
		self.tabelkeberuntungan.SetColSize( 3, 159 )
		self.tabelkeberuntungan.SetColSize( 4, 100 )
		self.tabelkeberuntungan.SetColSize( 5, 80 )
		self.tabelkeberuntungan.SetColSize( 6, 112 )
		self.tabelkeberuntungan.SetColSize( 7, 80 )
		self.tabelkeberuntungan.SetColSize( 8, 80 )
		self.tabelkeberuntungan.EnableDragColMove( False )
		self.tabelkeberuntungan.EnableDragColSize( True )
		self.tabelkeberuntungan.SetColLabelSize( 30 )
		self.tabelkeberuntungan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelkeberuntungan.AutoSizeRows()
		self.tabelkeberuntungan.EnableDragRowSize( False )
		self.tabelkeberuntungan.SetRowLabelSize( 80 )
		self.tabelkeberuntungan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelkeberuntungan.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.tabelkeberuntungan.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer10.Add( self.tabelkeberuntungan, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer9 = wx.FlexGridSizer( 0, 8, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button9 = wx.Button( self.m_panel6, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.Size( 110,45 ), 0 )
		self.m_button9.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_button9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		fgSizer9.Add( self.m_button9, 0, wx.ALL, 5 )

		self.m_button92 = wx.Button( self.m_panel6, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.Size( 110,45 ), 0 )
		self.m_button92.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button92.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_button92.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		fgSizer9.Add( self.m_button92, 0, wx.ALL, 5 )

		self.m_button91 = wx.Button( self.m_panel6, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.Size( 110,45 ), 0 )
		self.m_button91.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button91.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_button91.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		fgSizer9.Add( self.m_button91, 0, wx.ALL, 5 )

		self.m_staticText48 = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )

		fgSizer9.Add( self.m_staticText48, 0, wx.ALL, 5 )

		self.m_staticText49 = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		fgSizer9.Add( self.m_staticText49, 0, wx.ALL, 5 )

		self.m_staticText52 = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		fgSizer9.Add( self.m_staticText52, 0, wx.ALL, 5 )

		self.m_button51 = wx.Button( self.m_panel6, wx.ID_ANY, u"Pesan", wx.DefaultPosition, wx.Size( 110,45 ), 0 )
		self.m_button51.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_button51.SetBackgroundColour( wx.Colour( 0, 215, 129 ) )

		fgSizer9.Add( self.m_button51, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self.m_panel6, wx.ID_ANY, u"Keluar", wx.DefaultPosition, wx.Size( 110,45 ), 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_button5.SetBackgroundColour( wx.Colour( 215, 0, 0 ) )

		fgSizer9.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer10.Add( fgSizer9, 0, wx.EXPAND, 5 )


		gbSizer1.Add( bSizer10, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


		self.m_panel6.SetSizer( gbSizer1 )
		self.m_panel6.Layout()
		gbSizer1.Fit( self.m_panel6 )
		bSizer7.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tabelkeberuntungan.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.tabelkeberuntunganOnGridCmdSelectCell )
		self.m_button9.Bind( wx.EVT_BUTTON, self.button_tambah )
		self.m_button92.Bind( wx.EVT_BUTTON, self.button_edit )
		self.m_button91.Bind( wx.EVT_BUTTON, self.refresh )
		self.m_button51.Bind( wx.EVT_BUTTON, self.button_pesan )
		self.m_button5.Bind( wx.EVT_BUTTON, self.button_keluar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tabelkeberuntunganOnGridCmdSelectCell( self, event ):
		event.Skip()

	def button_tambah( self, event ):
		event.Skip()

	def button_edit( self, event ):
		event.Skip()

	def refresh( self, event ):
		event.Skip()

	def button_pesan( self, event ):
		event.Skip()

	def button_keluar( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"TAMBAH MENU BARU", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5.SetMinSize( wx.Size( -1,170 ) )
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Kode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl3.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Nama Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl4.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Jenis Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL )
		self.m_textCtrl6.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Harga Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText15.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl7.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl7, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer5.Add( self.m_button5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		fgSizer51 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer51.SetFlexibleDirection( wx.BOTH )
		fgSizer51.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Try another way?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText16.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer51.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.m_button51.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button51.SetBackgroundColour( wx.Colour( 191, 23, 23 ) )

		fgSizer51.Add( self.m_button51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer5.Add( fgSizer51, 1, wx.EXPAND, 5 )


		bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.button_simpan )
		self.m_button51.Bind( wx.EVT_BUTTON, self.button_batal )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def button_simpan( self, event ):
		event.Skip()

	def button_batal( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame5
###########################################################################

class MyFrame5 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"==================================================", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText1011 = wx.StaticText( self, wx.ID_ANY, u"UBAH MENU", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1011.Wrap( -1 )

		self.m_staticText1011.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText1011.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText1011, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.tabelkeberuntungan = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 375,200 ), 0 )

		# Grid
		self.tabelkeberuntungan.CreateGrid( 0, 10 )
		self.tabelkeberuntungan.EnableEditing( False )
		self.tabelkeberuntungan.EnableGridLines( True )
		self.tabelkeberuntungan.EnableDragGridSize( False )
		self.tabelkeberuntungan.SetMargins( 0, 35 )

		# Columns
		self.tabelkeberuntungan.SetColSize( 0, 80 )
		self.tabelkeberuntungan.SetColSize( 1, 241 )
		self.tabelkeberuntungan.SetColSize( 2, 159 )
		self.tabelkeberuntungan.SetColSize( 3, 159 )
		self.tabelkeberuntungan.SetColSize( 4, 100 )
		self.tabelkeberuntungan.SetColSize( 5, 80 )
		self.tabelkeberuntungan.SetColSize( 6, 112 )
		self.tabelkeberuntungan.SetColSize( 7, 80 )
		self.tabelkeberuntungan.SetColSize( 8, 80 )
		self.tabelkeberuntungan.EnableDragColMove( False )
		self.tabelkeberuntungan.EnableDragColSize( True )
		self.tabelkeberuntungan.SetColLabelSize( 30 )
		self.tabelkeberuntungan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelkeberuntungan.AutoSizeRows()
		self.tabelkeberuntungan.EnableDragRowSize( False )
		self.tabelkeberuntungan.SetRowLabelSize( 80 )
		self.tabelkeberuntungan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelkeberuntungan.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.tabelkeberuntungan.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer12.Add( self.tabelkeberuntungan, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		fgSizer11 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer11.SetMinSize( wx.Size( -1,-200 ) )
		self.m_toggleBtn1 = wx.ToggleButton( self, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.Size( 130,50 ), 0 )
		self.m_toggleBtn1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_toggleBtn1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_toggleBtn1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		fgSizer11.Add( self.m_toggleBtn1, 0, wx.ALL, 5 )

		self.m_toggleBtn11 = wx.ToggleButton( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( 130,50 ), 0 )
		self.m_toggleBtn11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_toggleBtn11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_toggleBtn11.SetBackgroundColour( wx.Colour( 255, 106, 106 ) )

		fgSizer11.Add( self.m_toggleBtn11, 0, wx.ALL, 5 )


		bSizer12.Add( fgSizer11, 1, wx.EXPAND, 5 )


		gbSizer2.Add( bSizer12, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5.SetMinSize( wx.Size( -1,200 ) )
		self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, u"Kode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		self.m_staticText111.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText111.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText111, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl3.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Nama Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl4.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Jenis Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL )
		self.m_textCtrl6.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Harga Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText15.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl7.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

		self.m_staticText151 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )

		self.m_staticText151.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText151.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText151, 0, wx.ALL, 5 )


		bSizer13.Add( fgSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_button5.SetMinSize( wx.Size( 130,50 ) )

		fgSizer12.Add( self.m_button5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.Size( 130,50 ), 0 )
		self.m_button51.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button51.SetBackgroundColour( wx.Colour( 191, 23, 23 ) )

		fgSizer12.Add( self.m_button51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer13.Add( fgSizer12, 1, wx.EXPAND, 5 )


		gbSizer2.Add( bSizer13, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


		bSizer4.Add( gbSizer2, 1, wx.EXPAND, 5 )

		self.m_staticText1012 = wx.StaticText( self, wx.ID_ANY, u"==================================================", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1012.Wrap( -1 )

		self.m_staticText1012.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText1012.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText1012, 0, wx.ALL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tabelkeberuntungan.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.tabelkeberuntunganOnGridCmdSelectCell )
		self.m_toggleBtn1.Bind( wx.EVT_TOGGLEBUTTON, self.button_Refresh2 )
		self.m_toggleBtn11.Bind( wx.EVT_TOGGLEBUTTON, self.button_kembali )
		self.m_button5.Bind( wx.EVT_BUTTON, self.button_simpanEdit )
		self.m_button51.Bind( wx.EVT_BUTTON, self.button_hapus )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tabelkeberuntunganOnGridCmdSelectCell( self, event ):
		event.Skip()

	def button_Refresh2( self, event ):
		event.Skip()

	def button_kembali( self, event ):
		event.Skip()

	def button_simpanEdit( self, event ):
		event.Skip()

	def button_hapus( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame6
###########################################################################

class MyFrame6 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"==================================================", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText1011 = wx.StaticText( self, wx.ID_ANY, u"PESAN MENU", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1011.Wrap( -1 )

		self.m_staticText1011.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText1011.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText1011, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.tabelkeberuntungan = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 375,200 ), 0 )

		# Grid
		self.tabelkeberuntungan.CreateGrid( 0, 10 )
		self.tabelkeberuntungan.EnableEditing( False )
		self.tabelkeberuntungan.EnableGridLines( True )
		self.tabelkeberuntungan.EnableDragGridSize( False )
		self.tabelkeberuntungan.SetMargins( 0, 35 )

		# Columns
		self.tabelkeberuntungan.SetColSize( 0, 80 )
		self.tabelkeberuntungan.SetColSize( 1, 241 )
		self.tabelkeberuntungan.SetColSize( 2, 159 )
		self.tabelkeberuntungan.SetColSize( 3, 159 )
		self.tabelkeberuntungan.SetColSize( 4, 100 )
		self.tabelkeberuntungan.SetColSize( 5, 80 )
		self.tabelkeberuntungan.SetColSize( 6, 112 )
		self.tabelkeberuntungan.SetColSize( 7, 80 )
		self.tabelkeberuntungan.SetColSize( 8, 80 )
		self.tabelkeberuntungan.EnableDragColMove( False )
		self.tabelkeberuntungan.EnableDragColSize( True )
		self.tabelkeberuntungan.SetColLabelSize( 30 )
		self.tabelkeberuntungan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelkeberuntungan.AutoSizeRows()
		self.tabelkeberuntungan.EnableDragRowSize( False )
		self.tabelkeberuntungan.SetRowLabelSize( 80 )
		self.tabelkeberuntungan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelkeberuntungan.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.tabelkeberuntungan.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer12.Add( self.tabelkeberuntungan, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		fgSizer11 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer11.SetMinSize( wx.Size( -1,-200 ) )
		self.m_toggleBtn1 = wx.ToggleButton( self, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.Size( 130,50 ), 0 )
		self.m_toggleBtn1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_toggleBtn1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_toggleBtn1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		fgSizer11.Add( self.m_toggleBtn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer12.Add( fgSizer11, 1, wx.EXPAND, 5 )


		gbSizer2.Add( bSizer12, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5.SetMinSize( wx.Size( -1,200 ) )
		self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		self.m_staticText111.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText111.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText111, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl3.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Tanggal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_datePicker1 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 150,-1 ), wx.adv.DP_DROPDOWN )
		fgSizer5.Add( self.m_datePicker1, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"No Meja", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl6.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Harga Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText15.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl7.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer5.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

		self.m_staticText151 = wx.StaticText( self, wx.ID_ANY, u"Rincian", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )

		self.m_staticText151.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText151.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		fgSizer5.Add( self.m_staticText151, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_toggleBtn9 = wx.ToggleButton( self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.m_toggleBtn9.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_toggleBtn9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer5.Add( self.m_toggleBtn9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer13.Add( fgSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Selsai", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_button5.SetMinSize( wx.Size( 130,50 ) )

		fgSizer12.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_toggleBtn11 = wx.ToggleButton( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( 130,50 ), 0 )
		self.m_toggleBtn11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_toggleBtn11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_toggleBtn11.SetBackgroundColour( wx.Colour( 255, 106, 106 ) )

		fgSizer12.Add( self.m_toggleBtn11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )


		bSizer13.Add( fgSizer12, 1, wx.EXPAND, 5 )


		gbSizer2.Add( bSizer13, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		bSizer131 = wx.BoxSizer( wx.VERTICAL )

		fgSizer51 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer51.SetFlexibleDirection( wx.BOTH )
		fgSizer51.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer51.SetMinSize( wx.Size( -1,200 ) )
		self.m_staticText1111 = wx.StaticText( self, wx.ID_ANY, u"                  .asdasd", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1111.Wrap( -1 )

		self.m_staticText1111.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText1111.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer51.Add( self.m_staticText1111, 0, wx.ALL, 5 )

		self.m_textCtrl31 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl31.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer51.Add( self.m_textCtrl31, 0, wx.ALL, 5 )

		self.m_staticText121 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )

		self.m_staticText121.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText121.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer51.Add( self.m_staticText121, 0, wx.ALL, 5 )

		self.m_textCtrl45 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer51.Add( self.m_textCtrl45, 0, wx.ALL, 5 )

		self.m_staticText141 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )

		self.m_staticText141.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText141.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer51.Add( self.m_staticText141, 0, wx.ALL, 5 )

		self.m_textCtrl61 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL )
		self.m_textCtrl61.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer51.Add( self.m_textCtrl61, 0, wx.ALL, 5 )

		self.m_staticText152 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText152.Wrap( -1 )

		self.m_staticText152.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText152.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer51.Add( self.m_staticText152, 0, wx.ALL, 5 )


		bSizer131.Add( fgSizer51, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		gbSizer2.Add( bSizer131, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


		bSizer4.Add( gbSizer2, 1, wx.EXPAND, 5 )

		self.m_staticText1012 = wx.StaticText( self, wx.ID_ANY, u"==================================================", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1012.Wrap( -1 )

		self.m_staticText1012.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText1012.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.m_staticText1012, 0, wx.ALL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tabelkeberuntungan.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.tabelkeberuntunganOnGridCmdSelectCell )
		self.m_toggleBtn1.Bind( wx.EVT_TOGGLEBUTTON, self.button_Refresh2 )
		self.m_staticText151.Bind( wx.EVT_LEFT_UP, self.klik_rincian )
		self.m_toggleBtn9.Bind( wx.EVT_TOGGLEBUTTON, self.button_tambah )
		self.m_button5.Bind( wx.EVT_BUTTON, self.button_simpanEdit )
		self.m_toggleBtn11.Bind( wx.EVT_TOGGLEBUTTON, self.button_hapus )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tabelkeberuntunganOnGridCmdSelectCell( self, event ):
		event.Skip()

	def button_Refresh2( self, event ):
		event.Skip()

	def klik_rincian( self, event ):
		event.Skip()

	def button_tambah( self, event ):
		event.Skip()

	def button_simpanEdit( self, event ):
		event.Skip()

	def button_hapus( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame7
###########################################################################

class MyFrame7 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer102 = wx.BoxSizer( wx.VERTICAL )

		bSizer102.SetMinSize( wx.Size( -1,50 ) )
		self.m_staticText371 = wx.StaticText( self, wx.ID_ANY, u"Rincian Seluruh Pemesanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText371.Wrap( -1 )

		self.m_staticText371.SetFont( wx.Font( 22, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText371.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer102.Add( self.m_staticText371, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer7.Add( bSizer102, 0, wx.EXPAND, 5 )

		fgSizer7 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		bSizer7.Add( fgSizer7, 0, wx.ALL, 5 )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.m_panel6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.tabelkeberuntungan = wx.grid.Grid( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,320 ), 0 )

		# Grid
		self.tabelkeberuntungan.CreateGrid( 0, 10 )
		self.tabelkeberuntungan.EnableEditing( False )
		self.tabelkeberuntungan.EnableGridLines( True )
		self.tabelkeberuntungan.EnableDragGridSize( False )
		self.tabelkeberuntungan.SetMargins( 0, 35 )

		# Columns
		self.tabelkeberuntungan.SetColSize( 0, 80 )
		self.tabelkeberuntungan.SetColSize( 1, 241 )
		self.tabelkeberuntungan.SetColSize( 2, 159 )
		self.tabelkeberuntungan.SetColSize( 3, 159 )
		self.tabelkeberuntungan.SetColSize( 4, 100 )
		self.tabelkeberuntungan.SetColSize( 5, 80 )
		self.tabelkeberuntungan.SetColSize( 6, 112 )
		self.tabelkeberuntungan.SetColSize( 7, 80 )
		self.tabelkeberuntungan.SetColSize( 8, 80 )
		self.tabelkeberuntungan.EnableDragColMove( False )
		self.tabelkeberuntungan.EnableDragColSize( True )
		self.tabelkeberuntungan.SetColLabelSize( 30 )
		self.tabelkeberuntungan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelkeberuntungan.AutoSizeRows()
		self.tabelkeberuntungan.EnableDragRowSize( False )
		self.tabelkeberuntungan.SetRowLabelSize( 80 )
		self.tabelkeberuntungan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelkeberuntungan.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.tabelkeberuntungan.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer10.Add( self.tabelkeberuntungan, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer9 = wx.FlexGridSizer( 0, 8, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button91 = wx.Button( self.m_panel6, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.Size( 110,45 ), 0 )
		self.m_button91.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button91.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_button91.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		fgSizer9.Add( self.m_button91, 0, wx.ALL, 5 )

		self.m_staticText48 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"                ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )

		fgSizer9.Add( self.m_staticText48, 0, wx.ALL, 5 )

		self.m_staticText49 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"                      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		fgSizer9.Add( self.m_staticText49, 0, wx.ALL, 5 )

		self.m_staticText491 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"                        ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText491.Wrap( -1 )

		fgSizer9.Add( self.m_staticText491, 0, wx.ALL, 5 )

		self.m_staticText521 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"                    ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText521.Wrap( -1 )

		fgSizer9.Add( self.m_staticText521, 0, wx.ALL, 5 )

		self.m_staticText52 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"                     ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		fgSizer9.Add( self.m_staticText52, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self.m_panel6, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( 110,45 ), 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_button5.SetBackgroundColour( wx.Colour( 215, 0, 0 ) )

		fgSizer9.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer10.Add( fgSizer9, 0, wx.EXPAND, 5 )


		gbSizer1.Add( bSizer10, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


		self.m_panel6.SetSizer( gbSizer1 )
		self.m_panel6.Layout()
		gbSizer1.Fit( self.m_panel6 )
		bSizer7.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tabelkeberuntungan.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.tabelkeberuntunganOnGridCmdSelectCell )
		self.m_button91.Bind( wx.EVT_BUTTON, self.refresh )
		self.m_button5.Bind( wx.EVT_BUTTON, self.button_keluar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tabelkeberuntunganOnGridCmdSelectCell( self, event ):
		event.Skip()

	def refresh( self, event ):
		event.Skip()

	def button_keluar( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame8
###########################################################################

class MyFrame8 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 10, 190, 154 ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer102 = wx.BoxSizer( wx.VERTICAL )

		bSizer102.SetMinSize( wx.Size( -1,50 ) )
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText371 = wx.StaticText( self, wx.ID_ANY, u"Pesanan Kak :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText371.Wrap( -1 )

		self.m_staticText371.SetFont( wx.Font( 22, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText371.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		gSizer1.Add( self.m_staticText371, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticText3711 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3711.Wrap( -1 )

		self.m_staticText3711.SetFont( wx.Font( 22, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText3711.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		gSizer1.Add( self.m_staticText3711, 0, wx.ALL, 5 )


		bSizer102.Add( gSizer1, 1, wx.EXPAND, 5 )


		bSizer7.Add( bSizer102, 0, wx.EXPAND, 5 )

		fgSizer7 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		bSizer7.Add( fgSizer7, 0, wx.ALL, 5 )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.m_panel6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.tabelkeberuntungan = wx.grid.Grid( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,320 ), 0 )

		# Grid
		self.tabelkeberuntungan.CreateGrid( 0, 10 )
		self.tabelkeberuntungan.EnableEditing( False )
		self.tabelkeberuntungan.EnableGridLines( True )
		self.tabelkeberuntungan.EnableDragGridSize( False )
		self.tabelkeberuntungan.SetMargins( 0, 35 )

		# Columns
		self.tabelkeberuntungan.SetColSize( 0, 80 )
		self.tabelkeberuntungan.SetColSize( 1, 241 )
		self.tabelkeberuntungan.SetColSize( 2, 159 )
		self.tabelkeberuntungan.SetColSize( 3, 159 )
		self.tabelkeberuntungan.SetColSize( 4, 100 )
		self.tabelkeberuntungan.SetColSize( 5, 80 )
		self.tabelkeberuntungan.SetColSize( 6, 112 )
		self.tabelkeberuntungan.SetColSize( 7, 80 )
		self.tabelkeberuntungan.SetColSize( 8, 80 )
		self.tabelkeberuntungan.EnableDragColMove( False )
		self.tabelkeberuntungan.EnableDragColSize( True )
		self.tabelkeberuntungan.SetColLabelSize( 30 )
		self.tabelkeberuntungan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelkeberuntungan.AutoSizeRows()
		self.tabelkeberuntungan.EnableDragRowSize( False )
		self.tabelkeberuntungan.SetRowLabelSize( 80 )
		self.tabelkeberuntungan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelkeberuntungan.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.tabelkeberuntungan.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer10.Add( self.tabelkeberuntungan, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer9 = wx.FlexGridSizer( 0, 8, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button5 = wx.Button( self.m_panel6, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( 110,45 ), 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_button5.SetBackgroundColour( wx.Colour( 215, 0, 0 ) )

		fgSizer9.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText49 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"                      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		fgSizer9.Add( self.m_staticText49, 0, wx.ALL, 5 )

		self.m_staticText491 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"                 ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText491.Wrap( -1 )

		fgSizer9.Add( self.m_staticText491, 0, wx.ALL, 5 )

		self.m_staticText521 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"               ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText521.Wrap( -1 )

		fgSizer9.Add( self.m_staticText521, 0, wx.ALL, 5 )

		self.m_staticText5211 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"               ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5211.Wrap( -1 )

		fgSizer9.Add( self.m_staticText5211, 0, wx.ALL, 5 )

		self.m_staticText48 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Total :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )

		self.m_staticText48.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText48.SetForegroundColour( wx.Colour( 10, 190, 154 ) )

		fgSizer9.Add( self.m_staticText48, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText481 = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText481.Wrap( -1 )

		self.m_staticText481.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tekton Pro Ext" ) )
		self.m_staticText481.SetForegroundColour( wx.Colour( 10, 190, 154 ) )

		fgSizer9.Add( self.m_staticText481, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText52 = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		fgSizer9.Add( self.m_staticText52, 0, wx.ALL, 5 )


		bSizer10.Add( fgSizer9, 0, wx.EXPAND, 5 )


		gbSizer1.Add( bSizer10, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


		self.m_panel6.SetSizer( gbSizer1 )
		self.m_panel6.Layout()
		gbSizer1.Fit( self.m_panel6 )
		bSizer7.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tabelkeberuntungan.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.tabelkeberuntunganOnGridCmdSelectCell )
		self.m_button5.Bind( wx.EVT_BUTTON, self.button_keluar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tabelkeberuntunganOnGridCmdSelectCell( self, event ):
		event.Skip()

	def button_keluar( self, event ):
		event.Skip()


