---
url: https://developer.rhino3d.com/guides/compute/configure-compute-for-https/
scraped_at: 2025-09-08T15:43:23.429778
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

[Configure Compute to use
HTTPS](https://developer.rhino3d.com/guides/compute/configure-compute-for-
https/)

  * Overview
  * Prerequisites
  * Modify the Host Name
  * Generate the Certificate

[Guides](https://developer.rhino3d.com/en/guides/) / [Compute
Guides](https://developer.rhino3d.com/en/guides/compute/) /

Configure Compute to use HTTPS

__

Windows only

by [Andy Payne](https://discourse.mcneel.com/u/andypayne/) (Last updated:
Tuesday, February 25, 2025)

## Overview

In this guide, we will walk through the process of creating a valid SSL
certificate so that Rhino.Compute can communicate with clients using the HTTPS
protocol.

## Prerequisites

The following must be completed:

  1. You must have an active virtual machine (VM) instance. Use the following guides to walk through setting up a VM.

     * [Create a Virtual Machine on Azure](../creating-an-Azure-VM).
     * [Create a Virtual Machine on AWS](../creating-an-aws-vm).
  2. The VM must be accessible to the web (open port 80, and 443).

  3. A static public IPv4 address must be associated with your virtual machine. To learn more about configuring static IP address, use the following links:

     * [Configure IP addresses for an Azure network interface](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/virtual-network-network-interface-addresses?tabs=nic-address-portal#add-ip-addresses)
     * [Associate an elastic IP address with an EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)
  4. You must have an existing domain and have access to its DNS settings. An **A record** in your DNS settings must point to the public IPv4 address of your virtual machine.

__Note __

For this guide, I have assoicated an elastic IP address with my virtual
machine instance. I have also setup an A record in my DNS settings to point
_rhino.compute.rhino3d.com_ at the IP address of my virtual machine.

## Modify the Host Name

Before we step through the process of generating an SSL certificate, we need
to make one modification to our existing IIS configuration for Rhino.Compute.

  1. If you have not already done so, log into your VM (via RDP). See the section [Connect via RDP](../deploy-to-iis/#connect-via-rdp) for more details.

  2. On the **Start** menu, click in the search area and type _Internet Information Services (IIS) Manager_. Click to launch the app.

  3. In the IIS Manager, **click** on the web server node in the **Connections** panel on the left to expand the menu tree. Then **click** on the **Sites** node to expand the sub-menu. Lastly, select the **Rhino.Compute** node from the menu tree to adjust its settings.

  4. In the **Actions** pane on the right, click **Bindings**. ![https://developer.rhino3d.com/images/Site_Binding_2.png](https://developer.rhino3d.com/images/Site_Binding_2.png)

  5. In the **Site Bindings** pane, select the **Add** button. ![https://developer.rhino3d.com/images/Site_Binding_3.png](https://developer.rhino3d.com/images/Site_Binding_3.png)

  6. In the **Host name** text field, type in the subdomain name that you created when setting up the A-Record. Click **OK** when done. ![https://developer.rhino3d.com/images/Site_Binding_1.png](https://developer.rhino3d.com/images/Site_Binding_1.png)

  7. At this point, you should have two site bindings listed. Click **Close** when done. ![https://developer.rhino3d.com/images/Site_Binding_4.png](https://developer.rhino3d.com/images/Site_Binding_4.png)

## Generate the Certificate

The next step in the process is to create and install an SSL certificate for
the local IIS server. An SSL certificate is a digital certificate that
authenticates a website’s identity and enables an encrypted connection. It is
required in order to use the HTTPS protocol.

To generate the certificate, we recommend using [Win-ACME](https://www.win-
acme.com/). Win-ACME is a simple interactive client which can create and
install the certificate as well as handle renewing the certificate when
needed.

  1. [Download the Win-ACME Client](https://github.com/win-acme/win-acme/releases/download/v2.2.2.1449/win-acme.v2.2.2.1449.x64.pluggable.zip) on the virtual machine. Note: Win-ACME is distributed as .zip file.

  2. Right-click on the download .zip file and select **Extract All**. It doesn’t really matter what directory you choose to extract the files to as we will manually move/rename them in the next step. Click **Extract**.

  3. Select the newly extracted directory and type **Ctrl+X** to **Cut** and then **Ctrl+V** to **Paste** this folder into the root _C:\_ drive.

  4. Now, right-click on the directory that you just copied to the _C:\_ drive and select **Rename** from the menu. Shorten the folder name to just _“win-acme”_. ![https://developer.rhino3d.com/images/win_acme_1.png](https://developer.rhino3d.com/images/win_acme_1.png)

  5. Click on the Windows Start menu and type in “Powershell”. In the menu that appears, right-click on the **Windows Powershell app** and choose **Run As Administrator**.

  6. Type in the following command and hit **Enter** to launch the Win-ACME application.

    
    
        C:\win-acme\wacs.exe
    

  1. You should see an interactive menu appear with a set of instructions which can be run by typing in a specific letter. ![https://developer.rhino3d.com/images/win_acme_7.png](https://developer.rhino3d.com/images/win_acme_7.png)

  2. Type the letter **N** and hit **Enter** to create a certificate with the default settings. You should see a list of available IIS sites that are available. If you do not see an entry for **Rhino.Compute (1 binding)** then it is likely that you have not set the host name correctly in the previous step. See the section on [modifying the host name](https://developer.rhino3d.com/guides/compute/configure-compute-for-https/#modify-the-host-name). ![https://developer.rhino3d.com/images/win_acme_8.png](https://developer.rhino3d.com/images/win_acme_8.png)

  3. Type the number associated with the row for **Rhino.Compute (1 binding)** and hit **Enter**. ![https://developer.rhino3d.com/images/win_acme_9.png](https://developer.rhino3d.com/images/win_acme_9.png)

  4. Hit **Enter** again to accept the default **Pick all bindings**.

  5. When prompted to _Continue with this selection?_ hit **Enter** or type **Y** for yes. ![https://developer.rhino3d.com/images/win_acme_10.png](https://developer.rhino3d.com/images/win_acme_10.png)

  6. You should see some information printed to the console as it generates the SSL certificate. ![https://developer.rhino3d.com/images/win_acme_11.png](https://developer.rhino3d.com/images/win_acme_11.png)

Congratulations. If successful, the application will then run a series of
authorization and validation tests to confirm host is secure. Win-ACME will
then generate the SSL certificate and install it with IIS and add a new
binding **(*:443)** to the Rhino.Compute site. The SSL certificate will be
valid for 90 days. However, the Win-ACME application will create a task
scheduler which will try to renew the certificate after 60 days. You should
now be able to send an HTTPS request to your Rhino.Compute server and get a
valid response back.

  

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/compute/configure-
compute-for-https/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/compute/configure-
compute-for-https/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

