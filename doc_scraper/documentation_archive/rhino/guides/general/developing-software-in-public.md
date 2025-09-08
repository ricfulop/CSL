---
url: https://developer.rhino3d.com/guides/general/developing-software-in-public/#related-topics
scraped_at: 2025-09-08T15:57:23.188615
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

[Developing Software In
Public](https://developer.rhino3d.com/guides/general/developing-software-in-
public/)

  * Overview
  * The Cycle
    * Code
    * Commit
    * Compile
    * Test
    * Publish
    * Listen
    * Track
    * Prioritize
    * Automation
  * In Public
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [General
Guides](https://developer.rhino3d.com/en/guides/general/) /

Developing Software In Public

by [Brian Gillespie](https://discourse.mcneel.com/u/brian/) (Last updated:
Thursday, May 15, 2025)

## Overview

Over the last 20 years we’ve put together a process that helps us build
customer delight. There are eight pieces to this process, and they are all
equally important. For years, we built our own proprietary tools to support
most of the parts of this process. But now, there are great commercially
available tools - tools we encourage you to use, too.

Our Software Development process, just like the other processes, is a cycle.
So we can start anywhere.

![Rhino Development Cycle](https://developer.rhino3d.com/images/developing-
software-in-public-01.png)

## The Cycle

Since this is a developer guide, let’s start with writing code.

### Code

This is what we as software developers spend a lot of our time doing. We’ve
got our favorite IDE open, we write code, we debug, we solve problems. We
don’t know a software developer that doesn’t love solving problems.

When we’ve got something, we _commit_ it to our version control system…

### Commit

We commit code to a [Version Control
System](https://en.wikipedia.org/wiki/Version_control). In our case, we use
[git](https://git-scm.com/) with [GitHub](https://github.com/). There are many
other version control systems out there. We used to use
[Subversion](https://subversion.apache.org/), but now we use
[GitHub](https://github.com/). [GitHub](https://github.com/) plays nicely with
so many other tools and has such a rich API. But there are others worth
considering: [BitBucket](https://bitbucket.org),
[Mercurial](https://www.mercurial-scm.org/), etc.

If you don’t use any version control, we beg you: please start. It’s so easy
now. It lets you get back to other versions of your software before you
introduced a problem. It helps you collaborate as a team. It is required for
any kind of build automation. Did we mention it’s easy?

As developers, we use a modified version of [GitHub
Flow](https://guides.github.com/introduction/flow/) to create and merge pull
requests into our master branch.

After we commit our code, we build it…

### Compile

In addition to compiling at our desks, we have dedicated
[TeamCity](https://www.jetbrains.com/teamcity/) servers that constantly build
our code, and verify that it works with our master branch on
[GitHub](https://github.com/). This makes sure that we don’t break each
other’s ability to get the latest code and compile.

These [TeamCity](https://www.jetbrains.com/teamcity/) servers verify every
commit and also build our daily releases - many of them - about every four
hours. They also build our public WIP and Service Release builds.

With every new build, we test…

### Test

When developers fix bugs and close issues, our internal testing staff makes
sure the public build works correctly. We also rely on our customers to test
WIP and Release Candidate builds.

Testing happens before and after the next step: Publishing…

### Publish

Whenever we’ve got a build that is ready to go out to customers, we deploy (or
publish) it.

This includes releasing …

  * [Downloadable installers](http://www.rhino3d.com/download)
  * [SDKs](http://developer.mcneel.com)
  * Documentation (this here site)

…and making public announcements by email, blogs, and social media.

__Release Schedule __

We plan to release new versions of Rhino the **2nd Tuesday of each month** ,
which includes a:

  * Service Release (SR) for all users who have updates enabled.
  * [Service Release Candidate (SRC)](https://discourse.mcneel.com/t/rhino-service-release-candidates/53358). After the SRC goes through final testing, it becomes the next Service Release the following 2nd Tuesday. SRCs are also published weekly - typically on Tuesdays - and we encourage users to [install Service Release Candidates](https://discourse.mcneel.com/t/rhino-service-release-candidates/53358) as they help us test the next update.
  * [Work-In-Progress (WIP)](https://discourse.mcneel.com/t/welcome-to-serengeti/9612) build.

### Listen

We listen in as many ways as we can:

  * [Chat](http://www.rhino3d.com/support)
  * [Email](mailto:tech@mcneel.com)
  * Telephone Support (206) 545-6877
  * [Forum (Discourse)](https://discourse.mcneel.com/)

And often, when we listen, we find problems that need to be fixed. Sometimes
they’re little…sometimes they’re HUGE. We always log an issue…

### Track

We log issues in [YouTrack](https://mcneel.myjetbrains.com).

[YouTrack](https://mcneel.myjetbrains.com) works well for us because it helps
us ensure that each issue gets properly tested and documented.

### Prioritize

Figuring out what is the next most important thing is HARD. We talk with our
customers. We talk with each other. We use Gmail, Google Drive, and Google
Docs to communicate. We chat 24 hours a day on [Slack](https://slack.com/).

We meet every week on Tuesday. Before we meet, we share what we’ve done in a
Google Doc. In that document, we share our goals for each of the products
we’re releasing next each of the feature groups we’re working on including
graphs of how we’re progressing over time there are links back to our
[YouTrack](https://mcneel.myjetbrains.com) issues and we get verbal reports
from each of the people working on the features.

Also, each developer writes down what they’ve been working on, what they plan
to do next, and what is getting in their way of completing their work.

### Automation

And last but not least, we do a LOT of automation.

Here are some of the things we automate:

  * Build every commit from every developer before it goes into our master development branch.
  * Closing issues in [YouTrack](https://mcneel.myjetbrains.com) when fixes get merged into our master development branch by the [TeamCity](https://www.jetbrains.com/teamcity/) servers.
  * Build internal and public releases on our [TeamCity](https://www.jetbrains.com/teamcity/) servers.
  * Publishing new WIP releases by typing a command into [Slack](https://slack.com/).
  * Upload public releases to our download servers.

## In Public

Up until recently, these are the parts of our processes that we’ve made
public:

  * Testing
  * Publishing (at least you see what we publish)
  * Listening

And in the last couple of years, we made our issue tracker public by switching
to YouTrack. Some issues we hide from public view for security or user privacy
reasons.

Something we’d like to do soon is to make even more of this public:

  * Sharing some of our code as public repos on GitHub so you’ve got some real, production-hardened code examples to work from
  * Letting you share fixes and improvements to our code.
  * Making it easier to build plug-in projects by publishing RhinoCommon as a NuGet package.
  * Helping with build automation where necessary.

## Related Topics

  * [Rhino Technology Overview](https://developer.rhino3d.com/guides/general/rhino-technology-overview/)
  * [Contributing](https://developer.rhino3d.com/guides/general/contributing/)
  * [Developer Prerequisites](https://developer.rhino3d.com/guides/general/rhino-developer-prerequisites/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/general/developing-
software-in-public/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/general/developing-
software-in-public/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

