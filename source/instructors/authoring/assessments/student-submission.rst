.. meta::
   :description: Student Submission Options
  
.. _student-submission:

Student Submission Options
==========================
You can control the following:

- How students submit individual questions.
- How students notify course instructors that an assignment is completed.

The Submit Button
--------------------
By default each assessment has a Submit button beneath the assessment. Once pressed, the answer is autograded. 

.. note:: You can customize the Submit button label to any text you prefer. In the assessment markdown, update the text to the left of "|assessment".
    
    .. image:: /img/guides/customizeSubmitbutton.png
       :alt: Customize Submit Button
       :width: 400px

Each assessment type allows you to define the number of attempts students can make. Students can see the number of attempts they have left to the right of the Submit button.

Suppressing the Submit Button
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can suppress the Submit button for the following assessment types: Advanced Code Test, Standard Code Test, MCQ, Fill in the Blank, Parsons Puzzle, LLM Rubric Auto Grade, LLM Rubric, Free Text, and Free Text Autograde.

This feature is useful for exams where students shouldn't need to worry about pressing a submit button. They can simply provide their response and move on to other assessments or pages.

To suppress the use of the **Submit** button, go to the **Settings** button in the guide and disable **Use submit buttons**.

  .. image:: /img/guides/globalsettings.png
     :alt: Global Settings


Once the project is marked as complete (see below) all assessment responses are submitted automatically. All student work must be marked as complete either manually or using the automated **Mark as Complete** option on the final deadline.



Mark as Complete
----------------

A student can proactively mark an assignment as complete. If there is an :ref:`assignment-level autograde script <auto-grade-scripts>` it will be run at this time and the completion status will be displayed in the teacher dashboard.

**Advantages:**
Instructors can grade students' work as soon as they mark it as complete.

**Drawbacks:**
Once students mark an assignment as complete, they can no longer make changes to the assignment, including answering assessments.

Viewing Completed Assignments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a project has been marked as completed, students can:

- Click on their grade to access grade feedback
- Click on the project name on the left side to view the content (read-only)

Disabling Student Mark as Complete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can disable students' ability to **Mark as Complete** entirely. This eliminates instances of prematurely marking as complete or forgetting to do so, and prevents students from needing to request that their assignment be re-enabled.

To disable this feature, go to the guide **Settings** and disable **Use mark as complete**.

Alternative Methods for Marking Complete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you disable student mark as complete, you can use one of the following methods:

- Once the assignment deadline has been reached, :ref:`mark all students' work as complete <grading>` from the assignment actions area
- Set an :ref:`end of assignment date <assignment-duration>` and specify that student work should be **Marked as Complete** automatically when the date is reached

Penalty Deadlines
-----------------
Another related feature is **Penalty Deadlines** which allow you to specify deadlines, before the final grading deadline, where a percentage deduction of the final grade is made. :ref:`Click here <penalties>` for more information on managing penalty deadlines.