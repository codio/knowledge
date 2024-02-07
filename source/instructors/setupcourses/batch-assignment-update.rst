.. meta::
   :description: Batch Assignment Settings Update


.. _batch-assignment-update:

Batch Assignment Update
=======================

You can do the batch update of some assignments settings like Start date/time of the assignment, Closing date/time of the assignment, Action when assignment closes and Prime Assignment Containers settings using a CSV file.

To batch update the assignments settings, follow these steps:

1. Go to **Bulk Settings** area and press **Open Updater** button from Update Assignment Setting

   .. image:: /img/bulk-setting-area.png
      :alt: Bulk Setting Area


2. Select the CSV file in which you have defined all the required settings and press **Detect CSV format** button

   .. image:: /img/select-csv-batch-update.png
      :alt: Select csv Batch Update


   You can use the below CSV as a starting point and customize it as per your needs

   .. csv-table:: 
      :file: /instructors/setupcourses/Batch-Update-Settings.csv
      :widths: 10, 10, 10, 10, 10, 10
      :header-rows: 1

   If the specific field is empty then the respective setting will not be updated. Also instead of Assignment Name you can also use Assignment ID or LTI Integration URL of the assignment for the assignment identification.

3. Our system will automatically detect the CSV fields as required setting fields, you can confirm them and change them if you need from CSV Configuration section as shown in the below image

   .. image:: /img/assignment-batch-update-setting.png
      :alt: Assignment Batch Update Setting


   Once everything is correct, click **Parse CSV** button

4. You will see the test result in the CSV Test Run section (you may also see the error messages if something is not correct in your CSV file)


   .. image:: /img/batch-csv-test-run.png
      :alt: Batch csv Test Run


   Click **Update Assignments** to reflect these settings to your actual assignments settings