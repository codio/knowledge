.. meta::
   :description: Integrating with D2L


.. _d2l:

D2L
===

In Codio: 
---------

- Create a Course.
- Add a Module and an assignment to the course and publish the assignment.
- Select the Admin tab and click on the blue Edit Details button at the bottom.
- Select the ENABLE LTI option.  

  .. image:: /img/lti/enable-lti.png
     :alt: enable lti
     

- Click Save.
- Click on your user name in the bottom left of your dashboard
- Select your Organization 
- Click on the LTI Integrations tab to bring up the following settings.

  .. image:: /img/lti/LTIintegrationinfo.png
     :alt: Org LTI info

In D2L:
-------

- Create an external link and name it Codio
- Type the information in (1) in URL field.
- Copy the Consumer Key information from Codio into (2).
- Copy the Secret Key information from Codio into (3).

  .. image:: /img/lti/D2Lscreenone.png
     :alt: D2L view

- Fill in the Security fields as depicted in (4) below.

  .. image:: /img/lti/DL2Screen2.png
     :alt: D2L view 2
     
- Click Save.
- You can use this tool to access your Codio assignments when you set them up in D2L.

Adding faculty and students
---------------------------

The final step is to add students to your course. This is done from the People tab. We recommend that you add the same test students to D2L that you have in Codio. The only field of data that needs to match is the email address. So, look up the Codio test student email addresses and add them to D2L in the student role.

When you add a student in D2L you will need to confirm from the email you are sent.

**Important** : make sure you log out of your teacher based D2L session before doing this.

Next, you should login to D2L as a test student and start the assignment. Please read on to see what happens next, which is dependent.

**Important** : when you access Codio from D2L, this user will become the dominant Codio user in the browser. This means that if you have a Codio session open (say you are logged in as faculty) and you start an assignment from D2L as a student, the old Codio session will be invalidated. To get around this, you should think about running your teacher account in a separate browser type or in an incognito window. Just be aware of this when testing.

Single sign-in and account creation
-----------------------------------

It is important to understand how Codio maps D2L users to Codio users. The following rules should be understood. If students or faculty access Codio via a D2L assignment then Codio will initially use the D2L email address to identify the user and create the Codio account. In all subsequent access, the D2L userID will be used so in the event the user changes their email address in D2L, the user will be mapped to the same Codio account.

-  If the user is not known to Codio then we will sign up the user as a new Codio user in the background and take the user directly into the Codio content. The D2L user role will be carried over as well.
-  If the user is known to Codio then Codio will take them directly into the Codio content without any sign-in required. If they are a Codio user but are not a member of your organization then they will be required to complete a verification via email.


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

Generating scores
-----------------

You should now generate some scores to pass back to Codio. You can do either of the following.

-  If your assigned Codio assignment has some autograded assessments(simple MCQs will do fine) then access the Codio content as students as answer the questions to generate a score
-  You can also manually grade the student assignment in Codio. You will need to enter a percentage value here as the LMS/LTI interface requires this.

Generating scores
-----------------

You should now generate some scores to pass back to Codio. You can do
either of the following.

-  If your assigned Codio assignment has some autograded assessments (simple MCQs will do fine) then access the Codio content as students as answer the questions to generate a score
-  You can also manually grade the student assignment in Codio. You will need to enter a percentage value here as the LMS/LTI interface requires this.

Releasing grades
----------------

By default, grades in Codio are neither passed back to the student nor to D2L until they are

-  Marked as complete by either the student or the teacher and
-  the **Release Grades** switch is enabled (or if you have set the course to automatically release grades when completed)

Once **Release Grades** is enabled, all completed student assignments are automatically sent through.

.. figure:: /img/lti/release-complete.png
   :alt: Release Grades

There are various ways to mark a student's work as complete

-  The student can do this from either the Course dashboard or from the **Education->Mark as Complete** menu in the assignment itself.
-  The teacher can do the same in the assignment when :ref:`viewing students code <viewing-student-work>`
-  The teacher can do the same from the assignment in the Course dashboard by hovering in the left side of a student entry and then setting the completed switch.
-  The teacher can mark all student assignments as completed in one action. This is done by

   -  selecting the assignment in the Course
   -  pressing the **Action** button
   -  pressing the **Mark all as Completed** button

**Important** : If you are running a staging or test D2L environment then you must have a valid SSL certificate on your D2L server otherwise grades will not be pass back to D2L successfully.
     