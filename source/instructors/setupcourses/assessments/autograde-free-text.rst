.. meta::
   :description: Free Text Autograde 
   
.. _free-text-autograde:

Free Text Autograde 
===================
The Free Text Autograde assessment is similar to the :ref:`Free Text <free-text>` assessment in that it allows students to answer questions in their own words, but includes a field for a command line to execute a script that allows autograding. The answer to the question is stored in the environment variable ``CODIO_FREE_TEXT_ANSWER``. 

Follow these steps to set up an autograde free text assessment:

1. On the **General** page, enter the following information:

   .. image:: /img/guides/assessment_autofree_exec.png
      :alt: General

  - **Name** - Enter a short name that describes the test. This name is displayed in the teacher dashboard so the name should reflect the how successful students are in understanding the assignment.

    If you want to hide the name in the challenge text the student sees, toggle the **Show Name** setting to disable it.
   
  - **Instruction** - Enter the instructions in markdown to be shown to the students.

3. Click **Execution** in the left navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_autofree_exec.png
      :alt: Execution

   - **Command** - Enter the command that executes the student code. If you store the assessment scripts in the **.guides/secure** folder, they run securely so students cannot see the script or the files in the folder. The files can be dragged and dropped from the File Tree into the field to automatically populate the necessary execution code:

   - **Timeout** - Enter the time period (in seconds) that the test runs before terminating.

4. Click **Grading** in the navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_free_grading.png
      :alt: Grading

  - **Points** - Enter the score for correctly answering the question. You can choose any positive numeric value. If this is an ungraded assessment, enter zero (0).

   - **Allow Partial Points** - Toggle to enable a percentage of total points to be given based on the percentage of answers they correctly answer.

   - **One Attempt Only** - Toggle to enable if you want to restrict the student to only answering the question once. If disabled, students can edit their answer until the assignment is marked as completed.

  - **Preview Type** - Choose the input (plaintext or markdown) to be provided by the student. LaTex is also supported and is useful when students need to enter mathematical formulas in their answers. The following options are available:

    - **Plaintext** - Students enter ordinary text with no markdown formatting; there is no preview window.
    - **Plaintext + LaTeX** - Students enter plaintext with no markdown formatting but offers support for LaTeX commands. A preview window is available where students can see the rendered LaTeX output.
    - **Markdown + LaTeX** - Students enter markdown that also offers support for LaTex commands. A preview window is available where students can see the rendered markdown with LaTeX output.

  - **Show Answer and Rationale to Students** - Toggle to enable if you want both the answer and the rationale for the answer to the student.

  - **Answer and Rationale** - Enter guidance for the assessment. This is visible to the teacher when the project is opened in the course or when opening the student's project. This guidance information can also be shown to students after they have submitted their answer and when they reload the assignment after marking it as completed. 

5. Click **Metadata** in the left navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_metadata.png
      :alt: Metadata

  - **Bloom's Level** - Click the drop-down and choose the level of .. _Bloom's Taxonomy: https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/ for the current assessement.
  - **Learning Objectives** specific educational goal of the current assessment. Typically, objectives begin with Students Will Be Able To (SWBAT). For example, if an assessment asks the student to predict the output of a recursive code segment, then its Learning Objectives could be *SWBAT follow the flow of recursive execution*.
  - **Tags** - By default, **Content** and **Programming Language** tags are provided and required. To add another tag, click **Add Tag** and enter the name and values.

5. Click **Files** in the left navigation pane and check the check boxes for additional external files to be included with the assessment. The files are then included in the **Additional content** list.

   .. image:: /img/guides/assessment_files.png
      :alt: Files

6. Click **Create** to complete the process.


Grading free text assessments
-----------------------------
To review and grade answers given by students in a free text assessment, follow these steps:

1. Select the assignment to view the list of all assessments in the assignment for the student.

   .. image:: /img/guides/freetext-grading.png
      :alt: Free Text Grading

   You can identify the free text assessments by the following icon in the **Type** column:

   .. image:: /img/guides/freetexticon.png
      :alt: Free Text Assessments Icon

2. Click any line to view the question and the answer submitted by the student.

3. In the **Points** for answer field, perform one of the following depending on whether **Allow Partial Points** was enabled or disabled for the question:

   - If **Allow Partial Points** was disabled, click **Correct** or **Incorrect**:

     .. image:: /img/guides/notpartial.png
        :alt: Allow Partial Points Disabled

   - If **Allow Partial Points** was enabled, select the points to give for the answer up to the maximum points:

     .. image:: /img/guides/partial.png
        :alt: Allow Partial Points Enabled

4. In the **Comments** field, enter any information (in markdown + latex) about the grade, which can be viewed by the student when the grade is released, and then click **Submit **Comment**. 

Example of a simple Bash script for partial points
..................................................

.. code:: bash

    #!/usr/bin/env bash
    POINTS=0
    if [ "${CODIO_FREE_TEXT_ANSWER}" == "answer1" ]
    then
      POINTS=1
    fi
    if [ "${CODIO_FREE_TEXT_ANSWER}" == "answer5" ]
    then
      POINTS=5
    fi
    if [ "${CODIO_FREE_TEXT_ANSWER}" == "answer10" ]
    then
      POINTS=10
    fi
    curl "$CODIO_PARTIAL_POINTS_URL&points=${POINTS}" > /dev/null


Example of a Python script for partial points
.............................................

.. code:: python

    #!/usr/bin/env python
    import os, requests, sys
    import random
    # get free text auto value
    text = os.environ['CODIO_FREE_TEXT_ANSWER']
    # import grade submit function
    sys.path.append('/usr/share/codio/assessments')
    from lib.grade import send_partial
    def main():
      # Execute the test on the student's code
      grade = 0  
      feedback = ''  
      if text == '1':
        grade = 1
        feedback = '1 point'
      elif text == '5':
        grade = 5
        feedback = '5 points'
      elif text == '10':
        grade = 10
        feedback = '10 points'
      else:
        grade = 0
        feedback = 'no points'    

      print(feedback)
      # Send the grade back to Codio with the penatly factor applied

      res = send_partial(int(round(grade)))
      exit( 0 if res else 1)

    main()



Autograding enhancements
------------------------
To provide you with more robust auto-grade scripts, you can send back feedback in different formats HTML, Markdown, or plaintext) and a URL is passed as an environment variable ```CODIO_PARTIAL_POINTS_V2_URL```. These variables allow POST and GET requests with the following parameters:

- **Points** (```CODIO_PARTIAL_POINTS_V2_URL```) - 0-100 points for assessment (should be scaled automatically for partial points). 
- **Feedback** - text
- **Format** - html, md, or txt (default)

