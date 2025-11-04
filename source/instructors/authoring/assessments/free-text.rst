.. meta::
   :description: Free text assessments allow students to answer questions in their own words.
   
.. _free-text:

Free Text
=========
Free text assessments allow students to answer questions in their own words. This type of assessment is recommended for math assessments since it allows for LaTeX formatting. Teachers are then able to review and manually grade their answers.



Assessment Auto-Generation
++++++++++++++++++++++++++

Assessments can be auto-generated using the text on the current guides page as context. For more information about generating assessments may be found on the :ref:`AI assessment generation <ai-assessment-generation>` page.

Assessment Manual Creation
++++++++++++++++++++++++++

Follow these steps to set up a free text assessment manually. For more information on General, Metadata, and Files, see :ref:`Assessments <assessments>`.

1. Complete **General**.

2. Click **Grading** in the navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_free_grading.png
      :alt: Grading

- **Points** - Enter the score for correctly answering the question. You can choose any positive numeric value. If this is an ungraded assessment, enter zero (0).

- **Partial Points** - Toggle to enable a percentage of total points to be given based on the percentage of answers they correctly answer. Once you toggle this on, you will be able to add rubric items. Rubric items are negative points, they will be subtracted from the total score of the assessment.

- **Preview Type** - Choose the input (plaintext or markdown) to be provided by the student. LaTex is also supported and is useful when students need to enter mathematical formulas in their answers. The following options are available:

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Format Type
     - Description
   * - **Plaintext**
     - Students enter ordinary text with no markdown formatting; there is no preview window.
   * - **Plaintext + LaTeX**
     - Students enter plaintext with no markdown formatting but offers support for LaTeX commands. A preview window is available where students can see the rendered LaTeX output.
   * - **Markdown + LaTeX**
     - Students enter markdown that also offers support for LaTeX commands. A preview window is available where students can see the rendered markdown with LaTeX output.

- **Define Number of Attempts** - Enable to allow and set the number of attempts students can make for this assessment. If disabled, the student can make unlimited attempts.
  
- **Show Rationale to Students** - Toggle to display the rationale for the answer, to the student. This guidance information will be shown to students after they have submitted their answer and any time they view the assignment after marking it as completed. You can set when to show this selecting from **Never**, **After x attempts**, **If score is greater than or equal to a % of the total** or **Always**

- **Rationale** - Enter guidance for the assessment. This is visible to the teacher when the project is opened in the course or when opening the student's project. This guidance information can also be shown to students after they have submitted their answer and when they reload the assignment after marking it as completed. 

3. **(Optional)** Complete **Metadata**.

4. **(Optional)** Complete **Files**.

5. Click **Create** to complete the process.


Grading Free Text Assessments
-----------------------------
To review and grade answers given by students in a free text assessment, follow these steps:

1. Select the assignment.

2. Find the student you want to grade and click the number under **Points** to view the list of all assessments in the assignment for the student.

   .. image:: /img/guides/freetext-grading.png
      :alt: Free Text Grading

   You can identify the free text assessments by the following icon in the **Type** column:

   .. image:: /img/guides/freetexticon.png
      :alt: Free Text Assessments Icon

3. Click any line to view the question and the answer submitted by the student.

4. In the **Points** for answer field, perform one of the following depending on whether **Allow Partial Points** was enabled or disabled for the question:

   - If **Allow Partial Points** was disabled, click **Correct** or **Incorrect**:

     .. image:: /img/guides/notpartial.png
        :alt: Allow Partial Points Disabled
        :width: 450px

   - If **Allow Partial Points** is enabled, assign points for the answer up to the maximum allowed. You can also add rubric items and specify the point value for each:
     
     .. image:: /img/guides/partial.png
        :alt: Allow Partial Points Enabled
        :width: 450px


5. In the **Comments** field, enter any information about the grade, which can be viewed by the student when the grade is released, and then click **Submit Comment**. 


Navigate Student Assessments
----------------------------

You can navigate through student assessments using the left (**<**) and right (**>**) arrow buttons at the bottom of the **Assessments grading** dialog. 

.. image:: /img/guides/freetext_navigate.png
   :alt: Navigating Assessments

View Graded Free Text Assessments
----------------------------------
You can view the points given and the Correct column checked for all free text assessments that have been graded.

.. image:: /img/guides/freetextanswer.png
   :alt: View Graded Assessment

Free Text Assessments That Are Automatically Graded as Correct
--------------------------------------------------------------
Free text assessments can be automatically graded as correct. To learn more see :ref:`Free Text Autograde <free-text-autograde>`.
