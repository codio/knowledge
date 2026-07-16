.. meta::
   :description: How your users are identified in Codio

.. _lms-users:

Creating User Accounts
======================

When integrating with an external system, you don't need to manually :ref:`add or invite <add-remove-students>` students and teachers to your course. User enrollment is handled automatically when they access assignments that are mapped to Codio, and the manual invitation features are disabled in this configuration.

Codio maps external system users to Codio users using the following rules.

.. important::
   Student accounts are **not** created via LMS integration while an organization is in trial mode. Activate a subscription to enable student enrollments.

First-Time Access
-----------------

- When students or faculty first access Codio via an LMS assignment, Codio uses the LMS email address to identify the user and create the Codio account.

- If the user is not known to Codio, Codio signs up the user as a new Codio user in the background and takes the user directly into the Codio content. The LMS user role is carried over as well.

- If a student joins Codio from an LMS, a new Codio account is created even if the student already has a Codio account using the same email address, because Codio does not yet have a userID + LMS system ID for that account.

.. note::
   Anonymous students (with no email associated) can access Codio through an LMS. This must be set up within the LMS.

.. tip::
   The user's LMS password is not passed to Codio. If the user wishes to log in to Codio directly in the future, they will need to create a password for their Codio account. As always, we recommend not reusing the same password across different applications. If you need to reset your password, you can use your username instead of your email address. Course instructors can assist with password resets; see :ref:`reset passwords <reset-pass>`.

Returning Users
---------------

- After the first access, Codio identifies the user by userID rather than email address. If the user changes their email address in the LMS, they are still mapped to the same Codio account.

- If the user is known to Codio, they are taken directly into the Codio content without any sign-in required. If they are a Codio user but not a member of your organization, they must complete a verification via email.

- If the user has changed details such as their name or email in their LMS account, Codio automatically updates those details the next time the user accesses Codio from their LMS. Codio does not update the email if another user with the same email already exists.


Teacher Roles
~~~~~~~~~~~~~

Based on the LMS role, if teachers join Codio via the LMS, the following will apply:

+----------------------+-----------------------------------------------------------------------------------------------------+
| **LMS Role**         | **Will be added to Codio with these rights**                                                        |
+======================+=====================================================================================================+
| Teaching Assistant   | TEACHER                                                                                             |
+----------------------+-----------------------------------------------------------------------------------------------------+
| Content Developer    | TEACHER                                                                                             |
+----------------------+-----------------------------------------------------------------------------------------------------+
| Mentor               | TEACHER (with :ref:`read only <add-teachers>` access to the course)                                 |
+----------------------+-----------------------------------------------------------------------------------------------------+

- Teachers who are enrolled with the Mentor role are designated as read-only teachers in the organization. 
- If you want Mentors to have access to specific students only, rather than all students in the course, see :ref:`Filter Learners For Mentors <filter-learners>`.


LTI Field to Uniquely Identify Students
---------------------------------------

This is a unique identifier for students found in a custom LTI field. This field is automatically added to the CSV export data files, enabling you to map results manually if necessary. You can adjust this option in the **LTI Integrations** section of your Organization Settings.

