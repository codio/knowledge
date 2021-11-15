.. meta::
   :description: All your course data, including student workspaces, can be downloaded to a zip file. User access data can be exported to a .csv file. Guide content may be exported to a .pdf file.


.. _export-course:

Export Course Data
==================
You can export course data (including students workspaces) prior to :ref:`deleting a course <delete-course>`, if you want to retain the data. Follow these steps to delete the course data:

1. Navigate to the **Courses** page and select the course to open it.
2. Click the **Admin** tab and then click **Course Data** in the **Export** section.

   .. image:: /img/class_export.png
      :alt: Export Course Data

   All the data from the course is compiled in a **.zip** file. An email is then sent to you that includes a link to download the course data. The link remains active for 7 days and then the file is removed.

3. To access the download file within the 7-day period it remains active or to export additional files, click **Course Data** and click **Export** to download the file.

   .. image:: /img/class_exportlinks.png
      :alt: Course Export Links
      
.. Note:: You can also export individual assignment data if you do not need or require data for all the assignments in your course. See :ref:`Export assignment data <export-assignment>`


.. _export-source:

Export Course Sources
---------------------
You can export course sources to obtain a zip file containing all the currently published assignments. 

1. Navigate to the **Courses** page and select the course to open it.
2. Click the **Admin** tab and then click **Course Sources** in the **Export** section.

   .. image:: /img/source_export.png
      :alt: Export Course Data

   The currently published versions of each assignment are compiled into a **.zip** file and each assignment is compiled into a **.tar.zst** file and can be downloaded. If you update the assignment in the future, you can create a new export.

3. To access the download or to export updated assignments, click **Course Sources** and click **Export** to create a new export or click the link to download the zip file.

   .. image:: /img/source_exportlinks.png
      :alt: Course Export Links
      
.. Note:: This feature is not available if your course is a child course of a licensed master course.

Export user access data
-----------------------
To export data related to users accessing assignments in the course, follow these steps:

1. Navigate to the **Courses** page and select the course to open it.
2. Click the **Admin** tab and then click **User Access Data** in the **Export** section. 

   .. image: /img/user_access_export.png
      :alt: Export User Access Data

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

.. _export-pdf:

PDF
---

   .. image:: /img/pdf_export.png
      :alt: PDF Export
      
Use this to obtain PDF versions of the guides content in your assignments. When selected, a dialog shows allowing you to select the assignments to obtain the PDF version

- You can select a single PDF where all selected assignments are compiled into one PDF file or to receive a PDF for each selected assignment

- The link will be active for 7 days and after this time the file will be removed.

.. _export-assessment-data:

Assessment Data
---------------

To export data related to students assessment in individual or multiple assignments in the course, follow these steps:

1. Navigate to the **Courses** page and select the course to open it.
2. Click the **Admin** tab and then click **Assessment Data** in the **Export** section. 

   .. image:: /img/assessment-data-export.png
      :alt: Assessment Data Export

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

.. _common-cartridge:

Common Cartridge
----------------

Allows you to export the `Common Cartridge 1.3 <http://www.imsglobal.org/cc/ccv1p3/imscc_Overview-v1p3.html>`_ data for the course to then use within your LMS system to import details of the assignments in your Codio courses.

   .. image:: /img/common-cartridge.png
      :alt: Common Cartridge Export

.. Important:: If working with Canvas, each assignment within your LMS still needs to be configured. Refer to the :ref:`system specific instructions <system-specific-directions>` for your LMS system

**See Also:**
- :ref:`Export Assignment Data <export-assignment>` to export individual assignment workspaces.
- :ref:`Export LTI Settings <export-lti>` to export unit LTI integration URLs.
- :ref:`Import Project <create-import-project>` to import the zipped exported folder to review student workspaces. The exported workspace does not include the stack so you should select the appropriate stack when importing the project or switch the stack in **Project > Stack > Settings**.