.. meta::
   :description: Open Student Assignments Directly from LMS

.. _open-student-assignments-lms:

Open Student Assignments Directly from LMS
==========================================


The **Open student assignments directly from LMS** feature allows teachers to access their students' assignments directly from their Learning Management System (LMS) without needing to navigate to the teacher dashboard. This streamlines the grading and feedback process, making it more efficient.


 .. important::
    Not all LMS systems support this direct integration feature. Please verify that your specific LMS platform is compatible with this functionality before relying on it for your workflow. If your LMS doesn't support direct assignment access, you'll need to use the traditional method of accessing assignments through the teacher dashboard.

LTI 1.3
"""""""


**Custom parameters**






+------------------+---------------------------------------------------------------+--------------------------------------------------+
| Parameter        | Description                                                   | Example                                          |
+==================+===============================================================+==================================================+
| id               | id= lms user identification                                   | "actual_user_id": "123"                          |
|                  |                                                               |                                                  |
|                  | This is equivalent of sub when the request is executed        |                                                  |
|                  | without changing the current user.                            |                                                  |
+------------------+---------------------------------------------------------------+--------------------------------------------------+
| email            | email= actual user email                                      |                                                  |
|                  |                                                               |                                                  |
|                  | Used for registration if ``custom_actual_user_id``            | "actual_user_email": "lms-admin@email.com"       |
|                  | does not match an existing user.                              |                                                  |
+------------------+---------------------------------------------------------------+--------------------------------------------------+
| role             | role= actual user role                                        |                                                  |
|                  |                                                               |                                                  |
|                  | This role must not be student-like.                           | "actual_user_role": "Instructor"                 |
+------------------+---------------------------------------------------------------+--------------------------------------------------+
| given_name       | given_name= actual user given name                            | "actual_user_given_name": "Name"                 |
+------------------+---------------------------------------------------------------+--------------------------------------------------+
| family_name      | family_name= actual user family name                          | "actual_user_family_name": "Family"              |
+------------------+---------------------------------------------------------------+--------------------------------------------------+
| full_name        | full_name= actual user full name                              |                                                  |
|                  |                                                               |                                                  |
|                  | This could be omitted if                                      | "actual_user_full_name": "Name Family"           |
|                  | custom_actual_user_name_family and                            |                                                  |
|                  | custom_actual_user_name_given passed.                         |                                                  |
+------------------+---------------------------------------------------------------+--------------------------------------------------+


.. Note:: The parameters should be set by LMS dynamically based on current user, not statically. If you need assistance contact help@codio.com


