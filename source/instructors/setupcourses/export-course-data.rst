.. meta::
   :description: All your course data, including student workspaces, can be downloaded to a zip file. User access data can be exported to a .csv file. Guide content may be exported to a .pdf file.


Data Exports
============

.. _export-course:

Export Coursework Data
----------------------
You can export course data (including students workspaces) prior to :ref:`deleting a course <delete-course>`, if you want to retain the data. Follow these steps to delete the course data:

1. Navigate to the **Courses** page and select the course to open it.
2. Click the **Export** tab and then click **Coursework Data** in the **Data Exports** section.

   .. image:: /img/class_export.png
      :alt: Export Course Data

   All the data from the course is compiled in a **.zip** file. An email is then sent to you that includes a link to download the course data. The link remains active for 7 days and then the file is removed.

3. To access the download file within the 7-day period it remains active or to export additional files, click **Course Data** and click **Export** to download the file.

   .. image:: /img/class_exportlinks.png
      :alt: Course Export Links
      
.. Note:: You can also export individual assignment data if you do not need or require data for all the assignments in your course. See :ref:`Export assignment data <export-assignment>`

.. Note:: Students inactive for more than 90 days will not have their course data available for export. See :ref:`Remove inactive students <remove-inactive-students>`

.. _export-studentcourse-data:

Export Student Data for the Course
----------------------------------

You can export course data for individual students (including their workspaces) rather than having to export the whole course data. Follow these steps to delete the course data:

1. Navigate to the **Courses** page and select the course to open it.
2. Click the **Students** tab and select the student
3. Right click the 3 blue dot menu and select **Export Student Data**.

   .. image:: /img/studentdata_export.png
      :alt: Export Student Data

   All the data from the course is compiled in a **.zip** file. An email is then sent to you that includes a link to download the students data. The link remains active for 7 days and then the file is removed.


.. Note:: Students inactive for more than 90 days will not have their course data available for export. See :ref:`Remove inactive students <remove-inactive-students>`

.. _export-assessment-data:

Export Assessment Data
----------------------

To export data related to students assessment in individual or multiple assignments in the course, follow these steps:

1. Navigate to the **Courses** page and select the course to open it.
2. Click the **Export** tab and then click **Assessment Data** in the **Data Exports** section.

When selected, a dialog shows allowing you to select the assignments to obtain the data. 

   The following data is exported to a **.csv** file for download (or into a **.zip** file containing individual csv files if multiple assignments selected):

   - Student_Name
   - First_Name
   - Last_Name
   - Username
   - Hashed_ID
   - Email Address
   - Assignment_Name
   - Total_Points_Earned
   - Total_Points_Possible
   - Time_Spent
   
and for each assessment:

   - <Assessment_Name>_Attempts
   - <Assessment_Name>_Answer
   - <Assessment_Name>_Earned_Points
   - <Assessment_Name>_Total_Points_Possible

.. Note:: The data is retained for a maximum of 6 months.


Export Course Access Data
-------------------------
To export data related to users accessing assignments in the course, follow these steps:

1. Navigate to the **Courses** page and select the course to open it. 
2. Click the **Export** tab and then click **Course Access Data** in the **Data Exports** section..

   The following data is exported to a **.csv** file for download:

   - Username
   - Users registered email address
   - First name
   - Last name
   - Date/time when user logged in
   - Access type (Log In, Log Out, Project Open, Project Close)
   - Assignment name (Book based assignments will report the name of the book)
   - Role in course (Teacher/Student)
   - Project path
   - IP address (IP address associated with login session)

.. Note:: The data is retained for a maximum of 6 months.

.. _export-course-coach-logs:

Export Course Coach Logs
------------------------
To export data related to users accessing assignments and feedback provided in a course, follow these steps:

1. Navigate to the **Courses** page and select the course to open it.
2. Click the **Export** tab and then click **Course Coach Logs** in the **Data Exports** section. 


The following data is exported to a **.csv** file for download:

   - Assignment_name (Book based assignments will report the name of the book)
   - Assessment_id
   - User_email
   - User_id
   - Time
   - Question
   - Context_guides
   - Context_error
   - Context_files
   - Response

Exporting and analyzing :ref:`course coach<virtual-coach>` log data helps the instructors to enhance the quality of the feedback and improve their learning experience.

Course Content Exports
======================

.. _export-pdf:

Export PDF
----------

1. Navigate to the **Courses** page and select the course to open it. 
2. Click the **Export** tab and then click **PDF** in the **Course Content Exports** section..

Use this to obtain PDF versions of the guides content in your assignments. When selected, a dialog shows allowing you to select the assignments to obtain the PDF version.

- You can select a single PDF that compiles all selected assignments into one file, or receive a separate PDF for each selected assignment.

- You can also include :ref:`teacher only notes <teacher-only>` in the PDF export

- The link will be active for 7 days and after this time the file will be removed.

.. _export-source:

Export Course Sources
---------------------
Export course sources to obtain a zip file containing all the currently published assignments. 

1. Navigate to the **Courses** page and select the course to open it. 
2. Click the **Export** tab and then click **Course Sources** in the **Course Content Exports** section..


   The currently published versions of each assignment are compiled into a **.zip** file and each assignment is compiled into a **.tar.zst** file and can be downloaded. If you update the assignment in the future, you can create a new export.

3. To access the download or to export updated assignments, click **Course Sources** and click **Export** to create a new export or click the link to download the zip file.

   .. image:: /img/source_exportlinks.png
      :alt: Course Export Links

.. _course-blueprint-transfer:

Course Blueprint Transfer
-------------------------

You can export course Blueprints to a file to transfer them to a different course.

   1. 1. Navigate to the **Courses** page and open the course from which you want to export **Blueprints**.
   2. Click the **Export** tab and then scroll down to **Course Blueprint Transfer**.
   3. Click the **Export** button.
   4. In the pop-up dialog, click **Export** again to download a JSON file containing the course Blueprints.
   

.. image:: /img/export_blueprints.png
      :alt: Export Blueprints window

With the exported file, you can share Blueprints with other instructors or import them into a different course.

   1. Navigate to the **Courses** page and open the course into which you want to import **Blueprints**.
   2. Click the **Export** tab and then scroll down to **Course Blueprint Transfer**.
   3. Click the **Import** button.
   4. In the pop-up dialog, you can import Blueprints from a file or a GitHub repository.

- For a file, select File as the source and then click the **Insert a File** field. This opens a dialog to select a file on your computer.

- For Git, select Git as the source. 

   - In the Git repository, use the `HTTPS` URL of the repo. `SSH` is not allowed. The repository must be publicly accessible.
   - For the **Path to blueprints**, use the full file path (including name and extension). For example:


.. image:: /img/export_import_blueprints.png
      :alt: Import Blueprints window from GitHub

.. Note:: Existing Blueprints aren't overwritten; imported Blueprints will be added to the existing ones.
