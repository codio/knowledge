.. meta::
   :description: LLM Free Text assessments allow students to answer questions in their own words and receive AI-assisted grading.
   
.. _llm-free-text:


LLM Free Text
=============

The **LLM Free Text** assessment type lets students respond to questions in their own words. It supports **LaTeX formatting**, making it especially well-suited for math-based assessments.


Responses are open-ended and are **graded manually by the instructor with AI assistance**. Feedback is displayed to students only after the instructor approves it, unless **Preliminary AI Feedback** is enabled, in which case students receive immediate automated feedback upon submission.


You can find this assessment type under the **Manually Graded** section of the assessments menu.


Assessment Creation
++++++++++++++++++++

Follow these steps to set up an LLM Free Text assessment. For more information on **General**, **Metadata** (optional), and **Files** (optional), see :ref:`Assessments <assessments>`.

1. Complete **General**.

2. Click **Grading** in the navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_LLM_free_grading.png
      :alt: Grading

   - **Points** — Enter the point value for a correct answer. You can use any positive number. Enter zero (0) for ungraded assessments.



   - **Instructor's Reference Answer** — Enter a reference answer in the field provided.


   - **Preview Type** — Select the input format students will use when writing their answer. LaTeX is recommended when students need to enter mathematical formulas.


     .. list-table::
        :widths: 20 80
        :header-rows: 1

        * - Format Type
          - Description
        * - **Plaintext**
          - Students enter plain text with no formatting support. No preview window is shown.
        * - **Plaintext + LaTeX**
          - Students enter plain text with LaTeX support. A preview window displays the rendered LaTeX output.
        * - **Markdown + LaTeX**
          - Students enter Markdown with LaTeX support. A preview window displays the rendered Markdown and LaTeX output.

   - **Define Number of Attempts** — Toggle on to limit the number of submission attempts. If left off, students can attempt the assessment an unlimited number of times.


   - **Preliminary AI Feedback** — Toggle on to provide students with immediate AI-generated feedback upon submission. The LLM compares the student's response to the instructor's **Reference Answer** and indicates how well they scored.


   - **Show Rationale to Students** — Toggle on to display rationale to students after submission or when they revisit a completed assignment. Control when it appears by selecting **Never**, **After x attempts**, **If score is ≥ x% of total**, or **Always**.


   - **Rationale** — Enter guidance or commentary for the assessment. This is always visible to the instructor and can optionally be shown to students depending on the **Show Rationale to Students** setting above.


3. Click **Create** to finish.


Grading LLM Free Text Assessments
---------------------------------

To review and grade student responses, follow these steps:

1. Select the assignment.

2. Find the student you want to grade and click the number under **Points** to view all assessments in the assignment.

   .. image:: /img/guides/freetext-grading.png
      :alt: Free Text Grading

   LLM Free Text assessments are identified by this icon in the **Type** column:

   .. image:: /img/guides/llmfreetexticon.png
      :alt: llm Free Text Assessment Icon

3. Click any row to view the question and the student's submitted answer.

4. Review the student's answer and preliminary results.

   - In the **Feedback** section, you can update or modify the feedback displayed to the student.
   - In the **Test Cases** section, review each test case and check the checkbox to accept it, or uncheck to reject it. You can also adjust the points and grading rationale for each.
   - Once finished, click **Apply Grade** in the bottom right.

   .. image:: /img/guides/llmfreetexttestcases.png
      :alt: llm Free Text Assessment grading window


Navigate Student Assessments
------------------------------

Use the left (**<**) and right (**>**) arrow buttons at the bottom of the **Assessments Grading** dialog to move between student submissions.

.. image:: /img/guides/llmfreetext_navigate.png
   :alt: Navigating Assessments
   :width: 550px


View Graded LLM Free Text Assessments
-------------------------------------

Once graded, you can view the points awarded and the checked status in the **Correct** column for all free text assessments.

.. image:: /img/guides/llmfreetextanswer.png
   :alt: View Graded Assessment


