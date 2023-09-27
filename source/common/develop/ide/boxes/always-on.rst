.. meta::
   :description: Always-on boxes all your projects to always be accessible.

.. _always on boxes:

Always-On Boxes
===============

The Always-On feature for boxes is now available for all paid subscribers. This feature enables you to set boxes to always be on, which means they remain active whether you are in the IDE or logged out. The number of Always-On boxes you can have depends on your payment plan.

If your project is archived due to inactivity (usually 30 days since last opened), this process removes it from the active fileserver and can no longer be *Always-On*. 

You can set a box to Always-On from the **Project > Settings** menu in the IDE or from the Project dashboard.

Enable Always-On
----------------

From IDE
^^^^^^^^
To set a box to Always-On from the IDE:

1. Click the **Project** tab on the menu and choose **Settings**.
2. On the **General Settings** tab, toggle the **Always-On Box** setting to **On**.
3. Click **Save Changes**.

From Project dashboard
^^^^^^^^^^^^^^^^^^^^^^
To set a box to Always-On from Project dashboard:

1. Click **My Projects** in the left navigation pane.
2. Click the **Settings** icon (gear) for the project you want to enable Always-On.
3. Under **Preferences**, toggle the **Always-On Box** setting to **On**.
4. Click **Save Changes**.


Keep terminal processes running
-------------------------------
When you exit your project in the IDE and return to the dashboard, any processes that were started from within a terminal window will terminate. You can prevent processes from terminating using one of the following methods:

- Append terminal command - Append `&` to the terminal command that starts your process. You will see output as usual but may need to press the **Enter** key to get a fresh command prompt. Before closing the terminal window or exiting your project, enter the following command:
  
  .. code:: bash

     disown -a
  

- Install tmux
