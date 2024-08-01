.. meta::
   :description: Multiple choice type assessments provide a question and then single or multiple response options.
   
.. _multiple-choice:

Multiple Choice
===============
Multiple choice type assessments provide a question and then single or multiple response options. 

Assessment Auto-Generation
++++++++++++++++++++++++++

Assessments can be auto-generated from text found on a guides page. Follow below steps to auto-generate a Multiple Choice assessment:

1. Select Multiple Choice assessment from Assessments list 

2. Press the **Generate** button present at bottom right corner 

   .. image:: /img/guides/generate-assessment-button.png
      :alt: Generate assessment button

3. Generation Prompt will open, press **Generate** to preview the generated assessment

   .. image:: /img/guides/assessment-generation-prompt.png
      :alt: Assessment Generation Prompt

 If you are unhappy with the generated assessment, you can **Regenerate** the assessment. If you wish to guide the prompt generation with information about how you want your assessment to be, add that information to the **Generation Prompt** field. For example, *create assessment based on the first paragraph with 2 correct answers.*

4. When happy, press **Apply** and then **Create**


Important points to consider when auto-generating assessment:

- whatever text is found on that page, the generator will use that to come up with assessment
- you should always check what is created by looking at **Execution** tab to see output and then by previewing as well when created
- you can edit/change the generated content as you per requirement
- showing rationale/answers is set to 'never' so review on the **Grading** tab when to show rationale along with the points you want to allocate to the assessment
- you cannot regenerate existing assessments, this is only for 'new' assessments
- Library assessments are not supported
- if there is not enough information, it may generate bad information so you should always check before creating the assessment
- if there are some fields broken, it will not generate but contact us with details of course/assignment/assessment and we can check it out

Assessment Manual Creation
++++++++++++++++++++++++++

Follow these steps to set up multiple choice assessments manually:

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
  
 - **Define Number of Attempts** - enable to allow and set the number of attempts students can make for this assessment. If disabled, the student can make unlimited attempts.
 
  - **Show Rationale to Students** - Toggle to display the rationale for the answer, to the student. This guidance information will be shown to students after they have submitted their answer and any time they view the assignment after marking it as completed. You can set when to show this selecting from **Never**, **After x attempts**, **If score is greater than or equal to a % of the total** or **Always**

  - **Rationale** - Enter guidance for the assessment. This is always visible to the teacher when the project is opened in the course or when opening the student's project. 
  - **Use maximum score** - Toggle to enable assessment final score to be the highest score attained of all runs. 

4. Click on the **Parameters** tab if you wish to set up **Parameterized Assessments**. See :ref:`Parameterized Assessments <parameterized>` for more information.

5. Click **Metadata** in the left navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_metadata.png
      :alt: Metadata

  - **Bloom's Level** - Click the drop-down and choose the level of Bloom's Taxonomy: https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/ for the current assessment.
  - **Learning Objectives** The objectives are the specific educational goal of the current assessment. Typically, objectives begin with Students Will Be Able To (SWBAT). For example, if an assessment asks the student to predict the output of a recursive code segment, then the Learning Objectives could be *SWBAT follow the flow of recursive execution*.
  - **Tags** - The **Content** and **Programming Language** tags are provided and required. To add another tag, click **Add Tag** and enter the name and values.

6. Click **Files** in the left navigation pane and check the check boxes for additional external files to be included with the assessment when adding it to an assessment library. The files are then included in the **Additional content** list.

   .. image:: /img/guides/assessment_files.png
      :alt: Files

7. Click **Create** to complete the process.
