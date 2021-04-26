.. meta::
   :description: Modify a project or assignment Stack by installing items using the terminal.

.. _modify-stack:

Modify a Stack
==============
Any changes you or an application makes to the software on the server (box) outside the **Workspace** folder is considered a stack modification. Such modifications may include changes made using `sudo apt-get install`, manually editing a config file, or changes to a database due to application usage. 

You can modify the stack at any time by opening a project, or course assignment and making the stack changes from the :ref:`command line <terminal>`. Keep in mind that your modifications will work fine on the project you are working on as the owner, but the modifications will not be transferred to those being run by your students. 

You must first create a clean stack with your modifications and then switch the project to the clean stack. See :ref:`Creating a Stack <create-stack>` and :ref:`Switching a Project Stack <switch-stack>` for more information.

Rules for modifying a stack
---------------------------

Before modifying a stack, be aware of the following rules:

- If you are the stack owner or have write access to the stack, you can create new versions of an existing stack. 

- If you do not have write access to the stack, which is the case for the Codio certified stacks, you need to create a new stack for which you are the owner and then create your own versions from that stack.

- If the stack is **Private** and the owner is set to an organization where you are a member, you have write access and can create new versions of that stack.  

See :ref:`Stacks <stacks>` for information about visibility and ownership.

Use case of a stack modification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If a MySQL database's data is in the normal location within the stack (`/var/lib/mysql/`), when the project is assigned to the course, each student gets their own database, independent of other students. However, if the stack is changed for any reason (for example, the project owner makes a change or the stack version has changed for an already assigned assignment), all database data will be reset to the state of the new stack since the database data folder is not a part of the workspace.

If you want to keep the database independent of the stack, you should include the database file in the **Workspace** folder (by editing `/etc/mysql/mysql.conf.d/mysqld.cnf`). You can then update the database software via a stack change but keep the database data intact when you switch stacks.

Remember the following points to avoid issues:

- Assignment = Selected Stack + Stack Changes + Workspace Folder
- When run by students from an assignment: Assignment = Selected Stack + Workspace (no stack modifications)
- Stack modifications in the source project or assignment are **not transferred** when students launch the assignment.

.. Note:: Once the project or assignment is run by students, if they make changes to their stacks, each stack is individually handled so there are no issues unless a new stack is selected in **Project > Stacks > Settings** on the menu bar.