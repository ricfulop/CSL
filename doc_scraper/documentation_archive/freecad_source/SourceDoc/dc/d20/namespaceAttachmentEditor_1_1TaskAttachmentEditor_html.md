---
url: https://freecad.github.io/SourceDoc/dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html
scraped_at: 2025-09-08T14:58:57.510921
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [AttachmentEditor](../../dc/d1a/namespaceAttachmentEditor.html)
  * [TaskAttachmentEditor](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html)

Classes | Functions | Variables

AttachmentEditor.TaskAttachmentEditor Namespace Reference

##  Classes  
  
---  
class | [AttachmentEditorTaskPanel](../../d8/d4c/classAttachmentEditor_1_1TaskAttachmentEditor_1_1AttachmentEditorTaskPanel.html)  
class | [CancelError](../../d8/d25/classAttachmentEditor_1_1TaskAttachmentEditor_1_1CancelError.html)  
  
##  Functions  
  
---  
def | [getAllDependent](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#ad8f22f93fa7f0f9f181693a369d654df) (feature)  
def | [GetSelectionAsLinkSubList](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#ac8866e862b6d3fd75c9b2b2de6e63ce3) ()  
def | [LinkFromStr](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#a6625269fcda921b886feebb09b5a2ba4) (strlink, document)  
def | [linkSubList_convertToOldStyle](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#ae309fb1c805b913c7332b8f32e5b56e0) (references)  
def | [PlacementsFuzzyCompare](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#af45a32298879302ebceb1ad63fb7eaa0) (plm1, plm2)  
def | [RefsFromStrList](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#a483b69f8093c6728facb140b37163e51) (strings, document)  
def | [StrFromLink](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#ae07a455dea9e49a238b37b0b4caffb6e) (feature, subname)  
def | [StrListFromRefs](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#a872031115d682e1a110250d19f992298) (references)  
def | [TempoVis](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#aef74e32725837b0f504d6cbf98984447) (doc, tag)  
  
##  Variables  
  
---  
|
[deg](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#a1ee8b912c4414151983f71bca5460c9e)
= App.Units.Degree  
|
[mm](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#a9b0b4b037ccd829b9feb4b2d2cee26d3)
= App.Units.MilliMetre  
|
[Q](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#ad69eb48eb6af2fa6c96b84e7f138cc36)
= App.Units.Quantity  
|
[translate](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#a4160223378154f683af83d29e143acda)
= App.Qt.translate  
  
## Function Documentation

## ◆ getAllDependent()

def AttachmentEditor.TaskAttachmentEditor.getAllDependent  | ( |  | _feature_| ) |   
---|---|---|---|---|---  
  
Referenced by
[AttachmentEditor.TaskAttachmentEditor.AttachmentEditorTaskPanel.addSelection()](../../d8/d4c/classAttachmentEditor_1_1TaskAttachmentEditor_1_1AttachmentEditorTaskPanel.html#aaa42ce1862ba2b811d8b78e5f90c6baf).

## ◆ GetSelectionAsLinkSubList()

def AttachmentEditor.TaskAttachmentEditor.GetSelectionAsLinkSubList  | ( | | ) |   
---|---|---|---|---  
  
## ◆ LinkFromStr()

def AttachmentEditor.TaskAttachmentEditor.LinkFromStr  | ( |  | _strlink_ ,   
---|---|---|---  
|  |  | _document_  
| ) | |   
  
Referenced by
[AttachmentEditor.TaskAttachmentEditor.AttachmentEditorTaskPanel.addSelection()](../../d8/d4c/classAttachmentEditor_1_1TaskAttachmentEditor_1_1AttachmentEditorTaskPanel.html#aaa42ce1862ba2b811d8b78e5f90c6baf),
and
[AttachmentEditor.TaskAttachmentEditor.RefsFromStrList()](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#a483b69f8093c6728facb140b37163e51).

## ◆ linkSubList_convertToOldStyle()

def AttachmentEditor.TaskAttachmentEditor.linkSubList_convertToOldStyle  | ( |  | _references_| ) |   
---|---|---|---|---|---  
  
Referenced by
[AttachmentEditor.TaskAttachmentEditor.StrListFromRefs()](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#a872031115d682e1a110250d19f992298).

## ◆ PlacementsFuzzyCompare()

def AttachmentEditor.TaskAttachmentEditor.PlacementsFuzzyCompare  | ( |  | _plm1_ ,   
---|---|---|---  
|  |  | _plm2_  
| ) | |   
  
Referenced by
[AttachmentEditor.TaskAttachmentEditor.AttachmentEditorTaskPanel.updatePreview()](../../d8/d4c/classAttachmentEditor_1_1TaskAttachmentEditor_1_1AttachmentEditorTaskPanel.html#ac9346cec8bcab000c5423d7449239e27).

## ◆ RefsFromStrList()

def AttachmentEditor.TaskAttachmentEditor.RefsFromStrList  | ( |  | _strings_ ,   
---|---|---|---  
|  |  | _document_  
| ) | |   
      
    
    input: strings as from UI. Output: list of tuples that can be assigned to PropertyLinkSubList.

References
[AttachmentEditor.TaskAttachmentEditor.LinkFromStr()](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#a6625269fcda921b886feebb09b5a2ba4).

Referenced by
[AttachmentEditor.TaskAttachmentEditor.AttachmentEditorTaskPanel.parseAllRefLines()](../../d8/d4c/classAttachmentEditor_1_1TaskAttachmentEditor_1_1AttachmentEditorTaskPanel.html#ac2904be900b2fe522fdd2381099dc522).

## ◆ StrFromLink()

def AttachmentEditor.TaskAttachmentEditor.StrFromLink  | ( |  | _feature_ ,   
---|---|---|---  
|  |  | _subname_  
| ) | |   
  
Referenced by
[AttachmentEditor.TaskAttachmentEditor.AttachmentEditorTaskPanel.addSelection()](../../d8/d4c/classAttachmentEditor_1_1TaskAttachmentEditor_1_1AttachmentEditorTaskPanel.html#aaa42ce1862ba2b811d8b78e5f90c6baf),
and
[AttachmentEditor.TaskAttachmentEditor.StrListFromRefs()](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#a872031115d682e1a110250d19f992298).

## ◆ StrListFromRefs()

def AttachmentEditor.TaskAttachmentEditor.StrListFromRefs  | ( |  | _references_| ) |   
---|---|---|---|---|---  
      
    
    input: PropertyLinkSubList. Output: list of strings for UI.

References
[AttachmentEditor.TaskAttachmentEditor.linkSubList_convertToOldStyle()](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#ae309fb1c805b913c7332b8f32e5b56e0),
and
[AttachmentEditor.TaskAttachmentEditor.StrFromLink()](../../dc/d20/namespaceAttachmentEditor_1_1TaskAttachmentEditor.html#ae07a455dea9e49a238b37b0b4caffb6e).

Referenced by
[AttachmentEditor.TaskAttachmentEditor.AttachmentEditorTaskPanel.fillAllRefLines()](../../d8/d4c/classAttachmentEditor_1_1TaskAttachmentEditor_1_1AttachmentEditorTaskPanel.html#a23cc57d2b65ca4230bb2876c2bb5a449).

## ◆ TempoVis()

def AttachmentEditor.TaskAttachmentEditor.TempoVis  | ( |  | _doc_ ,   
---|---|---|---  
|  |  | _tag_  
| ) | |   
  
## Variable Documentation

## ◆ deg

AttachmentEditor.TaskAttachmentEditor.deg = App.Units.Degree  
---  
  
## ◆ mm

AttachmentEditor.TaskAttachmentEditor.mm = App.Units.MilliMetre  
---  
  
## ◆ Q

AttachmentEditor.TaskAttachmentEditor.Q = App.Units.Quantity  
---  
  
Referenced by
[AttachmentEditor.TaskAttachmentEditor.AttachmentEditorTaskPanel.attachmentOffsetChanged()](../../d8/d4c/classAttachmentEditor_1_1TaskAttachmentEditor_1_1AttachmentEditorTaskPanel.html#a8fff02fcd77197d71d886c9e3e4992a1).

## ◆ translate

AttachmentEditor.TaskAttachmentEditor.translate = App.Qt.translate  
---  
  
* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

