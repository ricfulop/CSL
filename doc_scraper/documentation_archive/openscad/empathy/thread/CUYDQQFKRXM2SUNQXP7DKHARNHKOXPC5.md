---
url: https://lists.openscad.org/empathy/thread/CUYDQQFKRXM2SUNQXP7DKHARNHKOXPC5
scraped_at: 2025-09-08T16:28:11.634893
title: Untitled
---

[ ![](/empathy/images/logo.png) ]( https://lists.openscad.org/empathy)

____

Hi,

Guest

![Pic](/empathy/images/default.jpg)

__

Sign In

Remember Me

Sign In

[ Click here to sign up for new account. ](/register)

[ Forgot your password? ](/password/reset)

###
[discuss@lists.openscad.org](https://lists.openscad.org/empathy/list/discuss.lists.openscad.org)

OpenSCAD general discussion Mailing-list

[View all
threads](https://lists.openscad.org/empathy/list/discuss.lists.openscad.org)

###  Re: Windows 11, Long OpenSCAD start-up time?

![](https://www.gravatar.com/avatar/63a0c2c7be96f2acab6aa0ba54bb1357?d=blank&s=100)

GS

Guenther Sohler

Thu, Sep 4, 2025 4:45 PM

It emits a signal in Preferences class, and the signal is NOT connected  
(not even implicitly, because Qt cannot know about Preferences)

Is not a function/slot either.

It's just an odd situation, because it does not make sense to emit  
signals, which are not connected.  
Not sure why you cause confusion :)

On Thu, Sep 4, 2025 at 5:37 PM Jordan Brown
[conceptis@jordan.maileater.net](mailto:conceptis@jordan.maileater.net)  
wrote:

____

For me it looks like, the culprit is here:

<https://github.com/openscad/openscad/blob/master/src/gui/Preferences.cc#L747>

Yes, that’s my conclusion too.

Only in windows builds emitting this signal takes 7 seconds.  
Remarkably enough, I cannot find where this signal is connected to, so can  
we skip sleeping 7 seconds here ?

As best I can tell, it leads into Qt-generated functions. It’s not  
sleeping - it’s CPU bound.

What it’s doing, I’m not sure. My guess is that it’s recalculating the  
layout of the preferences dialog, but I don’t know why it takes that long.

It emits a signal in Preferences class, and the signal is NOT connected (not
even implicitly, because Qt cannot know about Preferences) Is not a
function/slot either. It's just an odd situation, because it does not make
sense to emit signals, which are not connected. Not sure why you cause
confusion :) On Thu, Sep 4, 2025 at 5:37 PM Jordan Brown
<conceptis@jordan.maileater.net> wrote: > > > For me it looks like, the
culprit is here: > > >
https://github.com/openscad/openscad/blob/master/src/gui/Preferences.cc#L747 >
> > Yes, that’s my conclusion too. > > Only in windows builds emitting this
signal takes 7 seconds. > Remarkably enough, I cannot find where this signal
is connected to, so can > we skip sleeping 7 seconds here ? > > > As best I
can tell, it leads into Qt-generated functions. It’s not > sleeping - it’s CPU
bound. > > What it’s doing, I’m not sure. My guess is that it’s recalculating
the > layout of the preferences dialog, but I don’t know why it takes that
long. >

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Thu, Sep 4, 2025 5:00 PM

On 9/4/2025 9:45 AM, Guenther Sohler via Discuss wrote:

____

It emits a signal in Preferences class, and the signal is NOT connected  
(not even implicitly, because Qt cannot know about Preferences)

Qt knows all. :-)

____

Is not a function/slot either.

It's just an odd situation, because it does not make sense to emit  
signals, which are not connected.  
Not sure why you cause confusion :)

You think that because you haven't found the reference, and you are  
forgetting that src/gui/Preferences.ui is in the picture.

The references are not in `src`. They are in your build directory, in  
the dynamically created moc_Preferences.cpp. I don't yet understand how  
they fit together or exactly what they do, but there are several  
references to applicationFontChanged there.

On 9/4/2025 9:45 AM, Guenther Sohler via Discuss wrote: > It emits a signal in
Preferences class, and the signal is NOT connected > (not even implicitly,
because Qt cannot know about Preferences) Qt knows all. :-) > Is not a
function/slot either. > > It's just an odd situation, because it does not make
sense to emit > signals, which are not connected. > Not sure why you cause
confusion :) You think that because you haven't found the reference, and you
are forgetting that src/gui/Preferences.ui is in the picture. The references
are not in `src`. They are in your build directory, in the dynamically created
moc_Preferences.cpp. I don't yet understand how they fit together or exactly
what they do, but there are several references to applicationFontChanged
there.

