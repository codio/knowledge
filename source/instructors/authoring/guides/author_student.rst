.. meta::
   :description: Author Student View
   
   
Author and student views
========================
The experience when authoring differs from that of a student. Students are not able to view the authoring tools. When they start a assignment or project, if there is content present, it will automatically be shown. The author can also specify whether the student is able to close the content or not.

If you are an author, you will often want to view the content as a student will see it.

Editing
*******
Only an author is able to edit the content. Students and users with read-only rights will not be able to. :ref:`Click here <page-editing>` for details on page editing.

Preview
*******
You can press the preview button in the top right area of the edit pane. This will switch to preview mode. You can then switch back to editor mode by pressing the **Editor** button.

You can also start the preview mode from the **Tools->Guide->Play**.

Finally, there is also a button at the top of the file tree that launches the content.

  .. image:: /img/guides/startguides.png
     :alt: StartGuides
     

Customizing IDE menu
********************
To simplify the educational process for students, the top menu can be customized to remove options from students that they cannot override. 

**Please note that only students will see this. Teachers previewing the assignment will not see the customization. If you wish to check this, the [test student](/courses/classes/#test-students) accounts can be used**

Through a `.codio-menu` file, a teacher can specify what menu items should be hidden.
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


**Be aware that if setting Status=false, students will need to use the 'Back to Dashboard' button shown on the last page of the guides to return to their dashboard area**

Setting up .codio-menu file:

  .. image:: /img/guides/codiomenu.png
     :alt: EditorMode



Menu items that the student will see:

  .. image:: /img/guides/codiomenupreview.png
     :alt: Preview Mode



Students will not see the .codio-menu file to be able to edit/change it.


Player Options
**************

  .. image:: /img/guides/playmode.png
     :alt: Player Options
     


When the content is rendered to a student, various options can be controlled

- The **Collapse table of contents**  button allows the user to collapse the content pane to provide larger working area if required. This option will not show if the page layout is One Pane
- **Navigation Buttons** allows the user to navigate forward/backward in the guide.
- **Settings** allows the user to view the assignment as a teacher (e.g. show solution information hidden to students) change the Theme (light/dyslexic), Mark as Complete, change the font size, reset both the theme and fonts, to restore the current files (see below) and to access Code Comments. See :ref:`Dyslexia Support <dyslexia>` section
- **Show/Hide Section List** Hamburger Icon allows the user to show/hide the section list.
- **Grading** button is visible for teachers to allow access to grading area. Students do not see this

Restore current files
---------------------
The Restore Current Files feature is a great way to reset/restore any files on that page to its initial state after hacking sample code around. Files can be restored from the menu as shown below.

  .. image:: /img/guides/reset.png
     :alt: Restore Current Files


