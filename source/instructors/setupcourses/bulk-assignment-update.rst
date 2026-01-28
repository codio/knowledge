.. meta::
   :description: Bulk Assignment Settings Update


.. _bulk-assignment-update:

Bulk Assignment Update
=======================

You have the ability to perform a bulk update for various assignment settings, including start date/time of the assignment, closing date/time of the assignment, action when assignment closes, due dates and penalties. For more information about these settings, see :ref:`Assignment Duration <assignment-duration>`, :ref:`Prime Assignment Containers <prime-assignment-containers>` and :ref:`Virtual Coach <enable-vc-bulk>` settings using a CSV file.


Before you begin, make sure to download the csv template file. You can download the csv template file of your course from  “Download Assignment Information” present in the “Assignment settings” in the  “Bulk Settings area”. You can update the fields as per your requirement(s) and use that csv file to update the assignment settings. 
Here is a sample screenshot of the csv template:


.. image:: /img/guides/screenshot-csv-bulk-template.png
      :alt: Sample csv Template 



Things you should know about the csv template:
   - Header names must be same as row 1 of above CSV
   - If the specific field is empty then the respective setting will not be updated     
   - All field are case-insensitive so complete and COMPLETE are same
   - If :ref:`Prime Setting <prime-assignment-containers>` is not enabled for the assignment but the prime_time is defined in the CSV then the Prime setting will be enabled automatically




**Here is a reference guide on how to update your csv template file:** 


.. list-table:: Assignment Configuration Fields
   :header-rows: 1
   :widths: 10 10 15 65

   * - Column Name
     - Data Type
     - Possible Values
     - Description
   * - name
     - text
     - assignment name(s)
     - The assignment name goes in this cell.
   * - visibility_on_completed
     - text
     - READ_ONLY_WITH_RESUBMIT, READ_ONLY, NO_ACCESS, NO_ACCESS_UNTIL_GRADES_RELEASED
     - This setting determines what level of access students have to a completed assignment.
   * - visibility_on_disabled
     - text
     - NO_ACCESS, READ_ONLY, NO_ACCESS_UNTIL_GRADES_RELEASED
     - This setting determines what level of access students have to a disabled assignment.
   * - start_time
     - integer and text
     - mm/dd/yyyy h:mm XX (e.g., 5/2/2025 9:11 AM)
     - Specify the start time, date (m/d/year) and the time (h:mm) and identify if its morning or night (XX).
   * - closing_time
     - integer and text
     - mm/dd/yyyy h:mm XX (e.g., 05/26/2025 11:59 PM)
     - Specify the closing time, the date (m/d/year) and the time (h:mm) and identify if its morning or night (XX).
   * - closing_action
     - text
     - DISABLE_AND_COMPLETE, DISABLE, COMPLETE
     - Specify what action you want to take when the assignment closes. You currently have 3 options: 1. Disable assignment and mark as complete 2. Disable assignment 3. Mark as complete
   * - due_at
     - integer and text
     - mm/dd/yyyy h:mm XX (e.g., 05/23/2025 11:59 PM)
     - Specify the due date, the date (m/d/year) and the time (h:mm) and identify if its morning or night (XX). Note: For more information about this setting please visit :ref:`Assignment Duration <assignment-duration>`
   * - mark_as_completed_on_due_date
     - text
     - TRUE, FALSE
     - Identify whether you would like the assignment to be marked completed on the due date.
   * - penalty_enabled
     - text
     - TRUE, FALSE
     - Identify if you want there to be a penalty for late submission of the assignment.
   * - deduction_interval
     - text
     - day, hour
     - If you have elected to have a penalty (penalty_enabled: TRUE), then in this cell you identify if you want the deduction to be by hour or by day after the due date.
   * - deduction_percent
     - integer
     - any whole number
     - If you have elected to have a penalty (penalty_enabled: TRUE), then in this cell you identify the deduction percentage. If you want to deduct 5%, then you would just put "5".
   * - lowest_grade_percent
     - integer
     - any whole number between 0 and 100
     - Identify the lowest possible grade a student can receive for this assignment. Note: For more information on penalty deductions, please see :ref:`Penalties <penalties>`
   * - allow_regrade_request
     - text
     - TRUE, FALSE
     - Identify if you want to allow students to request for a regrade of their assignment.
   * - prime_time
     - integer and text
     - mm/dd/yyyy h:mm XX (e.g., 05/08/2025 06:44 PM)
     - Specify the Start Time when you want the containers available. Note: For more information about this setting, please visit :ref:`Prime Assignment Containers <prime-assignment-containers>`
   * - prime_count
     - integer
     - any whole number
     - In this cell you will specify the Number of Students that will start the assignment at the same time. Note: For more information about this setting, please visit :ref:`Prime Assignment Containers <prime-assignment-containers>`
   * - coach_summarize_prompt
     - text
     - TRUE, FALSE
     - Identify whether the student can request a summary of the assessment prompt or not.
   * - coach_error_augmentation
     - text
     - TRUE, FALSE
     - Identify whether you want to provide more detailed explanations for error message text on request.
   * - coach_next_steps_hint
     - text
     - TRUE, FALSE
     - Identify whether the student can request hints for completing the assessment requirements.



Once you have updated/modified your csv template file now you are ready to bulk update the assignment settings.

To bulk update the assignments settings, follow these steps:


1. On the **Courses** page, click the course that contains the assignment you want to edit

2. Go to **Bulk Settings** area and press **Open Updater** button from Update Assignment in the Assignment Setting area.

3. Select or drag and drop the CSV file in which you have defined all the required settings.

   .. image:: /img/select-csv-batch-update.png
      :alt: Select csv Batch Update


4. You will see the test result in the CSV Test Run section (you may also see the error messages if something is not correct in your CSV file)


   .. image:: /img/batch-csv-test-run.png
      :alt: Batch csv Test Run


   Click **Apply** to reflect these settings to your actual assignments settings