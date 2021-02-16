.. _autocomplete:

Autocomplete
============
Autocomplete is supported in HTML, CSS, and Javascript files. Simply start typing and matches are automatically displayed.

If you choose, you can disable autocomplete in your preferences:

``automatic_completions = false``

Other languages are supported with **language server protocol** although in such files, autocomplete is not automatically enabled. See :ref:`Language Server Protocol <langserver>` for more information.

HTML tags
---------
Autocomplete is context sensitive, so you will only be shown tags that are relevant to your location in the HTML file.

For example, if you are not in ``<body></body>``, fewer autocomplete options are shown. If you place your cursor inside the ``<body></body>`` tags, a full list of standard HTML tags are shown.

HTML attributes
---------------
If you enter ``<a`` and invoke autocomplete, a list of relevant attributes for the ``<a>`` tag are shown.

Tern and javascript
-------------------
We support intelligent autocomplete using TernJS. Tern also supports explicit directives in the **.tern-project** file, which you can move to the root of your project.

The file looks like this:

```json
{
  "libs": [
    "browser",
    "jquery"
  ],
  "loadEagerly": [
    "importantfile.js"
  ],
  "plugins": {
    "requirejs": {
      "baseURL": "./",
      "paths": {}
    }
  }
}
```

Codio only supports autocomplete for the currently opened file and items specified in the ``libs`` section of the **.tern-project** file. Refer to the [Tern documentation](https://ternjs.net/doc/manual.html#configuration) for full details on how to configure the **.tern-project** file.

CSS
---
To invoke autocomplete in a css file, use the **ctrl+space** keyboard shortcut.

Command bar
-----------
The Command Bar allows you to access almost all of the Codio actions from a searchable list. You can also use it to look up keyboard shortcuts. You simply start typing and the list is refined as you type.

.. image:: /img/command-bar.png
   :alt: Command Bar

Use one of the following methods to invoke the Command Bar:

- Click **Tools** on the menu bar and choose **Command Bar**.
- Press **Cmd+Shift+P** (Mac) or **Ctrl+Shift+P** (PC/Linux) on the keyboard.