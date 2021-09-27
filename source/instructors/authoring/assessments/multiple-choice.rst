.. meta::
   :description: Multiple choice type assessments provide a question and then single or multiple response options.
   
.. _multiple-choice:

Multiple Choice
===============
Multiple choice type assessments provide a question and then single or multiple response options. Follow these steps to set up multiple choice assessments:

1. On the **General** page, enter the following information:

   .. image:: /img/guides/assessment_mc_general.png
      :alt: General

  - **Name** - Enter a short name that describes the test. This name is displayed in the teacher dashboard so the name should reflect the challenge and thereby be clear when reviewing.

    If you want to hide the name in the challenge text the student sees, toggle the **Show Name** setting to disable it.
   
  - **Question** - Enter the question instruction that is shown to the student.

2. Click **Execution** in the navigation pane and complete the following information:

   .. image:: /img/guides/assessment_mc_exec.png
      :alt: Execution

  - **Shuffle Answers** - Toggle to randomize the order of the answers so each student sees the answers in a different order.
  - **Multiple Response** - Toggle to enable a user to select more than one answer. 
  - **Answers** - Mark the correct answer(s) to the question. You can add as many options as needed. For each answer, toggle to enable as correct answer (for multiple responses), or click the radio button for the correct single response.
  - **Ordering** - Use the **Up** and **Down** arrows to change the order in which the answers are presented.

3. Click **Grading** in the navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_mc_grading.png
      :alt: Grading

  - **Correct Points** - Enter the score if the student selects the correct answer. You can choose any positive numeric value. If this is an ungraded assessment, enter zero (0).

  - **Incorrect Points** is the score to be deducted if the student makes an incorrect selection. Typically, this value will be 0 but you can assign any positive numeric value if you wish to penalize guessing. If this assessment is to be ungraded, set '0' points

  - **Allow Partial Points** - Toggle to enable a percentage of total points to be given based on the percentage of answers they correctly answer.

  - **Show Expected Answer** - Toggle to show the students the expected output when they have submitted an answer for the question. To suppress expected output, disable the setting.

  - **Show Answer and Rationale to Students** - Toggle to display the answer, and the rationale for the answer, to the student. This guidance information will be shown to students after they have submitted their answer and any time they view the assignment after marking it as completed. You can set when to show this selecting from **Never**, **After x attempts**, **If score is greater than or equal to a % of the total** or **Always**

  - **Answer and Rationale** - Enter guidance for the assessment. This is always visible to the teacher when the project is opened in the course or when opening the student's project.  

4. Click **Metadata** in the left navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_metadata.png
      :alt: Metadata

  - **Bloom's Level** - Click the drop-down and choose the level of Bloom's Taxonomy: https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/ for the current assessement.
  - **Learning Objectives** The objectives are the specific educational goal of the current assessment. Typically, objectives begin with Students Will Be Able To (SWBAT). For example, if an assessment asks the student to predict the output of a recursive code segment, then the Learning Objectives could be *SWBAT follow the flow of recursive execution*.
  - **Tags** - The **Content** and **Programming Language** tags are provided and required. To add another tag, click **Add Tag** and enter the name and values.

5. Click **Files** in the left navigation pane and check the check boxes for additional external files to be included with the assessment when adding it to an assessment library. The files are then included in the **Additional content** list.

   .. image:: /img/guides/assessment_files.png
      :alt: Files

6. Click **Create** to complete the process.
