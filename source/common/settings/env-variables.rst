.. meta::
   :description: Environment Variables allow you to set your own environment variables. 

.. _env-var:

Environment Variables
=====================
Environment Variables allow you to set your own environment variables in your projects. You access the **Environment Variables** from your project by going to **Codio > Preferences > Environment Variables** on the menu bar. Once set they are available in all your projects. The variables are not passed to students assignments in Courses.

- When adding and saving, the project needs to be restarted (**Project > Restart Box**) for the new variables to be available.

Student Assignments
===================

As mentioned above, any variables you set in your projects/assignments are not inherited by students in any course assignments. You can use the variables within :ref:`Secure Scripts <auto-grade-scripts>` but your students will need to manually create the variables themselves in the assignment.

- **Environment Variables** are not supported for :ref:`Pair Programming <group-work>` assignments.



.. Important:: Be aware that if you change the `HOME` variable you are changing the entry point for profile and it could adversely affect the user variables. If you do change this variable, it is your responsibility how environment will behave after that.

