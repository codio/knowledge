.. meta::
   :description: Using a standard code test, student code is executed and the output is compared to an expected output.
   
.. _standard-code-test:

Standard Code Test
==================
Standard code tests are dialog driven, where you specify input data and the expected output. Codio then executes the student code, supplies the specified input data, and compares the expected output to the student code's actual output.

.. Note:: The output (including white space) of all the test cases in your Standard Code test cannot exceed 20,000 characters.
    If your output will exceed this limit, or you need finer control of the tests, you can create custom code tests. See :ref:`Advanced Code Tests <advanced-code-test>` for more information.


For more information about adding a Standard Code Test, view this video

.. raw:: html

   <script src="https://fast.wistia.com/embed/medias/rsmrdwd2y2.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_rsmrdwd2y2 videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/rsmrdwd2y2/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>
    

Assessment Auto-Generation
--------------------------

Assessments can be auto-generated using the text on the current guide page as context. For more information, see the :ref:`AI assessment generation <ai-assessment-generation>` page.

The Standard Code Test assessment generation creates:

- Instructions for the student
- Test cases using standard input or command line arguments
- Expected output specifications
- A solution with explanation
- A code file for the student with the solution bracketed within :ref:`solution templates <solution-file-templating>`




Assessment Manual Creation
--------------------------

Follow these steps to set up a standard code test. For more information on **General**, **Metadata** (Optional) and **Files** (Optional) see :ref:`Assessments <assessments>`.


1. Complete **General**.


2. Click **Execution** in the navigation pane and complete the following information:

   .. image:: /img/guides/assessment_sct_execution.png
      :alt: Execution
      :width: 350px

   .. Note:: If you store the assessment scripts in the **.guides/secure** folder, they run securely and students cannot see the script or the files in the folder. The files can be dragged and dropped from the File Tree into the field to automatically populate the necessary execution and run code.
  
   - **Command** - Command that executes the student code (usually run).
   - **Pre-exec command** - Command to execute before each test runs (usually compile). If this fails, the main Command will not run.
   - **Timeout** - Amend the timeout setting for code execution (up to 300 seconds via arrows, or manually enter a longer period).

   **Language-Specific Commands**

   .. tabs::

      .. tab:: Java

         - Compile: ``javac -cp path/to/file filename.java``
         - Run: ``java -cp path/to/file filename``

      .. tab:: Python

         - Run: ``python path/to/file/filename.py``

      .. tab:: C

         - Compile: ``gcc filename.c -o filename -lm``
         - Run: ``./filename``

      .. tab:: C++

         - Compile: ``g++ -o filename filename.cpp``
         - Run: ``./filename``

      .. tab:: Ruby

         - Run: ``ruby filename.rb``

      .. tab:: Bash

         - Run: ``bash full_path.sh``

      .. tab:: SQL

         Codio provides helper scripts to run queries via ODBC (stricter spacing than sqlcmd).
         
         .. Note:: First install the appropriate helper script via **Tools > Install Software** (MSSQL, MySQL, or PostgreSQL).
         
         .. image:: /img/guides/sql-helpers.png
            :alt: Install SQL Helper Script
            :width: 500px
         
         Run the appropriate command:
         
         - MSSQL: ``python .guides/scripts/helper_mssql.py --db_host localhost --db_user SA --db_pass YourPassword --db_name DBNAME``
         - MySQL: ``python .guides/scripts/helper_mysql.py --db_host localhost --db_user root --db_pass YourPassword --db_name DBNAME``
         - PostgreSQL: ``python .guides/scripts/helper_postgres.py --db_host localhost --db_port 5432 --db_user postgres --db_pass YourPassword --db_name DBNAME``
      
      
3. Click **Grading** in the left navigation pane and complete the following fields:

.. image:: /img/guides/Grading-new-feature1.png
   :alt: Grading
   :width: 500px

