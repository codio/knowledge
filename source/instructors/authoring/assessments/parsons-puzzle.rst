.. meta::
   :description: Parson’s Puzzles are formative assessments that ask students to arrange blocks of scrambled code.
   
.. _parsons-puzzle:

Parsons Puzzle
==============
Parson’s problems are available in Codio as Parsons Puzzles. Parson’s Puzzles are formative assessments that ask students to arrange blocks of scrambled code, allowing them to focus on the purpose and flow of the code (often including a new pattern or feature) instead of syntax. Codio uses `js-parsons <http://js-parsons.github.io/documentation/>`_ for Parson's Puzzles.

Complete the following steps to set up a Parsons Puzzle assessment:

1. On the **General** page, enter the following information:

   .. image:: /img/guides/assessment_general.png
      :alt: General

  - **Name** - Enter a short name that describes the test. This name is displayed in the teacher dashboard so the name should reflect the challenge and thereby be clear when reviewing.

    If you want to hide the name in the challenge text the student sees, toggle the **Show Name** setting to disable it.
   
  - **Instruction** - Enter the instructions in markdown to be shown to the students.

2. Click **Execution** in the navigation pane and complete the following information:

   .. image:: /img/guides/assessment_parsons_exec.png
      :alt: Execution

  - **Code to Become Blocks** - Enter code blocks that make up the initial state of the puzzle for the students.
  - **Code to Become Distractor Blocks** - Enter code blocks that serve as distractions. 
  - **Max Distractors** - Enter the maximum number of distractors allowed.
  - **Grader** - Choose the appropriate grader for the puzzle from the drop-down list. 

3. Click **Grading** in the navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_grading.png
      :alt: Grading

  - **Points** - Enter the score if the student selects the correct answer. You can choose any positive numeric value. If this is an ungraded assessment, enter zero (0).

  - **One Attempt Only** - Toggle to enable if you want to restrict the student to only answering the question once. If disabled, students can edit their answer until the assignment is marked as completed.

  - **Show Answer and Rationale to Students** - Toggle to display the answer, and the rationale for the answer, to the student. This guidance information will be shown to students after they have submitted their answer and any time they view the assignment after marking it as completed. You can set when to show this selecting from **Mever**, **After x attempts**, **If score is greater than or equal to a % of the total** or **Always**

  - **Answer and Rationale** - Enter guidance for the assessment. This is visible to the teacher when the project is opened in the course or when opening the student's project. This guidance information can also be shown to students after they have submitted their answer and when they reload the assignment after marking it as completed. 

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


Grader Options
--------------
- VariableCheckGrader - Executes the code in the order submitted by the student and checks variable values afterwards.

  Expected and supported options:

  - ``vartests`` (required)  array of variable test objects
    
    Each variable test object can/must have the following properties:

    - ``initcode`` - code that will be prepended before the learner solution code
    - ``code`` - code that will be appended after the learner solution code
    - ``message`` (required) - a textual description of the test, shown to learner

  Properties specifying what is tested:

  - ``variables`` - an object with properties for each variable name to be tested; the value of the property is the expected value
  
  or
  
  - ``variable`` - a variable name to be tested
  - ``expected`` - expected value of the variable after code execution

- TurtleGrader - for exercises that draw turtle graphics in Python. Grading is based on comparing the commands executed by the model and student turtle. If the ``executable_code`` option is also specified, the code on each line of that option will be executed instead of the code in the student constructed lines. 

  .. Note:: Student code should use the variable ``myTurtle`` for commands to control the turtle in order for the grading to work.

  Required options:

  - ``turtleModelCode`` - The code constructing the model drawing. The turtle is initialized to modelTurtle variable, so your code should use that variable. The following options are available:

    - ``turtlePenDown`` - A boolean specifying whether or not the pen should be put down initially for the student constructed code
    - ``turtleModelCanvas`` - ID of the canvas DOM element where the model solution will be drawn. Defaults to `modelCanvas`.
    - ``turtleStudentCanvas`` - ID of the canvas DOM element where student turtle will draw. Defaults to `studentCanvas`.

- UnitTestGrader - Executes student code and Skulpt unit tests.

- LanguageTranslationGrader - Code translating grader.

- LineBasedGrader - Treats student answers as correct if and only if they match the order and indentation found in **Initial Values**. For incorrect answers, it highlights the lines that were not ordered or indented properly.

Sample Starter Pack
-------------------
There is a Starter Pack project - Demo Guides and Assessments that you can add to your account that includes examples of Parson's Puzzle assessments. If not already loaded to your account (in your **My Projects** area), go to Starter Packs and search for **Demo Guides and Assessments**
