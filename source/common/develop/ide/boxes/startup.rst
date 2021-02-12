.. _startup:

Autostart Services
==================
Your box is put to sleep under the conditions explained in :ref:`IDE Box Overview <overview>`. When you open your project, the box and services are started, and installed software (using **Tools > Install Software**) is automatically configured to autostart. 

You can also configure other services to autostart in the **startup.sh** bash script in your project or by installing **Autostart Support** from **Tools > Install Software**.

For the script to be included in the stack we recommend `/home/codio/startup.sh`.

If the project is using guides, you can use `.guides/startup.sh` or you can put the file in the workspace; students may be able to access and edit files visible to them in the workspace. 

Upstart
-------
Upstart can be used in Ubuntu 14.04 boxes. If you want to configure services to start when your box starts up, you should configure a **.conf** file. If you are not familiar with upstart, please Google it for configuration details.

Systemd
-------
Systemd can be used in Ubuntu 18.04 boxes. If you want to configure services to start when your box starts up, you should configure a **.service** file and run ``sudo systemctl daemon-reload``. If you are not familiar with systemd, please Google it for configuration details.

**Important** - You must specify the user account under which the service is run using ``setuid codio``.
