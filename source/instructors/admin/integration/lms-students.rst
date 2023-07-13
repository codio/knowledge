.. meta::
   :description: How your users are identified in Codio

.. _lms-users:

User account creation
=====================

When integrating with an external system, you do not :ref:`add/invite <add-remove-students>` students or teachers to your course. All is handled when the users access an assignment in the system mapped to Codio and the features to invite students into the course are not enabled.

It is also important to understand how Codio maps external system users to Codio users. The following rules should be understood. 

- If students or faculty access Codio via an LMS assignment then Codio will initially use the LMS email address to identify the user and create the Codio account. 

.. Note:: Anonymous students (with no email associated) can access Codio through an LMS. This must be set up within the LMS. 

- In all subsequent access, the userID will be used so in the event the user changes their email address in the LMS, the user will be mapped to the same Codio account.
- If the user is not known to Codio then we will sign up the user as a new Codio user in the background and take the user directly into the Codio content. The LMS user role will be carried over as well.

.. Note:: The users LMS password is not passed to Codio so if the user may wish to log into Codio directly in the future, they will need to create a :ref:`password <password>` for their Codio account (and of course it is always recommended that the same passwords are not used in different applications).

- If the user is known to Codio then Codio will take them directly into the Codio content without any sign-in required. If they are a Codio user but are not a member of your organization then they will be required to complete a verification via email.

- After successful mapping of an user's LMS account to their Codio account, if the user has changed their details such as name or email in their LMS account, Codio will automatically update those details the next time the user accesses Codio from their LMS. Codio will not update the email if another user with the same email already exists.

Teacher Roles
~~~~~~~~~~~~~

Based on the LMS role, if teachers join Codio via the LMS, the following will apply:

+----------------------+-----------------------------------------------------------------------------------------------------+
| LMS Role             | Will be added to Codio with these rights                                                            |
+======================+=====================================================================================================+
| Teaching Assistant   | TEACHER                                                                                             |
+----------------------+-----------------------------------------------------------------------------------------------------+
| Content Developer    | TEACHER                                                                                             |
+----------------------+-----------------------------------------------------------------------------------------------------+
| Mentor               | TEACHER (with :ref:`read only <add-teachers>` access to the course}                                 |
+----------------------+-----------------------------------------------------------------------------------------------------+

If you wish to only allow Mentors to view/manage specific students in the course, see :ref:`Filter Learners For Mentors <filter-learners>`