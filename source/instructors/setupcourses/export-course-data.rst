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

**Note:** The data is retained for a maximum of 6 months.

**See Also:**

- :ref:`Export LTI Settings <export-lti>` to export unit LTI integration URLs.
- :ref:`Import Project <import-project>` to import the zipped exported folder to review student workspaces. The exported workspace does not include the stack so you should select the appropriate stack when importing the project or switch the stack in **Project > Stack > Settings**.