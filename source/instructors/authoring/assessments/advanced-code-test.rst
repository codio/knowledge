.. meta::
   :description: The advanced code test assessment type allows you to write code in any language that checks code a student has written.
   
.. _advanced-code-test:

Advanced Code Test
==================
The advanced code test assessment type allows you to write code in any language that checks code a student has written. 

To ensure that your test scripts run securely and to prevent student access to your testing files or executables place them in the **.guides/secure** folder. This folder is not available to students in their assignments and they cannot access it from the command line. Only the person creating the assignment has access to the **.guides/secure** folder, it is not included in the student assignment.

Codio provides a Starter Pack project that contains examples for all assessment types and a guides authoring cheat sheet. Go to **Starter Packs** and search for **Demo Guides and Assessments** if not already loaded in your **My Projects** area. Click **Use Pack** and then **Create** to install it to your Codio account.

Complete each section to set up your standard code test.

1. On the **General** page, enter the following information:

   .. image:: /img/guides/assessment_general.png
      :alt: General

   - **Name** - Enter a short name that describes the test. This name is displayed in the teacher dashboard so the name should reflect the challenge and thereby be clear when reviewing.

     Toggle the **Show Name** setting to hide the name in the challenge text the student sees.
     
   - **Instructions** - Enter text that is shown to the student using optional Markdown formatting.

2. Click **Execution** in the navigation pane and complete the following information:

   - **Language Type** - Click the drop-down and choose the language. The following languages are supported:

     - **Ruby**: `rubocop` or `rspec`
     - **Java**: [JUnit](/project/ide/features/#junit-testing-framework) or `checkstyle`
     - **Python**: `pycodestyle` or `UnitTest`
     - **JavaScript**: `jshint` or `jslint`
     - **Custom**
   - **Language Assessment Subtype** - Click the drop-down and choose a subtype for the selected language type, if applicable.
      
     **Using Pycodestyle**

     If you choose **pycodestyle**, you must first install it. Use the following commands to install pycodestyle:

.. code:: ini

      sudo apt update
      sudo apt install python3-pip
      sudo python3 -m pip install pycodestyle
     

.. image:: /img/guides/assessment_act_exec_pycodestyle.png
    :alt: Pycodestyle

     To add individual Python source files whose style should be checked, either enter their relative path to `~/namespace` or drag them from the File Tree into the **Add Case** text box and click **Add Case**. You may add as many cases as needed. When the assessment executes, ``pycodestyle`` inspects each added file and outputs all styling issues.
     
     **Using JUnit**

     When using JUnit you can add your own custom feedback to the standard feedback Junit returns to students. The feedback message is passed to the assert method as the first parameter. 

    `assertEquals(feedback, expected, actual)`

     **Using UnitTest**

     When using Python unit test you can define the location of the student folder (their ```.py```files), if it's not in the **workspace** folder, and have it be separate from test file folder (```.guides/secure```).

    **Using Jshint or Jslint**

    **JSHint** or **JSLint** must first be installed as a Node.js global package using the following command:

    ``sudo npm install -g jshint jslint``

    To add individual JavaScript source files for style checking, either enter their relative path to `~/namespace` or drag them from the File Tree into the **Add Case** text box and click **Add Case**. You may add as many cases as needed. 

    You can also choose **JSLint** or **JSHint** in the **Language Assessment Subtype** drop-down menu. When the assessment executes, each added file is inspected and outputs all styling issues that were found.

    **Using Custom**

    If you choose **Custom**, enter the following information:

    .. image:: /img/guides/assessment_act_exec_custom.png
       :alt: Custom
       
    - **Allow Partial Points** - Toggle to enable partial points, the grade is then based on the percentage of test cases the code passes. See :ref:`Allow Partial Points <partial-points>` for more information.

    - **Command** - Enter the command that executes the student code. 

    **Note:** If you store the assessment scripts in the **.guides/secure** folder, they run securely and students cannot see the script or the files in the folder. 
    The files can be dragged and dropped from the File Tree into the field to automatically populate the necessary execution and run code.

    - **Timeout** - Enter the time period (in seconds) that the test runs before terminating.

3. Click **Grading** in the left navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_grading.png
      :alt: Grading

  - **Points** - The score given to the student if the code test passes. You can enter any positive numeric value. If this assessment should not be graded, enter 0 points.

  - **One Attempt Only** - Toggle to enable the assessment to run only once. The student will be warned that they cannot resubmit the assessment. It's recommended that you provide a :ref:`Run Button <customizable-run-menu>` for the student to test the code before running the actual assessment.
  - **Show Answer and Rationale to Students** - Toggle to display the answer, and the rationale for the answer, to the student. This guidance information will be shown to students after they have submitted their answer and any time they view the assignment after marking it as completed. 
  - **Answer and Rationale** - Enter guidance for the assessment. This is always visible to the teacher when the project is opened in the course or when opening the student's project. 

4. Click **Metadata** in the left navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_metadata.png
      :alt: Metadata

  - **Bloom's Level** - Click the drop-down and choose the level of Bloom's Taxonomy: https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/ for the current assessement.
  - **Learning Objectives** The objectives are the specific educational goal of the current assessment. Typically, objectives begin with Students Will Be Able To (SWBAT). For example, if an assessment asks the student to predict the output of a recursive code segment, then the Learning Objectives could be *SWBAT follow the flow of recursive execution*.
  - **Tags** - The **Content** and **Programming Language** tags are provided and required. To add another tag, click **Add Tag** and enter the name and values.

5. Click **Files** in the left navigation pane and check the check boxes for additional external files to be included with the assessment. The files are then included in the **Additional content** list.

   .. image:: /img/guides/assessment_files.png
      :alt: Files

6. Click **Create** to complete the process.