.. list-table:: Grading Configuration Options
   :widths: 25 75
   :header-rows: 1

   * - Setting
     - Description
   * - **Points**
     - The score given to the student if the code test passes. You can enter any positive numeric value. If this assessment should not be graded, enter 0 points.
   * - **Allow Partial Points**
     - Toggle to enable partial points, the grade is then based on the percentage of test cases the code passes. See :ref:`Allow Partial Points <partial-points>` for more information.
   * - **Use Maximum Score**
     - Toggle to enable assessment final score to be the highest score attained of all runs.
   * - **Case Insensitive**
     - Toggle to enable a case insensitive output comparison. By default, the comparison is case sensitive.
   * - **Ignore White Space**
     - Toggle to enable stripping out any white space characters (carriage return, line feed, tabs, etc.) from both the expected output and the student output.
   * - **Substring Match**
     - Toggle to enable substring match when comparing the expected output to the student output. The entire expected output needs to be contiguous in the student output.
   * - **Search**
     - Search the test cases by the number/index assigned to it.
   * - **Expand All/Collapse All**
     - Click to expand/collapse all test cases.
   * - **Add Item to Check**
     - Click to create another set of input/output fields.
   * - **Delete**
     - Click to delete the test case.
   * - **Check All**
     - Press to check all test cases at once so you can see how many of them are passed or failed.


.. image:: /img/guides/std-assessment-args.png
   :alt: Input Arguments
   :width: 450px

- **Input - Arguments and Input - Stdin**

.. tabs::

   .. tab:: Input - Arguments

      Enter the command line arguments that are read by the student code.

   .. tab:: Input - Stdin

      Enter data that would be entered manually in the console. For example, Enter your Name:. If using this input method:

      - The input data should have a new line if it would be expected in the actual program execution.
      - In the **Output** field, the prompt text that is displayed to the user appears in ``stdout`` and should be reflected in your output field but without the data entered by the user. You do **not** need a new line in the output field between each input prompt as the new line character is part of the user input.
      - **Ignore white space** and **Substring match** are recommended options as they make the test more tolerant. The following image shows how to format input and output fields if you are **not** ignoring white space or doing a **Substring match**. Note how the input field only supplied the values to be input, not the prompt itself (which is actually a part of ``stdout``). It is important to accurately account for all spaces and carriage returns.

        .. image:: /img/guides/std-assessment-stdin.png
           :alt: Input and Output Example

        The following image shows the more tolerant approach with the **Ignore whitespace** option set. In this case everything on its own line for readability. The whitespace characters will be stripped out of both the expected output and the student output at runtime.

        .. image:: /img/guides/std-assessment-stdin-ignore.png
           :alt: Ignore Whitespace
           :width: 400px


.. list-table:: Assessment Settings
   :widths: 25 75
   :header-rows: 1

   * - Setting
     - Description
   * - **Run Test**
     - Click this button to generate the expected output based on the input you provided in the left half of the box. You need to have the solution code in the code file in order for the output to be generated. If there is already some content in the output box then you will get a pop up asking you if you want to overwrite the existing output.
   * - **Check Test**
     - Use this to test whether running the solution code, using the optional input, will result in the value in the expected output box. If the test fails an output box will appear below showing the difference between the current output and the expected output.

       .. image:: /img/guides/assessment_sct_check.png
          :alt: Check Test Case

   * - **Show Error Feedback**
     - Toggle to enable feedback to students about errors related to the specific test case.

       .. image:: /img/guides/std-assessment-error.png
          :alt: Show Error Feedback
          :width: 400px

   * - **Show Expected Answer**
     - Toggle to show the students the expected output when they have submitted an answer for the question. To suppress expected output, disable the setting.
   * - **Define Number of Attempts**
     - Enable to allow and set the number of attempts students can make for this assessment. If disabled, the student can make unlimited attempts.
   * - **Show Rationale to Students**
     - Toggle to display the answer, and the rationale for the answer, to the student. This guidance information will be shown to students after they have submitted their answer and any time they view the assignment after marking it as completed. You can set when to show this selecting from **Never**, **After x attempts**, **If score is greater than or equal to a % of the total** or **Always**
   * - **Rationale**
     - Enter guidance for the assessment. This is always visible to the teacher when the project is opened in the course or when opening the student's project.


4. Click **Create** to complete the process.



Output Written to a File
------------------------
If the output of a program is written to a file rather than Standard Output (stdout) you can use the **Command** portion of the execution tab to run a bash command to list out the contents of the file.

For example if the output is written to a file called ``output.txt``, you would put the following into the **Command**. 

.. code-block:: Bash

   cat output.txt

In Linux, the command ``cat`` lists out the contents of the file. You can use the **Pre-exec command** to run the student code in this case.