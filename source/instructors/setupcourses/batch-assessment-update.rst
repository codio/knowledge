.. meta::
   :description: Batch Assessment Settings Update


.. _batch-assessment-update:


Batch Assessment Update
=======================

You have the ability to perform bulk updates for various assessment settings, including points, partial points, use of maximum score, show expected answer, number of attempts, and showing rationale to students.

Before you begin, make sure to download the XLSX template file. You can download the XLSX template file for your course from **Download Assessment Template** in the **Assessment Settings** section of the **Bulk Settings** area. Update the fields as per your requirements and use that XLSX file to update the assessment settings.

Here is a sample screenshot of the XLSX template:

.. image:: /img/guides/assessment-screenshot-XLSX-bulk-template.png
      :alt: Sample XLSX Template


Things you should know about the XLSX template:

   - Header names must be same as row 1 of above XLSX
   - Do not modify assessment types in column A.
   - Ensure option values match exactly as shown (case-sensitive).
   - Fields marked as "Locked" in the original template cannot be modified.
   - Save the file in XLSX format before uploading.
   

**Here is a reference guide on how to update your XLSX template file:** 


.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Column
     - Description
     - Available Options
   * - Assessment Type
     - The type of assessment (e.g., Standard Code Test, Multiple Choice, Free Text Autograde)
     - Cannot be modified - these are predefined assessment types
   * - Points
     - The point value for the assessment
     - Enter a numeric value (e.g., 20, 50, 100)
   * - Allow Partial Points
     - Whether partial credit is allowed
     - - **Yes**: Enable partial points
       - **No**: Disable partial points
       - **No Change**: Keep current setting
       - **Locked**: Cannot be changed
   * - Use Maximum Score
     - Whether to use the maximum score
     - - **Yes**: Use the maximum score
       - **No**: Do not use maximum score
       - **No Change**: Keep current setting
       - **Locked**: Cannot be changed
   * - Show Expected Answer
     - When to show the expected answer
     - - **Always**: Always show to students
       - **Never**: Never show to students
       - **When Grades Are Released**: Show when grades are released
       - **No Change**: Keep current setting
       - **Locked**: Cannot be changed
   * - Defined Number of Attempts
     - Number of attempts allowed
     - - **No**: No limit on attempts
       - **1-9**: Enter a specific number (1 through 9)
       - **No Change**: Keep current setting
       - **Locked**: Cannot be changed
   * - Show Rationale to Student
     - When to show rationale
     - - **Always**: Always show rationale
       - **Never**: Never show rationale
       - **When Grades Are Released**: Show when grades released
       - **Attempts**: Show after specific number of attempts (requires value in column H)
       - **Score**: Show based on score threshold (requires value in column H)
       - **No Change**: Keep current setting
       - **Locked**: Cannot be changed
   * - If Attempts or Score selected
     - Additional threshold value (column H)
     - - **1-99**: Enter if "Attempts" selected (attempt count)
       - **0-100**: Enter if "Score" selected (score percentage)
       - Leave blank if not using Attempts or Score options

How to Update the CSV Template
-------------------------------

1. **Download the template**: Download the CSV template from "Download Assessment Template" in the "Assessment Settings" section.

2. **Open the file**: Open the CSV file in a spreadsheet application (Excel, Google Sheets, etc.).

3. **Review locked fields**: Fields marked as "Locked" cannot be changed. These appear in gray in the template.

4. **Update settings**: For each assessment type, update the fields according to your requirements using the options listed in the table above.

5. **Use "No Change"**: If you want to keep the current setting for a particular field, enter "No Change".

6. **Set conditional options**: If you select "Attempts" or "Score" in the "Show Rationale to Student" column, make sure to enter the corresponding threshold value in column H.

7. **Save the file**: Save the CSV file with your changes.

8. **Upload**: Upload the modified CSV file through the bulk settings interface.

