.. meta::
   :description: Integrating with Canvas


.. _canvas:

System specific instructions
================================

.. toctree::
   :caption: Integrating with external systems
   :hidden:
   
   blackboard
   d2l
   moodle
   google-classroom
   
Canvas 
******

Please be sure to check out the :ref:`Codio LTI App <lti-app>` which allows for an easy way to integrate and to map Codio course assignments to your Canvas system but if that can't be used you can manually integrate following these steps

**In Codio:** 

Enable LTI for Your Course
--------------------------

- Open the course you would like to connect or create a new course.
- Make sure you have at least one published assignment or add a new one. (see :ref:`Add and Remove Course Assignments <add-remove-assignment>`)
- Select the **Admin** tab and click on the blue **Edit Details** button at the bottom.
- Select the **ENABLE LTI** option.  

  .. image:: /img/lti/enable-lti.png
     :alt: enable lti
     

- Click **Save**.

Bring up the LTI Integration Information
----------------------------------------

- Click your user name in the bottom left of your dashboard
- Choose your Organization 
- Click the **LTI Integrations** tab to bring up the following settings.

  .. image:: /img/lti/LTIintegrationinfo.png
     :alt: Org LTI info

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

-  In Codio, go to your course and click on the **Admin** tab near the top.
-  Select **Edit Details** in the bottom of the page.
-  Near the bottom is a switch **Enable LTI** which you should check is enabled.
-  Below this is an empty field **Course LMS URL**. Switch back to Canvas and make sure you are on the Home page of the course. Copy the url in the address bar of your browser to the clipboard and paste it into the above mentioned field in Codio. The url format should end with something like ``/courses/1121212`` although the number will be   different.

This URL ensures that Codio knows how to redirect students back to the correct Canvas course should they attempt to access the course through their dashboard.

Mapping an Assignment to a Canvas Assignment
--------------------------------------------

The final mapping step needs to be taken for each individual assignment within Codio. It maps a Canvas assignment to a Codio assignment.

In Codio
~~~~~~~~

-  On the main course screen, make sure the **Edit** tab is selected.
-  Click the **Add Assignment** button and select **Project Based**.
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

Authentication and account creation
-----------------------------------

To add students/teachers see :ref:`Users account creation <lms-users>`

