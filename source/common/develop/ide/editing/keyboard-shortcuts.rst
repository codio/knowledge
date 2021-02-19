.. _shortcuts:

Keyboard Shortcuts
==================

Codio offers default keyboard shortcuts, which can be customized or Emmet keyboard shortcust.Codio

Default Keyboard Shortcuts
--------------------------
General keyboard shortcuts can be found `in this section </project/ide/editing/#keyboard-shortcuts>`__. All other productivity shortcuts are found here in this chapter.

Emmet Keyboard Shortcuts
~~~~~~~~~~~~~~~~~~~~~~~~

A set of powerful `productivity shortcuts </project/ide/editing/#special-keyboard-actions>`__ for HTML5, CSS and Javascript.


Special keyboard actions
~~~~~~~~~~~~~~~~~~~~~~~~

Emmet also offers a very nice range of keyboard shortcuts to speed productivity even further. Keyboard actions can be modified in `Preferences </project/ide/settings/#user-preferences>`__

Match Tag Pair
~~~~~~~~~~~~~~

``Mac:Cmd+D (inward) and Shift+Cmd+D (outward)``
``WinLin:Ctrl+D (inward) and Shift+Ctrl+D (outward)``

A well-known tag balancing: searches for tag or tag's content bounds from current cursor position and selects it. It will expand (outward balancing) or shrink (inward balancing) selection when called multiple times. Not every editor supports both inward and outward balancing due of some implementation issues, most editors have outward balancing only.

Click here to see it in the Emmet site.

Go To Matching Pair
~~~~~~~~~~~~~~~~~~~

``Mac: Shift+Cmd+T`` ``Win: Shift+Ctrl+T``

In HTML, allows you to quickly traverse between opening and closing tag.

Click here to see it in the Emmet site.

Wrap with Abbreviation
~~~~~~~~~~~~~~~~~~~~~~

``Mac/Win: Shift+Cmd+A``

A very powerful feature, it takes an abbreviation, expands it and places currently selected content in the last element of generated snippet. If there’s no selection, action will silently call “Match Tag Pair” to wrap context element.

Click here to see it in the Emmet site.

Go to Edit Point
~~~~~~~~~~~~~~~~

``Win: Ctrl+Alt+Right Arrow or Left Arrow``

This action works for HTML code blocks and allows you to quickly traverse between important code points:

-  between tags
-  empty attributes
-  newlines with indentation

Click here to see it in the Emmet site.

Select Item
~~~~~~~~~~~

``Mac/Win: Shift+Cmd+``

Action is similar to “Go to Edit Point”, but selects important code parts.

In HTML, these are tag name, full attribute and attribute value. For class attribute it also selects distinct classes.

In CSS, it matches selector, full property and property value. For complex values and functions like 1px solid red or url(image.jpg) also selects part of it.

Click here to see it in the Emmet site.

Toggle Comment
~~~~~~~~~~~~~~

``Mac: Cmd+/`` ``Win: Ctrl+/``

This action, as name says, toggles comments on and off for the selected line. Works nicely in CSS and HTML files.

Click here to see it in the Emmet site.

Remove Tag
~~~~~~~~~~

``Mac: Cmd+K`` ``Win: Ctrl+K``

Quickly removes tag, found by “Match Tag Pair” from current cursor position, and adjusts indentation.

Click here to see it in the Emmet site.

Merge Lines
~~~~~~~~~~~

``Mac: Shift+Cmd+M`` ``Win: Shift+Ctrl+M``

Merges selected lines into a single line. But when there’s no selection, will match context HTML tag.

Click here to see it in the Emmet site.

Inline Calculator
~~~~~~~~~~~~~~~~~

``Mac: Shift+Cmd+Y`` ``Win: Shift+Ctrl+Y``

Evaluates simple math expressions like 2\*4 or 10/2 and outputs its result. You can use ``\`` operator which is equivalent to round(a/b).

Very useful in CSS where numeric values should be modified frequently.

Click here to see it in the Emmet site.

Increment/Decrement Number
~~~~~~~~~~~~~~~~~~~~~~~~~~

``Mac/Win : Alt+Up/Down (inc/dec by 0.1)``
``Mac/Win : Ctrl+Up/Down (inc/dec by 1)``
``Mac/Win : Ctrl+Alt+Up/Down (inc/dec by 10)``

This action, as name says, increments or decrements the number under the cursor with different steps: 0.1, 1 or 10.

Click here to see it in the Emmet site.

Complete reference
~~~~~~~~~~~~~~~~~~

Emmet has a huge number of shortcuts available. Check out the `Emmet Cheat Sheet <http://docs.emmet.io/cheat-sheet/>`__

.. figure:: /img/emmet-ref.png
   :alt: Emmet Cheat Sheet


Keyboard shortcuts
------------------

You have full control over the keyboard shortcuts for code editing. You should refer to the `Codio Preferences </project/ide/settings/#user-preferences>`__ section to read more about this.

Codio has its own complete set of defaults, all of which can be overriden. You can use Vim or Emacs key bindings by modifying the ``keymap`` preference setting. If you do not use ``keymap=default``, you cannot override keyboard shortcuts.

The sections that contain productivity specific actions and shortcuts are ``[Editor]`` and ``[Emmet]``.
