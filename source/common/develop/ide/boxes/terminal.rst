.. meta::
   :description: Terminal Window

.. _terminal:

Terminal Window
===============

You can open a terminal window in a new IDE panel using the menu bar or the icons in the Filetree:

- To open from menu bar, click **Tools > Terminal** on the menu bar.

- To open from the file tree, click the **Terminal** icon in the upper menu bar of the file tree. 

  .. image:: /img/terminalicon.png
     :alt: Terminal Icon

You can also have multiple terminals open simultaneously.

You can create panels and tabs to customize your project layout. See :ref:`Panels and Tabs <panels>` for more information.

.. image:: /img//terminal.png
   :alt: Terminal


Terminal settings
-----------------
You can modify the Terminal settings from the **Codio > Preferences** menu. The following settings can be modified (defaults are shown): 

.. code:: ini

    [terminal]

    ;Font size.
    ; Type: int 
    font_size = 12

    ;Terminal theme.
    ; Type: string 
    theme = dark

    ;Number of lines available in the scroll history.
    ; Type: int 
    scrollback = 3000

    ;Quick Connect
    ; Type: hotkey 
    show-connect-dialog = 

    ;Connections Manager
    ; Type: hotkey 
    show-connections-manager = 

    ;Terminal. SSH connection to the box
    ; Type: hotkey 
    backend-connection = Shift+Alt+T

Preferences can be modified at the User level as described in :ref:`User Preferences <user-prefs>` or at the Project level.

**Note:** When changing settings at the Project level, the settings will be applied for all users looking at the project.