---
url: https://wiki.freecad.org/PySide_Intermediate_Examples
title: PySide Intermediate Examples
scraped_at: 2025-09-08 16:47:01
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction Toggle Introduction subsection
    * 1.1 Notes
  * 2 Code Based Discussion - Declarative Portion Toggle Code Based Discussion - Declarative Portion subsection
    * 2.1 Import Statement
    * 2.2 Class Definition
    * 2.3 Window Return Status
    * 2.4 Window Creation
    * 2.5 Label Creation
    * 2.6 Checkbox Creation
    * 2.7 Radio Button Creation
    * 2.8 Pop-Up Menu Creation
    * 2.9 Button Creation Part 1
    * 2.10 Button Creation Part 2
    * 2.11 Text Input Creation
    * 2.12 QuantitySpinBox Creation
    * 2.13 Contextual Menu Creation
    * 2.14 Numeric Input Creation
    * 2.15 Window Display
  * 3 Code Based Discussion - Operative Portion Toggle Code Based Discussion - Operative Portion subsection
    * 3.1 Generic Handler
    * 3.2 Pop-Up Menu Handler
    * 3.3 Mouse Event Handler
  * 4 Code Based Discussion - Main Routine
  * 5 Complete Modal Code Example
  * 6 Code Based Discussion - Nonmodal Code Example Toggle Code Based Discussion - Nonmodal Code Example subsection
    * 6.1 Import Statement
    * 6.2 Class Definition
    * 6.3 Window Creation
    * 6.4 Mouse Move Event Handler
    * 6.5 Invoking the Window
  * 7 Complete Nonmodal Code Example
  * 8 Misc Additional Topics Toggle Misc Additional Topics subsection
    * 8.1 Available Screen Size
    * 8.2 Frame Size and Geometry

# PySide Intermediate Examples

  * [Page](/PySide_Intermediate_Examples "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:PySide_Intermediate_Examples&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/PySide_Intermediate_Examples)
  * [Edit](/index.php?title=PySide_Intermediate_Examples&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=PySide_Intermediate_Examples&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/PySide_Intermediate_Examples.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=PySide_Intermediate_Examples&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/PySide_Intermediate_Examples)
  * [Edit](/index.php?title=PySide_Intermediate_Examples&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=PySide_Intermediate_Examples&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=PySide_Intermediate_Examples&action=history)

General

  * [What links here](/Special:WhatLinksHere/PySide_Intermediate_Examples "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/PySide_Intermediate_Examples "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=PySide_Intermediate_Examples&oldid=1619301 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=PySide_Intermediate_Examples&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=PySide_Intermediate_Examples&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
PySide+Intermediate+Examples&action=page&filter=&language=en)This is the
approved revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-PySide+Intermediate+Examples&language=&task=view "Start translation for this language")
  * [Deutsch](/PySide_Intermediate_Examples/de "PySide Beispiele für fortgeschrittene Anfänger \(19% translated\)")
  * English
  * [français](/PySide_Intermediate_Examples/fr "PySide : Exemples pour niveau intermédiaire \(100% translated\)")
  * [italiano](/PySide_Intermediate_Examples/it " Esempi di livello medio di PySide \(100% translated\)")
  * [polski](/PySide_Intermediate_Examples/pl "PySide przykłady dla średniozaawansowanych \(4% translated\)")
  * [русский](/PySide_Intermediate_Examples/ru "Примеры PySide среднего уровня \(11% translated\)")

## Introduction

