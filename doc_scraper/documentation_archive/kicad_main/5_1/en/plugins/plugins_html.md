---
url: https://docs.kicad.org/5.1/en/plugins/plugins.html
scraped_at: 2025-09-08T15:25:44.310249
title: Untitled
---


    /* Return a UTF-8 string naming the Plugin Class */
    char const* GetKicadPluginClass( void );
    
    /* Return version information for the Plugin Class API */
    void GetClassVersion( unsigned char* Major, unsigned char* Minor,
         unsigned char* Patch, unsigned char* Revision );
    
    /*
       Return true if the version check implemented in the plugin
       determines that the given Plugin Class API is compatible.
     */
    bool CheckClassVersion( unsigned char Major,
        unsigned char Minor, unsigned char Patch, unsigned char Revision );
    
    /* Return the name of the specific plugin, for example "PLUGIN_3D_VRML" */
    const char* GetKicadPluginName( void );
    
    /* Return version information for the specific plugin */
    void GetPluginVersion( unsigned char* Major, unsigned char* Minor,
         unsigned char* Patch, unsigned char* Revision );

