.. _langserver:

Language Server Protocol
========================

The Language Server rotocol (LSP) is used to integrate features such as autocomplete, go to definition, and find all references. Currently, Java, OCAML, and Python LSPs are available.

Below is a Python example:

.. image:: /img/pythonexample.png
   :alt: Python
   
Enable LSP support
------------------

To enable enable LSP support, enter the following in your :ref:`User <user-prefs>` or :ref:`Project <project-prefs>` Preferences:

.. code:: ini

    [codio-lsp]
    enable_lsp_support = true

If you are authoring content for use in a course, we recommend enabling LSP in :ref:`Project <project-prefs>` Preferences, as these are applied over user preferences.

Install LSP
-----------
To install LSPs, follow these steps:

1. Click the **Tools** tab and choose **Install Software**.
2. Find the relevant component and click the **Install** icon. 

The installation may take a few minutes and you should then :ref:`Restart <Restart and Reset>` your box before proceeding.

Autocomplete
------------

Autocomplete is not automatically triggered as in HTML/CSS/JS files. To invoke autocomplete for LSP implemented files, use the following shortcuts:

- Mac - Shift+Space
    
- Others - Ctrl+Space

If you want to change the default preference, see :ref:`User Preferences <user-prefs>`.