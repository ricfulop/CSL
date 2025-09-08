---
url: https://wiki.freecad.org/Dialog_creation_with_various_widgets
title: Dialog creation with various widgets
scraped_at: 2025-09-08 16:46:44
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Method 1
  * 3 Method 2

# Dialog creation with various widgets

  * [Page](/Dialog_creation_with_various_widgets "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Dialog_creation_with_various_widgets&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Dialog_creation_with_various_widgets)
  * [Edit](/index.php?title=Dialog_creation_with_various_widgets&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Dialog_creation_with_various_widgets&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Dialog_creation_with_various_widgets.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Dialog_creation_with_various_widgets&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Dialog_creation_with_various_widgets)
  * [Edit](/index.php?title=Dialog_creation_with_various_widgets&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Dialog_creation_with_various_widgets&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Dialog_creation_with_various_widgets&action=history)

General

  * [What links here](/Special:WhatLinksHere/Dialog_creation_with_various_widgets "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Dialog_creation_with_various_widgets "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Dialog_creation_with_various_widgets&oldid=1536428 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Dialog_creation_with_various_widgets&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Dialog_creation_with_various_widgets&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Dialog+creation+with+various+widgets&action=page&filter=&language=en)This is
the approved revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Dialog+creation+with+various+widgets&language=&task=view "Start translation for this language")
  * [Deutsch](/Dialog_creation_with_various_widgets/de "Dialogerstellung mit verschiedenen Widgets \(100% translated\)")
  * English
  * [français](/Dialog_creation_with_various_widgets/fr "Création d'une fenêtre de dialogues avec différents widgets \(100% translated\)")
  * [italiano](/Dialog_creation_with_various_widgets/it "Creare una finestra di dialogo con diversi widget \(14% translated\)")
  * [polski](/Dialog_creation_with_various_widgets/pl "Tworzenie dialogów z różnymi widżetami \(100% translated\)")

## Introduction

This is an example of [dialog creation](/Dialog_creation "Dialog creation")
with [PySide](/PySide "PySide").

In this example, the entire interface is defined in [Python](/Python
"Python"). Although this is possible for small interfaces, for larger
interfaces the recommendation is to create .ui files through Qt Designer, and
load these in the program.

## Method 1

