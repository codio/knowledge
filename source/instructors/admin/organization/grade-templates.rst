.. meta::
   :description: The grading rubric/template feature includes a two-dimensional grid that provides grading guidance for manually assessing a coding project.

.. _grade-template:

Create Grading Templates
========================
The Grading Rubric feature includes a two-dimensional grid that provides grading guidance for manually assessing a coding project.

.. image:: /img/class_administration/grading/template-example.png
   :alt: Rubric Example

You create the templates from the Grading Templates menu on the Organizations page, and then instructors can assign the templates to their assignments. 

.. Note:: Only organization Owners can access this page and create grading templates.

Follow these steps to create a rubric grading template:

1. Click your profile icon in the lower left corner of the screen.

   .. image:: /img/class_administration/profilepic.png
      :alt: Profile

2. In the **Organizations** area, click the name of your organization.

   .. image:: /img/class_administration/addteachers/myschoolorg.png
      :alt: My Organizations

3. Click the **Rubrics** tab.

   .. image:: /img/class_administration/grading/templates.png
      :alt: Grading Templates

4. Click **Create a New Template** and then complete the following information:

  - **Name** - Enter a template name.
  - **Rows** - A row addresses a single assessment criterion and you must enter a weight percentage value where all rows total 100%.
  - **Columns** - Each column contains a score that you assign. Typically, the first column includes a 0 value that corresponds to failure to address the criterion. The remaining columns contain a range of values that you choose, with the far right column including a value for completely meeting the assessment criterion. Please read the following paragraph before choosing column values.

   **Important:** When grading student code, the grading rubric is displayed and is clickable; point are awarded based on where you click. Codio then weighs the scores according to the weightings that are provided for each row.

   A final score is calculated based on the selections and is re-based to the maximum column value. If you want the scores to calculate to percentages, choose a maximum value of 100, with other column values distributed between 0 and 100.

.. Note:: A rubric can be cloned from another assignment instead of manually creating a new template. In the assignment that has a rubric template assigned to it, click the **Settings** icon to select the assignment.