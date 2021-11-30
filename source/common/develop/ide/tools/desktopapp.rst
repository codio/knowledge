.. meta::
   :description: An overview of the Codio desktop app

.. _desktop-app:

Desktop App
===========

.. raw:: html

   <iframe src="https://player.vimeo.com/video/273506364" width="640" height="436" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

The desktop app is to allow a local code workspace to synchronize with a Codio box.

Assignments/Projects from the :ref:`Courses dashboard <navigate-student-dashboard>` My Projects area can be connected.

A Codio account is required

Excluding files
---------------

Files/folders can be excluded from synchronisation by using `.codioignore`` file in the source project. Enter on a new line the file/folders to be excluded defining them relative to the location of he ``.codioignore`` file and defining folders with ``/``

For example if the ``.codioignore`` file is located in the project workspace and you wish to exclude

-  ``bin`` & ``node_modules`` folder
-  the file ``error.jade`` in the ``views`` folder
-  the files ``app.js`` and ``README.md``

the ``.codioignore`` file will be

::

    /bin
    /node_modules
    /views/error.jade
    app.js
    README.md

.. figure:: /img/codioignore.png
   :alt: codioignore


Please note that the ``.codioignore`` file is included in the desktop app files.

If students wish to exclude files when pushing back to their Codio account they can do so, either by editing any existing ``.codioignore``file or creating the file themselves. If the teacher creates the ``.codioignore`` file, adding a 'comment' line to the top of the file to make it clear to any students what they should not change could help avoid potential problems. A line starting with ``#`` serves as a comment

`Click here <https://www.codio.com/download>`_ to go to the download page and install to your local machine

Starting the app
----------------

When first starting the app you need to choose the server to connect to. In most cases this will be **https://codio.com** but if you are in the United Kingdom/Europe, it maybe **https://codio.co.uk**.

.. figure:: /img/desktop_server.png
   :alt: desktop server


You can check by logging into your Codio account in your browser and you will see the server domain noted there

Having selected the server log in using your codio credentials.

.. Note:: that if you usually access Codio through an :ref:`LMS <integrate-lms>`, you may not have a Codio account password set. If that is the case, go to the online login screen where you can go through the:ref:`lost password <password>` process to define a codio account password. We would then recommend you log into your account online and change this password to one you will remember in the future. Setting a Codio account password will not effect or change how you currently access Codio via your LMS

Accessing and connecting to your online content
-----------------------------------------------

.. figure:: /img/desktop_options.png
   :alt: desktop options


When logged in you first see a list of all courses you are a member of and can access your content either from **Courses** or **My Projects** area.

To pull the code, click on your course or My Projects

.. figure:: /img/desktop_connect.png
   :alt: desktop connect


and then select either:

-  **connect** - to pull all the code from the selected assignment to a folder on your PC that you define.

|desktop workspace|.

-  **Open in Codio** - to open the assignment in your Codio account

When connecting, browse to a folder on your PC where you would like to store the code and pull the content

Managing your offline content
-----------------------------

When you have connected you can then push/pull/open the assignment in Codio and manage the local workspace folder settings.

.. figure:: /img/desktop_connected.png
   :alt: desktop connected

  
**1.** Click the **pull** button to pull content in from your Codio account. **Note** Any files you already have stored locally will be overwritten

**2.** Click the **push** button to push the content from your local workspace folder back to your Codio account. **Note** This will overwrite the project/assignment in your Codio account

**3.** Click the **Open in Codio** button to open your assignment in a browser tab. This can be useful if you wish to compare what you have stored locally to what you last pulled from your Codio account

**4.** Click the **folder** icon to manage your local workspace folder settings

Local workspace folder settings
-------------------------------

.. figure:: /img/desktop_worspacesettings.png
   :alt: desktop workspace settings


**1.** Click the **Open the folder** button to open the folder containing your local files

**2.** Click the **Change folder** button to change the folder storing your local files. **Note** the content of the previous folder will not be automatically copied or transferred to the newly selected folder. If you wish to do this, you should return to the previous screen and **pull** to that new folder

**3.** Click the **Disconnect** button to disconnect the assignment from your Codio account. You will be returned to the previous screen where you can then
connect the assignment again if you wish

.. |desktop workspace| image:: /img/desktop_workspace.png
