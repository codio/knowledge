.. meta::
   :description: Storing code tests and solutions securely.
   
.. _assessment-security:

Assessment Security
====================

File Organization
-----------------

Assessment data is stored in individual files within the ``.guides/assessments`` folder. The ``.guides`` directory automatically contains the following subdirectories:

- ``.guides/assessments`` - Assessment configuration files
- ``.guides/img`` - Image assets
- ``.guides/content`` - Content files

Student Workspace Limitations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When students receive an assignment, they only get access to:

- The ``.guides`` folder
- The ``.guides/img`` folder

If you have not enabled student access to the file tree in the :ref:`page layout <page>`, the ``.guides`` folder will not be visible to them.



Using the .guides Folder
------------------------


Benefits and Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``.guides`` folder provides a secure location for storing bash scripts and data files, as students cannot easily delete them through the file tree interface. However, be aware that students with terminal access can view any files in their Linux container, including contents of the ``.guides`` folder.

Updating Published Assignments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Files stored in the ``.guides`` folder can be updated even after students have started an assignment. When you republish an assignment that students have already begun:

- Files in ``.guides`` **will be updated**.
- Pre-existing files in the student workspace (``/home/codio/workspace``) **will not be updated** to prevent overwriting student work.

For more information, see the :ref:`modify assignments <modify-assignments>` page.



Blocking Student Access to the Terminal
---------------------------------------


The :ref:`terminal <terminal>` can be accessed through multiple methods:

- From the file tree
- From the menu
- Via keyboard shortcuts (Shift+Alt+T on PC, Shift+Option+T on Mac)

To completely block student access to the terminal, you must:

1. Hide the file tree in the page layout
2. :ref:`Customize the IDE menu <custom-ide>` to remove terminal access
3. Block the keyboard shortcut in :ref:`project preferences <project-prefs>`



The Secure Folder
-----------------

Overview
~~~~~~~~

The ``.guides/secure`` folder provides a protected location for storing testing scripts and unit tests. This folder offers enhanced security because it is **not copied** to the student version of the assignment.

How It Works
~~~~~~~~~~~~

When a student runs a code test that references files in ``.guides/secure``, an **ephemeral container** is created that combines:

- The student workspace
- The instructor's ``.guides/secure`` folder

This container is called "ephemeral" because it only exists during assessment execution. If you open a student project to review their work, you will not see the secure folder—it does not exist in the student environment.

Important Limitations
~~~~~~~~~~~~~~~~~~~~~


**Do not write to the secure folder** during test execution, as changes will not persist. All output must be conveyed through:

- Standard output (stdout)
- The feedback buffer (described in individual assessment documentation)

Assessment Types Supporting Secure Folder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following assessment types can access the secure folder:

- :ref:`Advanced Code Test <advanced-code-test>`
- :ref:`Free Text Autograde <free-text-autograde>`
- :ref:`Assignment Level Scripts <auto-grade-scripts>`

Using Secure Folder with Standard Code Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`Standard Code Tests <standard-code-test>` do not have access to the secure folder by default. However, you can force a Standard Code Test to run in an **ephemeral container** by including a file path with ``.guides/secure`` in the **Command** field on the **Execution** tab.

Implementation Methods
~~~~~~~~~~~~~~~~~~~~~~

You can trigger ephemeral container creation by:

- Passing a secure folder file name as a parameter
- Including the file name on the command line (it will be ignored by your program, but signals Codio to mount the secure folder)

Once the ephemeral container is created, you can specify files in ``.guides/secure`` as input parameters for your tests.