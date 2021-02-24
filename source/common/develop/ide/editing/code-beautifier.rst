.. _code-beautifier:

Code Beautifier
===============
The Code Beautifier feature automatically indents and manages spaces in your code to format it correctly. You apply the Code Beautifier using the shortcut keys, which can be customized in :ref:`User Preferences <user-prefs>`.

* key_format_code = cmd+Shift+B (Mac)
* key_format_code = Ctrl+Shift+B (PC/Linux)

As an example, if you enter code as follows:

.. code:: js

    if ('this_is'==/an_example/){of_beautifer();}else{var a=b?(c%d):e[f];}


It transforms to this after applying the Code Beautifier shortcut:

.. code:: js

    if ('this_is' == /an_example/) {
        of_beautifer();
    } else {
        var a = b ? (c % d) : e[f];
    }


Settings
--------
The **Code Beautifier** settings can be found in the [code-beautifier] section of the Codio Preferences. You can also modify these settings in :ref:`Project Preferences <project-prefs>` to force beautification to all code, regardless of who edits it.