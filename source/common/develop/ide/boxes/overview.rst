.. _overview: 

IDE Box Overview
================

Each Codio project gets its own dedicated Ubuntu Server (box) with sudo access. Review the information in these topics to learn how to access your box, administer it, and install software dependencies.

To view details about your project box, click the **Project** tab on the menu bar and choose **Box Info** from the drop-down menu.

.. image:: /img/box_info.png
   :alt: Box Info

Use the following information to get started understanding Codio IDE boxes:

- **Waking and putting box to sleep** - When you create a Codio Project, it is automatically assigned an Ubuntu server. Once you open the project in the IDE, the box is up and running (awake). The server is put to sleep within a few minutes of exiting the project or after 60 minutes inactivity.

  You can use the :ref:`always on boxes` feature if you are a paid subscriber. This feature allows you to mark those projects that should not be put to sleep when you exit.

- **SSH into box** - You can SSH into your Codio box if the project is open and the box is ready to receive incoming SSH connections. If you have :ref:`always on boxes` enabled on the box, it is always ready to receive SSH connections. See :ref:`SSH and Code Access <ssh>` for more information. 

- **Rebooting a box** - You can restart or reset a box from the Project menu. See :ref:`Restart and Reset a Box <Restart and Reset>` for more information.

- **Allowing others to administer your box** - Use the Project Permissions to grant other users Admin permission which grants them full access to your box and the code. See :ref:`Project Permissions <project-permissions>` for more information.

- **Installing software dependencies** - You have sudo access, so should use the full power of the `apt <https://help.ubuntu.com/community/AptGet/Howto>`_ package management system, and the packages it provides via the Ubuntu community.

- **Accessing box from code** - See :ref:`External Access to Boxes and Ports <external access>` to learn how to access your box from code.

- **Firewall issues** - Codio boxes do not run on port 80 and some companies block outbound access to ports other than port 80. See  :ref:`External Access to Boxes and Ports <external access>` for information about how to work around using port 80.

- **Important `localhost` configuration information** - When referencing accessing localhost in your configuration files, you must use '0.0.0.0' instead of the typical `127.0.0.1`.