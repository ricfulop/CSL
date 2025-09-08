# Engineering & Design Software – API Documentation Reference

This document lists the **official API documentation locations** for major CAD, EDA, BIM, and design tools.  
It is intended as a quick reference for building CSL/Triple Lindy adapters.

---

## 🧩 CAD Systems

| Tool                          | API Docs                                                     |
|-------------------------------|--------------------------------------------------------------|
| **Autodesk Fusion 360**       | [Fusion Automation API \(GA\)](https://aps.autodesk.com/developer/overview/design-automation-api) · [Fusion 360 API Home](https://aps.autodesk.com/developer/overview/autodesk-fusion-api?check_logged_in=1)[Help](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-A92A4B10-3781-4925-94C6-47DA85A4F65A) |
| **Autodesk Inventor**         | [Inventor API Reference](https://aps.autodesk.com/developer/overview/inventor) |
| **SolidWorks**                | [SolidWorks API Help](https://help.solidworks.com/2025/english/api/sldworksapiprogguide/Welcome.htm) |
| **Siemens NX**                | [NX Open (C++, C#, Java, Python)](https://docs.plm.automation.siemens.com/data_services/resources/nx/) |
| **CATIA (Dassault Systèmes)** | [CAA V5 Automation Docs (login required)](https://dsxclient.3ds.com) |
| **Onshape**                   | [REST API Explorer](https://cad.onshape.com/glassworks/explorer) · [FeatureScript Docs](https://cad.onshape.com/FsDoc/) |
| **PTC Creo**                  | [Creo Toolkit / J-Link / Web.Link](https://support.ptc.com/help/creo/) |
| **FreeCAD**                   | [FreeCAD Python API](https://wiki.freecad.org/Api)[Help TOC](https://wiki.freecad.org/Online_Help_Toc)[FreeCAD source documentation](https://freecad.github.io/SourceDoc/index.html)[Github Repo](https://github.com/FreeCAD/FreeCAD) |
| **Blender**                   | [Blender Python API](https://docs.blender.org/api/current/)  |

---

## ⚡ EDA / Electronics CAD

| Tool                                         | API Docs                                                     |
|----------------------------------------------|--------------------------------------------------------------|
| **KiCad**                                    | [KiCad Python API Reference](https://klc.kicad.org)          |
| **Altium Designer**                          | [Altium Scripting & SDK Docs](https://www.altium.com/documentation/altium-365/requirements-systems-portal/rest-python-api-documentation) |
| **Cadence (OrCAD/Allegro)**                  | [SKILL Language Docs \(login required\)](https://support.cadence.com/apex/Coveo_CommunitySearch#q=python%2520api&t=AllContent&searchboxDropdown=1&firstQueryCause=omniboxFromLink&firstQueryMeta=%7B%2522expression%2522:%2522python%2520api%2522%2520,%2520%2522advancedExpression%2522:%2522%2522%2520,%2520%2522JSUIVersion%2522:%25222.10095.2%253B2.10095.2%2522%2520,%2520%2522accountName%2522:%2522Massachusetts%2520Institute%2520of%2520Tech%2522%2520,%2520%2522accountId%2522:%2522001d000000HqdJRAAZ%2522%7D) |
| **Mentor Graphics (Siemens EDA, Xpedition)** | Siemens Support Portal (login required)                      |

---

## 🏗️ BIM / Architecture

| Tool                    | API Docs                                                     |
|-------------------------|--------------------------------------------------------------|
| **Autodesk Revit**      | [Revit API Docs](https://help.autodesk.com/view/RVT/ENU/?guid=GUID-API-Home) |
| **Autodesk AutoCAD**    | [AutoCAD .NET/ObjectARX API](https://help.autodesk.com/view/ACD/ENU/?guid=GUID-API-Home) |
| **Rhino (McNeel)**      | [RhinoCommon .NET API](https://developer.rhino3d.com/api/RhinoCommon/)[Rhino and Grasshopper Developer Documentation](https://developer.rhino3d.com/) |
| **Grasshopper (Rhino)** | [Grasshopper SDK Docs](https://developer.rhino3d.com/api/grasshopper/)[Rhino and Grasshopper Developer Documentation](https://developer.rhino3d.com/) |
| **Higharc**             | Developer API not public (available to partners only)        |

---

## 🎬 Design & Media (Geometry / Asset Crossover)

| Tool | API Docs |
|------|----------|
| **Unreal Engine** | [Unreal API Docs](https://docs.unrealengine.com/) |
| **Unity** | [Unity Scripting API (C#)](https://docs.unity3d.com/ScriptReference/) |

---

### Notes

- Some APIs (CATIA, NX, Creo, Cadence, Mentor) require vendor login or licensed SDK access.  
- Open-source tools (FreeCAD, Blender, KiCad) provide free public documentation.  
- Use this table to align CSL adapters with each tool’s scripting environment.

---

✅ **Ready for use with CSL/Triple Lindy orchestration**.  
