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


Codio offers the following grading features:

- **Assign Grade** - Manually review student projects and assign a grade.
- **Grading Moderation** - Other instructors review grades already assigned to monitor grading consistency.
- **Grading Rubric** - A two-dimensional grid that provides grading guidance for manually assessing a coding project.
- **LMS Gradebook Synchronization** - Ensures that when grades are released, the data is automatically passed to any LTI enabled LMS platform such as Moodle, Blackboard and Canvas.

Grading process
---------------
Once students have completed their assignments, they notify the teacher by using the **Education > Mark as Completed** menu in the IDE. Instructors can also mark the assignment as complete or change the status to incomplete. Follow these steps to view and grade the assignments:

1. Open the assignment and view the students that have a green check mark to the left of their name. This indicates that they have marked as complete.  

  .. image:: /img/grading-unit.png
    :alt: Grading Access

2. Optionally, click the **Filter** drop-down and choose one of the following options to filter the list of students based on the status of the assignments:

  .. image:: /img/filter.png
   :alt: Filtering

  - Any Status
  - Started
  - Not Started
  - Has Final Grade
  - No Final Grade
  - Completed
  - Uncompleted
  - Needs Grading

3. Click the **Options** menu and choose **Open the Project** to start grading the student's assignment.

4. Use one of the following methods to assign the grade:

  - In the IDE, click the **Education** menu. You must have a student project open in the IDE.
  - On the Course dashboard, click the **Grade** icon > **Add Grade** and complete the fields. You can also add comments.

  .. image:: /img/grading-assign.png
     :alt: Assign Grade

In the IDE, you can jump to next/previous student's assignment using **Next** or **Previous** button at the top.

If there is another assessment that is ungraded in the assingment, the **Next Ungraded** and **Previous Ungraded** button will appear in the top menu. When clicked, you will be brought to the respective guide page where the ungraded assessment is present.

  .. image:: /img/speedgrading.png
     :alt: Speed Grading buttons

.. _grading-queue:

Grading Queue
-------------

Information on all students that require grading for all assignments in the course can be seen from the course **Queue** area in the **Grading** section.

By default the Grading Queue displays all students' submission that require grading, organized by module/assignment but using the Do Not Group button you can swap to view the queue where the list is sorted by submission time, with the oldest submission at the top but other filters can be set as required.

  .. image:: /img/gradingqueue.png
     :alt: Grading Queue


- Student Name
- Answered
- Points
- Grade
- Time
- Graded


As explained in the previous section, once you open a student's submission then you can use **Next**, **Previous**, **Next Ungraded** and **Previous Ungraded** buttons to move to the next/previous student submission or next/previous ungraded assessment in that specific assignment.

Override Grade
--------------

If the students assignment has already been graded, another teacher in the course can click **Override Grade** to manually change the grade with additional comments.

The **Override Grade** feature can also be used to provide comments at the assignment level. If you do not wish to alter the numeric grade when adding assignment level comments, re-enter it under **Grade**, add your comment and then select **Done.**

  .. image:: /img/class_administration/grading/assignment-comments.png
     :alt: Assignment Comments

Grading rubric is no longer visible to student if teacher overrides grade
-------------------------------------------------------------------------
When a teacher manually grades an assignment using the rubric and then overrides the grades, Grading rubric is no longer visible to students.

This one has the grade overridden and this is what the student dashboard looks like

.. image:: /img/Overridengarde.png
     :alt: Overriden-grade

This is the student's dashboard view if the grade has not been overridden


.. image:: /img/No-overrindengrade.png
     :alt: No-Overriden-grade

Removing Penalties
------------------

If required you can remove penalties currently applied to the students grade.

   .. image:: /img/latepenalty.png
      :alt: Remove Penalties


Anonymous grading
-----------------
If required, anonymous grading can be set for the course so students cannot see the names of the teachers who graded their work. The teacher names are hidden in the shared feedback, project, and dashboard. 

To enable anonymous grading, follow these steps:

1. Open the course and click the **Grading/Basic Settings** tab.
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