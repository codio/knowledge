.. meta::
   :description: Installing software packages

.. _box_parts:

Install Software Packages
=========================

You can view all software that is installed on your box and install new software from the **Tools > Install Software** menu. From the **Install software** page, you can run scripts that install, configure, or reconfigure software components instead of manually installing it from the command line. 

.. image:: /img/install-sw-g2.png
   :alt: Install Software

Locate the software that you want to install and click the **Install** icon to start the installation.

Install software from the command line
--------------------------------------
Our boxes provide full `sudo` (root) access, so you can also use the Ubuntu `apt <https://help.ubuntu.com/community/AptGet/Howto>`_ package manager, which provides thousands of software packages that are maintained by the Ubuntu community.

If you want to provide fully pre-configured boxes, use :ref:`Stacks <stacks>` instead the **Install Software** option.


Add or request new software packages
------------------------------------
You can request new software packages or add a new package yourself. If you require a new script to be added to the **Install Software** list, use one of the following methods:

- Visit the `Issues <https://github.com/codio/install_software/issues>`_ page on our GitHub repository and create a new issue detailing your requirements.

- Fork our `GitHub repository <https://github.com/codio/install_software>`_, add the script yourself, and then submit a pull request.

For instructions on how to add your own software package scripts, see :ref:`Add Your Own Packages <parts-coding>`.

Autostart
---------
Services that require a restart, are automatically started on installation. You can manually start, stop, and restart services using the following terminal commands:

``$ sudo service <package-name> start``

``$ sudo service <package-name> stop``

``$ sudo service <package-name> restart``
