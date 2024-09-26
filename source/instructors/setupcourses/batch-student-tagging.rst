.. meta::
   :description: Batch Student Tagging using a CSV


.. _batch-student-tagging:

Batch Student Tagging
=====================

You can easily assign tags to all or multiple students at once using a CSV file. Once the tags are assigned, you can quickly search and filter students based on those tags in the search bar. This is a useful feature when you want to :ref:`view the work <viewing-student-work>` of specific students.

To search for a specific tag, use '#' followed by the tag name. For instance, if you have assigned the tag 'groupA' to a group of students, you can locate them by typing '#groupA' into the search bar.

You can download the csv template file from **Download Student Tags** setting present in the **Bulk Settings** area. You can update the fields as per your requirement and use that csv file to bulk upload student tags.

To bulk upload the student tags, follow these steps:

1. On the **Courses** page, click the course whose students you want to add tags for

2. Go to **Bulk Settings** area and press **Open Updater** button from Bulk Upload Tags

3. Select the CSV file in which you have defined student tags and press **Update student tags** button

   .. image:: /img/batch-tags-upload.png
      :alt: Select csv to batch upload the student tags


The CSV contains four columns: tag, user_email, codio_user_id, lti_id. Either user_email or codio_user_id is required. 

To assign multiple tags to a single student, add a new line for each tag while keeping the student’s details the same.

If you want to reset all student tags, click **Reset tags** button present at bottom right corner of Student Tags Settings.