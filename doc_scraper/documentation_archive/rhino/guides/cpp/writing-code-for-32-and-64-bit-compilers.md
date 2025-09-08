---
url: https://developer.rhino3d.com/guides/cpp/writing-code-for-32-and-64-bit-compilers/
scraped_at: 2025-09-08T15:40:21.771830
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

[Writing Code for 32- and 64-bit
Compilers](https://developer.rhino3d.com/guides/cpp/writing-code-
for-32-and-64-bit-compilers/)

  * strlen
  * fread and fwrite
  * Sort functions that compare pointers
  * size_t
  * Formatted printing
  * Windows SendMessage
  * Windows SetWindowLong and GetWindowLong
    * Timers

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Writing Code for 32- and 64-bit Compilers

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## strlen

The return type of string length functions like `strlen` and `wcslen` is a
`size_t`. Since we will never have null terminated strings with more than
2,147,483,647 characters, simply use a cast like so:

    
    
    int length = (int)wcslen(str);  //(int) cast for 64 bit compilers
    

## fread and fwrite

The return type of `fread` and `fwrite` is a `size_t`. Design your calls to
`fread` and `fwrite` so that the count argument is never > 2,147,483,648 and
use an int cast on the return type like so:

    
    
    int count = ...;  some number <= 2,147,483,648
    if ( count != (int)fread( buffer, size, count, fp ) )
    {
      //fread failed
      //handle file reading error
    }
    

or

    
    
    int count = ...;  some number <= 2,147,483,648
    if ( count != (int)fwrite( buffer, size, count, fp ) )
    {
      //fwrite failed
      //handle file writing error
    }
    

If you are compelled to write 9,223,372,036,854,775,808 bytes in a single call
to `fwrite`, you can do so with:

    
    
    size_t size = 9223372036854775808;
    void* buffer = ...;
    FILE* fp = ...;
    if ( 1 != fwrite( buffer, size, 1, fp ) )
    {
      //failed to write 9223 terrabytes in a single call to fwrite - duh
      //printf("You're a looser\n");
    }
    

## Sort functions that compare pointers

Use `INT_PTR` to store the difference between two pointers.

    
    
    //Sort functions have to return 32 bit ints
    static int compar( const void** a, const void** b )
    {
    //pointer differences have to be INT_PTR (64 bit int on x64)
     INT_PTR i = ((const CTheRealType**)b)->pRhinoObject - ((const CTheRealType**)a)->pRhinoObject
      //Expect i to be > MAX_INT, so do something like this
     return ( (i<0) ? -1 : ( (i>0) ? 1 : 0 );
    }
    

## size_t

The type `size_t` is 64 bits on a 64-bit compiler. See the `strlen` and
`fread` sections above for examples on dealing with this.

## Formatted printing

You really need to pay attention to the size of your integer arguments to
formatted printing strings.

    
    
    int i = ...;
    size_t sz = ...;
    void* ptr = ...;
    INT_PTR ip = ...;
    hyper h = ...;
    __int64 i64 = ...;
    RhinoApp().Print("i = %d  sz = %Id ptr = %I08X ip = %Id h = %I64d i64 = %I64d\n",
                     i,sz,ptr,ip,h,i64);
    

## Windows SendMessage

If you cast the `WPARAM` and `LPARAM` arguments as (`WPARAM`) and (`LPARAM`),
and put the return value in an `LRESULT`, everything works perfectly for both
the 32- and 64-bit compilers. Since the value of `smresult` can be an `int`,
`pointer`, `handle`, whatever, cast `smresult` as shown below.

    
    
    LRESULT smresult = SendMessage((UNIT)id, (WPARAM)&gt, (LPARAM)sText);
    int rc = (int)smresult ;  //In this case, I the rest of the code want
    HWND hwnd = (HWND)smresult;
    char** ptr = (char**)smresult;
    

## Windows SetWindowLong and GetWindowLong

Replace every single instance of Windows calls that pass pointers as mystery
meat with the `Ptr` versions.

    
    
    //BAD            //GOOD
    SetWindowLong -> SetWindowLongPtr
    GetWindowLong -> GetWindowLongPtr
    

If you do this, then your code will work perfectly and compile cleanly on both
32- and 64-bit platforms.

The `Ptr` part of the function names is misleading. The `Ptr` versions work
when the return value or last argument has any type.

Bad:

    
    
    SetWindowLong( *pDockFrame, GWL_USERDATA, (LONG)this);
     WNDPROC wp = (WNDPROC)::GetWindowLong( *pDockFrame, GWL_WNDPROC);
     DWORD dwStyle = ::GetWindowLong( pMsg->hwnd, GWL_STYLE)
    

Good:

    
    
    SetWindowLongPtr( hwnd, id, (LONG_PTR)this);
    WNDPROC wp = (WNDPROC)::GetWindowLongPtr( *pDockFrame, GWL_WNDPROC);
    DWORD dwStyle = (DWORD)::GetWindowLongPtr( pMsg->hwnd, GWL_STYLE)
    

### Timers

The value returned by `Windows ::SetTimer()` needs to be saved in a
`UINT_PTR`.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/writing-
code-for-32-and-64-bit-compilers/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/writing-
code-for-32-and-64-bit-compilers/index.md) [
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

