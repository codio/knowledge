.. meta::
   :description: Batch Assignment Settings Update


.. _batch-assignment-update:

Batch Assignment Update
=======================

You can do the batch update of some assignments settings like Start date/time of the assignment, Closing date/time of the assignment, Action when assignment closes (for more information about these settings, see :ref:`Assignment Duration <assignment-duration>`) and :ref:`Prime Assignment Containers <prime-assignment-containers>` settings using a CSV file.

To batch update the assignments settings, follow these steps:

1. On the **Courses** page, click the course that contains the assignment you want to edit

2. Go to **Bulk Settings** area and press **Open Updater** button from Update Assignment Setting

3. Select the CSV file in which you have defined all the required settings and press **Detect CSV format** button

   .. image:: /img/select-csv-batch-update.png
      :alt: Select csv Batch Update


   Below is an example of a csv file:

   .. csv-table:: 
      :file: /instructors/setupcourses/Batch-Update-Settings.csv
      :widths: 10, 10, 10, 10, 10, 10
      :header-rows: 1

 
   - If the specific field is empty then the respective setting will not be updated  
   - The field values are case-insensitive so complete and COMPLETE are same
   - Header names in the above csv (name, start_time, prime_time, etc) don't have to be same, you can use any names you want for the header field, and when you press 'Detect CSV format' you can check and map the fields to whatever you want to update
   - Instead of Assignment Name you can also use Assignment ID or LTI Integration URL of the assignment for the assignment identification (sometimes you may have multiple assignments with the same name so you can use these other unique identifiers to avoid any conflicts)

      - Check out :ref:`Get the Course and Assignment ID <get-course-assignment-id>` to see how you can get the assignment ID.
      - Check out :ref:`LTI Integration Assignment URLs <lti-integration-assignment-urls>` to see how you can get LTI Integration URL of the assignment or you can export the LTI Integration URLs of all assignments in the course, see :ref:`Export LTI Settings <export-lti>`
   - You can define one of these 3 possible actions when the assignment closes - Complete, Disable, Complete_and_Disable
   - If :ref:`Prime Setting <prime-assignment-containers>` is not enabled for the assignment but the prime_time is defined in the CSV then the Prime setting will be enabled automatically

4. Our system will automatically detect the CSV fields as required setting fields, you can confirm them and change them if you need from CSV Configuration section as shown in the below image

   .. image:: /img/assignment-batch-update-setting.png
      :alt: Assignment Batch Update Setting


   Once everything is correct, click **Parse CSV** button

5. You will see the test result in the CSV Test Run section (you may also see the error messages if something is not correct in your CSV file)


   .. image:: /img/batch-csv-test-run.png
      :alt: Batch csv Test Run


   Click **Update Assignments** to reflect these settings to your actual assignments settings