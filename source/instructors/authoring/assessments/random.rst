.. meta::
   :description: The Random assessment type is to allow a range of defined assessments from the assessment library to be randomly assigned to students
   
.. _random:

Random Assessment
=================

The Random assessment type allows you to define a pool of assessments, with each student receiving a randomly selected assessment from that pool. Note that specific layout requirements apply.

**Layout Requirements**

* **Simple Layout (1 Panel without tree)**: Multiple Random assessments can be added on the same page
* **Complex Layout (any other layout)**: 
  
  * Cannot be added on the same page
  * Cannot be mixed with any other assessments
  * Warning will display when Publishing if mixed with other assessments
  * May not function as intended if layout requirements are violated

**Duplication Prevention**

Codio automatically prevents duplicate assessments at the assignment level by checking library assessment IDs for uniqueness. This ensures students won't see the same assessment question multiple times within an assignment.

**Requirements for duplication prevention:**

* All questions in the assessment library must be unique
* All randomized assessments must be drawn from the same library

.. note::
   If duplicate assessments are generated, the assessment library does not contain enough unique assessments to satisfy all random assessment queries in the assignment.

Creating a Random Assessment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. On the **General** page, enter the name of your assessment that describes the test. This name is displayed in the teacher dashboard so the name should reflect the challenge and thereby be clear when reviewing.

2. On the **Grading** page, enter the amount of points to assign to the assessment. Enter the score for correctly answering the question they are assigned. You can choose any positive numeric value. If this is an ungraded assessment, enter zero (0).

- **Use maximum score** - Toggle to enable assessment final score to be the highest score attained of all runs.

3. On the **Execution** page, browse to an assessment library where you can set up filters define the range of assessments to randomly assign. You can work from any assessment library you have access to.

.. list-table:: Filter Categories and Inputs
   :widths: 30 70
   :header-rows: 1

   * - Category
     - Available Inputs & Description
   * - Bloom's Taxonomy Level
     - .. tab-set::

          .. tab-item:: Levels I-III
          
             * Level I - Remembering
             * Level II - Understanding
             * Level III - Applying

          .. tab-item:: Levels IV-VI
          
             * Level IV - Analyzing
             * Level V - Evaluating
             * Level VI - Creating
   * - Assessment Type (auto-detected)
     - .. tab-set::

          .. tab-item:: Code-Based
          
             * Standard Code Test 
             * Advanced Code Test 
             * Parsons Puzzle 

          .. tab-item:: Text-Based
          
             * Multiple Choice 
             * Fill in the Blanks 
             * Free Text Autograde 
   * - Programming Language
     - Select the programming language for code-based assessments (e.g., Python, Java, C++, JavaScript)
   * - Category (topic-level)
     - Broad subject area or topic category for filtering assessments (e.g., variables, functions, loops).
   * - Content (sub-topic level)
     - Specific subtopic or concept within the category (e.g., modyfying variables, creating functions, nesting for loops).
   * - Learning Objective (SWBAT form)
     - Define what "Students Will Be Able To..." accomplish after completing the assessment
       
       Example: "Students will be able to implement binary search algorithms efficiently"


:ref:`Click here <assess-library>` for more information on how to use Assessment Libraries.




Updating Random Assessments
~~~~~~~~~~~~~~~~~~~~~~~~~~~


Modifying Assessment Parameters
-------------------------------

To update, change, or review the assessments assigned to a random assessment:

1. Navigate to the **Execution** tab
2. Select the **Update Search** button
3. The assessment library field will open with your saved search parameters

   .. image:: /img/guides/random-update.png
      :alt: Update Random assessment
      :width: 450px


Publishing Changes
------------------

After reviewing assessments, follow the appropriate publishing method based on your situation:

**If ONLY random assessment changes were made:**

* Students have not started: Publish normally
* Students have already started: Use the **Sync** button on the **Edit** tab (see Synchronizing Changes below)

**If other assignment changes were also made:**

* Publish normally first
* Then navigate to the **Edit** tab to sync if students have started

Synchronizing Changes from the Course
-------------------------------------

When random assessment changes are made (either by you or another organization member), synchronize them from the **Edit** tab in the course.

A **Sync** button appears on the **Edit** tab when changes are available to synchronize.

.. image:: /img/guides/random-sync.png
   :alt: Synchronise Random assessment
   :width: 500px

.. warning::
   Students who have already started the assignment will not receive updates unless their assignment is reset. Resetting will cause them to start "as new" and **all previous work will be lost**.

Sync Options
------------

When you press the **Sync** button, Codio will check if students have started and present appropriate options:

**No students have started**

The assignment will sync and publish to all students.

   .. image:: /img/guides/random-sync-nostudents.png
      :alt: Synchronise Random assessment - no students started
      
**Students have started**  

You can choose to:

* **Reset and publish**: All students restart with new changes (previous work lost)
* **Publish only**: Only students who haven't started receive the changes

   .. image:: /img/guides/random-sync-studentsstarted.png
      :alt: Synchronise Random assessment - students started