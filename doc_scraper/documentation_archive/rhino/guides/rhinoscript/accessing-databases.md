---
url: https://developer.rhino3d.com/guides/rhinoscript/accessing-databases/
scraped_at: 2025-09-08T15:42:31.211247
title: Untitled
---

[RhinoDeveloper®](/)

[design, model, present, analyze, realize...](/)

[![Rhino Logo](https://developer.rhino3d.com/images/rhinodevlogo.png)](/)

__

[Guides](https://developer.rhino3d.com/guides)
[Samples](https://developer.rhino3d.com/samples)
[API](https://developer.rhino3d.com/api)
[Videos](https://developer.rhino3d.com/videos)
[Community](https://discourse.mcneel.com/c/rhino-developer) [my account
](https://www.rhino3d.com/my-account/ "Manage your account, licenses, and
teams")

[Accessing
Databases](https://developer.rhino3d.com/guides/rhinoscript/accessing-
databases/)

  * Overview
  * Connecting to a Database
  * Working with Recordsets
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Accessing Databases

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Probably the most popular use for VBScript is connecting to databases. It’s
incredibly useful and surprisingly easy.

The first thing you need is the database, of course. A variety of programs can
be used to create it, but probably the most popular is Microsoft Access. You
can also use FoxPro or create it directly in an SQL Server using whichever
utilities are supplied with the server.

In this example, we will connect to a simple Microsoft Access database. You
can download the database used in this demonstration
[here](https://developer.rhino3d.com/files/test_access_mdb.zip).

Most VBScript developers use Microsoft’s ADO (ActiveX database objects) to get
data from database. ADODB is comprised of 3 main objects: Connection,
RecordSet, and Command. We will demonstrate the first two objects.

## Connecting to a Database

The Datasource is essentially a connection from the server or workstation to a
database, which can either be on a dedicated machine running SQL server or a
database file sitting somewhere on the web server.

To specify what database you would like to use, you need to add a DSN. That is
short for Data Source Name. Data Source Name provides connectivity to a
database through an ODBC driver. The DSN contains database name, directory,
database driver, UserID, password, and other information. Once you create a
DSN for a particular database, you can use the DSN in an application to call
information from the database.

There are essentially two types of Datasources (DSN’s):

  1. **System DSN** \- A datasource created on the web server by the administrator of the server. T he most popular type of DSN and generally a lot more reliable.
  2. **File DSN** \- Essentially a connection that your script makes itself each time access to the database is required, specifying the path to and name of the database. The database must reside on the server in a directory that your script can access for this to work.

The code below is designed around a System DSN named “test” that points to the
above database. You can create System DSNs using the Data Sources (OBDC)
applet found in Control Panel. In Windows, the shortcut to the ODBC control
panel can be found in the following location:

_Start_ > _Control Panels_ > _Administrative Tools_ > _Data Sources (ODBC)_

## Working with Recordsets

In order to read information from a Datasource, you need to open a ‘Recordset’
- a set of database records based on some type of criteria, either all of the
records in a table or those matching some condition or set of conditions.

## Sample

The following example RhinoScript code demonstrates how to connect to a system
DSN named “test” and read point coordinate records from a table named
“points.”

    
    
    Sub Test
       Const adOpenStatic = 3
       Const adLockOptimistic = 3
       Const adUseClient = 3
    
       Dim objConnection, objRecordset
       Set objConnection = CreateObject("ADODB.Connection")
       Set objRecordset = CreateObject("ADODB.Recordset")
    
       objConnection.Open "DSN=test;"
       objRecordset.CursorLocation = adUseClient
       objRecordset.Open "SELECT * FROM points" , objConnection, adOpenStatic, adLockOptimistic
    
       objRecordSet.MoveFirst
    
       Dim x, y, z
       Do Until objRecordset.EOF
        x = objRecordset.Fields.Item("x")
        y = objRecordset.Fields.Item("y")
        z = objRecordset.Fields.Item("z")
        Rhino.AddPoint Array(x,y,z)
        objRecordset.MoveNext
       Loop
    
       objRecordset.Close
       objConnection.Close
    
     End Sub
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/accessing-
databases/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/accessing-
databases/index.md) [ Admin](https://developer.rhino3d.com/admin)

[Find a Reseller](https://www.rhino3d.com/sales)

[Shop online](https://www.rhino3d.com/store) or find a
[Reseller](https://www.rhino3d.com/sales)

[Find a Reseller](https://www.rhino3d.com/sales)

[Privacy Policy](https://www.rhino3d.com/privacy) •
[About](https://www.rhino3d.com/mcneel/about) • [Contact
Us](https://www.rhino3d.com/mcneel/contact) • [
Language](https://www.rhino3d.com/language "Change to a different region or
language")

[Copyright © 1993-2025 Robert McNeel & Associates. All Rights
Reserved.](https://www.rhino3d.com/mcneel/about)

[](https://www.facebook.com/McNeelRhinoceros/)
[](https://twitter.com/bobmcneel) [](https://www.linkedin.com/groups/75313/)
[](https://www.youtube.com/user/RhinoGuide/videos) [](https://vimeo.com/rhino)
[![Blogger
icon](https://developer.rhino3d.com/images/blogger.svg)](http://blog.rhino3d.com/)
[![Food4Rhino](https://developer.rhino3d.com/images/f4r_icon_01.svg)](https://www.food4rhino.com)

