.. meta::
   :description: Use an LLM to generate a rubric and grade based on that rubric. 
   
.. _llm-based-auto-rubric:


LLM Rubric Autograde
====================

The **LLM Rubric Autograde** assessment automatically grades student submissions using an LLM-generated rubric and displays feedback directly to students without requiring instructor approval.

It can be found in the **Auto-Graded** section of the assessments menu. If you wish to approve the LLM grading before it is displayed to the student, see the :ref:`LLM Rubric <llm-based-rubric>` assessment in the **Manually Graded** section.

More information about adding assessments can be found in our :ref:`assessment documentation <add-assessment>`.

There are two steps to the **LLM Rubric Autograde** process:

1. Rubric generation
2. LLM-based grading using the generated rubric


Add an **LLM Rubric Autograde** assessment to your guide page and follow the steps below.

LLM Based Rubric Creation (Step 1)
----------------------------------

Complete the sections below to set up your rubric grader. For more information on **General**, **Metadata** and **Files** see :ref:`Assessments <assessments>`.

1. Complete **General**.

2. Click **Grading** in the navigation pane and complete the following information:

.. image:: /img/guides/llmbasedrubric.png
   :height: 600
   :alt: Generate a rubric

- Add a solution file (1) if you wish the rubric creation process to consider your solution.

- Click the **Generate Rubrics** (2) button to initiate the process.

The **Rubric Creation Agent** uses the following items to generate the rubric items:

- The assessment name
- Instructions provided in the **General** tab of the assessment
- Content of the Guide Page where the assessment is being added
- Contents of the provided solution file
- The Course, Module, and Assignment name
- Requirements specified in the Rubric creation tab

.. Note:: If you do not specify rubric requirements, the system will generate rubric items using general code grading norms.

Add your requirements in the **Rubric Requirements** dialog (optional): 

.. image:: /img/guides/llmrubricreqs.png
   :height: 600
   :alt: Area to add your rubric requirements


- Once you are done, click **Generate Using AI**. 
- You can provide additional rubric items by clicking **Add Rubric** and entering information.
- Once you have reviewed the rubric items and other settings, click **Save** to save the assessment.


LLM Grading Based on the Created Rubric (Step 2)
------------------------------------------------

The grading occurs when the student clicks the **Check It** button. The LLM Grading agent uses the following to grade the student's work:

- Instructions provided in the **General** tab of the assessment
- Contents of the Guide page where the assessment is located
- Contents of the specified solution file
- The student file
- The rubric generated in the previous step to identify the grading criteria

Sample feedback for the Auto-Graded Version:

.. image:: /img/guides/rubricfinal.png
    :height: 600
    :alt: Final grading information displayed to the student

Rubric Requirements Example
---------------------------
(You can view another example on the :ref:`LLM Rubric Grader <llm-based-rubric>` page.) 

Use only the following criteria for evaluating the student code:

- The code correctly implements the requested task and outputs the correct values.
- Variable and function names are descriptive and clearly indicate their purpose in the program. 
- The code includes at least two meaningful comments.