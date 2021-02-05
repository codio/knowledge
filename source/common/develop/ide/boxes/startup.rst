Auto starting services
======================
Your Box will be put to sleep under the conditions :ref:`explained here <overview>`. When you open your project, the Box will start and services will start. Software installed using `Tools->Install Software` will be automatically configured to autostart.
If you have need to autostart other services, you can do so within a `startup.sh` bash script located in your project, and also installing `Autostart Support` from `Tools->Install Software`.
For the script to be included in the stack we'd recommend `/home/codio/startup.sh`.
If your project is using guides, you can use `.guides/startup.sh` or you can locate this file in the workspace although bear in mind that students may be able to access/edit files visible to them in the workspace. 

Upstart/Systemd
---------------
Upstart can be used in Ubuntu 14.04 boxes. If you want to configure services to start when your box starts up, you should configure a `.conf` file. If you are not familiar with upstart, please Google it for configuration details.


Systemd can be used in Ubuntu 18.04 boxes. If you want to configure services to start when your box starts up, you should configure a `.service` file and run `sudo systemctl daemon-reload`. If you are not familiar with systemd, please Google it for configuration details.

**Important** - you need to specify the user account under which the service is run using `setuid codio`.
