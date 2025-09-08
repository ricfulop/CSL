---
url: https://wiki.freecad.org/PySide_usage_snippets
title: PySide usage snippets
scraped_at: 2025-09-08 16:46:53
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Some useful commands
  * 3 Encoding problems Toggle Encoding problems subsection
    * 3.1 UTF8
    * 3.2 ASCII

# PySide usage snippets

  * [Page](/PySide_usage_snippets "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:PySide_usage_snippets&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/PySide_usage_snippets)
  * [Edit](/index.php?title=PySide_usage_snippets&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=PySide_usage_snippets&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/PySide_usage_snippets.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=PySide_usage_snippets&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/PySide_usage_snippets)
  * [Edit](/index.php?title=PySide_usage_snippets&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=PySide_usage_snippets&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=PySide_usage_snippets&action=history)

General

  * [What links here](/Special:WhatLinksHere/PySide_usage_snippets "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/PySide_usage_snippets "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=PySide_usage_snippets&oldid=1068427 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=PySide_usage_snippets&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=PySide_usage_snippets&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
PySide+usage+snippets&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-PySide+usage+snippets&language=&task=view "Start translation for this language")
  * [Deutsch](/PySide_usage_snippets/de "PySide Verwendungsschnipsel \(62% translated\)")
  * English
  * [français](/PySide_usage_snippets/fr "Extraits d'utilisation de PySide \(100% translated\)")
  * [italiano](/PySide_usage_snippets/it "Frammenti di codice per l'utilizzo di PySide \(15% translated\)")
  * [polski](/PySide_usage_snippets/pl "PySide przydatne wycinki \(100% translated\)")

## Introduction

These are snippets of code that are useful when [creating
interfaces](/Dialog_creation "Dialog creation") with [PySide](/PySide
"PySide").

## Some useful commands

    
    
    # Here the code to display the icon on the '''pushButton''', 
    # change the name to another button, ('''radioButton, checkBox''') as well as the path to the icon,
    
           # Displays an icon on the button PushButton
           # self.image_01 = "C:\Program Files\FreeCAD0.13\icone01.png" # he name of the icon
           self.image_01 = path+"icone01.png" # the name of the icon
           icon01 = QtGui.QIcon() 
           icon01.addPixmap(QtGui.QPixmap(self.image_01),QtGui.QIcon.Normal, QtGui.QIcon.Off)
           self.pushButton.setIcon(icon01) 
           self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft) # This command reverses the direction of the button
    
    
    # path = FreeCAD.ConfigGet("UserAppData") # gives the user path
      path = FreeCAD.ConfigGet("AppHomePath") # gives the installation path of FreeCAD
    
    # This command reverses the horizontal button, right to left
    self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft) # This command reverses the horizontal button
    
    # Displays an info button
    self.pushButton.setToolTip(_translate("MainWindow", "Quitter la fonction", None)) # Displays an info button
    
    # This function gives a color button
    self.pushButton.setStyleSheet("background-color: red") # This function gives a color button
    
    # This function gives a color to the text of the button
    self.pushButton.setStyleSheet("color : #ff0000") # This function gives a color to the text of the button
    
    # combinaison des deux, bouton et texte
    self.pushButton.setStyleSheet("color : #ff0000; background-color : #0000ff;" ) #  combination of the two, button, and text
    
    # replace the icon in the main window
    MainWindow.setWindowIcon(QtGui.QIcon('C:\Program Files\FreeCAD0.13\View-C3P.png'))
    
    # connects a lineEdit on execute
    self.lineEdit.returnPressed.connect(self.execute) # connects a lineEdit on "def execute" after validation on enter
    # self.lineEdit.textChanged.connect(self.execute) # connects a lineEdit on "def execute" with each keystroke on the keyboard
    
    # display text in a lineEdit
    self.lineEdit.setText(str(val_X)) # Displays the value in the lineEdit (convert to string)
    
    # extract the string contained in a lineEdit
     val_X = self.lineEdit.text() # extract the (string) string contained in lineEdit
     val_X = float(val_X0)        # converted the string to an floating
     val_X = int(val_X0)          # convert the string to an integer
    
    # This code allows you to change the font and its attributes
           font = QtGui.QFont()
           font.setFamily("Times New Roman")
           font.setPointSize(10)
           font.setWeight(10)
           font.setBold(True) # same result with tags "<b>your text</b>" (in quotes)
           self.label_6.setFont(font)
           self.label_6.setObjectName("label_6")
           self.label_6.setStyleSheet("color : #ff0000") # This function gives a color to the text
           self.label_6.setText(_translate("MainWindow", "Select a view", None))
    

## Encoding problems

### UTF8

By using the characters with accents, where you get the error:

    
    
    UnicodeDecodeError: 'utf8' codec can't decode bytes in position 0-2: invalid data
    

Several solutions are possible.

    
    
    # conversion from a lineEdit
    App.activeDocument().CopyRight.Text = str(unicode(self.lineEdit_20.text() , 'ISO-8859-1').encode('UTF-8'))
    DESIGNED_BY = unicode(self.lineEdit_01.text(), 'ISO-8859-1').encode('UTF-8')
    

or with the procedure

    
    
    def utf8(unio):
        return unicode(unio).encode('UTF8')
    

### ASCII

    
    
    UnicodeEncodeError: 'ascii' codec can't encode character u'\xe9' in position 9: ordinal not in range(128)
    
    
    
    # conversion
    a = u"Nom de l'élément : "
    f.write('''a.encode('iso-8859-1')'''+str(element_)+"\n")
    

or with the procedure

    
    
    def iso8859(encoder):
        return unicode(encoder).encode('iso-8859-1')
    

or

    
    
    iso8859(unichr(176))
    

or

    
    
    unichr(ord(176))
    

or

    
    
    uniteSs = "mm"+iso8859(unichr(178))
    print(unicode(uniteSs, 'iso8859'))
    

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
  * **Graphical interface:** [Interface creation](/Interface_creation "Interface creation"), [Interface creation completely in Python](/Dialog_creation "Dialog creation") ([1](/Dialog_creation_with_various_widgets "Dialog creation with various widgets"), [2](/Dialog_creation_reading_and_writing_files "Dialog creation reading and writing files"), [3](/Dialog_creation_setting_colors "Dialog creation setting colors"), [4](/Dialog_creation_image_and_animated_GIF "Dialog creation image and animated GIF"), 5), [PySide](/PySide "PySide"), PySide examples [beginner](/PySide_Beginner_Examples "PySide Beginner Examples"), [intermediate](/PySide_Intermediate_Examples "PySide Intermediate Examples"), [advanced](/PySide_Advanced_Examples "PySide Advanced Examples")
  * **Macros:** [Macros](/Macros "Macros"), [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