![](https://www.gravatar.com/avatar/b19e2e8fa3505b0c13f5f8aba31dab95?d=blank&s=100)

MK

Marius Kintel

Thu, Sep 4, 2025 11:36 PM

On Sep 4, 2025, at 12:45, Guenther Sohler via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

____

It emits a signal in Preferences class, and the signal is NOT connected  
(not even implicitly, because Qt cannot know about Preferences)

Is not a function/slot either.

It looks connected to me:

QObject::connect(GlobalPreferences::inst(),
&Preferences::applicationFontChanged, &app,  
&OpenSCADApp::setApplicationFont);

<https://github.com/openscad/openscad/blob/5d6e37dd177d9d9329234cb5d3c0491ab0f23dcd/src/openscad_gui.cc#L247-L248>

Should be doable to add some debug/timing statements to see if there is
anything in that function itself that is slow.

-Marius

On Sep 4, 2025, at 12:45, Guenther Sohler via Discuss
<discuss@lists.openscad.org> wrote: > > It emits a signal in Preferences
class, and the signal is NOT connected > (not even implicitly, because Qt
cannot know about Preferences) > > Is not a function/slot either. > It looks
connected to me: QObject::connect(GlobalPreferences::inst(),
&Preferences::applicationFontChanged, &app, &OpenSCADApp::setApplicationFont);
https://github.com/openscad/openscad/blob/5d6e37dd177d9d9329234cb5d3c0491ab0f23dcd/src/openscad_gui.cc#L247-L248
Should be doable to add some debug/timing statements to see if there is
anything in that function itself that is slow. -Marius

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Thu, Sep 4, 2025 11:48 PM

On 9/4/2025 4:36 PM, Marius Kintel via Discuss wrote:

____

It looks connected to me:

QObject::connect(GlobalPreferences::inst(),
&Preferences::applicationFontChanged, &app,  
&OpenSCADApp::setApplicationFont);

<https://github.com/openscad/openscad/blob/5d6e37dd177d9d9329234cb5d3c0491ab0f23dcd/src/openscad_gui.cc#L247-L248>

Should be doable to add some debug/timing statements to see if there is
anything in that function itself that is slow.

The thing that probably confused him, and that confused me for a while,  
is that there's no obvious definition of  
Preferences::applicationFontChanged:

    
    
    $ grep -R applicationFontChanged src
    src/gui/Preferences.cc:  emit applicationFontChanged(family, size);
    src/gui/Preferences.h:  void applicationFontChanged(const QString& family, uint size) const;
    src/openscad_gui.cc:  QObject::connect(GlobalPreferences::inst(), &Preferences::applicationFontChanged, &app,
    

It's defined in a dynamically created source file:

    
    
    $ grep applicationFontChanged b/OpenSCAD_autogen/MXUWEOXILK/moc_Preferences.cpp
    QT_MOC_LITERAL(9, 97, 22), // "applicationFontChanged"
        "family\0size\0applicationFontChanged\0"
            case 4: _t->applicationFontChanged((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< uint(*)>(_a[2]))); break;
                if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&Preferences::applicationFontChanged)) {
    void Preferences::applicationFontChanged(const QString & _t1, uint _t2)const
    

So while it's not impossible to add additional diagnostics, it must be  
done with care.

On 9/4/2025 4:36 PM, Marius Kintel via Discuss wrote: > It looks connected to
me: > > QObject::connect(GlobalPreferences::inst(),
&Preferences::applicationFontChanged, &app, >
&OpenSCADApp::setApplicationFont); > >
https://github.com/openscad/openscad/blob/5d6e37dd177d9d9329234cb5d3c0491ab0f23dcd/src/openscad_gui.cc#L247-L248
> > Should be doable to add some debug/timing statements to see if there is
anything in that function itself that is slow. The thing that probably
confused him, and that confused me for a while, is that there's no obvious
definition of Preferences::applicationFontChanged: $ grep -R
applicationFontChanged src src/gui/Preferences.cc: emit
applicationFontChanged(family, size); src/gui/Preferences.h: void
applicationFontChanged(const QString& family, uint size) const;
src/openscad_gui.cc: QObject::connect(GlobalPreferences::inst(),
&Preferences::applicationFontChanged, &app, It's defined in a dynamically
created source file: $ grep applicationFontChanged
b/OpenSCAD_autogen/MXUWEOXILK/moc_Preferences.cpp QT_MOC_LITERAL(9, 97, 22),
// "applicationFontChanged" "family\0size\0applicationFontChanged\0" case 4:
_t->applicationFontChanged((*reinterpret_cast< const
QString(*)>(_a[1])),(*reinterpret_cast< uint(*)>(_a[2]))); break; if
(*reinterpret_cast<_t *>(_a[1]) ==
static_cast<_t>(&Preferences::applicationFontChanged)) { void
Preferences::applicationFontChanged(const QString & _t1, uint _t2)const So
while it's not impossible to add additional diagnostics, it must be done with
care.

![](https://www.gravatar.com/avatar/b19e2e8fa3505b0c13f5f8aba31dab95?d=blank&s=100)

MK

Marius Kintel

Thu, Sep 4, 2025 11:54 PM

____

On Sep 4, 2025, at 19:48, Jordan
Brown[openscad@jordan.maileater.net](mailto:openscad@jordan.maileater.net)
wrote:

The thing that probably confused him, and that confused me for a while, is
that there's no obvious definition of Preferences::applicationFontChanged:

It’s a signal so the implementation will always be auto-generated by Qt.
Günther is pretty familiar with Qt I think so it was likely just an oversight
on his part:

signals:  
[…]  
void applicationFontChanged(const QString& family, uint size) const;

____

So while it's not impossible to add additional diagnostics, it must be done
with care.

Signals themselves and their connections is an extremely robust and performant
mechanism in Qt, so it _should_ be sufficient to test the function it’s
connected to, to at least prove or disprove that the blocking behaviour
actually happens there an not somewhere else.

-Marius

> On Sep 4, 2025, at 19:48, Jordan Brown <openscad@jordan.maileater.net>
> wrote: > > The thing that probably confused him, and that confused me for a
> while, is that there's no obvious definition of
> Preferences::applicationFontChanged: It’s a signal so the implementation
> will always be auto-generated by Qt. Günther is pretty familiar with Qt I
> think so it was likely just an oversight on his part: signals: […] void
> applicationFontChanged(const QString& family, uint size) const; > So while
> it's not impossible to add additional diagnostics, it must be done with
> care. > Signals themselves and their connections is an extremely robust and
> performant mechanism in Qt, so it _should_ be sufficient to test the
> function it’s connected to, to at least prove or disprove that the blocking
> behaviour actually happens there an not somewhere else. -Marius

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Fri, Sep 5, 2025 12:06 AM

On 9/4/2025 4:54 PM, Marius Kintel wrote:

____

Signals themselves and their connections is an extremely robust and  
performant mechanism in Qt, so it _should_ be sufficient to test the  
function it’s connected to, to at least prove or disprove that the  
blocking behaviour actually happens there an not somewhere else.

Ah, and so _I_ wasn't understanding it deeply enough. I wasn't finding  
applicationFontChanged and wasn't familiar with Qt signals, so didn't  
take the next step to OpenSCADApp::setApplicationFont. Sigh.

Now I can look deeper...

On 9/4/2025 4:54 PM, Marius Kintel wrote: > Signals themselves and their
connections is an extremely robust and > performant mechanism in Qt, so it
_should_ be sufficient to test the > function it’s connected to, to at least
prove or disprove that the > blocking behaviour actually happens there an not
somewhere else. Ah, and so *I* wasn't understanding it deeply enough. I wasn't
finding applicationFontChanged and wasn't familiar with Qt signals, so didn't
take the next step to OpenSCADApp::setApplicationFont. Sigh. Now I can look
deeper...

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Fri, Sep 5, 2025 12:16 AM

On 9/4/2025 5:06 PM, Jordan Brown via Discuss wrote:

____

Now I can look deeper...

It's this call to scadApp->setStyleSheet():

<https://github.com/openscad/openscad/blob/5d6e37dd177d9d9329234cb5d3c0491ab0f23dcd/src/gui/OpenSCADApp.cc#L91>

(Which may well trigger callbacks to various other components, but I  
haven't tried to track them down yet.)

If that stylesheet is empty, there's no delay.

On 9/4/2025 5:06 PM, Jordan Brown via Discuss wrote: > Now I can look
deeper... It's this call to scadApp->setStyleSheet():
https://github.com/openscad/openscad/blob/5d6e37dd177d9d9329234cb5d3c0491ab0f23dcd/src/gui/OpenSCADApp.cc#L91
(Which may well trigger callbacks to various other components, but I haven't
tried to track them down yet.) If that stylesheet is empty, there's no delay.

![](https://www.gravatar.com/avatar/b19e2e8fa3505b0c13f5f8aba31dab95?d=blank&s=100)

MK

Marius Kintel

Fri, Sep 5, 2025 2:04 AM

____

On Sep 4, 2025, at 20:16, Jordan
Brown[openscad@jordan.maileater.net](mailto:openscad@jordan.maileater.net)
wrote:

On 9/4/2025 5:06 PM, Jordan Brown via Discuss wrote:

____

Now I can look deeper...

It's this call to scadApp->setStyleSheet():

<https://github.com/openscad/openscad/blob/5d6e37dd177d9d9329234cb5d3c0491ab0f23dcd/src/gui/OpenSCADApp.cc#L91>

(Which may well trigger callbacks to various other components, but I haven't
tried to track them down yet.)

If that stylesheet is empty, there's no delay.

We used to have that stylesheet code elsewhere, but what’s new is that we also
override the font. This is recent (Aug 2nd), so it checks out.  
Torsten may know more as he added the font change :)

-Marius

> On Sep 4, 2025, at 20:16, Jordan Brown <openscad@jordan.maileater.net>
> wrote: > > On 9/4/2025 5:06 PM, Jordan Brown via Discuss wrote: >> Now I can
> look deeper... > > It's this call to scadApp->setStyleSheet(): > >
> https://github.com/openscad/openscad/blob/5d6e37dd177d9d9329234cb5d3c0491ab0f23dcd/src/gui/OpenSCADApp.cc#L91
> > > (Which may well trigger callbacks to various other components, but I
> haven't tried to track them down yet.) > > If that stylesheet is empty,
> there's no delay. > We used to have that stylesheet code elsewhere, but
> what’s new is that we also override the font. This is recent (Aug 2nd), so
> it checks out. Torsten may know more as he added the font change :) -Marius

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

