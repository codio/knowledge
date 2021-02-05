.. _overview: 

Overview
========

Waking a Box
------------
When you create a Codio Project, it is automatically assigned an Ubuntu server. You can think of this server as being asleep until you open up your Project in the IDE. As soon as the Project loads in the IDE, the Box is up and running.

When is the Server put back to sleep?
-------------------------------------
Your server is put to sleep within a few minutes of you exiting your Project or after 60mins of inactivity.

Can I have my Box 'Always on'?
------------------------------
Paid subscribers can use the :ref:`Always on Boxes <Always on Boxes>` feature. This allows you to mark Projects that you don't want to be put to sleep when you exit your Project.

Can I SSH into my Box?
----------------------
Yes, see :ref: `SSH into your box <SSH into your box>` documentation.

Can I reboot my Box?
--------------------
Yes. Please refer to the :ref:`Restart and Reset <Restart and Reset>` documentation.

Can I let other people administer my Box?
-----------------------------------------
Paid subscribers can use the Admin property of the [Permissions](/docs/ide/customization/permissions) feature to allow other Codio users to access their Project and have full access to your Codio Box as well as the code.

Do I have sudo access?
----------------------    
Yes, our Boxes provide sudo access.

How do I install software dependencies?
---------------------------------------
You have sudo access, so should use the full power of the `apt <https://help.ubuntu.com/community/AptGet/Howto>`_ package management system, and the packages it provides via the Ubuntu community.

How do I access my Box from code?
---------------------------------
We have :ref:`full documentation <external access>` on how to access your Box from code.

Firewall issues
---------------
Codio Boxes do not run on port 80. Some companies block outbound access to ports other than port 80. Please read :ref:`this section <external access>` on how to work around this.

Important `localhost` configuration information
-----------------------------------------------
In many config files on your Box you would include a reference to `127.0.0.1` to access localhost. Please be sure to use `0.0.0.0` instead.
