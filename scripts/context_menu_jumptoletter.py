import xbmc
import xbmcgui

home = xbmcgui.Window(10000)
skin = home.getProperty("CurrentSkin")
if skin == "skin.estuary.mod_v2":
    xbmc.executebuiltin("SetFocus(8000)")
else:
    pass 