An example of a dialog box complete with its connections.

    
    
    # -*- coding: utf-8 -*-
    # Create by flachyjoe
    
    from PySide import QtCore, QtGui
    
    try:
        _fromUtf8 = QtCore.QString.fromUtf8
    except AttributeError:
        def _fromUtf8(s):
            return s
    
    try:
        _encoding = QtGui.QApplication.UnicodeUTF8
        def _translate(context, text, disambig):
            return QtGui.QApplication.translate(context, text, disambig, _encoding)
    except AttributeError:
        def _translate(context, text, disambig):
            return QtGui.QApplication.translate(context, text, disambig)
    
    
    class Ui_MainWindow(object):
    
         def __init__(self, MainWindow):
            self.window = MainWindow
    
            MainWindow.setObjectName(_fromUtf8("MainWindow"))
            MainWindow.resize(400, 300)
            self.centralWidget = QtGui.QWidget(MainWindow)
            self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
    
            self.pushButton = QtGui.QPushButton(self.centralWidget)
            self.pushButton.setGeometry(QtCore.QRect(30, 170, 93, 28))
            self.pushButton.setObjectName(_fromUtf8("pushButton"))
            self.pushButton.clicked.connect(self.on_pushButton_clicked) #connection pushButton
    
            self.lineEdit = QtGui.QLineEdit(self.centralWidget)
            self.lineEdit.setGeometry(QtCore.QRect(30, 40, 211, 22))
            self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
            self.lineEdit.returnPressed.connect(self.on_lineEdit_clicked) #connection lineEdit
    
            self.checkBox = QtGui.QCheckBox(self.centralWidget)
            self.checkBox.setGeometry(QtCore.QRect(30, 90, 81, 20))
            self.checkBox.setChecked(True)
            self.checkBox.setObjectName(_fromUtf8("checkBoxON"))
            self.checkBox.clicked.connect(self.on_checkBox_clicked) #connection checkBox
    
            self.radioButton = QtGui.QRadioButton(self.centralWidget)
            self.radioButton.setGeometry(QtCore.QRect(30, 130, 95, 20))
            self.radioButton.setObjectName(_fromUtf8("radioButton"))
            self.radioButton.clicked.connect(self.on_radioButton_clicked) #connection radioButton
    
            MainWindow.setCentralWidget(self.centralWidget)
    
            self.menuBar = QtGui.QMenuBar(MainWindow)
            self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 26))
            self.menuBar.setObjectName(_fromUtf8("menuBar"))
            MainWindow.setMenuBar(self.menuBar)
    
            self.mainToolBar = QtGui.QToolBar(MainWindow)
            self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
            MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
    
            self.statusBar = QtGui.QStatusBar(MainWindow)
            self.statusBar.setObjectName(_fromUtf8("statusBar"))
            MainWindow.setStatusBar(self.statusBar)
    
            self.retranslateUi(MainWindow)
    
         def retranslateUi(self, MainWindow):
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
            self.pushButton.setText(_translate("MainWindow", "OK", None))
            self.lineEdit.setText(_translate("MainWindow", "tyty", None))
            self.checkBox.setText(_translate("MainWindow", "CheckBox", None))
            self.radioButton.setText(_translate("MainWindow", "RadioButton", None))
    
         def on_checkBox_clicked(self):
            if self.checkBox.checkState()==0:
                App.Console.PrintMessage(str(self.checkBox.checkState())+"  CheckBox KO\r\n")
            else:     
                App.Console.PrintMessage(str(self.checkBox.checkState())+" CheckBox OK\r\n")
    #        App.Console.PrintMessage(str(self.lineEdit.setText("tititi"))+" LineEdit\r\n") #write text to the lineEdit window !
    #        str(self.lineEdit.setText("tititi")) #écrit le texte dans la fenêtre lineEdit
            App.Console.PrintMessage(str(self.lineEdit.displayText())+" LineEdit\r\n")
    
         def on_radioButton_clicked(self):
            if self.radioButton.isChecked():
                 App.Console.PrintMessage(str(self.radioButton.isChecked())+" Radio OK\r\n")
            else:
                 App.Console.PrintMessage(str(self.radioButton.isChecked())+"  Radio KO\r\n")
    
         def on_lineEdit_clicked(self):
    #        if self.lineEdit.textChanged():
                 App.Console.PrintMessage(str(self.lineEdit.displayText())+" LineEdit Display\r\n")
    
         def on_pushButton_clicked(self):
            App.Console.PrintMessage("Terminé\r\n")
            self.window.hide()
    
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    

Here the same window but with an icon on each button.

