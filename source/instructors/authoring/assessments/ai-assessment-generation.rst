.. meta::
   :description: General guidelines for assessment generation.
   
.. _ai-assessment-generation:

Generating Assessments With AI
==============================
Important points to consider when auto-generating assessments:

- The assessment generator will use the text on the current page to generate the assessment.

- You should always review the generated assessment for correctness, including the question prompt, button text, expected output and generated code solutions. 

- You can edit the assessment contents once they have been generated.

- Review the items on the Execution and Grading tabs, as the default settings may not match your needs. 

- The regenerate option is not available for existing assessments. However, you can create a new assessment to replace an existing one. 

- When there is insufficient information, the assessment generator may output incorrect information. It is very important to always review generated assessments carefully.

This is a new feature, and if it does not work properly for you, please let us know via the support chat or by emailing help@codio.com. If you would like us to take a look, send us your course name, the module, the assignment, and the page.

.. note:: Not all assessments can be AI-generated. If you don't see a "Generate" button in the bottom right corner when you click on an assessment, that assessment type does not support AI generation. 


How to Generate an Assessment with AI
-------------------------------------

Assessments can be auto-generated using the text on the current guides page as context. Follow the steps below to auto-generate an assessment:

1. Select an assessment from the Assessments list.

2. Press the **Generate** button at bottom right corner. 

   .. image:: /img/guides/generate-assessment-button.png
      :alt: Generate assessment button

3. The Generation Prompt will open, press **Generate Using AI** to preview the generated assessment. 

   .. image:: /img/guides/assessment-generation-prompt.png
      :alt: Assessment Generation Prompt


4. When you are satisfied with the result, press **Apply** and then **Create**. If you are not satisfied with the result, select **Regenerate** to create a new version of the assessment. You can provide additional guidance in the **Generation Prompt** field. For example, ``create assessment based on the first paragraph with 2 correct answers``.



.. important:: The generate assessment feature does not configure the page :ref:`layout; <layout>` you should specify the layout depending on how you want to present the information to the students.




Example Prompts
----------------
**Multiple choice**

- Create a question about how to refactor the code below with multiple correct answers: (include code)

**Parson's Problem**

- Create a Python script that reads a text file named 'input.txt' and rewrites its content to 'output.txt' with each sentence on a separate line. Assume sentences end with '.', '!', or '?'. 

**Fill in the Blanks**

- List different government cybersecurity recommendations and have the student specify which agency recommended them and or what year they were recommended.

**Standard Code Test**

- Provide the student with simple instructions, including the formula used to calculate compound interest. Students should use standard input to prompt for input values. 
