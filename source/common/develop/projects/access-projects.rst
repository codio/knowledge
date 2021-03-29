.. meta::
   :description: Access Projects

.. _access-projects:

Access Projects
===============

You access your projects from **My Projects** in the left navigation pane. The **Projects** page shows all of your coding projects and those projects that have been shared with you.

If a project has been shared with you, you can view the projects from the **Shared with me** page on the **Projects** dashboard.

.. image:: /img/console-shared.png
   :alt: Shared Project

Access another user's project
-----------------------------
If you know the user name of another Codio user, you can enter the URL for their account (https://codio.com/username) and view their **Project** dashboard, where all of their public projects will be displayed. You can click the project to load it into the IDE and copy it into your account (you cannot edit another user's project). See Copying a Project for more information.

You cannot edit another user's project but you can :ref:`copy a project <copy-project>` into your own account.


Open a project
--------------
To open a project in the IDE, simply click the project name.

Access project settings
-----------------------
Use one of the following methods to access your project settings:

- Open the project and click the **Settings** (gear) icon.
- Open the project, click the **Project** tab and choose **Settings** on the menu bar.


Filter projects
---------------
You can filter how the projects are displayed on the Project page by name or most recently accessed. Click the filter drop-down and choose **Name** or **Last Accessed**.

Search projects
---------------

To search for a specific project, enter the name in the Search text box. The file list dynamically filters the projects as you enter characters.

Codio also supports advanced search capabilities which use search tokens to narrow your search criteria. The following search tokens are supported:

- Tokens with parameters allow you to type the search criteria after the colon delimiter:

  - `name:` search the project name
  - `desc:` search the project description
  - `owner:` search the project owner
  - `org:` search for an organization name
  - `begin:` search for a class start date (Education feature)
  - `end:` search for a class end date (Education feature)

- Tokens without parameters can be used simply by adding a space after them if you have anything else to enter in the search line:

  - `my:` show only projects owned by me
  - `shared:` show only projects that are shared with me
  - `public:` show only my public projects
  - `private:` show only my private projects

For example:

- `public: desc:javascript` searches your public projects where 'javascript' appears in the project description.
- `owner:superman javascript` searches projects owned by the user 'superman'' where 'javascript' appears in the project name or description.