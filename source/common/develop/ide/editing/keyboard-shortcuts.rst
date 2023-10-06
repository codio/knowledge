.. meta::
   :description: Keyboard Shortcuts available in the IDE.

.. _shortcuts:

Keyboard Shortcuts
==================

Codio offers default keyboard shortcuts and Emmet keyboard shortcuts; all of which can be customized in :ref:`User Preferences <user-prefs>`. General keyboard shortcuts can be found in the **Help > Shortcuts** menu. 

See the `Emmet Cheat Sheet <http://docs.emmet.io/cheat-sheet/>`__ for a complete list of shortcuts.

.. figure:: /img/emmet-ref.png
   :alt: Emmet Cheat Sheet


Match tag pair
--------------
Searches for tag(s) content bounds from current cursor position and selects it. It will expand (outward balancing) or shrink (inward balancing) selection when called multiple times. Not every editor supports both inward and outward balancing due of some implementation issues, most editors have outward balancing only.

* Mac - **Cmd+D** (inward) and **Shift+Cmd+D** (outward)
* PC/Linux - **Ctrl+D** (inward) and **Shift+Ctrl+D** (outward)

Go to matching pair
-------------------
Allows you to quickly traverse between opening and closing tag in HTML code.

*Mac - **Shift+Cmd+T**
*PC/Linux- **Shift+Ctrl+T**

Wrap with abbreviation
----------------------
Expands an abbreviation and places currently selected content in the last element of generated snippet. If there’s no selection, action silently calls **Match tag pair** to wrap context element.

* Mac - **Shift+Cmd+A**
* PC/Linux - **Shift+Cmd+A**

Go to edit point
----------------
Allows you to quickly traverse between important code points in HTML code blocks, including between tags, empty attributes, and new lines with indentation.

* Win - **Ctrl+Alt+Right Arrow** or **Ctrl+Alt+Left Arrow**

Select item
-----------
Action selects important code parts. In HTML, it selects tag name, full attribute, and attribute value. For class attribute it also selects distinct classes. In CSS, it matches selector, full property, and property value. For complex values and functions like 1px solid red or url (image.jpg), it also selects part of it.

* Mac - **Shift+Cmd+**
* PC/Linux - **Shift+Cmd+**

Toggle comment
--------------
Toggles comments on and off for the selected line in HTML and CSS files.

* Mac - **Cmd+/**
* PC/Linux - **Ctrl+/**

Remove tag
----------
Quickly removes tag, found by **Match tag pair** from current cursor position, and adjusts indentation.

* Mac - **Cmd+K**
* PC/Linux - **Ctrl+K**

Merge lines
-----------
Merges selected lines into a single line. When there is no selection, it matches context HTML tag.

*Mac - **Shift+Cmd+M**
*PC/Linux - **Shift+Ctrl+M**

Inline calculator
-----------------
Evaluates simple math expressions like 2\*4 or 10/2 and outputs its result. You can use ``\`` operator which is equivalent to round(a/b).

* Mac - **Shift+Cmd+Y**
* PC/Linux - **Shift+Ctrl+Y**

Increment/decrement number
--------------------------
Increments or decrements the number under the cursor with different steps: 0.1, 1 or 10.

* Mac/PC/Linux - **Alt+Up/Down** (inc/dec by 0.1)
* Mac/PC/Linux - **Ctrl+Up/Down** (inc/dec by 1)
* Mac/PC/Linux - **Ctrl+Alt+Up/Down** (inc/dec by 10)


