.. meta::
   :description: Using Git and GitHub in Codio.

.. _git:

Git and GitHub
==============
Git and GitHub are preinstalled, as well as Mercurial and SVN. You can open a :ref:`Terminal window <terminal>` to access them from the command line. The **Tools > Git** menu includes options for using Git. 

You can also configure your **.codio** file to create a **Run** menu from which you can access common commands in the Codio IDE. See :ref:`Customize Run Button <customizable-run-menu>` for more information.

If you are new to Git, refer to this reference page to get started `Git reference <http://git-scm.com/docs>`__



Use Git Without Remote Repos
----------------------------
You can use Git commands in your Codio project without using a remote repo, providing more collaborative capabilities and comprehensive version control. However, you can add a remote repository, such as GitHub (recommended), if you want to save your code in more than one location as a back up. 

To add a repo, click **Tools > Git > Remotes**.

Alternatively, you can use the regular ``git`` commands in your terminal.


Find Stack Version ID
.....................
To find the appropriate stack to use with your repo, go to **Stacks** in the Dashboard, choose the stack to be used, and click **Use Stack**. In the address bar, you can view the stack version ID to add to your link in the readme.md file.

Example showing the **Empty Stack** stack version ID:

.. figure:: /img/stackversionid.png
   :alt: Empty Stack Version ID

You can use any method for linking to Codio but we recommend using the following images:

.. figure:: /img/open-in-ide.png
   :alt: Open in IDE
   
.. figure:: /img/demo-in-ide.png
   :alt: Demo in IDE


Manually Import a Git repo Into Codio
-------------------------------------
To manually import a Git repo into Codio, follow these steps:


+--------------------------------------------------------------+--------------------------------------------------------------------+
| 1. In GitHub, click the green **Code** button on the right   | .. image:: /img/github-clone-url.png                               |
|    and copy to the clipboard.                                |    :alt: create from GitHub                                        |
|                                                              |    :width: 510px                                                   |
|                                                              |                                                                    |
| 2. Log in to Codio and click **New Project**.                |                                                                    |
|                                                              |                                                                    |
|                                                              | .. image:: /img/github-create.png                                  |
| 3. Click the **Click here** link for more options.           |    :alt: create from GitHub                                        |
|                                                              |    :width: 350px                                                   |
|                                                              |                                                                    |
| 4. In the **Select your Starting Point** area, click         |                                                                    |
|    **Import**.                                               |                                                                    |
|                                                              |                                                                    |
|                                                              |                                                                    |
| 5. From the **Source** drop-down list, choose **Git**.       |                                                                    |
|                                                              |                                                                    |
|                                                              |                                                                    |
| 6. Paste the Git URL into the **URL** field and add          |                                                                    |
|    details about the project.                                |                                                                    |
|                                                              |                                                                    |
|                                                              |                                                                    |
| 7. Click **Create**. Codio loads the repo and displays it.   |                                                                    |
+--------------------------------------------------------------+--------------------------------------------------------------------+



.. raw:: html

  <div style="margin: 0 0 10px 20px; padding: 10px; background: #f0f0f0; border: 3px solid #00ece5;">
  <strong>Note:</strong> If you are cloning using SSH, you must have already added the Codio SSH public key as described in <a href="https://docs.codio.com/common/settings/upload-ssh-key-remote-server.html#upload-ssh-key-remote-server">Upload SSH Key to Remote Server</a>.
  </div>

Create New GitHub Repo From Codio
---------------------------------
If you have code in Codio and want to create a new GitHub (or other remote) repo, follow these steps:

.. image:: /img/github-new-repo.png
   :alt: github repo
   :align: right
   :width: 400px

1. Create a new project in Codio or open up an existing project.
2. Open the terminal (**Tools > Terminal**), type **git init** and press **Enter** to initialize Git.
3. Create a new, empty repo on GitHub or other remote repo.
4. Copy the repo url to the clipboard. 

.. raw:: html

   <div style="float: right; width: 350px; margin: 0 0 10px 20px; padding: 10px; background: #f0f0f0; border: 3px solid #00ece5;">
   <strong>Note:</strong> If you're using GitHub, use the <strong>SSH url</strong> rather than <strong>https</strong>. Also make sure that your Codio public key is uploaded to your GitHub account or repo settings as described in <a href="https://docs.codio.com/common/settings/upload-ssh-key-remote-server.html#upload-ssh-key-remote-server">Upload SSH Key to Remote Server</a>.
   </div>

5. In the Codio IDE, click **Tools > Git > Remotes** on the menu.
6. Click the **Edit** icon and enter the **Name** and paste the **URL** into the field. It is recommended you use **origin** as the name to confirm the normal standards. You do not need to specify a username or password if you are using SSH.
7. Click **Save**.


Github Commands
-----------------

GitHub functions normally within Codio, giving you access to all the standard Git commands and GitHub features you're familiar with.

.. raw:: html

   <div style="margin: 0 0 10px 20px; padding: 10px; background: #f0f0f0; border: 3px solid #00ece5;">
   <strong>Note:</strong> The Guides folder is automatically included in your project, unless you manually remove it</a>.
   </div>