Download associated icons (click right "Copy the image below ...)"

[![](/images/e/e8/Icone01.png)](/index.php?title=File:Icone01.png&filetimestamp=20150729163936&)
[![](/images/c/c1/Icone02.png)](/index.php?title=File:Icone02.png&filetimestamp=20150729170240&)
[![](/images/6/65/Icone03.png)](/index.php?title=File:Icone03.png&filetimestamp=20150729164122&)

    
    
    # -*- coding: utf-8 -*-
    
    from PySide import QtCore, QtGui
    
    try:
        _fromUtf8 = QtCore.QString.fromUtf8
    except AttributeError:
        def _fromUtf8(s):
            return s
    
    try:
        _encoding = QtGui.QApplication.UnicodeUTF8
        def _translate(context, text, disambig):
            return QtGui.QApplication.translate(context, text, disambig, _encoding)
    except AttributeError:
        def _translate(context, text, disambig):
            return QtGui.QApplication.translate(context, text, disambig)
    
    
    class Ui_MainWindow(object):
    
         def __init__(self, MainWindow):
            self.window = MainWindow
            path = FreeCAD.ConfigGet("UserAppData")
    #        path = FreeCAD.ConfigGet("AppHomePath")
    
            MainWindow.setObjectName(_fromUtf8("MainWindow"))
            MainWindow.resize(400, 300)
            self.centralWidget = QtGui.QWidget(MainWindow)
            self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
    
            self.pushButton = QtGui.QPushButton(self.centralWidget)
            self.pushButton.setGeometry(QtCore.QRect(30, 170, 93, 28))
            self.pushButton.setObjectName(_fromUtf8("pushButton"))
            self.pushButton.clicked.connect(self.on_pushButton_clicked) #connection pushButton
    
            self.lineEdit = QtGui.QLineEdit(self.centralWidget)
            self.lineEdit.setGeometry(QtCore.QRect(30, 40, 211, 22))
            self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
            self.lineEdit.returnPressed.connect(self.on_lineEdit_clicked) #connection lineEdit
    
            self.checkBox = QtGui.QCheckBox(self.centralWidget)
            self.checkBox.setGeometry(QtCore.QRect(30, 90, 100, 20))
            self.checkBox.setChecked(True)
            self.checkBox.setObjectName(_fromUtf8("checkBoxON"))
            self.checkBox.clicked.connect(self.on_checkBox_clicked) #connection checkBox
    
            self.radioButton = QtGui.QRadioButton(self.centralWidget)
            self.radioButton.setGeometry(QtCore.QRect(30, 130, 95, 20))
            self.radioButton.setObjectName(_fromUtf8("radioButton"))
            self.radioButton.clicked.connect(self.on_radioButton_clicked) #connection radioButton
    
            MainWindow.setCentralWidget(self.centralWidget)
    
            self.menuBar = QtGui.QMenuBar(MainWindow)
            self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 26))
            self.menuBar.setObjectName(_fromUtf8("menuBar"))
            MainWindow.setMenuBar(self.menuBar)
    
            self.mainToolBar = QtGui.QToolBar(MainWindow)
            self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
            MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
    
            self.statusBar = QtGui.QStatusBar(MainWindow)
            self.statusBar.setObjectName(_fromUtf8("statusBar"))
            MainWindow.setStatusBar(self.statusBar)
    
            self.retranslateUi(MainWindow)
    
            # Affiche un icone sur le bouton PushButton
            # self.image_01 = "C:\Program Files\FreeCAD0.13\Icone01.png" # adapt the icon name
            self.image_01 = path+"Icone01.png" # adapt the name of the icon
            icon01 = QtGui.QIcon() 
            icon01.addPixmap(QtGui.QPixmap(self.image_01),QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton.setIcon(icon01) 
            self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft) # This command reverses the direction of the button
    
            # Affiche un icone sur le bouton RadioButton 
            # self.image_02 = "C:\Program Files\FreeCAD0.13\Icone02.png" # adapt the name of the icon
            self.image_02 = path+"Icone02.png" # adapter le nom de l'icone
            icon02 = QtGui.QIcon() 
            icon02.addPixmap(QtGui.QPixmap(self.image_02),QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.radioButton.setIcon(icon02) 
            # self.radioButton.setLayoutDirection(QtCore.Qt.RightToLeft) #  This command reverses the direction of the button
    
            # Affiche un icone sur le bouton CheckBox 
            # self.image_03 = "C:\Program Files\FreeCAD0.13\Icone03.png" # the name of the icon
            self.image_03 = path+"Icone03.png" # adapter le nom de l'icone
            icon03 = QtGui.QIcon() 
            icon03.addPixmap(QtGui.QPixmap(self.image_03),QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.checkBox.setIcon(icon03) 
            # self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft) # This command reverses the direction of the button
    
    
         def retranslateUi(self, MainWindow):
            MainWindow.setWindowTitle(_translate("MainWindow", "FreeCAD", None))
            self.pushButton.setText(_translate("MainWindow", "OK", None))
            self.lineEdit.setText(_translate("MainWindow", "tyty", None))
            self.checkBox.setText(_translate("MainWindow", "CheckBox", None))
            self.radioButton.setText(_translate("MainWindow", "RadioButton", None))
    
         def on_checkBox_clicked(self):
            if self.checkBox.checkState()==0:
                App.Console.PrintMessage(str(self.checkBox.checkState())+"  CheckBox KO\r\n")
            else:     
                App.Console.PrintMessage(str(self.checkBox.checkState())+" CheckBox OK\r\n")
               # App.Console.PrintMessage(str(self.lineEdit.setText("tititi"))+" LineEdit\r\n") # write text to the lineEdit window !
               # str(self.lineEdit.setText("tititi")) #écrit le texte dans la fenêtre lineEdit
            App.Console.PrintMessage(str(self.lineEdit.displayText())+" LineEdit\r\n")
    
         def on_radioButton_clicked(self):
            if self.radioButton.isChecked():
                 App.Console.PrintMessage(str(self.radioButton.isChecked())+" Radio OK\r\n")
            else:
                 App.Console.PrintMessage(str(self.radioButton.isChecked())+"  Radio KO\r\n")
    
         def on_lineEdit_clicked(self):
              # if self.lineEdit.textChanged():
              App.Console.PrintMessage(str(self.lineEdit.displayText())+" LineEdit Display\r\n")
    
         def on_pushButton_clicked(self):
            App.Console.PrintMessage("Terminé\r\n")
            self.window.hide()
    
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    

Here the code to display the icon on the **pushButton** , change the name for
another button, (**radioButton, checkBox**) and the path to the icon.

    
    
    # Affiche un icône sur le bouton PushButton
            # self.image_01 = "C:\Program Files\FreeCAD0.13\icone01.png" # the name of the icon
            self.image_01 = path+"icone01.png" # the name of the icon
            icon01 = QtGui.QIcon() 
            icon01.addPixmap(QtGui.QPixmap(self.image_01),QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton.setIcon(icon01) 
            self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft) # This command reverses the direction of the button
    

The command **UserAppData** gives the user path **AppHomePath** gives the
installation path of FreeCAD

    
    
    #        path = FreeCAD.ConfigGet("UserAppData")
            path = FreeCAD.ConfigGet("AppHomePath")
    

This command reverses the horizontal button, right to left.

    
    
    self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft) # This command reverses the direction of the button
    

## Method 2

Another method to display a window, here by creating a file **QtForm.py**
which contains the header program (module called with **import QtForm**), and
a second module that contains the code window all these accessories, and your
code (the calling module).

This method requires two separate files, but allows to shorten your program
using the file ' ' QtForm.py ' ' import. Then distribute the two files
together, they are inseparable.

The file **QtForm.py**

    
    
    # -*- coding: utf-8 -*-
    # Create by flachyjoe
    from PySide import QtCore, QtGui
    
    try:
        _fromUtf8 = QtCore.QString.fromUtf8
    except AttributeError:
       def _fromUtf8(s):
          return s
    
    try:
        _encoding = QtGui.QApplication.UnicodeUTF8
        def _translate(context, text, disambig):
          return QtGui.QApplication.translate(context, text, disambig, _encoding)
    except AttributeError:
       def _translate(context, text, disambig):
          return QtGui.QApplication.translate(context, text, disambig)
    
    class Form(object):
       def __init__(self, title, width, height):
          self.window = QtGui.QMainWindow()
          self.title=title
          self.window.setObjectName(_fromUtf8(title))
          self.window.setWindowTitle(_translate(self.title, self.title, None))
          self.window.resize(width, height)
    
       def show(self):
          self.createUI()
          self.retranslateUI()
          self.window.show()
       
       def setText(self, control, text):
          control.setText(_translate(self.title, text, None))
    

The calling file that contains the window and your code.

The file my_file.py

The connections are to do, a good exercise.

    
    
    # -*- coding: utf-8 -*-
    # Create by flachyjoe
    from PySide import QtCore, QtGui
    import QtForm
    
    class myForm(QtForm.Form):
       def createUI(self):
          self.centralWidget = QtGui.QWidget(self.window)
          self.window.setCentralWidget(self.centralWidget)
          
          self.pushButton = QtGui.QPushButton(self.centralWidget)
          self.pushButton.setGeometry(QtCore.QRect(30, 170, 93, 28))
          self.pushButton.clicked.connect(self.on_pushButton_clicked)
          
          self.lineEdit = QtGui.QLineEdit(self.centralWidget)
          self.lineEdit.setGeometry(QtCore.QRect(30, 40, 211, 22))
          
          self.checkBox = QtGui.QCheckBox(self.centralWidget)
          self.checkBox.setGeometry(QtCore.QRect(30, 90, 81, 20))
          self.checkBox.setChecked(True)
          
          self.radioButton = QtGui.QRadioButton(self.centralWidget)
          self.radioButton.setGeometry(QtCore.QRect(30, 130, 95, 20))
       
       def retranslateUI(self):
          self.setText(self.pushButton, "Fermer")
          self.setText(self.lineEdit, "essais de texte")
          self.setText(self.checkBox, "CheckBox")
          self.setText(self.radioButton, "RadioButton")
       
       def on_pushButton_clicked(self):
          self.window.hide()
    
    myWindow=myForm("Fenetre de test",400,300)
    myWindow.show()
    

**Other example**

  * [![Qt example 1](/images/thumb/f/fe/Qt_Example_00.png/167px-Qt_Example_00.png)](/index.php?title=File:Qt_Example_00.png&filetimestamp=20170612135241& "Qt example 1")

Qt example 1

  * [![Qt example details](/images/thumb/d/d4/Qt_Example_01.png/167px-Qt_Example_01.png)](/index.php?title=File:Qt_Example_01.png&filetimestamp=20170612140101& "Qt example details")

Qt example details

Are treated :

  1. icon for window
  2. horizontalSlider
  3. progressBar horizontal
  4. verticalSlider
  5. progressBar vertical
  6. lineEdit
  7. lineEdit
  8. doubleSpinBox
  9. doubleSpinBox
  10. doubleSpinBox
  11. button
  12. button
  13. radioButton with icons
  14. checkBox with icon checked and unchecked
  15. textEdit
  16. graphicsView with 2 graphes

The code page and the icons [Qt_Example](/Qt_Example "Qt Example")

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), [Introduction to Python](/Introduction_to_Python "Introduction to Python"), [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

* * *

  * **Modules:** [Builtin modules](/Builtin_modules "Builtin modules"), [Units](/Units "Units"), [Quantity](/Quantity "Quantity")
  * **Workbenches:** [Workbench creation](/Workbench_creation "Workbench creation"), [Gui Commands](/Gui_Command "Gui Command"), [Commands](/Command "Command"), [Installing more workbenches](/Installing_more_workbenches "Installing more workbenches")
  * **Meshes and Parts:** [Mesh Scripting](/Mesh_Scripting "Mesh Scripting"), [Topological data scripting](/Topological_data_scripting "Topological data scripting"), [Mesh to Part](/Mesh_to_Part "Mesh to Part"), [PythonOCC](/PythonOCC "PythonOCC")

* * *

  * **Parametric objects:** [Scripted objects](/Scripted_objects "Scripted objects"), [Viewproviders](/Viewprovider "Viewprovider") ([Custom icon in tree view](/Custom_icon_in_tree_view "Custom icon in tree view"))
  * **Scenegraph:** [Coin (Inventor) scenegraph](/Scenegraph "Scenegraph"), [Pivy](/Pivy "Pivy")
  * **Graphical interface:** [Interface creation](/Interface_creation "Interface creation"), [Interface creation completely in Python](/Dialog_creation "Dialog creation") (1, [2](/Dialog_creation_reading_and_writing_files "Dialog creation reading and writing files"), [3](/Dialog_creation_setting_colors "Dialog creation setting colors"), [4](/Dialog_creation_image_and_animated_GIF "Dialog creation image and animated GIF"), [5](/PySide_usage_snippets "PySide usage snippets")), [PySide](/PySide "PySide"), PySide examples [beginner](/PySide_Beginner_Examples "PySide Beginner Examples"), [intermediate](/PySide_Intermediate_Examples "PySide Intermediate Examples"), [advanced](/PySide_Advanced_Examples "PySide Advanced Examples")
  * **Macros:** [Macros](/Macros "Macros"), [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

