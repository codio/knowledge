.. meta::
   :description: Each Codio project or assignment IDE gets it's own dedicated Ubuntu Server (box) with sudo access. This is an overview of the Codio IDE box. 

.. _overview: 

IDE Box Overview
================

.. toctree::
   :caption: Boxes
   :hidden:
   
   terminal
   ext-access
   restart-reset
   runmenu
   startup

Each Codio project gets its own dedicated Ubuntu Server (box) with sudo access. Review the information in these topics to learn how to access your box, administer it, and install software dependencies.

To view details about your project box, click the **Project** tab on the menu bar and choose **Box Info** from the drop-down menu.

.. image:: /img/box_info.png
   :alt: Box Info
   
Important 'localhost' configuration information
-----------------------------------------------
In many config files on your Box you would include a reference to `127.0.0.1` to access localhost. Please be sure to use `0.0.0.0` instead.

