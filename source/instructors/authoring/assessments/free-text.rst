.. meta::
   :description: Free text assessments allow students to answer questions in their own words.
   
.. _free-text:

Free Text
=========
Free text assessments allow students to answer questions in their own words. Because Free Text assessments allow for LaTeX formatting, this type of assessment is recommended for math assessments. Teachers are then able to review and manually grade their answers. Follow these steps to set up a free text assessment:

1. On the **General** page, enter the following information:

   .. image:: /img/guides/assessment_free_general.png
      :alt: General

  - **Name** - Enter a short name that describes the test. This name is displayed in the teacher dashboard so the name should reflect the challenge and thereby be clear when reviewing.

    If you want to hide the name in the challenge text the student sees, toggle the **Show Name** setting to disable it.
   
  - **Instruction** - Enter the instructions in markdown to be shown to the students.

2. Click **Grading** in the navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_free_grading.png
      :alt: Grading

  - **Points** - Enter the score for correctly answering the question. You can choose any positive numeric value. If this is an ungraded assessment, enter zero (0).

  - **Allow Partial Points** - Toggle to enable a percentage of total points to be given based on the percentage of answers they correctly answer.

  - **Preview Type** - Choose the input (plaintext or markdown) to be provided by the student. LaTex is also supported and is useful when students need to enter mathematical formulas in their answers. The following options are available:

    - **Plaintext** - Students enter ordinary text with no markdown formatting; there is no preview window.
    - **Plaintext + LaTeX** - Students enter plaintext with no markdown formatting but offers support for LaTeX commands. A preview window is available where students can see the rendered LaTeX output.
    - **Markdown + LaTeX** - Students enter markdown that also offers support for LaTex commands. A preview window is available where students can see the rendered markdown with LaTeX output.

  - **Define Number of Attempts** - enable to allow and set the number of attempts students can make for this assessment. If disabled, the student can make unlimited attempts.
  
  - **Show Rationale to Students** - Toggle to display the rationale for the answer, to the student. This guidance information will be shown to students after they have submitted their answer and any time they view the assignment after marking it as completed. You can set when to show this selecting from **Never**, **After x attempts**, **If score is greater than or equal to a % of the total** or **Always**

  - **Rationale** - Enter guidance for the assessment. This is visible to the teacher when the project is opened in the course or when opening the student's project. This guidance information can also be shown to students after they have submitted their answer and when they reload the assignment after marking it as completed. 

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

4. In the **Comments** field, enter any information (in markdown + LaTeX) about the grade, which can be viewed by the student when the grade is released, and then click **Submit Comment**. 

Navigate student assessments
.............................
You can navigate through student assessments using the left (**<**) and right (**>**) arrow buttons at the top of the **Assessments grading** dialog. 

.. image:: /img/guides/freetext_navigate.png
   :alt: Navigating Assessments

View graded free text assessments
.................................
You can view the points given and the Correct column checked for all free text assessments that have been graded.

.. image:: /img/guides/freetextanswer.png
   :alt: View Graded Assessment
   