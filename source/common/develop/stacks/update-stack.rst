.. _update-stack:

Updating a Stack
================

After :ref:`creating a new stack <create-stack>`, you may want to update the stack properties or take another stack snapshot from a Codio project. You can update your stack from the **Stacks** area on the Codio dashboard or from the IDE.

Updating stack from the dashboard
---------------------------------
To update the stack from the Codio dashboard, follow these steps:

1. In the navigation pane, click **Stacks** and then select the stack from the list.
  
   .. image:: /img/stackdetails.png
      :alt: Stacks Dashboard 

2. Click **Edit** to update the **Stack Name** or **Description**.

3. Click **New Version** to create a new version of the stack and then choose the project from which the stack should be generated from the **Source** drop-down list. 

4. Add a comment describing what has changed since the last version.  A new version is generated (this can take a few minutes).

Updating stack from the IDE
---------------------------

You may find it easier to update a stack from within the IDE and the project that you are currently working on. After you have finished making changes to your box (installing new components etc.), follow these steps to create a new stack version:

1. Click the **Projects** tab on the menu bar and choose **Stack > Create New**.

   .. image:: /img/stacknewversion.png
      :alt: Stacks New Version

2. Click **New Version** and enter a description of the changes since the last stack version.  A new version is generated (this can take a few minutes).

   If your stack is pointing to the latest version, you've completed the procedure. However, if the stack is pointing to a specific stack version, you must change it to point to the latest version or the version you just built.

3. Click **Project** on the menu bar and choose **Stack > Settings** to point to a different stack.

Viewing stack version history
-----------------------------
You can view the version history of a stack from the **Stacks** page on the Codio dashbaord. Select the stack from the listing and then click the **Versions** link at the top of the page.

.. image:: /img/stacks_versions.png
   :alt: Stack Version History

