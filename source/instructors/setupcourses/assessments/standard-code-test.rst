.. meta::
   :description: Standard Code Test
   
.. _standard-code-test:

Standard Code Test
==================
Standard code tests are dialog driven, where you specify input data and the expected output. Codio then executes the student code, supplies the specified input data, and compares the expected output to the student code's actual output.

**Note:** You can also write code tests that give you in-depth control by allowing you to write your own code to execute tests. See :ref:`Advanced Code Tests <advanced-code-test>` for more information.

Codio provides a Starter Pack project that contains examples for all assessment types and a guides authoring cheat sheet. Go to **Starter Packs** and search for **Demo Guides and Assessments** if not already loaded in your **My Projects** area. Click **Use Pack** to install it to your Codio account.

For more information about adding a Standard Code Test, view this video

.. raw:: html

    <iframe width="620" height="349" src="https://codio.wistia.com/medias/dwts4k9ftt?wvideo=dwts4k9ftt" allowtransparency="true" frameborder="0" scrolling="no" class="wistia_embed" name="wistia_embed" allowfullscreen mozallowfullscreen webkitallowfullscreen oallowfullscreen msallowfullscreen width="620" height="349"></iframe>



Follow these steps to set up a standard code test:

1. On the **General** page, enter the following information:

   .. image:: /img/guides/assessment_general.png
      :alt: General

   - **Name** - Enter a short name that describes the test. This name is displayed in the teacher dashboard so the name should reflect the how successful students are in understanding the assignment.

     If you want to hide the name in the challenge text the student sees, toggle the **Show Name** setting to disable it.
   - **Instructions** - Enter the markdown text that is shown to the student.

2. Click **Execution** in the navigation pane and complete the following information:

   .. image:: /img/guides/assessment_sct_execution.png
      :alt: Execution

  - **Command** - Enter the command that executes the student code. If you store the assessment scripts in the **.guides/secure** folder, they run securely so students cannot see the script or the files in the folder. The files can be dragged and dropped from the File Tree into the field to automatically populate the necessary execution code:

     - **Java**
       
       Compile: javac -cp path/to/file filename.java
       
       Run: java -cp path/to/file filename

     - **Python**
       
       Run: python path/to/file/filename.py

     - **C**

       Compile: gcc filename.c -o filename -lm

       Run: ./filename

     - **C++**

       Compile: g++ -o filename filename.cpp

       Run: ./filename

     - **Ruby**

      Run: ruby filename.rb

     - **Bash**

      Run: bash full_path.sh


 
  - **Pre-exec command** - Enter the command to execute before each test is run. This is normally a compile command.



3. Click **Grading** in the left navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_sct_grading.png
      :alt: Grading

  - **Points** - Enter the score given to the student if the code test passes. You can enter any positive numeric value. If this assessments should not be graded, enter 0 points.
  - **Allow Partial Points** - Toggle to enable partial points so that the grade is based on the percentage of test cases the code passes. See :ref:`Allow Partial Points <partial-points>` for more information.
  - **Case Insensitive** - Toggle to enable if you want Codio to make a case insensitive output comparison. By default, the comparison is case sensitive.
  - **Ignore White Space** - Toggle to enable if you want Codio to strip out any white space characters (carriage return, line feed, tabs, etc.) from both the expected output and the student output. 
  - **Substring Match** - Toggle to enable if you want Codio to perform a substring match when comparing the expected output to the student output.
  - **One Attempt Only** - Toggle to enable if you want the assessment to run only once. The student is warned that they cannot resubmit the assessment. It's recommended that you provide a :ref:`Run Button <customizable-run-menu>` for the student to test the code before running the actual assessment.
  - **Add Item to Check** - Click this button to create another set of input/output fields.
  - **Input - Arguments** - Enter the argument data that is read by the student code.

    .. image:: /img/guides/std-assessment-args.png
       :alt: Input Arguments

  - **Input - Stdin** - Enter the data that would normally be entered manually in the console. For example, Enter your Name. If using this input method:

    - The input data should have a new line if this would be expected in the actual program execution.
    - In the **Output** field, you need to be aware that the prompt text that is displayed to the user appears in ``stdout`` and so it should be reflected in your output field but without the data entered by the user. Normally, you uld **not** put a new line in the output field between each input prompt as the new line character is generawoted by the user when pressing the enter key is not a part of the output.
    - We recommend that you enable the **Ignore white space** and **Substring match** options to be more tolerant. The following image shows how to format input and output fields if you are **not** ignoring white space or doing a **Substring match**. Note how the input field only supplied the values to be input, not the prompt itself (which is actually a part of `stdout`). It is important to accurately account for all spaces and carriage returns.

      .. image:: /img/guides/std-assessment-stdin.png
         :alt: Input and Output Example

     The following image shows the more tolerant approach that has the **Ignore whitespace** option set. In this case, we have put everything on its own line for readability. The whitespace characters will be stripped out of both the expected output and the student output at runtime.

     .. image:: /img/guides/std-assessment-stdin-ignore.png
        :alt: Ignore Whitespace


  - **Generate Item** - Click this button and enter the following information to generate the item to be checked by your code:

    .. image:: /img/guides/generateitem.png
       :alt: Generate Items
  
  - **Show Error Feedback** - Toggle to enable the ability to provide feedback about issues in the student's code. 

    .. image:: /img/guides/std-assessment-error.png
       :alt: Show Error Feedback


  - **Show Expected Answer** - Toggle to enable if you want to show the students the expected output when they have submitted an answer for the question. To suppress this, disable the setting.
  - **Show Answer and Rationale to Students** - Toggle to enable if you want both the answer and the rationale for the answer to the student.
  - **Answer and Rationale** - Enter guidance for the assessment. This is visible to the teacher when the project is opened in the course or when opening the student's project. This guidance information can also be shown to students after they have submitted their answer and when they reload the assignment after marking it as completed. 

4. Click **Metadata** in the left navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_metadata.png
      :alt: Metadata

  - **Bloom's Level** - Click the drop-down and choose the level of Bloom's Taxonomy: https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/ for the current assessement.
  - **Learning Objectives** specific educational goal of the current assessment. Typically, objectives begin with Students Will Be Able To (SWBAT). For example, if an assessment asks the student to predict the output of a recursive code segment, then its Learning Objectives could be *SWBAT follow the flow of recursive execution*.
  - **Tags** - By default, **Content** and **Programming Language** tags are provided and required. To add another tag, click **Add Tag** and enter the name and values.

5. Click **Files** in the left navigation pane and check the check boxes for additional external files to be included with the assessment. The files are then included in the **Additional content** list.

   .. image:: /img/guides/assessment_files.png
      :alt: Files

6. Click **Create** to complete the process.


