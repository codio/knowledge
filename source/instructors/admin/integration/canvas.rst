.. meta::
   :description: Integrating with Canvas


.. _canvas:

Canvas 
======
 Please be sure to check out the :ref:`Codio LTI App <lti-app>` which allows for an easy way to integrate and to map Codio course assignments to your Canvas system but if that can't be used you can manually integrate following these steps

Preparation
-----------

The following steps need to be taken only one time per course.

In Codio
~~~~~~~~

-  Go to your organization account settings by clicking on your user name in the bottom left of your dashboard and then selecting your organization within **My Organizations**.
-  Select the **LTI Integrations** tab.
-  Scroll down to the **LTI Integration 1.0** section. You should see the following fields. Remain on this screen for the time being.

.. figure:: /img/lti/lti-org-fields.png
   :alt: LTI Fields

In Canvas, adding Codio as an App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Canvas user who carries out these steps must be a system administrator.

-  Create a new Course in Canvas. We suggest you create a test course called **Codio Canvas** before you do it with a production course.
-  Select the Course.
-  Click on **Settings** in the left set of options.
-  In the top links, select **Apps**.
-  Click the large button **View App Configurations**.
-  Click on the blue **+ App** button.

In Codio and Canvas
~~~~~~~~~~~~~~~~~~~

We will now copy the following global integration fields from Codio to Canvas.

-  LTI Consumer -> Consumer Key
-  LTI Secret -> Shared Secret
-  LTI URL -> Launch URL

In Canvas you should then use one of the following steps

Manual Entry
~~~~~~~~~~~~

-  Enter a suitable name (Codio Canvas LTI) in the **Name** field.
-  Enter **apollo.codio.com** into the **Domain** field.
-  In the **Privacy** field, select **Public**
-  Paste in the 3 Codio fields to the appropriate fields

You should end up with something like this.

.. figure:: /img/lti/canvas-global.png
   :alt: Canvas Global

By URL
~~~~~~

-  Enter a suitable name (Codio Canvas LTI) in the **Name** field.
-  In Codio select the Copy Consumer button to copy in to the Consumer Key field.
-  select the Copy Secret Key to copy in to the Shared Secret field.
-  select the Copy XML URL to copy in the to the Config URL field.
-  and Submit

Paste XML
~~~~~~~~~

-  Enter a suitable name (Codio Canvas LTI) in the **Name** field.
-  In Codio select the Copy Consumer button to copy in to the Consumer Key field.
-  select the Copy Secret Key to copy in to the Shared Secret field.
-  click on the ``XML Configuration`` link to open the XML and then copy in the to the XML Configuration field.
-  and Submit

Codio course setup
~~~~~~~~~~~~~~~~~~

You need to perform the following actions one time only for a course. The Canvas user who carries out these steps does not need to be a system administrator but must have suitable privileges to edit courses and assignments.

-  In Codio, create a new course and name it **Canvas Demo**.
-  Click on the **Admin** tab near the top.
-  Select **Edit Details** in the bottom of the page.
-  Near the bottom is a switch **Enable LTI** which you should enable.
-  Below this is an empty field **Course LMS URL**. Switch back to Canvas and make sure you are on the Home page of the course. Copy the url in the address bar of your browser to the clipboard and paste it into the above mentioned field in Codio. The url format should end with something like ``/courses/1121212`` although the number will be   different.

This URL ensures that Codio knows how to redirect students back to the correct Canvas course should they attempt to access the course through their dashboard.

Mapping an Assignment to a Canvas Assignment
--------------------------------------------

The final mapping step needs to be taken for each individual assignment within Codio. It maps a Canvas assignment to a Codio assignment.

In Codio
~~~~~~~~

-  On the main course screen, make sure the **Assignments** tab is selected.
-  Click the **+** button and select **Add Project**.
-  Select a project that has some autograded assessments. The **My First Project** that you created earlier in the Onboarding Guide has some auto-graded assessments. You can also assign another project but you will need to manually grade the assignment so there are some scores to pass back to the Canvas gradebook.
-  Once the assignment has been added to the course, you should click the icon with 3 blue dots and select **LTI Integration URL**.
-  You should copy the LTI integration url to the clipboard by clicking on the field (it will auto copy).

.. figure:: /img/lti/LMS-Unit-URL.png
   :alt: Unit URL

In Canvas
~~~~~~~~~

We now return to Canvas complete the mapping.

-  Make sure you are in the Courses area.
-  Click on the **Assignments** link in the left hand side.
-  Provide a name for the Assignment.
-  Set the points for the Assignment. When the grades get passed back later, the Codio percentage score will be scaled to the points value you specify here.
-  Scroll down and look for the **Submission Type** field.

.. figure:: /img/lti/canvas-submission-type.png
   :alt: Canvas Submission

-  You should now click on the dropdown list and select **External Tool**.
-  In the new set of fields that appear, paste the Codio **LTI Integration URL** field into the url field in Canvas.
-  Select **Load This Tool In a New Tab**.
-  Click the **Save and Publish** button.
-  Make sure the Canvas course is published.

Adding faculty and students
---------------------------

The final step is to add students to your course. This is done from the People tab. We recommend that you add the same test students to Canvas that you have in Codio. The only field of data that needs to match is the email address. So, look up the Codio test student email addresses and add them to Canvas in the student role.

When you add a student in Canvas you will need to confirm from the email you are sent.

**Important** : make sure you log out of your teacher based Canvas session before doing this.

Next, you should login to Canvas as a test student and start the assignment. Please read on to see what happens next, which is dependent.

**Important** : when you access Codio from Canvas, this user will become the dominant Codio user in the browser. This means that if you have a Codio session open (say you are logged in as faculty) and you start an assignment from Canvas as a student, the old Codio session will be invalidated. To get around this, you should think about running your teacher account in a separate browser type or in an incognito window. Just be aware of this when testing.

Single sign-in and account creation
-----------------------------------

It is important to understand how Codio maps Canvas users to Codio users. The following rules should be understood. If students or faculty access Codio via a Canvas assignment then Codio will initially use the Canvas email address to identify the user and create the Codio account. In all subsequent access, the Canvas userID will be used so in the event the user changes their email address in Canvas, the user will be mapped to the same Codio account.

-  If the user is not known to Codio then we will sign up the user as a new Codio user in the background and take the user directly into the Codio content. The Canvas user role will be carried over as well.
-  If the user is known to Codio then Codio will take them directly into the Codio content without any sign-in required. If they are a Codio user but are not a member of your organization then they will be required to complete a verification via email.


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

Generating scores
-----------------

You should now generate some scores to pass back to Codio. You can do either of the following.

-  If your assigned Codio assignment has some autograded assessments(simple MCQs will do fine) then access the Codio content as students as answer the questions to generate a score
-  You can also manually grade the student assignment in Codio. You will need to enter a percentage value here as the LMS/LTI interface requires this.

Releasing grades
----------------

By default, grades in Codio are neither passed back to the student nor to Canvas until they are

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