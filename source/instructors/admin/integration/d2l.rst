.. meta::
   :description: Connecting your Codio course with your D2L Learning Management System.


.. _d2l:

D2L
===

In Codio: 
---------

1. Open the course you would like to connect or create a new course.
2. Make sure you have at least one published assignment or add a new one. (see :ref:`Add and Remove Course Assignments <add-remove-assignment>`)
3. Select the **Admin** tab and click on the blue **Edit Details** button at the bottom.
4. Select the **ENABLE LTI** option.  

  .. image:: /img/lti/enable-lti.png
     :alt: enable lti
     

5. Click **Save**.
6. Click your user name in the bottom left of your dashboard
7. Choose your Organization 
8. Click the **LTI Integrations** tab to bring up the following settings.

  .. image:: /img/lti/LTIintegrationinfo.png
     :alt: Org LTI info

In D2L:
-------

1. Create an external link and name it Codio
2. Type the information in (1) in URL field.
3. Copy the **Consumer Key** information from Codio into (2).
4. Copy the **Secret Key** information from Codio into (3).

  .. image:: /img/lti/D2Lscreenone.png
     :alt: D2L view

5. Fill in the Security fields as depicted in (4) below.

  .. image:: /img/lti/DL2Screen2.png
     :alt: D2L view 2
     
6. Click **Save**. You will use this tool to access your Codio assignments when you set them up in D2L.


Single sign-in and account creation
-----------------------------------

Codio maps D2L users to Codio users by using the D2L email address to identify the user and create the Codio account. In all subsequent access, the D2L userID will be used. In the event the user changes their email address in D2L, the user will be mapped to the same Codio account.

-  If the user does not have a Codio account, a new user account will be created in the background and the user will enter directly into the Codio content. The D2L user role is carried into Codio.
-  If the user already has an account they will enter into the Codio content without any sign-in required. If they already have a Codio account, but are not a member of the organization, they will be required to complete an email verification.


Teacher Roles
-------------

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
