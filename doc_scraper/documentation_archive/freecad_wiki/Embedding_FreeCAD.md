---
url: https://wiki.freecad.org/Embedding_FreeCAD
title: Embedding FreeCAD
scraped_at: 2025-09-08 16:42:16
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Using FreeCAD without GUI
  * 3 Using FreeCAD with GUI
  * 4 Caveats
  * 5 Related

# Embedding FreeCAD

  * [Page](/Embedding_FreeCAD "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Embedding_FreeCAD&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Embedding_FreeCAD)
  * [Edit](/index.php?title=Embedding_FreeCAD&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Embedding_FreeCAD&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Embedding_FreeCAD.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Embedding_FreeCAD&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Embedding_FreeCAD)
  * [Edit](/index.php?title=Embedding_FreeCAD&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Embedding_FreeCAD&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Embedding_FreeCAD&action=history)

General

  * [What links here](/Special:WhatLinksHere/Embedding_FreeCAD "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Embedding_FreeCAD "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Embedding_FreeCAD&oldid=1479955 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Embedding_FreeCAD&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Embedding_FreeCAD&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Embedding+FreeCAD&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Embedding+FreeCAD&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Embedding_FreeCAD/id "Embedding FreeCAD \(5% translated\)")
  * [Deutsch](/Embedding_FreeCAD/de "FreeCAD einbinden \(100% translated\)")
  * English
  * [Türkçe](/Embedding_FreeCAD/tr "Embedding FreeCAD/tr \(0% translated\)")
  * [español](/Embedding_FreeCAD/es "Embedding FreeCAD \(36% translated\)")
  * [français](/Embedding_FreeCAD/fr "Intégrer FreeCAD \(100% translated\)")
  * [italiano](/Embedding_FreeCAD/it "Incorporare FreeCAD \(100% translated\)")
  * [polski](/Embedding_FreeCAD/pl "Osadzanie programu FreeCAD \(100% translated\)")
  * [português](/Embedding_FreeCAD/pt "Embedding FreeCAD \(5% translated\)")
  * [română](/Embedding_FreeCAD/ro "Încorporarea FreeCAD \(45% translated\)")
  * [svenska](/Embedding_FreeCAD/sv "Embedding FreeCAD \(36% translated\)")
  * [čeština](/Embedding_FreeCAD/cs "Embedding FreeCAD \(5% translated\)")
  * [русский](/Embedding_FreeCAD/ru "Embedding FreeCAD \(50% translated\)")
  * [中文（中国大陆）](/Embedding_FreeCAD/zh-cn "Embedding FreeCAD/zh-cn \(0% translated\)")
  * [日本語](/Embedding_FreeCAD/ja "FreeCADの組み込み \(100% translated\)")

## Introduction

FreeCAD can be imported as a [Python](/Python "Python") module in other
programs or in a standalone Python console, together with all its modules and
components. It's even possible to import the FreeCAD user interface as a
python module but with some restrictions indicated in Caveats.

## Using FreeCAD without GUI

The first, direct, easy, and useful application you can make of this is to
import FreeCAD documents into your program. In the following example, we'll
import the Part geometry of a FreeCAD document into
[blender](http://www.blender.org). Here is the complete script. I hope you'll
be impressed by its simplicity:

    
    
    FREECADPATH = '/usr/lib/freecad-python3/lib/' # path to your FreeCAD.so or FreeCAD.pyd file,
    # for Windows you must either use \\ or / in the path, using a single \ is problematic
    # FREECADPATH = 'C:\\FreeCAD\\bin'
    import Blender, sys
    sys.path.append(FREECADPATH)
     
    def import_fcstd(filename):
       try:
           import FreeCAD
       except ValueError:
           Blender.Draw.PupMenu('Error%t|FreeCAD library not found. Please check the FREECADPATH variable in the import script is correct')
       else:
           scene = Blender.Scene.GetCurrent()
           import Part
           doc = FreeCAD.open(filename)
           objects = doc.Objects
           for ob in objects:
               if ob.Type[:4] == 'Part':
                   shape = ob.Shape
                   if shape.Faces:
                       mesh = Blender.Mesh.New()
                       rawdata = shape.tessellate(1)
                       for v in rawdata[0]:
                           mesh.verts.append((v.x,v.y,v.z))
                       for f in rawdata[1]:
                           mesh.faces.append.append(f)
                       scene.objects.new(mesh,ob.Name)
           Blender.Redraw()
    
    def main():
       Blender.Window.FileSelector(import_fcstd, 'IMPORT FCSTD', 
                            Blender.sys.makename(ext='.fcstd'))    
     
    # This lets you import the script without running it
    if __name__=='__main__':
       main()
    

The first and important part is to make sure python will find our FreeCAD
library. Once it finds it, all FreeCAD modules such as Part (that we'll use as
well) will be available automatically. So we simply take the `sys.path`
variable, which is where python searches for modules, and we append the
FreeCAD library path. This modification is only temporary, and will be lost
when we'll close our python interpreter. An alternate way could be: making a
link to your FreeCAD library in one of the python search paths. I stored the
path in a constant (`FREECADPATH`) so it'll be easier for another user of the
script to configure it to their own system. For Windows users it is important
that the path be specified using `\\` or `/` as separator instead of just `\`
since it is an escape character.

    
    
    FREECADPATH = 'C:\\FreeCAD\\bin' # path to your FreeCAD.so or FreeCAD.pyd file
    import sys
    sys.path.append(FREECADPATH)
    

Once we are sure the library is loaded (the `try`/`except` sequence), we can
now work with FreeCAD, the same way as we would inside FreeCAD's own python
interpreter. We open the FreeCAD document that is passed to us by the `main()`
function, and we make a list of its objects. Then, as we chose only to care
about Part geometry, we check if the Type property of each object contains
"`Part`", then we tesselate it.

    
    
    import Part
           doc = FreeCAD.open(filename)
           objects = doc.Objects
           for ob in objects:
               if ob.Type[:4] == 'Part':
    

The tesselation produce a list of vertices and a list of faces defined by
vertices indexes. This is perfect, since it is exactly the same way as blender
defines meshes. So, our task is ridiculously simple, we just add both lists
contents to the verts and faces of a blender mesh. When everything is done, we
just redraw the screen, and that's it!

    
    
    if ob.Type[:4] == 'Part':
                   shape = ob.Shape
                   if shape.Faces:
                       mesh = Blender.Mesh.New()
                       rawdata = shape.tessellate(1)
                       for v in rawdata[0]:
                           mesh.verts.append((v.x,v.y,v.z))
                       for f in rawdata[1]:
                           mesh.faces.append.append(f)
                       scene.objects.new(mesh,ob.Name)
           Blender.Redraw()
    

Of course this script is very simple (in fact I made a more advanced [FreeCAD
to Blender
importer](https://yorik.uncreated.net/archive/scripts/blender24/import_freecad.py)),
you might want to extend it, for example importing mesh objects too, or
importing Part geometry that has no faces, or import other file formats that
FreeCAD can read. You might also want to export geometry to a FreeCAD
document, which can be done the same way. You might also want to build a
dialog, so the user can choose what to import, etc... The beauty of all this
actually lies in the fact that you let FreeCAD do the ground work while
presenting its results in the program of your choice.

_Note:_ checkout [Headless FreeCAD](/Headless_FreeCAD "Headless FreeCAD") for
running FreeCAD without the GUI.

## Using FreeCAD with GUI

From version 4.2 on Qt has the intriguing ability to embed Qt-GUI-dependent
plugins into non-Qt host applications and share the host's event loop.

Especially, for FreeCAD this means that it can be imported from within another
application with its whole user interface where the host application has full
control over FreeCAD, then.

The whole python code to achieve that has only two lines

    
    
    import FreeCADGui 
    FreeCADGui.showMainWindow()
    

If the host application is based on Qt then this solution should work on all
platforms which Qt supports. However, the host should link the same Qt version
as FreeCAD because otherwise you could run into unexpected runtime errors.

For non-Qt applications, however, there are a few limitations you must be
aware of. This solution probably doesn't work together with all other
toolkits. For Windows it works as long as the host application is directly
based on Win32 or any other toolkit that internally uses the Win32 API such as
wxWidgets, MFC or WinForms. In order to get it working under
[X11](https://en.wikipedia.org/wiki/X_Window_System) the host application must
link the [glib](https://docs.gtk.org/glib/) library.

Note, for any console application this solution of course doesn't work because
there is no event loop running.

## Caveats

Although it is possible to import FreeCAD to an external Python interpreter,
this is not a common usage scenario and requires some care. Generally, it is
better to use the Python included with FreeCAD, run FreeCAD via command line,
or as a subprocess. See [Start up and
Configuration](/Start_up_and_Configuration "Start up and Configuration") for
more on the last two options.

Since the FreeCAD Python module is compiled from C++ (rather than being a pure
Python module), it can only be imported from a compatible Python interpreter.
Generally this means that the Python interpreter must be compiled with the
same C compiler as was used to build FreeCAD. Information about the compiler
used to build a Python interpreter (including the one built with FreeCAD) can
be found as follows:

    
    
    >>> import sys
    >>> sys.version
    '2.7.13 (default, Dec 17 2016, 23:03:43) \n[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)]'
    

## Related

  * [Headless FreeCAD](/Headless_FreeCAD "Headless FreeCAD")

  

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
  * **Graphical interface:** [Interface creation](/Interface_creation "Interface creation"), [Interface creation completely in Python](/Dialog_creation "Dialog creation") ([1](/Dialog_creation_with_various_widgets "Dialog creation with various widgets"), [2](/Dialog_creation_reading_and_writing_files "Dialog creation reading and writing files"), [3](/Dialog_creation_setting_colors "Dialog creation setting colors"), [4](/Dialog_creation_image_and_animated_GIF "Dialog creation image and animated GIF"), [5](/PySide_usage_snippets "PySide usage snippets")), [PySide](/PySide "PySide"), PySide examples [beginner](/PySide_Beginner_Examples "PySide Beginner Examples"), [intermediate](/PySide_Intermediate_Examples "PySide Intermediate Examples"), [advanced](/PySide_Advanced_Examples "PySide Advanced Examples")
  * **Macros:** [Macros](/Macros "Macros"), [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** Embedding FreeCAD, [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