This page covers medium level examples of the [PySide](/PySide "PySide") GUI
manager (accompanying pages cover aspects that are both less or more advanced,
[Beginner PySide Examples](/PySide_Beginner_Examples "PySide Beginner
Examples") and [Advanced PySide Examples](/PySide_Advanced_Examples "PySide
Advanced Examples")). In this page an example program is used to cover the
different PySide topics. The intention is to present some functional PySide
code so anyone who needs to use PySide can copy out the relevant section,
modify and adapt it to their own purposes.

### Notes

  * This page is not intended to cover the Python language or to serve as an instruction in Python.
  * The variable names are not descriptive but have been kept in sequence to better organise the explanations
  * There are numerous naming conventions for GUI components, none of which are "right" or "wrong"
  * There are a variety of different sequencings of the declarations for the widgets, the signals, the methods, once again none are "right" or "wrong"
  * It is worth keeping in mind that PySide operates with strings when dealing with user input, what appears on the screen as a number is actually a text representation of a number

## Code Based Discussion - Declarative Portion

The "example program" is actually a large Class definition, the definition of
a PySide GUI class, and has over 150 lines of code (including comments). There
is no functional purpose to the Class or it's behaviour, the sole purpose is
to demonstrate possible GUI actions and present some code that hopefully can
be used by other FreeCAD users.

The Class definition and the small number of lines of code that invoke are
described in the order the occur in the file. This order is based on the
screen layout which is rather arbitrary and solely intended to demonstrate
features. This is the modal GUI screen the PySide Class generates:

[![](/images/3/38/PySideScreenSnapshot3.jpg)](/index.php?title=File:PySideScreenSnapshot3.jpg&filetimestamp=20150207142110&)

Most of the remainder of this section will describe the contents of the Class
definition which appears at the end of this section. First we will cover the
declarative elements that define how things operate and how the GUI is
assembled, then we will cover the operative sections (i.e. the code that will
execute when user interactions occur). This window is based on the class
QDialog and so is modal - which means no activities can be made outside of the
window while it is open.

### Import Statement

The mandatory Import statement

    
    
    from PySide import QtGui, QtCore
    

This is best placed at the top of the Python file.

### Class Definition

    
    
    class ExampleModalGuiClass(QtGui.QDialog):
    	""""""
    	def __init__(self):
    		super(ExampleModalGuiClass, self).__init__()
    		self.initUI()
    	def initUI(self):
    

This code is best copied out verbatim and altered. The gist of the code is
that we are sub-classing the QDialog Class of PySide. In adapting this code
you will want to change the class name "ExampleModalGuiClass" - make sure to
change it in both locations (e.g. lines 1 & 4).

### Window Return Status

    
    
    self.result = userCancelled
    

This is not mandatory but rather a good programming practice, this sets a
default return status for the window which will be there regardless of what
the user does. Later in the code this may be changed by the Python code to
indicate different options the user may have selected.

### Window Creation

    
    
    # create our window
    # define window		xLoc,yLoc,xDim,yDim
    self.setGeometry(	250, 250, 400, 350)
    self.setWindowTitle("Our Example Program Window")
    self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    

Remembering that screen dimensions are measured from the upper-left corner, on
the 3rd line the values refer to:

  * the number of pixels the upper-left corner will be to the right of the lefthand screen edge (250)
  * the number of pixels the upper-left corner will be below the upper screen edge (250)
  * the width of the screen in pixels (400)
  * the height of the screen in pixels (350)

The title of the window is set and the final line simply means that this
window will never be obscured by another window - if this is not desired then
simply place a Python comment character ('#') as the first character of the
line.

### Label Creation

    
    
    # create some Labels
    self.label1 = QtGui.QLabel("                       ", self)
    self.label1.setFont('Courier') # set to a non-proportional font
    self.label1.move(20, 20)
    self.label2 = QtGui.QLabel("sample string number two", self)
    self.label2.move(20, 70)
    self.label3 = QtGui.QLabel("                        ", self)
    self.label3.setFont('Courier') # set to a non-proportional font
    self.label3.move(20, 120)
    self.label4 = QtGui.QLabel("can you see this?", self)
    self.label4.move(20, 170)
    

In PySide labels serve two purposes, static labels (as the name implies) as
well as read-only (i.e. display-only) text fields. So unchanging instructions
to the user such as "Don't push the red button" as well as dynamic calculation
results such as "42" can be communicated to the user. The 2nd line declares a
Label and sets it's initial value (which is blank in this case). The 3rd line
specifies the font, any font (on the system) can be specified, if not
specified the default font is used. In this case the font is specified as a
non-proportional one. The label is moved to it's location in the window - it's
coordinates specify it's position with respect to the window (not the screen).

### Checkbox Creation

    
    
    # checkboxes
    self.checkbox1 = QtGui.QCheckBox("Left side", self)
    self.checkbox1.clicked.connect(self.onCheckbox1)
    #self.checkbox1.toggle() # will set an initial value if executed
    self.checkbox1.move(210,10)
    #
    self.checkbox2 = QtGui.QCheckBox("Right side", self)
    self.checkbox2.clicked.connect(self.onCheckbox2)
    self.checkbox2.move(210,30)
    

Checkboxes can be off and on in any combination (unlike radio buttons). Line 2
declares one and set's it initial Value. Line 3 specifies which method will be
executed when the Checkbox is clicked (in this case the method 'onCheckBox1').
If the 4th line did not have the Python comment character ('#') as the first
character, then it would be executed and it would mark the checkbox as
checked. Finally the 5th line moves the Checkbox into position.

### Radio Button Creation

    
    
    # radio buttons
    self.radioButton1 = QtGui.QRadioButton("random string one",self)
    self.radioButton1.clicked.connect(self.onRadioButton1)
    self.radioButton1.move(210,60)
    #
    self.radioButton2 = QtGui.QRadioButton("owt gnirts modnar",self)
    self.radioButton2.clicked.connect(self.onRadioButton2)
    self.radioButton2.move(210,80)
    

The creation of the Radio Buttons is very similar to the Checkboxes. The only
difference really is the behaviour of the Radio Buttons in that only one of
them can be 'on' at a time.

### Pop-Up Menu Creation

    
    
    # set up lists for pop-ups
    self.popupItems1 = ("pizza","apples","candy","cake","potatoes")
    # set up pop-up menu
    self.popup1 = QtGui.QComboBox(self)
    self.popup1.addItems(self.popupItems1)
    self.popup1.setCurrentIndex(self.popupItems1.index("candy"))
    self.popup1.activated[str].connect(self.onPopup1)
    self.popup1.move(210, 115)
    

In line 2 a list is built up of what will be the user choices. An alternative
is to build up a Dictionary but only use the Keys for the list of menu
choices. Line 4 creates the pop-up menu (known as a ComboBox to PySide), the
user options are added in line 5.

As a side note, if the Dictionary was used then the lines would appear as:

    
    
    self.popupItems1 = OrderedDict([("2","widget"),("pink","foobar"),("4","galopsis")])
    
    self.popup1.addItems(self.popupItems1.keys())
    

Returning to the main code sample for this section, line 6 sets the default
choice, this line may be omitted, also the value of the default choice could
be loaded into the corresponding Label (once again if appropriate). And
finally the move into position at line 8.

### Button Creation Part 1

    
    
    # toggle visibility button
    pushButton1 = QtGui.QPushButton('Toggle visibility', self)
    pushButton1.clicked.connect(self.onPushButton1)
    pushButton1.setAutoDefault(False)
    pushButton1.move(210, 165)
    

The button is created in line 2 with it's name, the handler for it's signal
when clicked is specified in line 3. Line 4 is there to prevent the button
from becoming the 'default button' - the button that will be clicked if the
user simply presses the Return key. And a move to position finished up the
code segment.

### Button Creation Part 2

    
    
    # cancel button
    cancelButton = QtGui.QPushButton('Cancel', self)
    cancelButton.clicked.connect(self.onCancel)
    cancelButton.setAutoDefault(True)
    cancelButton.move(150, 280)
    # OK button
    okButton = QtGui.QPushButton('OK', self)
    okButton.clicked.connect(self.onOk)
    okButton.move(260, 280)
    

Both buttons are created with a name (which will appear as their label),
associated with a method which will execute when they are clicked, and moved
into position. The one exception is line 4 which specifies the 'Cancel' button
as the default button - that means it will be "clicked" if the user preses the
Return key.

### Text Input Creation

    
    
    # text input field
    self.textInput = QtGui.QLineEdit(self)
    self.textInput.setText("cats & dogs")
    self.textInput.setFixedWidth(190)
    self.textInput.move(20, 220)
    

The QLineEdit widget is probably the most common for user textual input, in
this example the code section after this one will set up a contextual menu to
operate on it. This code section creates (line 2), sets an initial value (line
3), sets a width to the field (line 4) and moves the widget into place (line
5).

### QuantitySpinBox Creation

    
    
    # QuantitySpinBox
    from FreeCAD import Units
    ui = FreeCADGui.UiLoader()
    quantityInput = ui.createWidget("Gui::QuantitySpinBox")
    self.quantityInput.setProperty( 'minimum', 0.0)
    potential = 2.87
    unit = "V"
    # only set the value
    self.quantityInput.setProperty('rawValue', potential )
    # set quantity (value + unit)
    quantity = Units.Quantity("{} {}".format(potential , unit))
    self.quantityInput.setProperty('value', quantity)
    # read value from the spinbox
    quantity = self.quantityInput.property('value')
    

The Gui::QuantitySpinBox widget is a FreeCAD-special, designed to display and
handle values together with their [units](/Expressions#Units "Expressions").
It is derived from Qt's [QAbstractSpinBox
class](https://doc.qt.io/qt-5/qabstractspinbox.html). For all its properties
see the list in the source code file
[QuantitySpinBox.h](https://github.com/FreeCAD/FreeCAD/blob/master/src/Gui/QuantitySpinBox.h#L42)

### Contextual Menu Creation

    
    
    # set contextual menu options for text editing widget
    # set text field to some dogerel
    popMenuAction1 = QtGui.QAction(self)
    popMenuAction1.setText("load some text")
    popMenuAction1.triggered.connect(self.onPopMenuAction1)
    # make text uppercase
    popMenuAction2 = QtGui.QAction(self)
    popMenuAction2.setText("uppercase")
    popMenuAction2.triggered.connect(self.onPopMenuAction2)
    # menu dividers
    popMenuDivider = QtGui.QAction(self)
    popMenuDivider.setText('---------')
    popMenuDivider.triggered.connect(self.onPopMenuDivider)
    # remove all text
    popMenuAction3 = QtGui.QAction(self)
    popMenuAction3.setText("clear")
    popMenuAction3.triggered.connect(self.onPopMenuAction3)
    # define menu and add options
    self.textInput.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
    self.textInput.addAction(popMenuAction1)
    self.textInput.addAction(popMenuAction2)
    self.textInput.addAction(popMenuDivider)
    self.textInput.addAction(popMenuAction3)
    

This code has numerous repetitions as the same action is performed with
different values - this is part of what makes GUI code so lengthy (no matter
what the system). First a QAction is created - it is a pairing (or linkage) of
the text that the user will see as their selectable option along with the
method that will execute if they select that option. It is basically a pairing
of a user choice with a piece of code. Line 3 creates it, line 4 defines the
user option (as they will see it) and line 5 specifies which piece of Python
code will execute.

Skipping to line 19 (the line with "self.textInput.setContextMenuPolicy") a
ActionsContextMenu is created which is holder for all the separate QAction
linkages between user choice and code to execute. Each widget can only have a
single Contextual Menu (i.e. the menu associated with the right-click) so line
19 defines that menu. The following 4 lines add the linkages created at the
beginning of this code section. Order is significant here, the user will see
the menu options in the order they are added. Notice that the 3rd menu option
is really a bit of nothing, it's code is null but it serves to separate 2
groups of options on the Contextual Menu.

### Numeric Input Creation

    
    
    # numeric input field
    self.numericInput = QtGui.QLineEdit(self)
    self.numericInput.setInputMask("999")
    self.numericInput.setText("000")
    self.numericInput.setFixedWidth(50)
    self.numericInput.move(250, 220)
    

The creation of the field for numeric input really follows that for Text Input
earlier. In fact the code is identical with exception of the 3rd and 4th
lines. The 3rd line sets the Mask as defined by PySide, which in this case
specifies up to 3 digits (which may include 0). A full list of the InputMask
codes can be found at [QLineEdit
InputMask](http://doc.qt.io/qt-5/qlineedit.html#inputMask-prop)

### Window Display

    
    
    # now make the window visible
    self.show()
    

There is only one line and it causes the GUI to be displayed after the setup.

## Code Based Discussion - Operative Portion

We now move onto the operative portion of the GUI definition which is the code
that executes in response to user interactions with the GUI. The order of
statement groups is not very relevant - with the caveat that something must be
declared before it can be referenced. Some people put all the handlers of a
certain type (e.g. handlers for buttons) in one group, others list the
handlers alphabetically. For specific application there may be a problem
related reason that all handlers relating to a specific aspect be gathered
together

There is a high degree of similarity between the handlers. Most do not receive
a parameter, the fact they are executing is realy the only parameter (or
signal) they get. Others like "onPopup1" and "mousePressEvent" accept a
parameter.

There must be a one to one correspondance between the handlers specified in
the declarative section and the handler declared in this, the operative
section. There may be extra handlers declared which are never invoked but
there may not be any missing.

### Generic Handler

In this code example, generic handlers handle the following events:

  * onCheckbox1
  * onCheckbox2
  * onRadioButton1
  * onRadioButton2
  * onPushButton1
  * onPopMenuAction1
  * onPopMenuAction2
  * onPopMenuDivider
  * onPopMenuAction3
  * onCancel
  * onOk

The general form for the handlers is:

    
    
    def handlerName(self):
    	lineOfCode1
    	lineOfCode2
    

The first line has the keyword "def" followed by the handler name. The handler
name must match the name from the earlier declarative section exactly. The
parameter "self" is part of the standard syntax as are the enclosing
parenthesis and the final colon character. Once the first line is finished
then there are no requirements of the following code, it is purely application
specific.

### Pop-Up Menu Handler

    
    
    def onPopup1(self, selectedText):
    

The Pop-Up menu handler is the same as the generic handler with exception that
a second parameter, the text selected by the user, is passed in. Remember that
everything is text coming from the Pop-Up menu and even if the user has
selected the number 3, it will be passed in as the string "3".

### Mouse Event Handler

    
    
    def mousePressEvent(self, event):
    	# print mouse position, X & Y
    	print("X = ", event.pos().x())
    	print("Y = ", event.pos().y())
    	#
    	if event.button() == QtCore.Qt.LeftButton:
    		print("left mouse button")
    	if self.label1.underMouse():
    		print("over the text '"+self.label1.text()+"'")
    

The Mouse Event handler is the same as the generic handler with exception that
a second parameter, the mouse event (e.g. left-click, right-click) from the
user is passed in. The name of the handler, "mousePressEvent", is reserved and
if it is changed then the handler will no longer receive the event from the
mouse presses.

The X and Y coordinates of the mouse press are given by the reference
"event.pos().x()" and "event.pos().y()". The constants "QtCore.Qt.LeftButton"
and "QtCore.Qt.RightButton" are used to determine which mouse button was
pressed.

A reference to a widget can be made of the form "self.widgetName.underMouse()"
which will return `true` or `false` as to whether the mouse cursor is over the
widget "widgetName". Although presented in the same code excerpt the
"underMouse()" handler is not tied to the "mousePressEvent" handler and can be
used at any time.

## Code Based Discussion - Main Routine

Most of the volume of code is in the GUI Class definition, there is not much
in the main procedure.

    
    
    # Constant definitions
    global userCancelled, userOK
    userCancelled = "Cancelled"
    userOK = "OK"
    

Lines 2,3 & 4 deal with coordinating the status of the user interaction with
the GUI - e.g. Cancelled, OK, or any other application defined status. The
handler routines "onCancel" and "onOk" earlier also set these statuses.

    
    
    form = ExampleGuiClass()
    form.exec_()
    
    if form.result==userCancelled:
    	pass # steps to handle user clicking Cancel
    if form.result==userOK:
    	# steps to handle user clicking OK
    	localVariable1 = form.label1.text()
    	localVariable2 = form.label2.text()
    	localVariable3 = form.label3.text()
    	localVariable4 = form.label4.text()
    

Lines 1 and 2 show the method for invoking the GUI. There may be multiple GUI
definitions for a program and also the GUI need not be invoked as the first
thing in the Python file, it may be invoked at any point. The Name of the GUI
Class is specified in line 1 ("ExampleGuiClass" in this case) but the rest of
the 2 lines are to be copied verbatim.

Lines 4 and 6 use the result field to determine the appropriate action. The
last 4 lines simply show the copying of the data in the GUI object to
variables local to the executing main procedure.

## Complete Modal Code Example

This is the complete code example (developed on FreeCAD v0.14):

    
    
    # import statements
    from PySide import QtGui, QtCore
    
    # UI Class definitions
    
    class ExampleModalGuiClass(QtGui.QDialog):
    	""""""
    	def __init__(self):
    		super(ExampleModalGuiClass, self).__init__()
    		self.initUI()
    	def initUI(self):
    		self.result = userCancelled
    		# create our window
    		# define window		xLoc,yLoc,xDim,yDim
    		self.setGeometry(	250, 250, 400, 350)
    		self.setWindowTitle("Our Example Modal Program Window")
    		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    		# create some Labels
    		self.label1 = QtGui.QLabel("                       ", self)
    		self.label1.setFont('Courier') # set to a non-proportional font
    		self.label1.move(20, 20)
    		self.label2 = QtGui.QLabel("sample string number two", self)
    		self.label2.move(20, 70)
    		self.label3 = QtGui.QLabel("                        ", self)
    		self.label3.setFont('Courier') # set to a non-proportional font
    		self.label3.move(20, 120)
    		self.label4 = QtGui.QLabel("can you see this?", self)
    		self.label4.move(20, 170)
    		# checkboxes
    		self.checkbox1 = QtGui.QCheckBox("Left side", self)
    		self.checkbox1.clicked.connect(self.onCheckbox1)
    		#self.checkbox1.toggle() # will set an initial value if executed
    		self.checkbox1.move(210,10)
    		#
    		self.checkbox2 = QtGui.QCheckBox("Right side", self)
    		self.checkbox2.clicked.connect(self.onCheckbox2)
    		self.checkbox2.move(210,30)
    		# radio buttons
    		self.radioButton1 = QtGui.QRadioButton("random string one",self)
    		self.radioButton1.clicked.connect(self.onRadioButton1)
    		self.radioButton1.move(210,60)
    		#
    		self.radioButton2 = QtGui.QRadioButton("owt gnirts modnar",self)
    		self.radioButton2.clicked.connect(self.onRadioButton2)
    		self.radioButton2.move(210,80)
    		# set up lists for pop-ups
    		self.popupItems1 = ("pizza","apples","candy","cake","potatoes")
    		# set up pop-up menu
    		self.popup1 = QtGui.QComboBox(self)
    		self.popup1.addItems(self.popupItems1)
    		self.popup1.setCurrentIndex(self.popupItems1.index("candy"))
    		self.popup1.activated[str].connect(self.onPopup1)
    		self.popup1.move(210, 115)
    		# toggle visibility button
    		pushButton1 = QtGui.QPushButton('Toggle visibility', self)
    		pushButton1.clicked.connect(self.onPushButton1)
    		pushButton1.setAutoDefault(False)
    		pushButton1.move(210, 165)
    		# text input field
    		self.textInput = QtGui.QLineEdit(self)
    		self.textInput.setText("cats & dogs")
    		self.textInput.setFixedWidth(190)
    		self.textInput.move(20, 220)
    		# set contextual menu options for text editing widget
    		# set text field to some dogerel
    		popMenuAction1 = QtGui.QAction(self)
    		popMenuAction1.setText("load some text")
    		popMenuAction1.triggered.connect(self.onPopMenuAction1)
    		# make text uppercase
    		popMenuAction2 = QtGui.QAction(self)
    		popMenuAction2.setText("uppercase")
    		popMenuAction2.triggered.connect(self.onPopMenuAction2)
    		# menu dividers
    		popMenuDivider = QtGui.QAction(self)
    		popMenuDivider.setText('---------')
    		popMenuDivider.triggered.connect(self.onPopMenuDivider)
    		# remove all text
    		popMenuAction3 = QtGui.QAction(self)
    		popMenuAction3.setText("clear")
    		popMenuAction3.triggered.connect(self.onPopMenuAction3)
    		# define menu and add options
    		self.textInput.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
    		self.textInput.addAction(popMenuAction1)
    		self.textInput.addAction(popMenuAction2)
    		self.textInput.addAction(popMenuDivider)
    		self.textInput.addAction(popMenuAction3)
    		# numeric input field
    		self.numericInput = QtGui.QLineEdit(self)
    		self.numericInput.setInputMask("999")
    		self.numericInput.setText("000")
    		self.numericInput.setFixedWidth(50)
    		self.numericInput.move(250, 220)
    		# cancel button
    		cancelButton = QtGui.QPushButton('Cancel', self)
    		cancelButton.clicked.connect(self.onCancel)
    		cancelButton.setAutoDefault(True)
    		cancelButton.move(150, 280)
    		# OK button
    		okButton = QtGui.QPushButton('OK', self)
    		okButton.clicked.connect(self.onOk)
    		okButton.move(260, 280)
    		# now make the window visible
    		self.show()
    		#
    	def onCheckbox1(self):
    		text = self.label1.text()
    		if text[0]==' ':
    			self.label1.setText('left'+text[4:])
    		else:
    			self.label1.setText('    '+text[4:])
    	def onCheckbox2(self):
    		text = self.label1.text()
    		if text[-1]==' ':
    			self.label1.setText(text[:-5]+'right')
    		else:
    			self.label1.setText(text[:-5]+'     ')
    	def onRadioButton1(self):
    		self.label2.setText(self.radioButton1.text())
    	def onRadioButton2(self):
    		self.label2.setText(self.radioButton2.text())
    	def onPopup1(self, selectedText):
    		if self.label3.text().isspace():
    			self.label3.setText(selectedText)
    		else:
    			self.label3.setText(self.label3.text()+","+selectedText)
    	def onPushButton1(self):
    		if self.label4.isVisible():
    			self.label4.hide()
    		else:
    			self.label4.show()
    	def onPopMenuAction1(self):
    		# load some text into field
    		self.textInput.setText("Lorem ipsum dolor sit amet")
    	def onPopMenuAction2(self):
    		# set text in field to uppercase
    		self.textInput.setText(self.textInput.text().upper())
    	def onPopMenuDivider(self):
    		# this option is the divider and is really there as a spacer on the menu list
    		# consequently it has no functional code to execute if user selects it
    		pass
    	def onPopMenuAction3(self):
    		# clear the text from the field
    		self.textInput.setText('')
    	def onCancel(self):
    		self.result			= userCancelled
    		self.close()
    	def onOk(self):
    		self.result			= userOK
    		self.close()
    	def mousePressEvent(self, event):
    		# print mouse position, X & Y
    		print("X = ", event.pos().x())
    		print("Y = ", event.pos().y())
    		#
    		if event.button() == QtCore.Qt.LeftButton:
    			print("left mouse button")
    		if self.label1.underMouse():
    			print("over the text '"+self.label1.text()+"'")
    		if self.label2.underMouse():
    			print("over the text '"+self.label2.text()+"'")
    		if self.label3.underMouse():
    			print("over the text '"+self.label3.text()+"'")
    		if self.label4.underMouse():
    			print("over the text '"+self.label4.text()+"'")
    		if self.textInput.underMouse():
    			print("over the text '"+self.textInput.text()+"'")
    		if event.button() == QtCore.Qt.RightButton:
    			print("right mouse button")
    # Class definitions
    
    # Function definitions
    
    # Constant definitions
    userCancelled = "Cancelled"
    userOK = "OK"
    
    # code ***********************************************************************************
    
    form = ExampleModalGuiClass()
    form.exec_()
    
    if form.result==userCancelled:
    	pass # steps to handle user clicking Cancel
    if form.result==userOK:
    	# steps to handle user clicking OK
    	localVariable1 = form.label1.text()
    	localVariable2 = form.label2.text()
    	localVariable3 = form.label3.text()
    	localVariable4 = form.label4.text()
    #
    #OS: Mac OS X
    #Word size: 64-bit
    #Version: 0.14.3703 (Git)
    #Branch: releases/FreeCAD-0-14
    #Hash: c6edd47334a3e6f209e493773093db2b9b4f0e40
    #Python version: 2.7.5
    #Qt version: 4.8.6
    #Coin version: 3.1.3
    #SoQt version: 1.5.0
    #OCC version: 6.7.0
    #
    

The best way to use this code is to copy it into an editor or FreeCAD macro
file and play around with it.

## Code Based Discussion - Nonmodal Code Example

All of the widget specific from the previous modal example transfer to use in
a nonmodal window. The main difference is that the nonmodal window does not
restrict the user from interacting with other windows. Basically, a nonmodal
window is one that can be opened and left open for as long as needed without
it placing any restrictions on other application windows. There are a small
number of code differences between the two which will be highlighted,
consequently this code example is quite brief. Anything that is the same as
the previous modal example will be left out in the interests of keeping this
overview brief. This is the nonmodal GUI screen the PySide Class generates:

[![](/images/4/45/PySideScreenSnapshot4.jpg)](/index.php?title=File:PySideScreenSnapshot4.jpg&filetimestamp=20150207163232&)

### Import Statement

The mandatory Import statement

    
    
    from PySide import QtGui, QtCore
    

This is best placed at the top of the Python file.

### Class Definition

    
    
    class ExampleNonmodalGuiClass(QtGui.QMainWindow):
    	""""""
    	def __init__(self):
    		super(ExampleNonmodalGuiClass, self).__init__()
    		self.initUI()
    	def initUI(self):
    

This code is best copied out verbatim and altered. The gist of the code is
that we are sub-classing the QMainWindow Class of PySide. In adapting this
code you will want to change the class name "ExampleNonmodalGuiClass" - make
sure to change it in both locations (e.g. lines 1 & 4).

### Window Creation

    
    
    # create our window
    # define window	xLoc,yLoc,xDim,yDim
    self.setGeometry(	250, 250, 400, 150)
    self.setWindowTitle("Our Example Nonmodal Program Window")
    self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    self.setMouseTracking(True)
    

Obviously our window dimensions and title are different. The main point to
note is the last line which lets PySide know that it is to send out mouse
position events as they happen. Note that these events will not be sent out
when the mouse is over a widget like a button as the widget will capture the
events.

### Mouse Move Event Handler

    
    
    def mouseMoveEvent(self,event):
    	self.label6.setText("X: "+str(event.x()) + " Y: "+str(event.y()))
    

This handler receives the event of a Mouse Move and displays the formatted
form of it. Test what happens when it is over widgets or outside of the
window.

### Invoking the Window

    
    
    form = ExampleNonmodalGuiClass()
    

Invoking the window is another area of difference from the previous example.
This time only 1 line is needed for invoking the GUI.

## Complete Nonmodal Code Example

    
    
    from PySide import QtGui, QtCore
    
    # UI Class definitions
    
    class ExampleNonmodalGuiClass(QtGui.QMainWindow):
    	""""""
    	def __init__(self):
    		super(ExampleNonmodalGuiClass, self).__init__()
    		self.initUI()
    	def initUI(self):
    		self.result = userCancelled
    		# create our window
    		# define window		xLoc,yLoc,xDim,yDim
    		self.setGeometry(	250, 250, 400, 150)
    		self.setWindowTitle("Our Example Nonmodal Program Window")
    		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    		self.setMouseTracking(True)
    		# create Labels
    		self.label4 = QtGui.QLabel("can you see this?", self)
    		self.label4.move(20, 20)
    		self.label5 = QtGui.QLabel("Mouse position:", self)
    		self.label5.move(20, 70)
    		self.label6 = QtGui.QLabel("               ", self)
    		self.label6.move(135, 70)
    		# toggle visibility button
    		pushButton1 = QtGui.QPushButton('Toggle visibility', self)
    		pushButton1.clicked.connect(self.onPushButton1)
    		pushButton1.setMinimumWidth(150)
    		#pushButton1.setAutoDefault(False)
    		pushButton1.move(210, 20)
    		# cancel button
    		cancelButton = QtGui.QPushButton('Cancel', self)
    		cancelButton.clicked.connect(self.onCancel)
    		cancelButton.setAutoDefault(True)
    		cancelButton.move(150, 110)
    		# OK button
    		okButton = QtGui.QPushButton('OK', self)
    		okButton.clicked.connect(self.onOk)
    		okButton.move(260, 110)
    		# now make the window visible
    		self.show()
    		#
    	def onPushButton1(self):
    		if self.label4.isVisible():
    			self.label4.hide()
    		else:
    			self.label4.show()
    	def onCancel(self):
    		self.result			= userCancelled
    		self.close()
    	def onOk(self):
    		self.result			= userOK
    		self.close()
    	def mouseMoveEvent(self,event):
    		self.label6.setText("X: "+str(event.x()) + " Y: "+str(event.y()))
    # Class definitions
    
    # Function definitions
    
    # Constant definitions
    global userCancelled, userOK
    userCancelled		= "Cancelled"
    userOK			= "OK"
    
    # code ***********************************************************************************
    
    form = ExampleNonmodalGuiClass()
    #
    #OS: Mac OS X
    #Word size: 64-bit
    #Version: 0.14.3703 (Git)
    #Branch: releases/FreeCAD-0-14
    #Hash: c6edd47334a3e6f209e493773093db2b9b4f0e40
    #Python version: 2.7.5
    #Qt version: 4.8.6
    #Coin version: 3.1.3
    #SoQt version: 1.5.0
    #OCC version: 6.7.0
    

## Misc Additional Topics

There are 3 concepts to the screen real estate in a GUI environment:

  * physical space on the screen
  * frame
  * geometry

Within the software all are measured in pixels. PySide has function to measure
in real world units but these are undependable as the manufacturers have no
standard for pixel size or aspect ratio.

The Frame is the size of a window including it's side bars, top bar (possibly
with a menu in it) and bottom bar. The Geometry is the space lying within the
Frame and so is always less than or equal to the Frame. In turn the Frame is
always less than or equal to the available screen size.

### Available Screen Size

    
    
    # get screen dimensions (Available Screen Size)
    screenWidth		= QtGui.QDesktopWidget().screenGeometry().width()
    screenHeight		= QtGui.QDesktopWidget().screenGeometry().height()
    # get dimensions for available space on screen
    availableWidth		= QtGui.QDesktopWidget().availableGeometry().width()
    availableHeight		= QtGui.QDesktopWidget().availableGeometry().height()
    

Generally the "availableHeight" should be less than the "screenHeight" by the
height of the menu bar. These 4 values are based on the hardware environment
and will change from computer to computer. They are not dependent on any
application window size.

(Since Python 3.9 this warning appears when the above code is executed:
**DeprecationWarning: QDesktopWidget.screenGeometry(int screen) const is
deprecated**. A replacement seems to be needed from Python 3.10 onwards.)

### Frame Size and Geometry

    
    
    # set up a variable to hold the Main Window to save some typing...
    mainWin = FreeCAD.Gui.getMainWindow()
    
    mainWin.showFullScreen() # no menu bars, every last pixel is given over to FreeCAD
    mainWin.geometry()
    mainWin.frameSize()
    mainWin.frameGeometry()
    
    mainWin.showMaximized() # show maximised within the screen, window edges and the menu bar will be displayed
    mainWin.geometry()
    mainWin.frameSize()
    mainWin.frameGeometry()
    
    mainWin.showNormal() # show at the last non-maximised or non-minimised size (and location)
    mainWin.geometry()
    mainWin.frameSize()
    mainWin.frameGeometry()
    
    mainWin.setGeometry(50, 50, 800, 800) # specifically set FreeCAD main window's size and location, this will become the new setting for 'showNormal()'
    
    mainWin.showMinimized() # FreeCAD will disappear from view after this command...
    mainWin.geometry()
    mainWin.frameSize()
    mainWin.frameGeometry()
    

These same commands can be executed on a user generated window, the syntax
does not change.

  

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
  * **Graphical interface:** [Interface creation](/Interface_creation "Interface creation"), [Interface creation completely in Python](/Dialog_creation "Dialog creation") ([1](/Dialog_creation_with_various_widgets "Dialog creation with various widgets"), [2](/Dialog_creation_reading_and_writing_files "Dialog creation reading and writing files"), [3](/Dialog_creation_setting_colors "Dialog creation setting colors"), [4](/Dialog_creation_image_and_animated_GIF "Dialog creation image and animated GIF"), [5](/PySide_usage_snippets "PySide usage snippets")), [PySide](/PySide "PySide"), PySide examples [beginner](/PySide_Beginner_Examples "PySide Beginner Examples"), intermediate, [advanced](/PySide_Advanced_Examples "PySide Advanced Examples")
  * **Macros:** [Macros](/Macros "Macros"), [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

