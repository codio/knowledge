.. meta::
   :description: Batch Assessment Settings Update


.. _batch-assessment-update:


Batch Assessment Update
=======================

You have the ability to perform bulk updates for various assessment settings, including points, partial points, use of maximum score, show expected answer, number of attempts, and showing rationale to students.

Before you begin, make sure to download the Excel (.xlsx)  template file. You can download the Excel (.xlsx)  template file for your course from **Download Assessment Template** in the **Assessment Settings** section of the **Bulk Settings** area. Update the fields as per your requirements and use that Excel (.xlsx) file to update the assessment settings.

Here is a sample screenshot of the template:

.. image:: /img/guides/assessment-screenshot-XLSX-bulk-template.png
      :alt: Sample XLSX Template


Things you should know about the template:  
   - Edit only the white cells with dropdowns or number inputs.		
   - Leave any cell set to No Change to keep the current published setting.		
   - Gray cells labeled Not Supported or Restricted cannot be edited for the selected assessment type.		
   - Save the file in XLSX format before uploading.
		


**Here is a reference guide on how to update your template file:** 



.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Column
     - Description
     - Available Options
   * - Assessment Type
     - Type of assessment
     - Predefined - cannot be modified
   * - Points
     - Point value for assessment
     - Numeric value (e.g., 20, 50, 100)
   * - Allow Partial Points
     - Whether partial credit is allowed
     - Yes, No, No Change, Not Supported
   * - Use Maximum Score
     - Whether to use maximum score
     - Yes, No, No Change, Not Supported
   * - Show Expected Answer
     - When to show expected answer
     - Always, Never, When Grades Are Released, No Change, Not Supported
   * - Defined Number of Attempts
     - Number of attempts allowed
     - No, 1-9, No Change, Not Supported
   * - Show Rationale to Student
     - When to show rationale
     - Always, Never, When Grades Are Released, Attempts, Score, No Change, Not Supported
   * - Value (for ATTEMPTS/SCORE)
     - Numeric threshold for Attempts or Score
     - 1-99 (attempts), 0-100 (score %), blank otherwise


Once you have updated/modified your Excel (.xlsx) template file now you are ready to bulk update the assessment settings.

To bulk update the assessment settings, follow these steps:

1. On the **Courses** page, click the course you want to update the assessment settings for. 

2. Go to **Bulk Settings** area and scroll to the **Assessment Settings** section.

3. In the **Assessment Settings** section click **Open updater**.

4. Select or drag and drop the Excel (.xlsx) file in which you have defined all the required settings.

5. Identify the assignments you want to update the assessment settings for.

   .. image:: /img/guides/select-excel-batch-update.png
      :alt: Select csv Batch Update

6. Click **Apply and Done**. A popup window will appear asking you to confirm, click **yes**.

.. note:: A green banner will appear at the bottom of the page letting you know your updates are processing. Once the update is complete you will receive an email from Codio. 