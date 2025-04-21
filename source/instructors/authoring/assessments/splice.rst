.. meta::
   :description: Codio allows you to display a SPLICE assessment embedded in an iFrame in Codio.
   
.. _splice:

SPLICE Assessments
==================

SPLICE (Standards, Protocols, and Learning Infrastructure for Computing Education) assessments are created externally. 
SPLICE provides a protocol for information exchange between the assessment and the application in which it is embedded. To use a SPLICE assessment, provide a link to the assessment, and Codio will display it in an iframe. More information about SPLICE assessments may be found here: https://cssplice.org/.

How to use a SPLICE Assesment in Codio
**************************************

1. On the **General** page, enter the name of your assessment that describes the test. This name is displayed in the teacher dashboard so the name should reflect the challenge and thereby be clear when reviewing.

2. On the **Execution** page, paste the URL for the assessment in the **ASSESSMENT URL** field.

3. On the **Grading** page, enter the amount of points to assign to the assessment. Enter the score for correctly answering the question they are assigned. You can choose any positive numeric value. If this is an ungraded assessment, enter zero (0).

- **Use maximum score** - Toggle to enable assessment final score to be the highest score attained of all runs.

4. (Optional) Click **Metadata** in the left navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_metadata.png
      :alt: Metadata

  - **Bloom's Level** - Click the drop-down and choose the level of Bloom's Taxonomy: https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/ for the current assessment.
  - **Learning Objectives** The objectives are the specific educational goal of the current assessment. Typically, objectives begin with Students Will Be Able To (SWBAT). For example, if an assessment asks the student to predict the output of a recursive code segment, then the Learning Objectives could be *SWBAT follow the flow of recursive execution*.
  - **Tags** - The **Content** and **Programming Language** tags are provided and required. To add another tag, click **Add Tag** and enter the name and values.

5. (Optional) Click **Files** in the left navigation pane and check the check boxes for additional external files to be included with the assessment when adding it to an assessment library. The files are then included in the **Additional content** list.

   .. image:: /img/guides/assessment_files.png
      :alt: Files

6. Click **Create** to complete the process.