.. meta::
   :description: Grading features available for assignments.
   
.. _grading:


Grading
=======

.. toctree::
   :caption: Grading
   :hidden:
   
   grade-freetext
   nbgrader
   release-grades
   reruncodetests


Codio offers the following grading features:

- **Assign Grade** - Manually review student projects and assign a grade.
- **Grading Moderation** - Other instructors review grades already assigned to monitor grading consistency.
- **Grading Rubric** - A two-dimensional grid that provides grading guidance for manually assessing a coding project.
- **LMS Gradebook Synchronization** - Ensures that when grades are released, the data is automatically passed to any LTI enabled LMS platform such as Moodle, Blackboard and Canvas.

Grading process
---------------
Once students have completed their assignments, they notify the teacher by using the **Education > Mark as Completed** menu in the IDE. Instructors can also mark the assignment as complete or change the status to incomplete. Follow these steps to view and grade the assignments:

1. Open the assignment and view the students who have a check mark to the left of their name in the **Completed** column. This indicates that they have marked as complete.  

  .. image:: /img/grading-unit.png
    :alt: Grading Access

2. You can click the status drop-down if you want to filter the list of students based on the status of their assignments. For example, **Started**, **Completed** or **Needs Grading**.

3. Click the three vertical dots in the **Actions** column and choose **Open student's project** to start grading the student's assignment.

4. Use one of the following methods to assign the grade:

- If you have opened the student's project, click the **Grading** button. 
- On the Course dashboard, click the item in the **Grade** column for that student and complete the fields. You can also add comments.

.. image:: /img/grading-assign.png
   :alt: Assign Grade

From inside a student's project, you can jump to next/previous student's assignment using **Next** or **Previous** button at the top.

If there is another assessment that is ungraded in the assignment, the **Next Ungraded** and **Previous Ungraded** buttons will appear in the top menu. When clicked, you will be brought to the respective guide page containing the ungraded assessment.

  .. image:: /img/speedgrading.png
     :alt: Speed Grading buttons

.. _grading-queue:

Grading Queue
-------------

Information on all students that require grading for all assignments in the course can be seen from the **Grading>Queue** item in your course.

By default the Grading Queue displays all students' submission that require grading, organized by module and assignment. You can use the **Do Not Group** button to sort the list by submission time, with the oldest submission at the top. Other filters can be set as required.


As explained in the previous section, once you open a student's submission then you can use **Next**, **Previous**, **Next Ungraded** and **Previous Ungraded** buttons to move to the next/previous student submission or next/previous ungraded assessment in that specific assignment.

Override Grade
--------------

If the students assignment has already been graded, another teacher in the course can click **Override Grade** to manually change the grade with additional comments.

The **Override Grade** feature can also be used to provide comments at the assignment level. If you do not wish to alter the numeric grade when adding assignment level comments, re-enter it under **Grade**, add your comment and then select **Done.**

  .. image:: /img/class_administration/grading/assignment-comments.png
     :alt: Assignment Comments

.. This is a comment
.. I took this whole bit about rubric not showing up with overriden grades because rubrics aren't showing up in any case and the screen shots were bad and had my name and a customer's name and I did not add them.

Removing Penalties
------------------

In the **Grade Adjustments** section of the grading screen you can remove penalties by toggling the **Do not apply penalty** option.

   .. image:: /img/latepenalty.png
      :alt: Remove Penalties


Anonymous grading
-----------------
Anonymous grading can be set for the course and then students cannot see the names of the teachers who graded their work. The teacher names are hidden in the shared feedback, project, and dashboard. 

To enable anonymous grading, follow these steps:

1. Open the course and select the **Grading>Basic Settings** tab.
2. Toggle **Anonymous Grading** to enable it and then click **Save Changes**.

Code Commenting
---------------
You can add comments to the code so that students can see them when they open the file. To comment on the code, follow these steps:

1. Open the project and then open the file. 
2. Hover over the left-hand side of the gutter bar and click + to open the comment window.
3. Enter your comments. You can select multiple lines of code, edit, and delete lines of code.

   .. image:: /img/commentcode.png
      :alt: Commenting

Students can then view the comments from the **Education > Code Comments** menu. They can also open the file from the comments.

.. image:: /img/guides/codecommentguides.png
   :alt: Code Comments

.. _autograde-failure-notification:

Autograde Failure Notification
------------------------------

You can set autograde failure notification, so whenever the auto-grade script fails for a student submission then you will receive email notification for that.

You can set all teachers in the course to receive notification or you can customize this to set only specific teachers to receive the notification.

To enable this feature:

1. Open the course and navigate to **Grading > Basic Settings**.
2. From **Autograde Failure Notification** setting, you can choose who should receive the notifications..
3. If you want to send notifications to all teachers in the course then select **Teachers** option from the dropdown but if you want to send notifications to only specific teachers then choose **Customize** option from dropdown and specify their email addressess (one email per line) in the **Notification Emails** area.
4. Click **Save Changes**.