.. meta::
   :description: Parson’s Puzzles are formative assessments that ask students to arrange blocks of scrambled code.
   
.. _parsons-puzzle:

Parsons Puzzle
==============
Parson’s problems are available in Codio as Parsons Puzzles. Parson’s Puzzles are formative assessments that ask students to arrange blocks of scrambled code, allowing them to focus on the purpose and flow of the code (often including a new pattern or feature) instead of syntax. Codio uses `js-parsons <http://js-parsons.github.io/documentation/>`_ for Parson's Puzzles.

Assessment Auto-Generation
++++++++++++++++++++++++++

Assessments can be auto-generated from text found on a guides page. To auto-generate a Parsons Puzzle, select Parsons Puzzle assessment from Assessments list and simply press the **Generate** button present at bottom right corner and press **Create** button to create the assessment.

   .. image:: /img/guides/generate-assessment-button.png
      :alt: Generate assessment button

Important points to consider when auto-generating assessment:

- whatever text is found on that page, the generator will use that to come up with assessment
- you should always check what is created by looking at **Execution** tab to see output and then by previewing as well when created
- you can edit/change the generated content as you per requirement
- showing rationale/answers is set to 'never' so review on the **Grading** tab when to show rationale along with the points you want to allocate to the assessment
- you cannot regenerate existing assessments, this is only for 'new' assessments
- Library assessments are not supported
- if there is not enough information, it may generate bad information so you should always check before creating the assessment
- if there are some fields broken, it will not generate but contact us with details of course/assignment/assessment and we can check it out



Complete the following steps to set up a **Line Based Grader** Parsons Puzzle assessment. The **Line Based Grader** assessment treats student answers as correct if and only if they match the order and indentation found in **Initial Values**. For incorrect answers, it highlights the lines that were not ordered or indented properly.

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
  - **Show Feedback** - Select to show feedback to student and highlight error in the puzzle. Deselect to hide feedback and not show highlight error in the puzzle.
  - **Require Dragging** - If you enter **Code to Become Distractor Blocks**, **Require Dragging** will automatically turn on. Without distractor blocks, you can decide whether or not you want students to drag blocks to a separate area to compose their solution.
  - **Disable Indentation** - If you do not want to require indention, check the **Disable Indentation** box. 
  - **Indent Size** - Each indention defaults to 50 pixels.

3. Click **Grading** in the navigation pane and complete the following fields:

   .. image:: /img/guides/Grading-new-feature1.png
      :alt: Grading

  - **Points** - Enter the score if the student selects the correct answer. You can choose any positive numeric value. If this is an ungraded assessment, enter zero (0).

  - **Define Number of Attempts** - enable to allow and set the number of attempts students can make for this assessment. If disabled, the student can make unlimited attempts.
  - **Show Rationale to Students** - Toggle to display the answer, and the rationale for the answer, to the student. This guidance information will be shown to students after they have submitted their answer and any time they view the assignment after marking it as completed. You can set when to show this selecting from **Never**, **After x attempts**, **If score is greater than or equal to a % of the total** or **Always**

  - **Rationale** - Enter guidance for the assessment. This is visible to the teacher when the project is opened in the course or when opening the student's project. This guidance information can also be shown to students after they have submitted their answer and when they reload the assignment after marking it as completed. 
  - **Use maximum score** - Toggle to enable assessment final score to be the highest score attained of all runs.

4. Click on the **Parameters** tab if you wish to set up **Parameterized Assessments**. See :ref:`Parameterized Assessments <parameterized>` for more information.

5. Click **Metadata** in the left navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_metadata.png
      :alt: Metadata

  - **Bloom's Level** - Click the drop-down and choose the level of Bloom's Taxonomy: https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/ for the current assessment.
  - **Learning Objectives** specific educational goal of the current assessment. Typically, objectives begin with Students Will Be Able To (SWBAT). For example, if an assessment asks the student to predict the output of a recursive code segment, then its Learning Objectives could be *SWBAT follow the flow of recursive execution*.
  - **Tags** - By default, **Content** and **Programming Language** tags are provided and required. To add another tag, click **Add Tag** and enter the name and values.

6. Click **Files** in the left navigation pane and check the check boxes for additional external files to be included with the assessment when adding it to an assessment library. The files are then included in the **Additional content** list.

   .. image:: /img/guides/assessment_files.png
      :alt: Files

7. Click **Create** to complete the process.


Grader Options
--------------

**VariableCheckGrader** - Executes the code in the order submitted by the student and checks variable values afterwards.

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/zyrxf8as9m.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:54.58% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_zyrxf8as9m videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/zyrxf8as9m/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

 
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

**TurtleGrader** - for exercises that draw turtle graphics in Python. Grading is based on comparing the commands executed by the model and student turtle. If the ``executable_code`` option is also specified, the code on each line of that option will be executed instead of the code in the student constructed lines. 

  .. Note:: Student code should use the variable ``myTurtle`` for commands to control the turtle in order for the grading to work.

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/818mmle6c1.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:54.58% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_818mmle6c1 videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/818mmle6c1/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

  Required options:

- ``turtleModelCode`` - The code constructing the model drawing. The turtle is initialized to modelTurtle variable, so your code should use that variable. The following options are available:

  - ``turtlePenDown`` - A boolean specifying whether or not the pen should be put down initially for the student constructed code
  - ``turtleModelCanvas`` - ID of the canvas DOM element where the model solution will be drawn. Defaults to `modelCanvas`.
  - ``turtleStudentCanvas`` - ID of the canvas DOM element where student turtle will draw. Defaults to `studentCanvas`.

**UnitTestGrader** - Executes student code and Skulpt unit tests. This grader is for Python problems where students create functions. Similar to traditional unit tests on code, this grader leverages a unit test framework where you set asserts - meaning this grader checks the functionality of student code. 

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/fafvc7pih9.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:54.58% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_fafvc7pih9 videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/fafvc7pih9/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

**LanguageTranslationGrader** - Code translating grader where Java or psuedocode blocks map to Python in the background. Selecting the language allows the Parson's problem to check for correct indentation and syntax.

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/epu2uofoo5.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:54.58% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_epu2uofoo5 videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/epu2uofoo5/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

Sample Starter Pack
-------------------
There is a Starter Pack project - Demo Guides and Assessments that you can add to your account that includes examples of Parson's Puzzle assessments. If not already loaded to your account (in your **My Projects** area), go to Starter Packs and search for **Demo Guides and Assessments**.
