.. meta::
   :description: Exluding files when assignments published

.. _exclude:

Excluding Files/Folders
========================

To Students
***********

Files/folders may need to be excluded from students assignments. Such files may be unused resources/logs and other files used when testing the assignment prior to publishing.

This can be handled by using **.unitignore** file in the source project and when published to a course, these files/folders will not be available to the students.

Enter on a new line the file/folders to be excluded defining them relative to the location of the **.unitignore** file and defining folders with /

For example if the **.unitignore** file is located in the project workspace and you wish to exclude

- testing & node_modules folder
- the file checkscore.js in the views folder
- the files app.js and README.md

the **.unitignore** file will be

.. code:: json

   /testing
   /node_modules
   /views/checkscore.js
   app.js
   README.md

To collaborating teachers
*************************

When collaborating with other teachers in Codio, an **.authorunitignore** file can be used in the same way as the **.unitignore** file above.  As collaborating teacher in the course accesses the published assignment in edit mode, the files/folders included in the file will not be available to them.

If using Desktop App
--------------------

See :ref:`Desktop App <desktop-app>` where **.codioignore** file is used in the same manner. 