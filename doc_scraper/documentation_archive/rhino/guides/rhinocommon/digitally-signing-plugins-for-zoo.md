---
url: https://developer.rhino3d.com/guides/rhinocommon/digitally-signing-plugins-for-zoo/
scraped_at: 2025-09-08T15:36:55.904279
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

[Digitally Signing LAN Zoo
Plugins](https://developer.rhino3d.com/guides/rhinocommon/digitally-signing-
plugins-for-zoo/)

  * Overview
  * Generate Private Key & Certificate Signing Request
  * Requesting a Signed Digital Certificate
  * Creating a Personal Information Exchange
  * Sign Your Plugins

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Digitally Signing LAN Zoo Plugins

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Monday,
October 7, 2024)

## Overview

To add plugins to the LAN Zoo, and to call the license functions from within
your Rhino plugin, you must digitally sign your plugins using a certificate
signed by the _Robert McNeel & Associates Code Signing Authority_.

## Generate Private Key & Certificate Signing Request

Follow these steps to generate the necessary info to forward to _Robert McNeel
& Associates Code Signing Authority_…

  1. Download and install the latest [OpenSSL](https://slproweb.com/products/Win32OpenSSL.html). Note, downloading and installing the “light” version (smaller download) is sufficient.
  2. After installation, use Windows Explorer to navigate to the OpenSSL installation folder and double-click on `start.bat` found in the `Bin` folder.
  3. From the Windows command prompt that opens, navigate to your plug-in’s project folder.
  4. Save the contents of [__mcneelcodesigning.zip](https://files.mcneel.com/zoo/mcneelcodesigning.zip) to your plug-in’s project folder.
  5. From the command prompt, run `CreateRequest.bat <filename>`, where _filename_ is the name (without an extension) that will be used to save your private key (_.key_), certificate signing request (_.csr_), and final signed digital certificate (_.crt_).
  6. You will be prompted to answer some questions. Be sure to answer them correctly…

    
    
    C:\Dev\Zoo> CreateRequest.bat TestZooPluginKey
    Loading 'screen' into random state - done
    Generating RSA private key, 4096 bit long modulus
    ................................................................................
    e is 65537 (0x10001)
    Loading 'screen' into random state - done
    You are about to be asked to enter information that will be incorporated
    into your certificate request.
    What you are about to enter is what is called a Distinguished Name or a DN.
    There are quite a few fields but you can leave some blank
    For some fields there will be a default value,
    If you enter '.', the field will be left blank.
    -----
    Country Name (2 letter code) []: <COUNTRY NAME>
    State or Province Name (full name) []: <STATE OR PROVINCE>
    Locality Name (eg, city) []: <CITY>
    Organization Name (eg, company) []: <ORGANIZATON>
    Organizational Unit Name (eg, section) []: <ORGANIZATIONAL UNIT>
    Common Name (eg, your websites domain name) []: <DOMAIN NAME>
    
    Please enter the following 'extra' attributes
    to be sent with your certificate request
    A challenge password []: <PASSWORD>
    
    Saved private key: 'TestZooPluginKey.key'
    Saved CSR: 'TestZooPluginKey.csr'
    

## Requesting a Signed Digital Certificate

  1. Email the certificate signing request (_.csr_) created above to [](mailto:brian@mcneel.com) [Brian Gillespie](mailto:brian@mcneel.com) along with a certificate request.
  2. We will process your request and, if it is approved, will send you a signed digital certificate (_.crt_).

## Creating a Personal Information Exchange

To digitally sign your LAN Zoo or Rhino plugin, convert the signed digital
certificate (_.crt_), emailed to you upon approval, into a personal
information exchange (_.pfx_) file…

  1. Copy the signed digital certificate (_.crt_) you receive into the same folder as your private key (_.key_) and certificate signing request (_.csr_).
  2. Use Windows Explorer to navigate to the OpenSSL installation folder and double-click on `start.bat` found in the `Bin` folder.
  3. From the Windows command prompt that opens, navigate to the above folder.
  4. From the command prompt, run `MakePfxFile.bat <filename>`, where _filename_ is the name (without an extension)…

    
    
    C:\Dev\Zoo\TestZooPlugin>MakePfxFile.bat TestZooPluginKey
    Loading 'screen' into random state - done
    Enter Export Password: <PRESS ENTER>
    Verifying - Enter Export Password: <PRESS ENTER>
    Created 'TestZooPluginKey.pfx'. Use this to sign your executable code.
    

## Sign Your Plugins

Now that you have a personal information exchange (_.pfx_), you can use it to
sign LAN Zoo and Rhino plugins.

  1. Open a _Visual Studio Command Prompt_.
  2. Use _Signtool.exe_ , with the following syntax, to digitally sign your plugins…

    
    
    signtool.exe sign /f <filename>.pfx /fd sha256 /tr http://timestamp.digicert.com /td sha256 /v <plugin>
    

**Note:** If you set a password for your PFX file, above, you’ll need to add
`/p <password>` to your signing script. Be careful with your password!

For example:

    
    
    C:\Dev\Zoo\TestZooPlugin> signtool sign /f TestZooPluginKey.pfx /fd sha256 /tr http://timestamp.digicert.com /td sha256 /v TestZooPlugin.dll
    The following certificate was selected:
        Issued to: MCNEEL.COM
        Issued by: McNeel Software Development
        Expires:   <DATE>
        SHA1 hash: <HASH>
    
    Done Adding Additional Store
    Successfully signed and timestamped: TestZooPlugin.dll
    
    Number of files successfully Signed: 1
    Number of warnings: 0
    Number of errors: 0
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/digitally-
signing-plugins-for-zoo/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/digitally-
signing-plugins-for-zoo/index.md) [
Admin](https://developer.rhino3d.com/admin)

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

