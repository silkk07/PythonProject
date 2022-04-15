########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
# INITIALIZE APP SETTINGS
settings = QSettings()
########################################################################



########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show() 

        ########################################################################
        # UPDATE APP SETTINGS LOADED FROM JSON STYLESHEET 
        # ITS IMPORTANT TO RUN THIS AFTER SHOWING THE WINDOW
        # THIS PROCESS WILL RUN ON A SEPARATE THREAD WHEN GENERATING NEW ICONS
        # TO PREVENT THE WINDOW FROM BEING UNRESPONSIVE
        ########################################################################
        # self = QMainWindow class
        QAppSettings.updateAppSettings(self)

        #######################################################################
        # CHECK THE CURRENT THEME SETTINGS
        #######################################################################
        settings = QSettings()
        # CURRENT ICONS 
        # CURRENT THEME NAME
        print("Current theme", settings.value("THEME"))
        print("Current Icons color", settings.value("ICONS-COLOR"))


        # CHANGE THE THEME NAME IN SETTINGS
        # Use one of the app themes from your JSON file
        # USE default dark or light theme
        settings.setValue("THEME", "LIGHT")

        # RE APPLY THE NEW SETINGS
        # CompileStyleSheet might also work
        # CompileStyleSheet.applyCompiledSass(self)
        QAppSettings.updateAppSettings(self)

        # READ ALL THEME NAMES CREATED FROM THE JSON FILE
        # NOTE THAT TWO THEMES (LIGHT AND DARK) WILL BE AUTOMATICALLY ADDED TO THE LIST
        # WHEN CREATING THEMES ON YOUR JSON FILE AVOID USING LIGHT OR DARK AS YOUR THEME NAME
        # for theme in self.ui.themes:
            #theme.name is the name of the theme
            #theme.backgroundColor is the theme bg color
            #theme.textColor is the theme text color
            #theme.accentColor is the theme accent color
            #theme.iconsColor is the theme icons color
            #theme.defaultTheme and theme.createNewIcons are bool values
            
            # print(theme.name)


        # Variables
        # print(self.theme.COLOR_BACKGROUND_1)






########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
