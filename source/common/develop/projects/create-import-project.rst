.. meta::
   :description: Create or Import a Project

.. _create-import-project:

Create or Import a Project
==========================

You can create a new project or import a project from the **Projects** page by following the relevant procedure.

Create empty project
--------------------

To create a new empty project, follow these steps:

1. Click **My Projects** in the navigation pane and click **New Project**.

   .. image:: /img/project_create.png
      :alt: Create Project

2. Click one of the following project templates:

   - Java 11  
   - Python 
   - Nodejs 
   - C
   - C++
   - Empty Stack 

   Projects created from a template include an explanatory README.md file that provides useful information to help you get started. The template (with the exception of **Empty Stack**) also includes a pre-configured .codio menu setup with basic actions the selected project requires. If you want to re-configure the .codio menu file, see :ref:`Customizable Run Menu <customizable-run-menu>` for more information.

  Because you have **sudo** level privileges, you can also customize any stack from the command line. See :ref:`Stacks <stacks>` to learn how to create and manage your own software configuration templates.

3. Enter a **Name** and **Description** for your project. This is the information that is displayed in your projects list.

4. Select the visibility of the project (Private or Public). By default, all projects are created as private and are only accessible to you (in **My Projects**, a padlock icon is displayed next to all private projects.

   **Note:** If enabled by your organization owner, you can create public projects but these are accessible by any Codio user. See :ref:`Public and Private Settings <public-private>` for more information.

  If your project is private, you can assign read, write, or full admin permissions (ability for others to access the box from the terminal) to other users from the **Project > Permissions** menu in the IDE.

Import a project
----------------

To import a project or choose an alternative software configuration, follow these steps:

1. Click **My Projects** in the navigation pane and click **New Project**.

   .. image:: /img/project_create.png
      :alt: Create Project

2. Click the **Click here** link to import or select an alternative software configuration.

3. Click one of the following options:

  - **Empty with Stack** - Create a new project and browse to the **Stack** you want to import.
  - **Copy Project** - Create a new project by copying one of your other projects. If you choose this option, browse to the project to **Copy From**.
  - **Starter Pack** - Create a project from a Stack and browse to the pre-configured **Starter Pack**. This option is a combination of a Stack and a pre-configured code workspace.
  - **Import** - Create a project by importing it from Git or from a Zip file of a Codio project. If you choose this option, browse to the **Stack** and choose the **Source** from the drop-down list.

   .. image:: /img/project_create_other.png
     :alt: Import Project

3. Enter a **Name** and **Description** for your project. This is the information that is displayed in your projects list.

4. Select the visibility of the project (Private or Public). By default, all projects are created as private and are only accessible to you (in **My Projects**, a padlock icon is displayed next to all private projects.

   **Note:** If enabled by your organization owner, you can create public projects but these are accessible by any Codio user. See :ref:`Public and Private Settings <public-private>` for more information. 
   
   

  If your project is private, you can assign read, write, or full admin permissions (ability for others to access the box from the terminal) to other users from the **Project > Permissions** menu in the IDE.
