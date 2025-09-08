---
url: https://freecad.github.io/SourceDoc/d5/d0d/classBase_1_1SequencerBase.html
scraped_at: 2025-09-08T15:17:15.113544
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html)

[List of all members](../../db/d86/classBase_1_1SequencerBase-members.html) | Public Member Functions | Static Public Member Functions | Protected Member Functions | Protected Attributes | Friends

Base::SequencerBase Class Reference

This class gives the user an indication of the progress of an operation and it
is used to reassure him that the application is still running.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#details)

`#include <Sequencer.h>`

##  Public Member Functions  
  
---  
virtual void | [checkAbort](../../d5/d0d/classBase_1_1SequencerBase.html#aa0341031675242aa6aff2a17b4325539) ()  
| Check if the operation is aborted by user.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#aa0341031675242aa6aff2a17b4325539)  
  
virtual [bool](../../d9/db9/classbool.html) | [isBlocking](../../d5/d0d/classBase_1_1SequencerBase.html#a0f260bdce91cdd1854dd9a448550ab9c) () const  
| Returns true if the running sequencer is blocking any user input.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a0f260bdce91cdd1854dd9a448550ab9c)  
  
[bool](../../d9/db9/classbool.html) | [isLocked](../../d5/d0d/classBase_1_1SequencerBase.html#a84588b6e9b8924d463aecfc3ab088283) () const  
| Returns true if the sequencer was locked, false otherwise.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a84588b6e9b8924d463aecfc3ab088283)  
  
[bool](../../d9/db9/classbool.html) | [isRunning](../../d5/d0d/classBase_1_1SequencerBase.html#a06f770a5ba78c654f4d132b235bccd28) () const  
| Returns true if the sequencer is running, otherwise returns false.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a06f770a5ba78c654f4d132b235bccd28)  
  
[bool](../../d9/db9/classbool.html) | [setLocked](../../d5/d0d/classBase_1_1SequencerBase.html#a137ca2a91b990d8053be9f3ca6add1ff) ([bool](../../d9/db9/classbool.html) bLock)  
| If _bLock_ is true then the sequencer gets locked.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a137ca2a91b990d8053be9f3ca6add1ff)  
  
[bool](../../d9/db9/classbool.html) | [wasCanceled](../../d5/d0d/classBase_1_1SequencerBase.html#a3e0668144ea48ef7cd9040513bcc4b3c) () const  
| Returns true if the pending operation was canceled.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a3e0668144ea48ef7cd9040513bcc4b3c)  
  
  
##  Static Public Member Functions  
  
---  
static [SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html) & | [Instance](../../d5/d0d/classBase_1_1SequencerBase.html#aa05bb36f60b72f0bdde3ee8bdea0490d) ()  
| Returns the last created sequencer instance.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#aa05bb36f60b72f0bdde3ee8bdea0490d)  
  
  
##  Protected Member Functions  
  
---  
[bool](../../d9/db9/classbool.html) | [next](../../d5/d0d/classBase_1_1SequencerBase.html#a708d36d490fcfb8ef3e5a65c68b692ac) ([bool](../../d9/db9/classbool.html) canAbort=false)  
| Performs the next step and returns true if the operation is not yet
finished.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a708d36d490fcfb8ef3e5a65c68b692ac)  
  
virtual void | [nextStep](../../d5/d0d/classBase_1_1SequencerBase.html#a65ca8eb627a8bf4c9f91274637867f48) ([bool](../../d9/db9/classbool.html) canAbort)  
| This method can be reimplemented in sub-classes to give the user a feedback
when the next is performed.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a65ca8eb627a8bf4c9f91274637867f48)  
  
size_t | [numberOfSteps](../../d5/d0d/classBase_1_1SequencerBase.html#ae72645f88f8f398096187bb6877e6e34) () const  
| Returns the number of steps.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#ae72645f88f8f398096187bb6877e6e34)  
  
[SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html) & | [operator=](../../d5/d0d/classBase_1_1SequencerBase.html#af30a06e06c0f87d55e716b7d0aec7519) (const [SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html) &)=default  
virtual void | [pause](../../d5/d0d/classBase_1_1SequencerBase.html#a804a91939fc20301356a1fa4cbd306b6) ()  
| Breaks the sequencer if needed.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a804a91939fc20301356a1fa4cbd306b6)  
  
[int](../../d1/da0/classint.html) | [progressInPercent](../../d5/d0d/classBase_1_1SequencerBase.html#ad8f695625153088ee4dd478c0830f72c) () const  
| Returns the current state of progress in percent.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#ad8f695625153088ee4dd478c0830f72c)  
  
void | [rejectCancel](../../d5/d0d/classBase_1_1SequencerBase.html#abf3ee0dbca29f0361881fb8c767d58ae) ()  
| If you tried to cancel but then decided to continue the operation.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#abf3ee0dbca29f0361881fb8c767d58ae)  
  
virtual void | [resetData](../../d5/d0d/classBase_1_1SequencerBase.html#a8c7af5d20b184eb577c09ce3f02782c8) ()  
| Resets internal data.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a8c7af5d20b184eb577c09ce3f02782c8)  
  
virtual void | [resume](../../d5/d0d/classBase_1_1SequencerBase.html#aea81b4efe906649564fd9b32e43484c3) ()  
| Continues with progress.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#aea81b4efe906649564fd9b32e43484c3)  
  
|
[SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html#a2e3a2199b335137138937c9ef7fc326f)
()  
| construction
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a2e3a2199b335137138937c9ef7fc326f)  
  
|
[SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html#ae4fa3bbfd02762f65b4dc01aab9e6326)
(const [SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html)
&)=default  
virtual void | [setProgress](../../d5/d0d/classBase_1_1SequencerBase.html#a20ca12713d51a8435bca90ce7cfa3ba7) (size_t)  
| Sets the progress indicator to a certain position.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a20ca12713d51a8435bca90ce7cfa3ba7)  
  
virtual void | [setText](../../d5/d0d/classBase_1_1SequencerBase.html#ab666acb27961c1927c77a1a82a19879f) (const char *pszTxt)  
| Sets a text what the pending operation is doing.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#ab666acb27961c1927c77a1a82a19879f)  
  
[bool](../../d9/db9/classbool.html) | [start](../../d5/d0d/classBase_1_1SequencerBase.html#a9e388dd22618a5f8c04f5128e888929b) (const char *pszStr, size_t steps)  
| Starts a new operation, returns false if there is already a pending
operation, otherwise it returns true.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a9e388dd22618a5f8c04f5128e888929b)  
  
virtual void | [startStep](../../d5/d0d/classBase_1_1SequencerBase.html#a45d8df4cace8ae2b5c5b70a0c432a8f7) ()  
| This method can be reimplemented in sub-classes to give the user a feedback
when a new sequence starts.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a45d8df4cace8ae2b5c5b70a0c432a8f7)  
  
[bool](../../d9/db9/classbool.html) | [stop](../../d5/d0d/classBase_1_1SequencerBase.html#af7abe491fae28be30f1f1fae10511303) ()  
| Stops the sequencer if all operations are finished.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#af7abe491fae28be30f1f1fae10511303)  
  
void | [tryToCancel](../../d5/d0d/classBase_1_1SequencerBase.html#afe4af6fa0632db72c75c533477526fb5) ()  
| Try to cancel the pending operation(s).
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#afe4af6fa0632db72c75c533477526fb5)  
  
virtual | [~SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html#a33bef6ebde4a0cf72fa5c542e519a8d2) ()  
| Destruction.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a33bef6ebde4a0cf72fa5c542e519a8d2)  
  
  
##  Protected Attributes  
  
---  
size_t | [nProgress](../../d5/d0d/classBase_1_1SequencerBase.html#a8f546309a7f6ab043a757e79d5d5409e)  
| Stores the current amount of progress.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a8f546309a7f6ab043a757e79d5d5409e)  
  
size_t | [nTotalSteps](../../d5/d0d/classBase_1_1SequencerBase.html#a34e1fc4574b504b22098ac12305a85a6)  
| Stores the total number of steps.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a34e1fc4574b504b22098ac12305a85a6)  
  
  
##  Friends  
  
---  
class | [SequencerLauncher](../../d5/d0d/classBase_1_1SequencerBase.html#ac5104ffb5f83a154155e23626096d377)  
  
## Detailed Description

This class gives the user an indication of the progress of an operation and it
is used to reassure him that the application is still running.

Here are some code snippets of how to use the sequencer:

#include <Base/Sequencer.h>

//first example

[Base::SequencerLauncher](../../d0/dcc/classBase_1_1SequencerLauncher.html
"The SequencerLauncher class is provided for convenience.") seq("my text", 10)

for (int i=0; i<10; i++)

{

// do something

seq.[next](../../d0/dcc/classBase_1_1SequencerLauncher.html#ab82c78eee0e3e0f79b3d99950e689b4a)
();

}

//second example

[Base::SequencerLauncher](../../d0/dcc/classBase_1_1SequencerLauncher.html
"The SequencerLauncher class is provided for convenience.") seq("my text", 10)

do

{

// do something

}

while (seq.next());

The implementation of this class also supports several nested instances at a
time. But note, that only the first instance has an effect. Any further
sequencer instance doesn't influence the total number of iteration steps. This
is simply because it's impossible to get the exact number of iteration steps
for nested instances and thus we have either too few steps estimated then the
sequencer may indicate 100% but the algorithm still running or we have too
many steps estimated so that the an algorithm may stop long before the
sequencer reaches 100%.

try {

//start the first operation

[Base::SequencerLauncher](../../d0/dcc/classBase_1_1SequencerLauncher.html
"The SequencerLauncher class is provided for convenience.") seq1("my text",
10)

for (int i=0; i<10, i++)

{

// do something

// start the second operation while the first one is still running

[Base::SequencerLauncher](../../d0/dcc/classBase_1_1SequencerLauncher.html
"The SequencerLauncher class is provided for convenience.") seq2("another
text", 10);

for (int j=0; j<10; j++)

{

// do something different

seq2.next ();

}

seq1.next ( true ); // allow to cancel

}

}

catch(const
[Base::AbortException](../../de/dce/classBase_1_1AbortException.html "The
AbortException is thrown if a pending operation was aborted.")&){

// cleanup your data if needed

}

Note

    If using the sequencer with [SequencerLauncher.next](../../d0/dcc/classBase_1_1SequencerLauncher.html#ab82c78eee0e3e0f79b3d99950e689b4a)(_true_) then you must take into account that the exception _[AbortException](../../de/dce/classBase_1_1AbortException.html "The AbortException is thrown if a pending operation was aborted.")_ could be thrown, e.g. in case the ESC button was pressed. So in this case it's always a good idea to use the sequencer within a try-catch block.
     Instances of [SequencerLauncher](../../d0/dcc/classBase_1_1SequencerLauncher.html "The SequencerLauncher class is provided for convenience.") should always be created on the stack. This is because if an exception somewhere is thrown the destructor is auto- matically called to clean-up internal data.
     It's not supported to create an instance of [SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html "This class gives the user an indication of the progress of an operation and it is used to reassure hi...") or a sub-class in another thread than the main thread. But you can create [SequencerLauncher](../../d0/dcc/classBase_1_1SequencerLauncher.html "The SequencerLauncher class is provided for convenience.") instances in other threads.

Author

    Werner Mayer 

## Constructor & Destructor Documentation

## ◆ SequencerBase() [1/2]

| SequencerBase::SequencerBase  | ( | | ) |   
---|---|---|---|---  
protected  
  
construction

References
[Base::SequencerP::appendInstance()](../../d1/dd0/structBase_1_1SequencerP.html#aac33512cc5793d5d006bdcd7515b1834).

## ◆ SequencerBase() [2/2]

| Base::SequencerBase::SequencerBase  | ( | const [SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html) & | | ) |   
---|---|---|---|---|---  
protecteddefault  
  
## ◆ ~SequencerBase()

| SequencerBase::~SequencerBase  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
Destruction.

References
[Base::SequencerP::removeInstance()](../../d1/dd0/structBase_1_1SequencerP.html#a294b0ebb9f3c4644a65fe2df79c9ed70).

## Member Function Documentation

## ◆ checkAbort()

| virtual void Base::SequencerBase::checkAbort  | ( | | ) |   
---|---|---|---|---  
virtual  
  
Check if the operation is aborted by user.

Reimplemented in
[Gui::SequencerBar](../../db/dae/classGui_1_1SequencerBar.html#aac14901da0adbe2bd0d66b5bfb140b85).

## ◆ Instance()

| [SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html) & SequencerBase::Instance  | ( | | ) |   
---|---|---|---|---  
static  
  
Returns the last created sequencer instance.

If you create an instance of a class inheriting
[SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html "This class gives
the user an indication of the progress of an operation and it is used to
reassure hi...") this object is retrieved instead.

This mechanism is very useful to have an own sequencer for each layer of
FreeCAD. For example, if FreeCAD is running in server mode you have/need no
GUI layer and therewith no (graphical) progress bar; in this case
[ConsoleSequencer](../../d6/d29/classBase_1_1ConsoleSequencer.html "This class
writes the progress to the console window.") is taken. But in cases FreeCAD is
running with GUI the
[Gui::ProgressBar](../../d2/d04/classGui_1_1ProgressBar.html) is taken
instead.

See also

    [Sequencer](../../db/d07/namespaceBase.html#a975e0274696620c14016b8c54fe7634e "Access to the only SequencerBase instance.")

References
[Base::SequencerP::getInstance()](../../d1/dd0/structBase_1_1SequencerP.html#adcd309a8b32cb6373682a4569315803d).

Referenced by
[Base::SequencerLauncher::next()](../../d0/dcc/classBase_1_1SequencerLauncher.html#ab82c78eee0e3e0f79b3d99950e689b4a),
[Base::SequencerLauncher::numberOfSteps()](../../d0/dcc/classBase_1_1SequencerLauncher.html#ab9458a363b7531131baafbd060f12608),
[Base::Sequencer()](../../db/d07/namespaceBase.html#a975e0274696620c14016b8c54fe7634e),
[Base::SequencerLauncher::SequencerLauncher()](../../d0/dcc/classBase_1_1SequencerLauncher.html#a1f72a046f7e9bab1995df453593d969d),
[Base::SequencerLauncher::setProgress()](../../d0/dcc/classBase_1_1SequencerLauncher.html#a74937014111344719ab100ed721b1e16),
[Base::SequencerLauncher::setText()](../../d0/dcc/classBase_1_1SequencerLauncher.html#a5a3b21d5fbeeb1c5ab6d91b55b724950),
[Base::SequencerLauncher::wasCanceled()](../../d0/dcc/classBase_1_1SequencerLauncher.html#a3dd373a3859ced0145dccc176b5ab3a0),
and
[Base::SequencerLauncher::~SequencerLauncher()](../../d0/dcc/classBase_1_1SequencerLauncher.html#a7471e6530431b1805b27d0e2af90b7a3).

## ◆ isBlocking()

| [bool](../../d9/db9/classbool.html) SequencerBase::isBlocking  | ( | | ) |  const  
---|---|---|---|---  
virtual  
  
Returns true if the running sequencer is blocking any user input.

This might be only of interest of the GUI where the progress bar or dialog is
used from a thread. If started from a thread this method should return false,
otherwise true. The default implementation always returns true.

Reimplemented in
[Gui::SequencerDialog](../../d2/da8/classGui_1_1SequencerDialog.html#a993e5e15269200512309c48e3440039c),
and
[Gui::SequencerBar](../../db/dae/classGui_1_1SequencerBar.html#a2a8bb63500302b0289d75c3d04204e41).

Referenced by
[Gui::ViewerEventFilter::eventFilter()](../../dc/d1d/classGui_1_1ViewerEventFilter.html#a03c5db053bf086d38650e7ffa2325bf6).

## ◆ isLocked()

[bool](../../d9/db9/classbool.html) SequencerBase::isLocked  | ( | | ) |  const  
---|---|---|---|---  
  
Returns true if the sequencer was locked, false otherwise.

References
[Base::SequencerP::mutex](../../d1/dd0/structBase_1_1SequencerP.html#a0bde1ec1441d27caba8ee72a0aa378b0).

## ◆ isRunning()

[bool](../../d9/db9/classbool.html) SequencerBase::isRunning  | ( | | ) |  const  
---|---|---|---|---  
  
Returns true if the sequencer is running, otherwise returns false.

References
[Base::SequencerP::mutex](../../d1/dd0/structBase_1_1SequencerP.html#a0bde1ec1441d27caba8ee72a0aa378b0).

Referenced by
[Gui::ProgressBar::delayedShow()](../../d2/d04/classGui_1_1ProgressBar.html#a85387b78198a14fb7ebc12b0bc94801f),
[Gui::ProgressBar::eventFilter()](../../d2/d04/classGui_1_1ProgressBar.html#a40f423a80561579ade393f915077b8bf),
[Gui::ViewerEventFilter::eventFilter()](../../dc/d1d/classGui_1_1ViewerEventFilter.html#a03c5db053bf086d38650e7ffa2325bf6),
and
[addonmanager_workers.InstallWorkbenchWorker::update_status()](../../d7/dc6/classaddonmanager__workers_1_1InstallWorkbenchWorker.html#a1c775af73dfc50bd38f5d20b8f30fc60).

## ◆ next()

| [bool](../../d9/db9/classbool.html) SequencerBase::next  | ( | [bool](../../d9/db9/classbool.html) | _canAbort_ = `false`| ) |   
---|---|---|---|---|---  
protected  
  
Performs the next step and returns true if the operation is not yet finished.

But note, when 0 was passed to
[start()](../../d5/d0d/classBase_1_1SequencerBase.html#a9e388dd22618a5f8c04f5128e888929b
"Starts a new operation, returns false if there is already a pending
operation, otherwise it returns t...") as the number of total steps this
method always returns false.

In this method
[nextStep()](../../d5/d0d/classBase_1_1SequencerBase.html#a65ca8eb627a8bf4c9f91274637867f48
"This method can be reimplemented in sub-classes to give the user a feedback
when the next is performe...") gets invoked that can be reimplemented in sub-
classes. If _canAbort_ is true then the operations can be aborted, otherwise
(the default) the operation cannot be aborted. In case it gets aborted an
exception [AbortException](../../de/dce/classBase_1_1AbortException.html "The
AbortException is thrown if a pending operation was aborted.") is thrown.

References
[nextStep()](../../d5/d0d/classBase_1_1SequencerBase.html#a65ca8eb627a8bf4c9f91274637867f48),
[nProgress](../../d5/d0d/classBase_1_1SequencerBase.html#a8f546309a7f6ab043a757e79d5d5409e),
and
[nTotalSteps](../../d5/d0d/classBase_1_1SequencerBase.html#a34e1fc4574b504b22098ac12305a85a6).

Referenced by
[Import::FeatureImportIges::Execute()](../../d7/dac/classImport_1_1FeatureImportIges.html#a458fb556aa3581534c7a713c960ded7b),
[Import::FeatureImportStep::Execute()](../../da/dde/classImport_1_1FeatureImportStep.html#a42d170d40ce67819f931b5894145d229),
and
[Base::SequencerLauncher::next()](../../d0/dcc/classBase_1_1SequencerLauncher.html#ab82c78eee0e3e0f79b3d99950e689b4a).

## ◆ nextStep()

| void SequencerBase::nextStep  | ( | [bool](../../d9/db9/classbool.html) | _canAbort_| ) |   
---|---|---|---|---|---  
protectedvirtual  
  
This method can be reimplemented in sub-classes to give the user a feedback
when the next is performed.

The default implementation does nothing. If _canAbort_ is true then the
pending operation can aborted, otherwise not. Depending on the re-
implementation this method can throw an
[AbortException](../../de/dce/classBase_1_1AbortException.html "The
AbortException is thrown if a pending operation was aborted.") if canAbort is
true.

Reimplemented in
[Base::ConsoleSequencer](../../d6/d29/classBase_1_1ConsoleSequencer.html#ab1f5986903447662ca0beba64385d824),
[Gui::SequencerDialog](../../d2/da8/classGui_1_1SequencerDialog.html#aef7cb32e82644ade8e774360c672c481),
and
[Gui::SequencerBar](../../db/dae/classGui_1_1SequencerBar.html#ab5e2ff86a675c87157ea15743df5fe55).

Referenced by
[next()](../../d5/d0d/classBase_1_1SequencerBase.html#a708d36d490fcfb8ef3e5a65c68b692ac).

## ◆ numberOfSteps()

| size_t SequencerBase::numberOfSteps  | ( | | ) |  const  
---|---|---|---|---  
protected  
  
Returns the number of steps.

References
[nTotalSteps](../../d5/d0d/classBase_1_1SequencerBase.html#a34e1fc4574b504b22098ac12305a85a6).

Referenced by
[Base::SequencerLauncher::numberOfSteps()](../../d0/dcc/classBase_1_1SequencerLauncher.html#ab9458a363b7531131baafbd060f12608).

## ◆ operator=()

| [SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html) & Base::SequencerBase::operator=  | ( | const [SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html) & | | ) |   
---|---|---|---|---|---  
protecteddefault  
  
## ◆ pause()

| void SequencerBase::pause  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
Breaks the sequencer if needed.

The default implementation does nothing. Every
[pause()](../../d5/d0d/classBase_1_1SequencerBase.html#a804a91939fc20301356a1fa4cbd306b6
"Breaks the sequencer if needed.") must eventually be followed by a
corresponding
[resume()](../../d5/d0d/classBase_1_1SequencerBase.html#aea81b4efe906649564fd9b32e43484c3).

See also

    [Gui::ProgressBar](../../d2/d04/classGui_1_1ProgressBar.html). 

Reimplemented in
[Gui::SequencerDialog](../../d2/da8/classGui_1_1SequencerDialog.html#ad0d5e5e080625d4178674c46720e7ab1),
and
[Gui::SequencerBar](../../db/dae/classGui_1_1SequencerBar.html#a7d2791b4e5e7b6df72a6196e91bddecc).

## ◆ progressInPercent()

| [int](../../d1/da0/classint.html) SequencerBase::progressInPercent  | ( | | ) |  const  
---|---|---|---|---  
protected  
  
Returns the current state of progress in percent.

Referenced by
[Base::ConsoleSequencer::nextStep()](../../d6/d29/classBase_1_1ConsoleSequencer.html#ab1f5986903447662ca0beba64385d824).

## ◆ rejectCancel()

| void SequencerBase::rejectCancel  | ( | | ) |   
---|---|---|---|---  
protected  
  
If you tried to cancel but then decided to continue the operation.

E.g. in [Gui::ProgressBar](../../d2/d04/classGui_1_1ProgressBar.html) a dialog
appears asking if you really want to cancel. If you decide to continue this
method must be called.

Referenced by
[Gui::SequencerBar::checkAbort()](../../db/dae/classGui_1_1SequencerBar.html#aac14901da0adbe2bd0d66b5bfb140b85),
[Gui::SequencerDialog::nextStep()](../../d2/da8/classGui_1_1SequencerDialog.html#aef7cb32e82644ade8e774360c672c481),
and
[Gui::SequencerBar::nextStep()](../../db/dae/classGui_1_1SequencerBar.html#ab5e2ff86a675c87157ea15743df5fe55).

## ◆ resetData()

| void SequencerBase::resetData  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
Resets internal data.

If you want to reimplement this method, it is very important to call it in the
re-implemented method.

Reimplemented in
[Gui::SequencerDialog](../../d2/da8/classGui_1_1SequencerDialog.html#a55d7c56ccdde6515f11eac8edb899e01),
and
[Gui::SequencerBar](../../db/dae/classGui_1_1SequencerBar.html#aaf3679b1cb68e9f134d06c7ce53a2691).

Referenced by
[stop()](../../d5/d0d/classBase_1_1SequencerBase.html#af7abe491fae28be30f1f1fae10511303).

## ◆ resume()

| void SequencerBase::resume  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
Continues with progress.

The default implementation does nothing.

See also

    [pause()](../../d5/d0d/classBase_1_1SequencerBase.html#a804a91939fc20301356a1fa4cbd306b6 "Breaks the sequencer if needed."), 
     [Gui::ProgressBar](../../d2/d04/classGui_1_1ProgressBar.html). 

Reimplemented in
[Gui::SequencerDialog](../../d2/da8/classGui_1_1SequencerDialog.html#aa428b6789d2ef2638ced760efa0cea72),
and
[Gui::SequencerBar](../../db/dae/classGui_1_1SequencerBar.html#a15da7a69e5e4de781c3ad5f95375a70f).

## ◆ setLocked()

[bool](../../d9/db9/classbool.html) SequencerBase::setLocked  | ( | [bool](../../d9/db9/classbool.html) | _bLock_| ) |   
---|---|---|---|---|---  
  
If _bLock_ is true then the sequencer gets locked.

[startStep()](../../d5/d0d/classBase_1_1SequencerBase.html#a45d8df4cace8ae2b5c5b70a0c432a8f7
"This method can be reimplemented in sub-classes to give the user a feedback
when a new sequence start...") and
[nextStep()](../../d5/d0d/classBase_1_1SequencerBase.html#a65ca8eb627a8bf4c9f91274637867f48
"This method can be reimplemented in sub-classes to give the user a feedback
when the next is performe...") don't get invoked any more until the sequencer
gets unlocked again. This method returns the previous lock state.

References
[Base::SequencerP::mutex](../../d1/dd0/structBase_1_1SequencerP.html#a0bde1ec1441d27caba8ee72a0aa378b0).

Referenced by
[MeshGui::ViewProviderMesh::partMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#a252f3b9789355271cbc9ff56a65ba495),
and
[MeshGui::ViewProviderMesh::segmMeshCallback()](../../d7/dc1/classMeshGui_1_1ViewProviderMesh.html#af03a51bed2f5b62f24d2aecf1e03c4b4).

## ◆ setProgress()

| void SequencerBase::setProgress  | ( | size_t  | | ) |   
---|---|---|---|---|---  
protectedvirtual  
  
Sets the progress indicator to a certain position.

Reimplemented in
[Gui::SequencerDialog](../../d2/da8/classGui_1_1SequencerDialog.html#ab6c2501d317bd99fb2ad9b9338174ba2),
and
[Gui::SequencerBar](../../db/dae/classGui_1_1SequencerBar.html#a4f875a7d3b7fa9505b0322d0e25bdbc9).

Referenced by
[Base::SequencerLauncher::setProgress()](../../d0/dcc/classBase_1_1SequencerLauncher.html#a74937014111344719ab100ed721b1e16).

## ◆ setText()

| void SequencerBase::setText  | ( | const char *  | _pszTxt_| ) |   
---|---|---|---|---|---  
protectedvirtual  
  
Sets a text what the pending operation is doing.

The default implementation does nothing.

Reimplemented in
[Gui::SequencerDialog](../../d2/da8/classGui_1_1SequencerDialog.html#a129984ebaf54d682a26b7d845754fc99),
and
[Gui::SequencerBar](../../db/dae/classGui_1_1SequencerBar.html#aaecd83041d8c572120151d451abc6066).

Referenced by
[Base::SequencerLauncher::setText()](../../d0/dcc/classBase_1_1SequencerLauncher.html#a5a3b21d5fbeeb1c5ab6d91b55b724950),
and
[start()](../../d5/d0d/classBase_1_1SequencerBase.html#a9e388dd22618a5f8c04f5128e888929b).

## ◆ start()

| [bool](../../d9/db9/classbool.html) SequencerBase::start  | ( | const char *  | _pszStr_ ,   
---|---|---|---  
|  | size_t  | _steps_  
| ) | |   
protected  
  
Starts a new operation, returns false if there is already a pending operation,
otherwise it returns true.

In this method
[startStep()](../../d5/d0d/classBase_1_1SequencerBase.html#a45d8df4cace8ae2b5c5b70a0c432a8f7
"This method can be reimplemented in sub-classes to give the user a feedback
when a new sequence start...") gets invoked that can be reimplemented in sub-
classes.

References
[nProgress](../../d5/d0d/classBase_1_1SequencerBase.html#a8f546309a7f6ab043a757e79d5d5409e),
[nTotalSteps](../../d5/d0d/classBase_1_1SequencerBase.html#a34e1fc4574b504b22098ac12305a85a6),
[setText()](../../d5/d0d/classBase_1_1SequencerBase.html#ab666acb27961c1927c77a1a82a19879f),
and
[startStep()](../../d5/d0d/classBase_1_1SequencerBase.html#a45d8df4cace8ae2b5c5b70a0c432a8f7).

Referenced by
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunctionSegment::asString()](../../d4/dac/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunctionSegment.html#ac275f303f2e223f8a7240acec097e41a),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunctionSegment::clone()](../../d4/dac/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunctionSegment.html#a1354b5f743c2a57fa99cd802c4de9cfe),
[Import::FeatureImportIges::Execute()](../../d7/dac/classImport_1_1FeatureImportIges.html#a458fb556aa3581534c7a713c960ded7b),
[Import::FeatureImportStep::Execute()](../../da/dde/classImport_1_1FeatureImportStep.html#a42d170d40ce67819f931b5894145d229),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunctionSegment::hasStart()](../../d4/dac/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunctionSegment.html#ababd4d080b38f5f4e7e51158a4eb02bc),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunctionSegment::negated()](../../d4/dac/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunctionSegment.html#aadf8aa9c649bfc94e297dd68674106ac),
[Base::SequencerLauncher::SequencerLauncher()](../../d0/dcc/classBase_1_1SequencerLauncher.html#a1f72a046f7e9bab1995df453593d969d),
and
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunctionSegment::value()](../../d4/dac/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunctionSegment.html#a3b11be6837c2555c2b55e7ebdd5f0aad).

## ◆ startStep()

| void SequencerBase::startStep  | ( | | ) |   
---|---|---|---|---  
protectedvirtual  
  
This method can be reimplemented in sub-classes to give the user a feedback
when a new sequence starts.

The default implementation does nothing.

Reimplemented in
[Base::ConsoleSequencer](../../d6/d29/classBase_1_1ConsoleSequencer.html#adadead29c71f05952a15053b64843e82),
[Gui::SequencerDialog](../../d2/da8/classGui_1_1SequencerDialog.html#a1afc1a30a71b3b70b03c75d32baea783),
and
[Gui::SequencerBar](../../db/dae/classGui_1_1SequencerBar.html#a51c16449bedadd5534f9c9a88bd83ac2).

Referenced by
[start()](../../d5/d0d/classBase_1_1SequencerBase.html#a9e388dd22618a5f8c04f5128e888929b).

## ◆ stop()

| [bool](../../d9/db9/classbool.html) SequencerBase::stop  | ( | | ) |   
---|---|---|---|---  
protected  
  
Stops the sequencer if all operations are finished.

It returns false if there are still pending operations, otherwise it returns
true.

References
[resetData()](../../d5/d0d/classBase_1_1SequencerBase.html#a8c7af5d20b184eb577c09ce3f02782c8).

Referenced by
[ArchPanel.NestTaskPanel::accept()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ad42cd95d7c0a23ddf59be8c4b2b4c85f),
[Import::FeatureImportIges::Execute()](../../d7/dac/classImport_1_1FeatureImportIges.html#a458fb556aa3581534c7a713c960ded7b),
[Import::FeatureImportStep::Execute()](../../da/dde/classImport_1_1FeatureImportStep.html#a42d170d40ce67819f931b5894145d229),
[ArchPanel.NestTaskPanel::reject()](../../da/d77/classArchPanel_1_1NestTaskPanel.html#ae3ce3d1461b9cfc20c6bf6091114a8ce),
and
[Base::SequencerLauncher::~SequencerLauncher()](../../d0/dcc/classBase_1_1SequencerLauncher.html#a7471e6530431b1805b27d0e2af90b7a3).

## ◆ tryToCancel()

| void SequencerBase::tryToCancel  | ( | | ) |   
---|---|---|---|---  
protected  
  
Try to cancel the pending operation(s).

E.g. [Gui::ProgressBar](../../d2/d04/classGui_1_1ProgressBar.html) calls this
method after the ESC button was pressed.

Referenced by
[Gui::ProgressBar::eventFilter()](../../d2/d04/classGui_1_1ProgressBar.html#a40f423a80561579ade393f915077b8bf),
and
[Gui::ProgressDialog::onCancel()](../../da/d21/classGui_1_1ProgressDialog.html#a2ac37598f27f5facda203c3a44488a68).

## ◆ wasCanceled()

[bool](../../d9/db9/classbool.html) SequencerBase::wasCanceled  | ( | | ) |  const  
---|---|---|---|---  
  
Returns true if the pending operation was canceled.

References
[Base::SequencerP::mutex](../../d1/dd0/structBase_1_1SequencerP.html#a0bde1ec1441d27caba8ee72a0aa378b0).

Referenced by
[Gui::SequencerBar::checkAbort()](../../db/dae/classGui_1_1SequencerBar.html#aac14901da0adbe2bd0d66b5bfb140b85),
[Gui::ProgressBar::delayedShow()](../../d2/d04/classGui_1_1ProgressBar.html#a85387b78198a14fb7ebc12b0bc94801f),
[Gui::SequencerDialog::nextStep()](../../d2/da8/classGui_1_1SequencerDialog.html#aef7cb32e82644ade8e774360c672c481),
[Gui::SequencerBar::nextStep()](../../db/dae/classGui_1_1SequencerBar.html#ab5e2ff86a675c87157ea15743df5fe55),
and
[Base::SequencerLauncher::wasCanceled()](../../d0/dcc/classBase_1_1SequencerLauncher.html#a3dd373a3859ced0145dccc176b5ab3a0).

## Friends And Related Function Documentation

## ◆ SequencerLauncher

| [friend](../../d7/d23/classfriend.html) class
[SequencerLauncher](../../d0/dcc/classBase_1_1SequencerLauncher.html)  
---  
friend  
  
## Member Data Documentation

## ◆ nProgress

| size_t Base::SequencerBase::nProgress  
---  
protected  
  
Stores the current amount of progress.

Referenced by
[next()](../../d5/d0d/classBase_1_1SequencerBase.html#a708d36d490fcfb8ef3e5a65c68b692ac),
[Gui::SequencerDialog::nextStep()](../../d2/da8/classGui_1_1SequencerDialog.html#aef7cb32e82644ade8e774360c672c481),
[Gui::SequencerBar::nextStep()](../../db/dae/classGui_1_1SequencerBar.html#ab5e2ff86a675c87157ea15743df5fe55),
and
[start()](../../d5/d0d/classBase_1_1SequencerBase.html#a9e388dd22618a5f8c04f5128e888929b).

## ◆ nTotalSteps

| size_t Base::SequencerBase::nTotalSteps  
---  
protected  
  
Stores the total number of steps.

Referenced by
[next()](../../d5/d0d/classBase_1_1SequencerBase.html#a708d36d490fcfb8ef3e5a65c68b692ac),
[Base::ConsoleSequencer::nextStep()](../../d6/d29/classBase_1_1ConsoleSequencer.html#ab1f5986903447662ca0beba64385d824),
[numberOfSteps()](../../d5/d0d/classBase_1_1SequencerBase.html#ae72645f88f8f398096187bb6877e6e34),
[start()](../../d5/d0d/classBase_1_1SequencerBase.html#a9e388dd22618a5f8c04f5128e888929b),
[Gui::SequencerDialog::startStep()](../../d2/da8/classGui_1_1SequencerDialog.html#a1afc1a30a71b3b70b03c75d32baea783),
and
[Gui::SequencerBar::startStep()](../../db/dae/classGui_1_1SequencerBar.html#a51c16449bedadd5534f9c9a88bd83ac2).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Sequencer.h
  * FreeCAD/src/Base/Sequencer.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

