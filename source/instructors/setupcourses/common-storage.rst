.. meta::
   :description: Instructors can create a shared storage to upload files available in all assignments.


.. _common-storage:

============================
Common Storage for a Courses
============================

Course Shared Storage lets instructors place common files (docs, data sets, starter code, assets) in one location that's available inside every assignment workspace. There are read-only files securily shared and available for all students.

Key Benefits
------------
- Single source of truth for course assets
- No per-assignment re-uploads or duplication
- Consistent path for code and terminal access

|

====================
Using Common Storage
====================

Enable Course Shared Storage
----------------------------

1. Open the course and go to ``Admin → Course Details``.
2. Scroll to **Course Shared Storage** and toggle **Shared storage**: **On**.
3. Click **Save Changes**.

.. image:: /img/enable-shared-storage.png
   :alt: Toggle to enable Course Shared Storage in Admin → Course Details
   :width: 80%
   :align: center

.. note:: Once enabled, you will see the **Storage** tab in the **Admin** area of the course.

Add Folders & Files
-------------------

1. Navigate to ``Admin → Storage``.
2. Use **Create Directory** to make a top-level folder (e.g., ``Assignment-1`` or ``Datasets``).
3. Select a folder, then use **Upload File** to add one or more files.
4. Repeat for additional assignments or resources as needed.

.. image:: /img/storage-browser.png
   :alt: Storage browser showing an dataset folder with uploaded files
   :width: 80%
   :align: center

.. topic:: You can upload many files, but no single file can be more than 5GB. 

Access Storage From Assignments
-------------------------------

Inside any assignment workspace, the shared storage appears under the ``storage/`` directory. Students and teachers can read files from there with the terminal, editors, or program code.

.. image:: /img/storage-assignment.png
   :alt: Storage section inside one assignment.
   :width: 80%
   :align: center
