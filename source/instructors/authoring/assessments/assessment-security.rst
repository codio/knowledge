.. meta::
   :description: Storing code tests and solutions securely.
   
.. _assessment-security:

Assessment Security
===================

Data for assessments is stored in individual files in the ``.guides/assessments`` folder. 
Other folders automatically created in the ``.guides`` directory are: ``.guides/img`` and ``.guides/content``.
Student assignments only receive the ``.guides`` folder and the ``.guides/img`` folder. If you have not provided student access to the file tree in the :ref:`page layout <page>`, the ``.guides`` folder will not be visible. 


The ``.guides`` folder is a good place to store bash files or data files because they can't be easily deleted by the student via the file tree. Keep in mind though, if students have access to the terminal they can use it to view any files in their Linux container, including the ``.guides`` folder.

Files that are stored in the ``.guides`` folder can be updated even if students have already started an assignment.
When you publish an assignment that students have already started, pre-existing files in the student workspace ``\home\codio\workspace`` will not be updated in order to make sure student work is not overwritten.
More information on this topic may be found on the :ref:`modify assignments <modify-assignments>` page.

Blocking student access to the terminal
---------------------------------------

The :ref:`terminal <terminal>` can be accessed from the file tree, the menu or by using the key combination (Shift+Alt+T on a PC, Shift+Option+T on a Mac). If you want to block all student access to the terminal you need to hide the file tree in the page layout, :ref:`customize the IDE menu<custom-ide>` and block the keyboard short cut in :ref:`project preferences<project-prefs>`.

The Secure folder
-----------------

If you are creating your own testing scripts or unit tests you can create a folder named ``.guides\secure`` to safely store test files. The secure directory is not copied over to the student version of the assignment. 
When a student runs a code test that references a file in the ``.guides\secure`` folder, an **ephemeral** container is created that is a combination of the student workspace and the ``.guides\secure`` folder the instructor created. 
This container is referred to as **ephemeral** because it only exists during the execution of the assessment. If you open a student project to view their work, you will not have access to the secure folder because it does not exist in the student environment.

Your test should not write any information to the ``.guides\secure`` folder because it does not persist. 
All output should conveyed using either stdout or the feedback buffer that is described in the individual assessesment types that can use the secure folder, :ref:`Advanced Code Test <advanced-code-test>`, :ref:`Free Text Autograde <free-text-autograde>` and :ref:`Assignment Level Scripts <auto-grade-scripts>`.

Standard code tests do not have access to the secure folder by default but you *can* force a :ref:`Standard Code Test <standard-code-test>` to run in an **ephemeral** container by including a file name with the ``.guides\secure`` path in the **Command** portion on the **Execution** tab. 
This could be done if you are passing a file name as a parameter or if you have no command line parameters, you can put the file name on the command line and it will be ignored by your program but Codio will run the test in a container with the Secure folder mounted. Then you can specify a file in ``.guides\secure`` as an input parameter.