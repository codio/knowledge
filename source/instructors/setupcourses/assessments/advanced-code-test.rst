.. _advanced-code-test:

Advanced Code Test
===================
The advanced code test assessment type allows you to write code in any language that checks code a student has written. However, if students can access the command line, they can explore the box and find the folder where your test scripts are located to modify the script. For compiled executables, they could replace your executables with those they've created if they know how the callbacks work.

If you want your scripts to run securely, where students cannot view the script or other files that contain secure data, move the script files to the **.guides/secure** folder. Only the original project author can access this folder. 

Codio provides a <Starter Pack> (https://codio.com/home/starter-packs/cc68d38b-b0ea-4825-9814-46a3594c2b11/) project that contains examples for all assessment types and a guides authoring cheat sheet. Click **Use Pack** to install it to your Codio account.

Complete each section to set up your standard code test.

1. On the **General** page, enter the following information:

   .. image:: /img/guides/assessment_general.png
      :alt: General

   - **Name** - Enter a short name that describes the test. This name is displayed in the teacher dashboard so the name should reflect the how successful students are in understanding the assignment.

     If you want to hide the name in the challenge text the student sees, toggle the **Show Name** setting to disable it.
   - **Instructions** - Enter the markdown text that is shown to the student.

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

       ```bash
       sudo apt update
      sudo apt install python3-pip
      sudo python3 -m pip install pycodestyle
      ```

    .. image:: /img/guides/assessment_act_exec_pycodestyle.png
       :alt: Pycodestyle

     To add individual Python source files whose style should be checked, either enter their relative path to `~/namespace` or drag them from the File Tree into the **Add Case** text box and click **Add Case**. You may add as many cases as needed. When the assessment executes, ``pycodestyle`` inspects each added file and outputs all styling issues that it found.

     **Using UnitTest**

     When using Python unit test and you want to implement a Python test and keep the test file (```.guides/secure```) separate from the student work (another directory), you can define the student folder where the students ```.py``` file is located if it's not in the **workspace** folder

    **Using Jshint or Jslint**

    If you choose **JSHint** or **JSLint**, they must first be installed as a Node.js global package using the following command:

    ``sudo npm install -g jshint jslint``

    To add individual JavaScript source files whose style should be checked, either enter their relative path to `~/namespace` or drag them from the File Tree into the **Add Case** text box and click **Add Case**. You may add as many cases as needed. 

    You can also choose **JSLint** or **JSHint** in the **Language Assessment Subtype** drop-down menu. When the assessment executes, each added file is inspected and outputs all styling issues that were found.

    **Using Custom**

    If you choose **Custom**, enter the following information:

    .. image:: /img/guides/assessment_act_exec_custom.png
       :alt: Custom

    - **Command** - Enter the command that executes the student code. If you store the assessment scripts in the **.guides/secure** folder, they run securely so students cannot see the script or the files in the folder. The files can be dragged and dropped from the File Tree into the field to automatically populate the necessary execution code:

    - **Timeout** - Enter the time period (in seconds) that the test runs before terminating.

3. Click **Grading** in the left navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_grading.png
      :alt: Grading

  - **Points** - Enter the score given to the student if the code test passes. You can enter any positive numeric value. If this assessments should not be graded, enter 0 points.

  - **One Attempt Only** - Toggle to enable if you want the assessment to run only once. The student is warned that they cannot resubmit the assessment. It's recommended that you provide a :ref:`Run Button <customizable-run-menu>` for the student to test the code before running the actual assessment.
  - **Answer and Rationale** - Enter guidance for the assessment. This is visible to the teacher when the project is opened in the course or when opening the student's project. This guidance information can also be shown to students after they have submitted their answer and when they reload the assignment after marking it as completed. 

4. Click **Metadata** in the left navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_metadata.png
      :alt: Metadata

  - **Bloom's Level** - Click the drop-down and choose the level of <Bloom's Taxonomy> (https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/) for the current assessement.
  - **Learning Objectives** specific educational goal of the current assessment. Typically, objectives begin with Students Will Be Able To (SWBAT). For example, if an assessment asks the student to predict the output of a recursive code segment, then its Learning Objectives could be *SWBAT follow the flow of recursive execution*.
  - **Tags** - By default, **Content** and **Programming Language** tags are provided and required. To add another tag, click **Add Tag** and enter the name and values.

5. Click **Files** in the left navigation pane and check the check boxes for additional external files to be included with the assessment. The files are then included in the **Additional content** list.

   .. image:: /img/guides/assessment_files.png
      :alt: Files

6. Click **Create** to complete the process.

