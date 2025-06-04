.. meta::
   :description: How your users are identified in Codio

.. _lms-users:

Creating User Account
======================

When integrating with an external system, you don't need to manually :ref:`add or invite <add-remove-students>` students and teachers to your course. User enrollment is handled automatically when they access assignments that are mapped to Codio, and the manual invitation features are disabled in this configuration.

Understanding how Codio maps external system users to Codio users is important. Here are the key mapping rules:

.. raw:: html

   <div style="float: right; width: 350px; margin: 0 0 10px 20px; padding: 10px; background: #f0f0f0; border: 3px solid #00ece5;">
   <strong>Note:</strong> Anonymous students (with no email associated) can access Codio through an LMS. This must be set up within the LMS. 
   </div>

- If students or faculty access Codio via an LMS assignment then Codio will initially use the LMS email address to identify the user and create the Codio account. 

- In all subsequent access, the userID will be used so in the event the user changes their email address in the LMS, the user will be mapped to the same Codio account.

- If the user is not known to Codio then we will sign up the user as a new Codio user in the background and take the user directly into the Codio content. The LMS user role will be carried over as well.

.. raw:: html

   <div style="float: right; width: 350px; margin: 0 0 10px 20px; padding: 10px; background: #f0f0f0; border: 3px solid #00ece5;">
   <strong>Note:</strong> The users LMS password is not passed to Codio so if the user may wish to log into Codio directly in the future, they will need to create a <a href="#password">password</a> for their Codio account (and of course it is always recommended that the same passwords are not used in different applications).
   </div>

- If the user is known to Codio then Codio will take them directly into the Codio content without any sign-in required. If they are a Codio user but are not a member of your organization then they will be required to complete a verification via email.

- If a student joins Codio from an LMS a new Codio account will be created even if the student already has a Codio account using the same email address where we do not have a userID + LMS system id.  

.. raw:: html

   <div style="float: right; width: 350px; margin: 0 0 10px 20px; padding: 10px; background: #f0f0f0; border: 3px solid #00ece5;">
   <strong>Note:</strong> If you need to reset your password, you can use your username instead of your email address. Alternatively, you can contact your course instructor, who can assist with <a href="https://docs.codio.com/instructors/teaching/resetpassword.html#reset-pass">resetting the password</a>.
   </div>

- After successful mapping of an user's LMS account to their Codio account, if the user has changed their details such as name or email in their LMS account, Codio will automatically update those details the next time the user accesses Codio from their LMS. Codio will not update the email if another user with the same email already exists.

.. raw:: html

   <div  style="margin: 0 0 10px 20px; padding: 10px; background: #f0f0f0; border: 3px solid #00ece5;">
   <strong>Note:</strong> If your organization is in trial mode, student accounts will not be created via LTI integration. Ensure your organization has an active subscription to allow student enrollments.
   </div>


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


LTI Field to Uniquely Identify Students
---------------------------------------

This is a unique identifier for students found in a custom LTI field. This field is automatically added to the CSV export data files, enabling you to map results manually if necessary. You can adjust this option in the **LTI Integrations** section of your Organization Settings.