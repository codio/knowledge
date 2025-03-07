.. meta::
   :description: LTI App

.. _lti-app:

LTI App
=======

.. Note:: To use the LTI App, your email address in Codio and your LMS system must match exactly. 

   The LTI App is only for the US version of Codio. It will not work with Codio UK (codio.co.uk).

The **Codio LTI App** method allows for an easy way to integrate and to map Codio course assignments to your LMS system. 

**Please note the steps below are for implementation in Canvas.** For details on other supported systems see https://www.eduappcenter.com/tutorials.

**Video - Connect Codio to Canvas using the LTI App:**

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/4lqbay97le.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_4lqbay97le seo=false videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/4lqbay97le/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

In Codio
~~~~~~~~

1.  Go to your organization account settings by clicking on your user name in the bottom left of your dashboard and then selecting your organization within **Organizations**.
2.  Select the **LTI Integrations** tab.
3.  Scroll down to the **LTI Integration 1.0** section. You should see the following fields. Remain on this screen for the time being.

.. figure:: /img/lti/lti-org-fields.png
   :alt: LTI Fields

In Canvas
~~~~~~~~~

The Canvas user who carries out these steps must be a system administrator.

4.  Create a new Course in your LMS system. We suggest you create a test course called **Codio Test Course** before you do it with a production course.
5.  Select the Course.
6.  Click on **Settings** in the left set of options.
7.  In the top links, select **Apps**.
8.  Click the large button **View App Configurations**.
9.  Click on the **View App Center** button.

.. figure:: /img/lti/appcenter.png
   :alt: appcenter

10.  Navigate (or filter) to find the **Codio** app, select and **+ Add App**

In Codio and Canvas
~~~~~~~~~~~~~~~~~~~

11. We will now copy the following global integration fields from Codio to Canvas.

-  LTI Consumer -> Consumer Key
-  LTI Secret -> Shared Secret

12. and select the **Add App** button to confirm. You should then have something similar to this:

.. figure:: /img/lti/appsetup.png
   :alt: appconfigured

Course LMS URL
--------------

The **Course LMS URL** is used to map an LMS course to a Codio course. It ensures that Codio knows how to redirect students back to the correct course should they attempt to access the course through the Codio dashboard. If not entered and students log into Codio to try to start new assignments there will be no link for them to click to be passed to your LMS Course. The LMS user who carries out these steps does not need to be a system administrator but must have suitable privileges to edit courses and assignments.

**Video - Course LMS URL:**

.. raw:: html

   <script src="https://fast.wistia.com/embed/medias/q17567v2nr.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_q17567v2nr videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/q17567v2nr/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

13.  In Codio, go to the **LTI/LMS** tab near the top.
14.  Go to the **LTI/LMS Settings** section.
15.  Select **Enable LTI** to enable.
16.  Below this is an empty field **Course LMS URL**. Switch back to your LMS and make sure you are on the Home page of the course. Copy the url in the address bar of your browser to the clipboard and paste it into the above mentioned field in Codio.

.. figure:: /img/lti/lti-class-url.png
   :alt: lti-class-url

.. _hide-assignments:

Hiding not started assignments in students dashboard
****************************************************

Toggling **Hide Not Started Assignments** to on will suppress the display of assignments that haven’t been started in the student dashboard. Students will need to log into their LMS system to start new assignments. Students may not realize they need to go back to their LMS system to start a new assignment when they don’t see them in Codio. If you don’t hide assignments that haven’t been started you can use the **Course LMS URL** which will provide them with a link back to their LMS system to start the assignment.


.. figure:: /img/lti/lms_hide.png
   :alt: Hide not started assignments

.. _filter-learners:

Filter learners for mentors
***************************

Enabling **Filter Learners for Mentors** to on will allow you to only show Mentor/Observers specific students that you wish them to see/manage in the Codio course.

To set this up, edit your LTI app as set up above or send as a custom parameter adding `codio_custom_mentor_for` as a custom field entering as the parameter either the students email addresses or their LMS user IDs.   To enter multiple students separate with comma (',')

Example:

.. code:: ini

   codio_custom_mentor_for="student1@email.com,student2@email.com"



.. figure:: /img/lti/filter_learners.png
   :alt: Filter learners for mentors

If you don't enable **Filter Learners for Mentors**, then mentors can see all the students in the course and access all students' work, even those for whom they are not a mentor.


.. _Destination_Page:

Set Destination Page
********************

The **Set Destination Page** feature allows you to define which page within an assignment should open by default when a student launches it. This ensures students start on the most relevant content immediately.

To configure this, navigate to **Settings** > **Apps** > **Edit App**, then add a custom field using either custom_codio_page or codio_page, specifying the exact page name you want students to land on. Finally, click the **Submit** button to save your changes.

Example:

.. code:: ini

    custom_codio_page=<page name> or codio_page=<page name>


.. figure:: /img/lti/DestinationPage.png
   :alt: Set Destination Page

This ensures that students are directed to the specified page upon opening the assignment instead of the default starting location.

Mapping an Assignment to a Canvas Assignment
============================================

The final mapping step needs to be taken for each individual assignment within Codio. It maps a Canvas assignment to a Codio assignment.

In Canvas
~~~~~~~~~

17.  Make sure you are in the Courses area.
18.  Click on the **Assignments** link in the left hand side.
19.  Provide a name for the Assignment.
20.  Set the points for the Assignment. When the grades get passed back later, the Codio percentage score will be scaled to the points value you specify here.
21.  Scroll down and look for the **Submission Type** field.

.. figure:: /img/lti/canvas-submission-type.png
   :alt: Canvas Submission

22.  You should now click on the dropdown list and select **External Tool**.
23.  Specify the assignment using one of the two options: 

    - **Add by Resource Selection Preview (recommended)**
        
        - Click the **Find** button.
        - Click the Codio tool.
        - Select the assignment you want to map to your course in Canvas. 
        
    - **Add by LTI Integration URL**
    
        - Return to Codio and navigate to the course. Ensure you are in **Overview** mode. 
        - To the right of the assignment, click the icon with 3 blue dots and select **LTI Integration URL**. You should copy the LTI integration url to the clipboard by clicking on the field (it will auto copy).
        - Paste the **LTI Integration URL** in the URL field under **Enter or find an External Tool URL.**

24.  Select **Load This Tool In a New Tab**.
25.  Click the **Save and Publish** button.
26.  Make sure the Canvas course is published.