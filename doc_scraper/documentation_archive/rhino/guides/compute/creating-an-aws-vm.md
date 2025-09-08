---
url: https://developer.rhino3d.com/guides/compute/creating-an-aws-vm/
scraped_at: 2025-09-08T15:43:21.426631
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

[How to create a virtual machine (VM) on Amazon Web
Service](https://developer.rhino3d.com/guides/compute/creating-an-aws-vm/)

  * Overview
  * Prerequisites
  * Launch the instance

[Guides](https://developer.rhino3d.com/en/guides/) / [Compute
Guides](https://developer.rhino3d.com/en/guides/compute/) /

How to create a virtual machine (VM) on Amazon Web Service

__

Windows only

by [Andy Payne](https://discourse.mcneel.com/u/andypayne/) (Last updated:
Tuesday, December 14, 2021)

## Overview

In this guide, we will walk through the process of setting up a virtual
machine using Amazon Elastic Compute Cloud (Amazon EC2).

To start, you will need to confirm your AWS subscription. If you are new to
AWS, you can get started with Amazon EC2 using the [AWS Free
Tier](https://aws.amazon.com/free/?all-free-tier.sort-
by=item.additionalFields.SortRank&all-free-tier.sort-
order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all).

__Note __

If you created your AWS account less than 12 months ago, and have not already
exceeded the free tier benefits for Amazon EC2, it will not cost you anything
to complete this tutorial. Otherwise, you’ll incur the standard Amazon EC2
usage fees from the time that you launch the instance until you terminate the
instance, even if it remains idle.

## Prerequisites

  1. [Create an account for AWS](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/get-set-up-for-amazon-ec2.html#sign-up-for-aws)

  2. [Create a key pair](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/get-set-up-for-amazon-ec2.html#create-a-key-pair). Note: We recommend saving the **private key file** as a **.pem** format with **RSA** encryption.

  3. [Create a security group](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/get-set-up-for-amazon-ec2.html#create-a-base-security-group). Note, we recommend adding a rule for **HTTP** , **HTTPS** , **RDP** , and **All ICMP - IPv4**.

## Launch the instance

To create a new virtual machine instance on AWS, follow these steps:

  1. Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/).

  2. From the EC2 console dashboard, select **Launch Instance**.

  3. Provide a name for the VM instance. For this tutorial, we’ll use the name **“RhinoComputeVM”**.

  4. Under the section titled Application and OS Images, click on the **Windows** button under the Quick Start tab. Under the Amazon Machine Image (AMI) section there should be a drop-down menu listing all of the available machine images. Select the AMI for **Microsoft Windows Server 2022 Base**.

![https://developer.rhino3d.com/images/AWS_Setup_11.png](https://developer.rhino3d.com/images/AWS_Setup_11.png)

  5. In the **Instance Type** section, select the **t2.micro** instance type (default) or a larger instance type if needed. Note: the _t2.micro_ instance type is elegible for the free tier. In regions where _t2.micro_ is unavailable, you can use a _t3.micro_ * instance under the free tier.

![https://developer.rhino3d.com/images/AWS_Setup_12.png](https://developer.rhino3d.com/images/AWS_Setup_12.png)

  6. In the **Key Pair (login)** section, select the key pair name that you created in step 2 of the prerequisite section [prerequisite section](../creating-an-aws-vm/#prerequisites) from the drop-down list.

![https://developer.rhino3d.com/images/AWS_Setup_13.png](https://developer.rhino3d.com/images/AWS_Setup_13.png)

  7. In the **Network Settings** section, under the **Firewall (security groups)** choose the **Select existing security group** radio button. Then, under the **Common Security Groups** drop-down list, select the security group you created in step 3 of the [prerequisite section](../creating-an-aws-vm/#prerequisites).

__Important __

If the **Auto-assign public IP** setting is set to **Disabled** , click on the
**Edit** button on the top-right of this section panel and change this setting
to **Enabled**.

![https://developer.rhino3d.com/images/AWS_Setup_14.png](https://developer.rhino3d.com/images/AWS_Setup_14.png)

  8. In the **Configure storage** section, select the default amount of storage for this instance.

  9. Now, on the far right select the **Launch Instance**.

  10. A confirmation page lets you know that your instance has successfully launched. In the top-most menu which reads **EC2 > Instances > Launch an instance**, select the **Instances** menu item to view the instances console window.

![https://developer.rhino3d.com/images/AWS_Setup_15.png](https://developer.rhino3d.com/images/AWS_Setup_15.png)

  11. On the **Instances** screen, you can view the status of the launched instance. The instance should automatically be running after launch, but if not select the instance row checkbox and then select the **Instance State** menu item at the top. Select **Start Instance** to start the virtual machine.

  12. With the instance row selected, click the **Connect** button in the top menu.

  13. On the **Connect to instance** page, select the **RDP client** tab.

  14. Next, select the **Get password** button.

  15. Choose **Upload private key file** and navigate to the private key (.pem) file that you created when you launched the instance.

  16. Choose **Decrypt Password**. The console displays the default administrator password for the instance under **Password** , replacing the **Get password** link shown previously. **Save this password in a safe place**. This passord is required to connect to the instance.

  17. Select **Download remote desktop file** to save the .rdp file to your local computer. You will need this file when you connect to your instance using the Remote Desktop Connect app.

Congratulations! In this tutorial, you successfully launched a virtual machine
on AWS and downloaded the RDP file which can be used to connect to that
instance.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/compute/creating-
an-aws-vm/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/compute/creating-
an-aws-vm/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

