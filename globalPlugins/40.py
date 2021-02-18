import globalPluginHandler
from .win32api import *
import gui, wx
from threading import Thread
import time

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		self.shown = False
		self.first = False
		d = Thread(target=self.check)
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		d.start()

	def check(self):
		if not self.first:
			self.first = True
			gui.messageBox("This product requires authorization and will continue to run in 40 minute mode until an authorization key has been purchased. The best way to update authorization for this product is to open your bank, and let the money pore out.", "activation")
		while True:
			time.sleep(1)
			cur = win32api.GetTickCount()
			if cur > 1800000 and not self.shown and cur < 1801002:
				self.shown = True
				gui.messageBox("this product will stop working in 10 minutes and will require a reboot to continue.", "40 minute mode is about to expire:")
			self.shown = False
			if cur > 2160000 and cur < 2161002 and not self.shown:
				self.shown = True
				gui.messageBox("This product will stop working in 6 minutes and will require a reboot to continue.", "40 minute mode is about to expire.")
			self.shown = False
			if cur > 2220000 and not self.shown and cur < 2221002:
				self.shown=True
				gui.messageBox("This product will stop working in 3 minutes and will require a reboot to continue. Please save any unsaved work now.", "40 minute 	mode is about to expire.")
			self.shown = False
			if cur > 2340000 and not self.shown and cur < 2341002:
				self.shown = True
				gui.messageBox("This product will stop working in 1 minutes and will require a reboot to continue. Please save any unsaved work now.", "40 minute 	mode is about to expire.")
			self.shown = False
			if cur > 2400000 and not self.shown :
				self.shown = True
				gui.messageBox("This demo version has expired, it will now stop working. Please restart this computer now.", "40 minute mode has expired.")
				gui.messageBox("Gotcha", "April Fools.")
				self.close()
				return

	def close(self):
		wx.GetApp().ExitMainLoop()
