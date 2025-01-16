.. meta::
   :description: Restarting a box is a reboot, resetting a box returns it to a fresh state. 

.. _Restart and Reset:

Restart or Reset Box
====================

You can restart or reset your project's box from the **Project** menu.

Restart
-------
To restart the box, click the **Project** tab and choose **Restart Box**. You can also restart by clicking the restart box icon in the file tree. The reboot normally takes a few seconds.

  .. image:: /img/restart.png
     :alt: Restart


Reset
-----
Resetting a box is fairly destructive and should be used with caution. When performing a box reset, the box is returned to a fresh state but your code files are untouched. It also results in the following:

- Any new folders or files that have been created will be deleted.
- All parts of the box outside the **~/workspace** folder will be reset.
- All code files in the **~/workspace** folder are untouched.
- Box restart.

After a Reset, you must reinstall components (npm modules, ruby gems, etc.) and other modifications you may have made.

