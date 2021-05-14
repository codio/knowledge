.. meta::
   :description: Author and student views of content in Guides.
   
   
Author and student views
========================
Students do not have access to the Codio content authoring tools in Guides. When a student begins an assignment, the Guide is automatically shown and the content will be rendered as intended for them and they cannot modify it. Content authors may specify whether students can close the Guides in the :ref:`Global Guide Settings <global>`. Content authors are able to view content as students would see it.

Editing content in Guides
*************************
Only an author is able to edit the content. Students and users with read-only rights will not be able to. :ref:`Click here <page-editing>` for details on page editing.

Preview content in Guides
*************************
You can preview content in Guides in one of the following ways:

- Press the preview button in the top right area of the edit pane, this will switch to preview mode. You can switch back to editor mode by pressing the **Editor** button.

- Select the **Tools->Guide->Play** menu option.

- Click the launch button at the top of the **Filetree**.

  .. image:: /img/guides/startguides.png
     :alt: StartGuides
     

Customizing IDE menu
********************
The top menu can be customized to remove options you don't want your students to have access to. 

.. Note::  Only students will see the modified menus. Teachers previewing the assignment will not see the customization. To view the environment as a student use the :ref:`test student <add-remove-students>` accounts.

Use a `.codio-menu` file to specify which menu items should be hidden.
Example:

.. code:: ini

    {
        "Logo": false, // hides the Codio logo
        "Codio": false, // hides the Codio menu dropdown
        "Project": {
             "Permissions": false // hides the Permissions option in the Project menu dropdown
        },
        "Help": false, // hides the Help menu dropdown
        "Run": false, // hides the Run menu dropdown
        "Preview": false, // hides the Preview menu dropdown
        "Debugger": false, // hides the Debugger menu dropdown
        "Status": false // hides the Status icon, user Avatar, user name and exit button
    }


.. Note:: If you set Status to false students will need to use the 'Back to Dashboard' button shown on the last page of the guides to return to their dashboard area. 

Setting up .codio-menu file:

  .. image:: /img/guides/codiomenu.png
     :alt: EditorMode



Menu items that the student will see:

  .. image:: /img/guides/codiomenupreview.png
     :alt: Preview Mode



Students do not have access to the .codio-menu file in the **Filetree**.

.. _player-options:

Guide player Options
********************

  .. image:: /img/guides/playmode.png
     :alt: Player Options
     


When the Guide is in Play mode, the following options may be available depending on who is viewing:

- The **Collapse** button allows the user to collapse the content pane to provide a larger working area. This option does not show if the page layout is One Pane.
- **Navigation Buttons** provide forward/backward scrolling in the guide.
- **Settings** allow the user to view the assignment as a teacher (e.g. show solution information hidden to students) change the Theme (light/dyslexic), Mark as Complete, change the font size, reset both the theme and fonts, to restore the current files (see below) and to access Code Comments. See :ref:`Dyslexia Support <dyslexia>` section
- **Show/Hide Index List** the Index icon allows the user to show/hide the index.
- **Grading** is available for teachers to access the grading area. Students do not see this option.

Restore current files
---------------------
The **Restore current files** feature provides the ability to reset/restore any edited files on that page to their initial state. Files can be restored from the menu as shown below.

  .. image:: /img/guides/reset.png
     :alt: Restore Current Files


