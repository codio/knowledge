.. meta::
   :description: Allowing Teachers to set prerequisite assignments before allowing students to access the assignment


.. _prerequisite:

Prerequisite Assignments
========================

The **Prerequisite Assignment** is used to set requirements based on other published assignments in the course so that students cannot start the assignment until they have been met. 

The prerequisite states that can be set are:

- Started
- Completed
- Passed (with a minimum grade)

Multiple assignments can be included if necessary but they all will have the same prerequisite state.

  .. image:: /img/prerequisite.png
     :alt: Prerequisite Rules

When enabled, students can start the assignment if the requirements are met. If not, they will receive a message advising them of the prerequisite requirements.

  .. image:: /img/student-prerequisite.png
     :alt: Student Warning

Copy workspace from Prerequisite Assignment
-------------------------------------------

The **Copy Workspace From** setting allows you to copy content from one assignment to a subsequent assignment.

.. Important:: This will only pull the workspace in upon the first opening of the assignment (when it is created for the student) -- there is no update mechanism. Because of this, we highly encourage you to setup the prerequisite assignment state to **Completed**. 

When the assignment is created by the student, the workspace files/folders (excluding **.guides**, **.git** folder, any node modules and any **.codio**, **.codio-menu** or **.settings** files) of the assignment selected in the dropdown will be copied into the prerequisite assignment's workspace and will be included in the new assignment. 

If a file of the same name exists in both assignnments, the most recent changes to the initial assignment will be updated in the subsequent assignment. This will apply to changes that students made.


