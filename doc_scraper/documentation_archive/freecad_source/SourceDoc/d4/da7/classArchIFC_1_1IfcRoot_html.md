---
url: https://freecad.github.io/SourceDoc/d4/da7/classArchIFC_1_1IfcRoot.html
scraped_at: 2025-09-08T14:57:51.273207
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [ArchIFC](../../de/d6f/namespaceArchIFC.html)
  * [IfcRoot](../../d4/da7/classArchIFC_1_1IfcRoot.html)

[List of all members](../../d1/d96/classArchIFC_1_1IfcRoot-members.html) | Public Member Functions

ArchIFC.IfcRoot Class Reference

##  Public Member Functions  
  
---  
def | [addIfcAttribute](../../d4/da7/classArchIFC_1_1IfcRoot.html#ab7c9808570241f10e88758d133847126) (self, obj, attribute)  
def | [addIfcAttributes](../../d4/da7/classArchIFC_1_1IfcRoot.html#aa5ebaf1c079500bd27c59afbb27d3187) (self, ifcTypeSchema, obj)  
def | [addIfcAttributeValueExpressions](../../d4/da7/classArchIFC_1_1IfcRoot.html#a906dec9543d3dbf5d07d4d06bb03ea71) (self, obj, attribute)  
def | [getCanonicalisedIfcTypes](../../d4/da7/classArchIFC_1_1IfcRoot.html#a8db35c1d257efce75535aa22f5423d72) (self)  
def | [getIfcAttributeSchema](../../d4/da7/classArchIFC_1_1IfcRoot.html#a2ab9341d531f46f4e2cfc298b88653f5) (self, ifcTypeSchema, name)  
def | [getIfcSchema](../../d4/da7/classArchIFC_1_1IfcRoot.html#a1abc46a43fd39bed50ffd2fe0329cccf) (self)  
def | [getIfcTypeSchema](../../d4/da7/classArchIFC_1_1IfcRoot.html#a7f15ded5bae325bfd4f920d1533e5a5e) (self, IfcType)  
def | [getObjIfcComplexAttribute](../../d4/da7/classArchIFC_1_1IfcRoot.html#abd6e51a58b1c8aed5893cd0cf43f63bb) (self, obj, attributeName)  
def | [migrateDeprecatedAttributes](../../d4/da7/classArchIFC_1_1IfcRoot.html#a503f3b8410e6533d4185e24102637af2) (self, obj)  
def | [onChanged](../../d4/da7/classArchIFC_1_1IfcRoot.html#abde72ec687dc6401837824722d16d9ea) (self, obj, prop)  
def | [purgeUnusedIfcAttributesFromPropertiesList](../../d4/da7/classArchIFC_1_1IfcRoot.html#a3d4b25db8f94b4810f5fcef008b021ab) (self, ifcTypeSchema, obj)  
def | [setObjIfcAttributeValue](../../d4/da7/classArchIFC_1_1IfcRoot.html#a5f1380f722823e4fac892a1a05076256) (self, obj, attributeName, value)  
def | [setObjIfcComplexAttributeValue](../../d4/da7/classArchIFC_1_1IfcRoot.html#a320c53d77ddddee77dcd33ecbb0fcb44) (self, obj, attributeName, value)  
def | [setProperties](../../d4/da7/classArchIFC_1_1IfcRoot.html#a085b21fd2e99fa8a5ac287d97fbe7fa2) (self, obj)  
def | [setupIfcAttributes](../../d4/da7/classArchIFC_1_1IfcRoot.html#af4c72df4764acc9c3f0edd77cce20627) (self, obj)  
def | [setupIfcComplexAttributes](../../d4/da7/classArchIFC_1_1IfcRoot.html#a6f01e2ef7ddbae31c1816317023b9d68) (self, obj)  
  
## Detailed Description

    
    
    This class defines the common methods and properties for managing IFC data.
    
    IFC, or Industry Foundation Classes are a standardised way to digitally
    describe the built environment.  The ultimate goal of IFC is to provide
    better interoperability between software that deals with the built
    environment. You can learn more here:
    https://technical.buildingsmart.org/standards/ifc/
    
    You can learn more about the technical details of the IFC schema here:
    https://standards.buildingsmart.org/IFC/RELEASE/IFC4/FINAL/HTML/
    
    This class is further segmented down into IfcProduct and IfcContext.
    

## Member Function Documentation

## ◆ addIfcAttribute()

def ArchIFC.IfcRoot.addIfcAttribute  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _attribute_  
| ) | |   
      
    
    Add an IFC type's attribute to the object, within its properties.
    
    Add the attribute's schema to the object's IfcData property, as an
    item under its "attributes" array.
    
    Also add the attribute as a property of the object.
    
    Parameters
    ----------
    attribute: dict
        The attribute to add. Should have the structure of an attribute
        found within the IFC schemas.
    

References
[ArchIFC.QT_TRANSLATE_NOOP()](../../de/d6f/namespaceArchIFC.html#af7187f8c6eea71823036472da4633840).

Referenced by
[ArchIFC.IfcRoot.addIfcAttributes()](../../d4/da7/classArchIFC_1_1IfcRoot.html#aa5ebaf1c079500bd27c59afbb27d3187).

## ◆ addIfcAttributes()

def ArchIFC.IfcRoot.addIfcAttributes  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _ifcTypeSchema_ ,   
|  |  | _obj_  
| ) | |   
      
    
    Add the attributes of the IFC type's schema to the object's properties.
    
    Add the attributes as properties of the object. Also add the
    attribute's schema within the object's IfcData property. Do so using
    the .addIfcAttribute() method.
    
    Also add expressions to copy data from the object's editable
    properties.  This means the IFC properties will remain accurate with
    the actual values of the object. Do not do so for all IFC properties.
    Do so using the .addIfcAttributeValueExpressions() method.
    
    Learn more about expressions here:
    https://wiki.freecadweb.org/Expressions
    
    Do not add the attribute if the object has a property with the
    attribute's name. Also do not add the attribute if its name is
    RefLatitude, RefLongitude, or Name.
    
    Parameters
    ----------
    ifcTypeSchema: dict
        The schema of the IFC type.
    

References
[ArchIFC.IfcRoot.addIfcAttribute()](../../d4/da7/classArchIFC_1_1IfcRoot.html#ab7c9808570241f10e88758d133847126),
and
[ArchIFC.IfcRoot.addIfcAttributeValueExpressions()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a906dec9543d3dbf5d07d4d06bb03ea71).

Referenced by
[ArchIFC.IfcRoot.setupIfcAttributes()](../../d4/da7/classArchIFC_1_1IfcRoot.html#af4c72df4764acc9c3f0edd77cce20627).

## ◆ addIfcAttributeValueExpressions()

def ArchIFC.IfcRoot.addIfcAttributeValueExpressions  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _attribute_  
| ) | |   
      
    
    Add expressions for IFC attributes, so they stay accurate with the object.
    
    Add expressions to the object that copy data from the editable
    properties of the object. This ensures that the IFC attributes will
    remain accurate with the actual values of the object.
    
    Currently, add expressions for the following IFC attributes:
    
    - OverallWidth
    - OverallHeight
    - ElevationWithFlooring
    - Elevation
    - NominalDiameter
    - BarLength
    - RefElevation
    - LongName
    
    Learn more about expressions here:
    https://wiki.freecadweb.org/Expressions
    
    Parameters
    ----------
    attribute: dict
        The schema of the attribute to add the expression for.
    

Referenced by
[ArchIFC.IfcRoot.addIfcAttributes()](../../d4/da7/classArchIFC_1_1IfcRoot.html#aa5ebaf1c079500bd27c59afbb27d3187).

## ◆ getCanonicalisedIfcTypes()

def ArchIFC.IfcRoot.getCanonicalisedIfcTypes  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    Get the names of IFC types, converted to the form used in Arch.
    
    Change the names of all IFC types to a more human readable form which
    is used instead throughout Arch instead of the raw type names. The
    names have the "Ifc" stripped from the start of their name, and spaces
    inserted between the words.
    
    Returns
    -------
    list of str
        The list of every IFC type name in their form used in Arch. List
        will have names in the same order as they appear in the schema's
        JSON, as per the .keys() method of dicts.

References
[ArchIFC.IfcRoot.getIfcSchema()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a1abc46a43fd39bed50ffd2fe0329cccf),
[ArchIFC.IfcProduct.getIfcSchema()](../../d9/db7/classArchIFC_1_1IfcProduct.html#a29f8b58103b9a31db34fc38480a831c9),
and
[ArchIFC.IfcContext.getIfcSchema()](../../d1/d50/classArchIFC_1_1IfcContext.html#ab258711f7bad7ab3fa4e1f8aa26872a9).

Referenced by
[ArchIFC.IfcRoot.setProperties()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a085b21fd2e99fa8a5ac287d97fbe7fa2).

## ◆ getIfcAttributeSchema()

def ArchIFC.IfcRoot.getIfcAttributeSchema  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _ifcTypeSchema_ ,   
|  |  | _name_  
| ) | |   
      
    
    Get the schema of an IFC attribute with the given name.
    
    Convert the IFC attribute's name from the human readable version Arch
    uses, and convert it to the less readable name it has in the IFC
    schema.
    
    Parameters
    ----------
    ifcTypeSchema: dict
        The schema of the IFC type to access the attribute of.
    name: str
        The name the attribute has in Arch.
    
    Returns
    -------
    dict
        Returns the schema of the attribute.
    None
        Returns None if the IFC type does not have the attribute requested.

Referenced by
[ArchIFC.IfcRoot.purgeUnusedIfcAttributesFromPropertiesList()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a3d4b25db8f94b4810f5fcef008b021ab).

## ◆ getIfcSchema()

def ArchIFC.IfcRoot.getIfcSchema  | ( |  | _self_| ) |   
---|---|---|---|---|---  
      
    
    Get the IFC schema of all types relevant to this class.
    
    Intended to be overwritten by the classes that inherit this class.
    
    Returns
    -------
    dict
        The schema of all the types relevant to this class.
    

Reimplemented in
[ArchIFC.IfcProduct](../../d9/db7/classArchIFC_1_1IfcProduct.html#a29f8b58103b9a31db34fc38480a831c9),
and
[ArchIFC.IfcContext](../../d1/d50/classArchIFC_1_1IfcContext.html#ab258711f7bad7ab3fa4e1f8aa26872a9).

Referenced by
[ArchIFC.IfcRoot.getCanonicalisedIfcTypes()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a8db35c1d257efce75535aa22f5423d72),
and
[ArchIFC.IfcRoot.getIfcTypeSchema()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a7f15ded5bae325bfd4f920d1533e5a5e).

## ◆ getIfcTypeSchema()

def ArchIFC.IfcRoot.getIfcTypeSchema  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _IfcType_  
| ) | |   
      
    
    Get the schema of the IFC type provided.
    
    If the IFC type is undefined, return the schema of the
    IfcBuildingElementProxy.
    
    Parameter
    ---------
    IfcType: str
        The IFC type whose schema you want.
    
    Returns
    -------
    dict
        Returns the schema of the type as a dict.
    None
        Returns None if the IFC type does not exist.
    

References
[ArchIFC.IfcRoot.getIfcSchema()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a1abc46a43fd39bed50ffd2fe0329cccf),
[ArchIFC.IfcProduct.getIfcSchema()](../../d9/db7/classArchIFC_1_1IfcProduct.html#a29f8b58103b9a31db34fc38480a831c9),
and
[ArchIFC.IfcContext.getIfcSchema()](../../d1/d50/classArchIFC_1_1IfcContext.html#ab258711f7bad7ab3fa4e1f8aa26872a9).

Referenced by
[ArchIFC.IfcRoot.setupIfcAttributes()](../../d4/da7/classArchIFC_1_1IfcRoot.html#af4c72df4764acc9c3f0edd77cce20627),
and
[ArchIFC.IfcRoot.setupIfcComplexAttributes()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a6f01e2ef7ddbae31c1816317023b9d68).

## ◆ getObjIfcComplexAttribute()

def ArchIFC.IfcRoot.getObjIfcComplexAttribute  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _attributeName_  
| ) | |   
      
    
    Get the value of the complex attribute, as stored in the IfcData JSON.
    
    Parameters
    ----------
    attributeName: str
        The name of the complex attribute to access.
    
    Returns
    -------
    The value of the complex attribute.
    

Referenced by
[ArchIFCView.IfcContextUI.prefillMapConversionForm()](../../d6/d87/classArchIFCView_1_1IfcContextUI.html#a0544c623b3745c8d7f0ec61e095e6ba4).

## ◆ migrateDeprecatedAttributes()

def ArchIFC.IfcRoot.migrateDeprecatedAttributes  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
      
    
    Update the object to use the newer property names for IFC related properties.
    

Referenced by
[ArchIFC.IfcRoot.setProperties()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a085b21fd2e99fa8a5ac287d97fbe7fa2).

## ◆ onChanged()

def ArchIFC.IfcRoot.onChanged  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _prop_  
| ) | |   
      
    
    Method called when the object has a property changed.
    
    If the object's IfcType has changed, change the object's properties
    that relate to IFC attributes in order to match the IFC schema
    definition of the new IFC type.
    
    If a property changes that is in the "IFC Attributes" group, also
    change the value stored in the IfcData property's JSON.
    
    Parameters
    ----------
    prop: string
        The name of the property that has changed.
    

Reimplemented in
[ArchBuildingPart.BuildingPart](../../d2/def/classArchBuildingPart_1_1BuildingPart.html#af29a6f8f0bd35ef5779a12f9bfc3c26e),
[ArchComponent.Component](../../de/d87/classArchComponent_1_1Component.html#ac10328dd9515bdac2dd7e11861c4609e),
[ArchCurtainWall.CurtainWall](../../d3/ddd/classArchCurtainWall_1_1CurtainWall.html#acbae8cc86609f0e9ef6cfe9a7078901f),
and
[ArchTruss.Truss](../../d9/d6f/classArchTruss_1_1Truss.html#ad5bacb59d6610e87c0aad5a4dc7f8987).

References
[ArchIFC.IfcRoot.setObjIfcAttributeValue()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a5f1380f722823e4fac892a1a05076256),
[ArchIFC.IfcRoot.setupIfcAttributes()](../../d4/da7/classArchIFC_1_1IfcRoot.html#af4c72df4764acc9c3f0edd77cce20627),
and
[ArchIFC.IfcRoot.setupIfcComplexAttributes()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a6f01e2ef7ddbae31c1816317023b9d68).

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftviewproviders.view_base.ViewProviderDraft.attach()](../../d6/d1b/classdraftviewproviders_1_1view__base_1_1ViewProviderDraft.html#af35acb7285aa095bf670e82338c9462d),
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[draftobjects.wire.Wire.execute()](../../d4/d14/classdraftobjects_1_1wire_1_1Wire.html#ad931a4e79d7d0516803bf1a8a33e7655),
[ArchBuildingPart.ViewProviderBuildingPart.updateData()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a12d40383666b8987a3277ea26454995d),
[ArchPanel.ViewProviderPanelCut.updateData()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a970ed7e44ebec3c959dcb48bf60b2d31),
[ArchPanel.ViewProviderPanelSheet.updateData()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a916cdf8131f60494dabf61e971d1a093),
[draftviewproviders.view_label.ViewProviderLabel.updateData()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#aab195af09dd4fbe60e1bb38d362385ba),
[draftviewproviders.view_layer.ViewProviderLayer.updateData()](../../d5/dcb/classdraftviewproviders_1_1view__layer_1_1ViewProviderLayer.html#a9c641727fd15eaa141c8a58837e14248),
and
[draftviewproviders.view_wpproxy.ViewProviderWorkingPlaneProxy.updateData()](../../da/dbf/classdraftviewproviders_1_1view__wpproxy_1_1ViewProviderWorkingPlaneProxy.html#ad58eb6ce87860ff0389b3498143d11c7).

## ◆ purgeUnusedIfcAttributesFromPropertiesList()

def ArchIFC.IfcRoot.purgeUnusedIfcAttributesFromPropertiesList  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _ifcTypeSchema_ ,   
|  |  | _obj_  
| ) | |   
      
    
    Remove properties representing IFC attributes if they no longer appear.
    
    Remove the property representing an IFC attribute, if it does not
    appear in the schema of the IFC type provided. Also, remove the
    property if its attribute is an enum type, presumably for backwards
    compatibility.
    
    Learn more about IFC enums here:
    https://standards.buildingsmart.org/IFC/RELEASE/IFC4/FINAL/HTML/schema/chapter-3.htm#enumeration
    

References
[ArchIFC.IfcRoot.getIfcAttributeSchema()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a2ab9341d531f46f4e2cfc298b88653f5).

Referenced by
[ArchIFC.IfcRoot.setupIfcAttributes()](../../d4/da7/classArchIFC_1_1IfcRoot.html#af4c72df4764acc9c3f0edd77cce20627).

## ◆ setObjIfcAttributeValue()

def ArchIFC.IfcRoot.setObjIfcAttributeValue  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _attributeName_ ,   
|  |  | _value_  
| ) | |   
      
    
    Change the value of an IFC attribute within the IfcData property's json.
    
    Parameters
    ----------
    attributeName: str
        The name of the attribute to change.
    value:
        The new value to set.
    

Referenced by
[ArchIFC.IfcRoot.onChanged()](../../d4/da7/classArchIFC_1_1IfcRoot.html#abde72ec687dc6401837824722d16d9ea).

## ◆ setObjIfcComplexAttributeValue()

def ArchIFC.IfcRoot.setObjIfcComplexAttributeValue  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_ ,   
|  |  | _attributeName_ ,   
|  |  | _value_  
| ) | |   
      
    
    Changes the value of the complex attribute in the IfcData property JSON.
    
    Parameters
    ----------
    attributeName: str
        The name of the attribute to change.
    value:
        The new value to set.
    

Referenced by
[ArchIFCView.IfcContextUI.accept()](../../d6/d87/classArchIFCView_1_1IfcContextUI.html#ab7d354b99609992d4e72469f8a78e1a0),
and
[importIFCHelper.ProjectImporter.setComplexAttributes()](../../d0/d2c/classimportIFCHelper_1_1ProjectImporter.html#a348daed84b62f0bd0f8503772ff8bf40).

## ◆ setProperties()

def ArchIFC.IfcRoot.setProperties  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
      
    
    Give the object properties for storing IFC data.
    
    Also migrate old versions of IFC properties to the new property names
    using the .migrateDeprecatedAttributes() method.
    

Reimplemented in
[ArchBuildingPart.BuildingPart](../../d2/def/classArchBuildingPart_1_1BuildingPart.html#a01e29cb1d764fda7df9055fe009dbf35),
[ArchComponent.Component](../../de/d87/classArchComponent_1_1Component.html#a83f183119924946069f3b00947ec9793),
[ArchCurtainWall.CurtainWall](../../d3/ddd/classArchCurtainWall_1_1CurtainWall.html#a1c7351250cd02e8b790e5ed84ebe7553),
and
[ArchTruss.Truss](../../d9/d6f/classArchTruss_1_1Truss.html#a90f32bb2105867d75078e021f1ba771c).

References
[ArchIFC.IfcRoot.getCanonicalisedIfcTypes()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a8db35c1d257efce75535aa22f5423d72),
[ArchIFC.IfcRoot.migrateDeprecatedAttributes()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a503f3b8410e6533d4185e24102637af2),
and
[ArchIFC.QT_TRANSLATE_NOOP()](../../de/d6f/namespaceArchIFC.html#af7187f8c6eea71823036472da4633840).

Referenced by
[ArchPanel.CommandPanelSheet.Activated()](../../d1/d94/classArchPanel_1_1CommandPanelSheet.html#abed1cd5ce53c5b156683ae24b81f75e4),
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[ArchSite.Compass.buildCoordinates()](../../d9/d61/classArchSite_1_1Compass.html#a4d1848dd6968a22f62d75ec9c71dddcd),
[ArchSchedule.CommandArchSchedule.IsActive()](../../d3/d2d/classArchSchedule_1_1CommandArchSchedule.html#aea4e379076ac7837ef44222df95fd97a),
[ArchBuildingPart.BuildingPart.onDocumentRestored()](../../d2/def/classArchBuildingPart_1_1BuildingPart.html#a8029b4336a228315b03abd4cbe009001),
[ArchCurtainWall.CurtainWall.onDocumentRestored()](../../d3/ddd/classArchCurtainWall_1_1CurtainWall.html#a95c6772213f7a083a0dd81eef6163150),
[ArchGrid.ArchGrid.onDocumentRestored()](../../d7/d52/classArchGrid_1_1ArchGrid.html#af3945be9606a8a88bdfdeb840068ca5d),
[ArchPanel.PanelView.onDocumentRestored()](../../dd/da0/classArchPanel_1_1PanelView.html#a6e956704109979457399259409b3c12e),
[ArchPanel.PanelCut.onDocumentRestored()](../../d6/dbd/classArchPanel_1_1PanelCut.html#a81bcbc2154418c01c75c606932184aee),
[ArchPanel.PanelSheet.onDocumentRestored()](../../dc/d22/classArchPanel_1_1PanelSheet.html#afb1ed907e00ab4c552d73f932a3beb6e),
[ArchTruss.Truss.onDocumentRestored()](../../d9/d6f/classArchTruss_1_1Truss.html#abf7290b67c66f8b38f2f24c3a913eb7d),
[draftobjects.hatch.Hatch.onDocumentRestored()](../../db/d7f/classdraftobjects_1_1hatch_1_1Hatch.html#a5f4a52b199d98d8ef1bf681170a39214),
[draftobjects.shape2dview.Shape2DView.onDocumentRestored()](../../dc/d42/classdraftobjects_1_1shape2dview_1_1Shape2DView.html#aeb419e3492426690e6df5043bdd8fbf3),
[ArchBuildingPart.ViewProviderBuildingPart.onDocumentRestored()](../../d8/dbf/classArchBuildingPart_1_1ViewProviderBuildingPart.html#a77d1c4103e062b3ee3d06a348b25310f),
[ArchPanel.ViewProviderPanelCut.onDocumentRestored()](../../d6/db4/classArchPanel_1_1ViewProviderPanelCut.html#a97810dc3b020c64a4352d53c96ee8500),
and
[ArchPanel.ViewProviderPanelSheet.onDocumentRestored()](../../d9/d71/classArchPanel_1_1ViewProviderPanelSheet.html#a4b5aa2a21de0a9ebd24cb59e54e54994).

## ◆ setupIfcAttributes()

def ArchIFC.IfcRoot.setupIfcAttributes  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
      
    
    Set up the IFC attributes in the object's properties.
    
    Add the attributes specified in the object's IFC type schema, to the
    object's properties. Do not re-add them if they're already present.
    Also remove old IFC attribute properties that no longer appear in the
    schema for backwards compatibility.
    
    Do so using the .addIfcAttributes() and
    .purgeUnusedIfcAttributesFromPropertiesList() methods.
    
    Learn more about IFC attributes here:
    https://standards.buildingsmart.org/IFC/RELEASE/IFC4/FINAL/HTML/schema/chapter-3.htm#attribute
    

References
[ArchIFC.IfcRoot.addIfcAttributes()](../../d4/da7/classArchIFC_1_1IfcRoot.html#aa5ebaf1c079500bd27c59afbb27d3187),
[ArchIFC.IfcRoot.getIfcTypeSchema()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a7f15ded5bae325bfd4f920d1533e5a5e),
and
[ArchIFC.IfcRoot.purgeUnusedIfcAttributesFromPropertiesList()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a3d4b25db8f94b4810f5fcef008b021ab).

Referenced by
[ArchIFC.IfcRoot.onChanged()](../../d4/da7/classArchIFC_1_1IfcRoot.html#abde72ec687dc6401837824722d16d9ea).

## ◆ setupIfcComplexAttributes()

def ArchIFC.IfcRoot.setupIfcComplexAttributes  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _obj_  
| ) | |   
      
    
    Add the IFC type's complex attributes to the object.
    
    Get the object's IFC type schema, and add the schema for the type's
    complex attributes within the IfcData property.
    

References
[ArchIFC.IfcRoot.getIfcTypeSchema()](../../d4/da7/classArchIFC_1_1IfcRoot.html#a7f15ded5bae325bfd4f920d1533e5a5e).

Referenced by
[ArchIFC.IfcRoot.onChanged()](../../d4/da7/classArchIFC_1_1IfcRoot.html#abde72ec687dc6401837824722d16d9ea).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Arch/ArchIFC.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

