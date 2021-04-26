.. meta::
   :description: Connecting a Codio project/assignment to a GitHub repo.

.. _connect-codio-github:

Connecting a Codio Box to a GitHub Repo
=======================================
The first step to using GitHub in Codio is connecting your Codio and GitHub accounts. You only have to do this once. Follow these steps:

1. Click your user name in the bottom left of the main menu. 

2. Click the **Applications** tab.

   .. image:: /img/GitHub1.png
      :alt: 

3. In the GitHub section, click **Connect account** and log in to your Github account when prompted.

   .. image:: /img/Github2.png
      :alt: GitHub Connect Account

4. If you are using SSH connections, click **Upload public key** so Codio and Github can exchange keys. 

In GitHub: Make a new repo
--------------------------
Each Codio box (Assignment, Book, or Project) can be mapped to a GitHub repo. This connection only needs to be established once per box.

.. Note:: If you have an existing repo you want to clone, you can import a project from a GitHub repo (https://docs.codio.com/project/projects/#creating-and-importing-a-project) and this connection is made during the importing process. If you are familiar with Git, skip the rest of this guide and just use the terminal as usual by going to **Tools > Terminal**. 

To create a new repo, follow these steps:

1. Go to your GitHub organization (or profile) and click the green **New** repository button.

   .. image:: /img/NewRepo.png
      :alt: New Repo Button

2. Complete the requested details. We suggest **not** initializing a README since one already exists in Codio and will result in an immediate conflict.

   .. image:: /img/RepoConfig.png
      :alt: Create New Repo

3. Copy either the **HTTP** or **SSH** URL on the created repo page (if you do not want to type credentials and you uploaded your public key, use SSH).

   .. image:: /img/RepoURL.png
      :alt: Repo URL

In Codio: Connect to repo
-------------------------
.. Note:: You can skip the rest of this guide and do your normal Git workflow via command line if you prefer. Open a terminal from **Tools > Terminal** on the menu.

To connect to your repo from Codio, follow these steps:

1. On the Codio Box you want to connect, click the **Tools > Git > Remotes** menu.

   .. image:: /img/RemoteMenu.png
      :alt: Remotes Menu

2. When prompted, click **Yes** to initialize a local git repository.
 
   .. image:: /img/gitInit.png
      :alt: Initialize

3. When prompted, click **Add Remote**.

   .. image:: /img/RemoteConfig.png
      :alt: Add Remote

4. Enter the name (origin is the git standard) and paste the URL that you copied into the URL field.

5. Click **Save** and then **Close**.

   .. image:: /img/RemoteConfig2.png

6. Click **Tools > Terminal** on the menu to open a terminal window.
 
   .. image:: /img/terminal.png
      :alt: Terminal

7. Type `git add .` and press **Enter/Return**.
8. Type `git commit -m "initial commit"` and press **Enter/Return**.
9. Type `git push --set-upstream origin master` and press **Enter/Return**.

Collaboration in Codio with GitHub
----------------------------------
If you share Codio boxes with other members of your GitHub repository (directly through **Project > Permissions** or a copy through **Project > Fork**), the connection to GitHub is maintained. However, other members must also link their GitHub and Codio accounts.

Saving your work with Git (Committing and Pushing)
--------------------------------------------------
Git allows you to save multiple versions of your work using a few commands in the terminal (**Tools > Terminal**).

.. image:: /img/terminal.png

Follow these steps to save your work:

1. In the terminal window, type `git add .` and press **Enter/Return**. This command tells git to go collect all the changes you have made since your last save (which is called a commit in Git).

2. Type `git commit -m "commit message"` and press **Enter/Return**. This command bundles all your changes and gives them a useful human-readable name so make sure you provide something useful for the **Commit Message**.

3. Type `git push` and press **Enter/Return**. This command sends this bundle of changes to GitHub so you have a copy in the cloud.

Going back to immediately previous save point (Reverting to previous commit)
----------------------------------------------------------------------------
To get rid of all changes since your last save or commit, follow these steps: 
Warning: Be careful, you cannot undo this!

1. First, check what your last commit or save was to make sure you know where you are going back to. You can either look on GitHub or type `git log`. If you have a lot of commits, you will need to type **Ctrl+c** to exit git log.

2. Type `git add . && git reset --hard HEAD`.

Manually importing a Git repo into Codio
----------------------------------------
To manually import a Git repo into Codio, follow these steps:

1. In GitHub, click the **Clone URL** link in the right pane and copy to the clipboard.

   .. figure:: /img/github-clone-url.png
      :alt: create from GitHub

  If you are cloning using SSH, you must have already added the Codio SSH public key as described in :ref:`Upload SSH Key to Remote Server <upload-ssh-key-remote-server>`.

2. Log in to Codio and click **New Project**.

3. Click the **Click here** link for more options.

   .. image:: /img/github-create.png
      :alt: create from GitHub

4. In the **Select your Starting Point** area, click **Import**.

5. From the **Source** drop-down list, choose **Git**.

6. Paste the Git URL into the **URL** field and add details about the project.

7. Click **Create**. Codio loads the repo and displays it.

A few Git helpers
-----------------
We have added a few Git helpers to the **Tools > Git** menu.

.. image:: /img/git-overview.png
   :alt: Git Overview

More Information
----------------
Refer to the documentation on GitHub.com and and http://git-scm.com/docs for complete information about using Git and GitHub.