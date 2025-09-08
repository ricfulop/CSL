---
url: https://developer.rhino3d.com/guides/compute/creating-an-azure-vm/
scraped_at: 2025-09-08T15:43:20.566984
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

[How to create a virtual machine (VM) on
Azure](https://developer.rhino3d.com/guides/compute/creating-an-azure-vm/)

  * Creating the Virtual Machine
    * Add an inbound port rule

[Guides](https://developer.rhino3d.com/en/guides/) / [Compute
Guides](https://developer.rhino3d.com/en/guides/compute/) /

How to create a virtual machine (VM) on Azure

__

Windows only

by [Andy Payne](https://discourse.mcneel.com/u/andypayne/) (Last updated:
Monday, February 14, 2022)

## Creating the Virtual Machine

In this guide, we will walk through the process of setting up a virtual
machine using Azure services.

To start, please confirm that you have a valid Azure subscription and that you
have already setup a resource group to hold the various resources for this
instance. To learn more about setting up a resource group on Azure, [visit
this page](https://docs.microsoft.com/en-us/azure/azure-resource-
manager/management/manage-resource-groups-portal).

  1. Sign in to the Azure [portal](https://portal.azure.com/#home).

  2. Type **virutal machines** in the search bar.

  3. Under **Services** , select **Virtual machines**.

  4. In the **Virtual machines** page, select **Create** then **Virtual Machine**

  5. In the **Basics** tab, under **Project details** , make sure the correct Subscription and Resource group are selected.

  6. Under **Instance details** , create a unique name for the virutal machine. We’ll use _Rhino-Compute-VM_ for our VM name. Select a region close to you, and then select _Windows Server 2022 Datacenter - Azure Edition Gen2_ for the **Image**. Feel free to select any **Size** VM that fits your needs. We’ll use _Standard DS2_v2_ for this example. Leave the other defaults. ![https://developer.rhino3d.com/images/Azure_VM_Create3.png](https://developer.rhino3d.com/images/Azure_VM_Create3.png)

  7. Under **Administrator account** , provide a username and a password. Take note of these credentials as we will use these when we log into the remote machine.

  8. Under **Inbound port rules** , choose **Allow selected ports** then select **RDP (3389)** , **HTTPS (443)** , and **HTTP (80)**. ![https://developer.rhino3d.com/images/Azure_VM_Create4.png](https://developer.rhino3d.com/images/Azure_VM_Create4.png)

  9. Select **Next : Disk >**.

  10. Select **Next : Networking >**.

  11. Under the **Network interface** section, click on the _Create new_ button under the **Public IP** subsection.

  12. When the pop-out blade opens up, select **Static** under the Assignment tab. Click **OK** to save this setting. ![https://developer.rhino3d.com/images/Azure_VM_Create5.png](https://developer.rhino3d.com/images/Azure_VM_Create5.png)

  13. Leave all other defaults. Select **Review + create**.

  14. Once your configuration passes the validation check, select **Create** to deploy your virtual machine.

  15. After deployment is complete, select **Go to resource**.

### Add an inbound port rule

Once your virtual machine has been deployed you should be able to go to the
resource home page. Here, you can change various settings and configurations.
We are going to add an inbound port rule so that we can send API requests on a
dedicated port.

By default, Azure denies and blocks all public inbound traffic - which also
includes ICMP traffic. This is a good thing since it improves security by
reducing the attack surface. The [Internet Control Message Protocol
(ICMP)](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol) is
typically used for diagnostics and to troubleshoot networking issues.

We’ll want to turn ICMP traffic on for our VM so that we can try to ping the
IP address and make sure we get a response. The first thing we need to do is
add an inbound port rule for ICMP traffic.

  1. On the left-hand side menu, select the **Networking** menu item. This will open the Networking blade.

  2. Click on the **Add inbound port rule** button ![https://developer.rhino3d.com/images/Azure_VM_Create6.png](https://developer.rhino3d.com/images/Azure_VM_Create6.png)

  3. In the **Add inbound security rule** pane, set the **Destination port ranges** to *, change the **Protocol** to **ICMP** , set the **Priority** to **100** , and type **ICMP** in the **Name** input. ![https://developer.rhino3d.com/images/Azure_VM_Create8.png](https://developer.rhino3d.com/images/Azure_VM_Create8.png)

  4. Click **Add** to create the new inbound port rule.

Congratulations! In this guide, you deployed a simple virtual machine on
Azure.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/compute/creating-
an-Azure-VM/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/compute/creating-
an-Azure-VM/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

