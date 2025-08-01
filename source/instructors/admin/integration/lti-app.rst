.. meta::
   :description: LTI App

.. _lti-app:

LTI App (LTI 1.1 Only)
=======================

The **Codio LTI App** method allows for an easy way to integrate and to map Codio course assignments to your LMS system. The LTI App is only available for LTI 1.1 only. 

**Please note the steps below are for implementation in Canvas.** For details on other supported systems see https://www.eduappcenter.com/tutorials.

.. Note:: To use the LTI App, your email address in Codio and your LMS system must match exactly. 

   The LTI App is only for the US version of Codio. It will not work with Codio UK (codio.co.uk).

In Codio
~~~~~~~~


+----------------------------------------------------------------------+------------------------------------------------------------------------------------------+
|                                                                      |                                                                                          |
| **1.** Click your username in the top-right corner, then select      | .. figure:: /img/lti/LTI1.1IntegrationCodio.png                                          |
| **Organization** from the menu. In the organization area, click the  |     :alt: LTI Fields                                                                     |
| name of your organization.                                           |                                                                                          |
|                                                                      |                                                                                          |
| **2.** Select the **LTI Integrations** tab.                          |                                                                                          |
|                                                                      |                                                                                          |
| **3.** Scroll down to the **LTI Integration 1.0** section. You should|                                                                                          |
| see the following fields. Remain on this screen for the time         |                                                                                          |
| being.                                                               |                                                                                          |
+----------------------------------------------------------------------+------------------------------------------------------------------------------------------+



In Canvas
~~~~~~~~~

**The Canvas user who carries out these steps must be a system administrator.**


+-----------------------------------------------------------------------+----------------------------------------------------------------------------+
|                                                                       |                                                                            |
| **4.** Create a new Course in your LMS system. We suggest you create a| .. figure:: /img/lti/appcenter.png                                         |
| test course called **Codio Test Course** before you do it with a      |     :alt: appcenter                                                        |
| production course.                                                    |                                                                            |
|                                                                       |                                                                            |
| **5.** Select the Course.                                             |                                                                            |
|                                                                       |                                                                            |
| **6.** Click on **Settings** in the left set of options.              |                                                                            |
|                                                                       |                                                                            |
| **7.** In the top links, select **Apps**.                             |                                                                            |
|                                                                       |                                                                            |
| **8.** Click the large button **View App Configurations**.            |                                                                            |
|                                                                       |                                                                            |
| **9.** Click on the **View App Center** button.                       |                                                                            | 
|                                                                       |                                                                            |
| **10.** Navigate (or filter) to find the **Codio** app, select and    |                                                                            |
| ** Add App**                                                          |                                                                            |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------+


In Codio and Canvas
~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------+--------------------------------------------------------------------------------------------+
|  **11.** We will now copy the following global          | .. figure:: /img/lti/appsetup.png                                                          |
|  integration fields from Codio to Canvas.               |    :alt: appconfigured                                                                     |
|                                                         |                                                                                            |
|     -  LTI Consumer -> Consumer Key                     |                                                                                            |
|     -  LTI Secret -> Shared Secret                      |                                                                                            |
|                                                         |                                                                                            |
|  **12.** Select the **Add App** button to confirm.      |                                                                                            |
|  You should then see a screen similar to the image on   |                                                                                            |
|  the right:                                             |                                                                                            |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------+



Course LMS URL
--------------

The **Course LMS URL** is used to map an LMS course to a Codio course. It ensures that Codio knows how to redirect students back to the correct course should they attempt to access the course through the Codio dashboard. If not entered and students log into Codio to try to start new assignments there will be no link for them to click to be passed to your LMS Course. The LMS user who carries out these steps does not need to be a system administrator but must have suitable privileges to edit courses and assignments.

**Video - Course LMS URL:**

.. raw:: html

   <script src="https://fast.wistia.com/embed/medias/q17567v2nr.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_q17567v2nr videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/q17567v2nr/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>





+--------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| **13.** In Codio, navigate to your course of choice.                     | .. figure:: /img/lti/lti-class-url.png                                           |
|                                                                          |    :alt: lti-class-url                                                           |                        
|                                                                          |                                                                                  |
| **14.** Go to the **LTI/LMS** section on the left under Admin.           |                                                                                  |
|                                                                          |                                                                                  |
| **15.** In **LTI/LMS Settings** toggle **Enable LTI** on.                |                                                                                  |
|                                                                          |                                                                                  |
| **16.** Use **Course LMS URL** to define where students return in the LMS|                                                                                  |
| after leaving Codio. Paste the desired page URL (e.g., the LMS course    |                                                                                  |
| home page) here.                                                         |                                                                                  |
+--------------------------------------------------------------------------+----------------------------------------------------------------------------------+



Hiding "not started" Assignments in Students Dashboard
*******************************************************

Toggling **Hide Not Started Assignments** to "on" will suppress the display of assignments that haven’t been started in the student dashboard. Students will need to log into their LMS system to start new assignments. Students may not realize they need to go back to their LMS system to start a new assignment when they don’t see them in Codio. If you don’t hide assignments that haven’t been started you can use the **Course LMS URL** which will provide them with a link back to their LMS system to start the assignment.


.. figure:: /img/lti/lms_hide.png
   :alt: Hide not started assignments

.. _filter-learners:

Filter Learners for Mentors
****************************

Enabling **Filter Learners for Mentors** to "on" will allow you to only show Mentor/Observers specific students that you wish them to see/manage in the Codio course.

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


Open Student Assignments Directly from LMS
*******************************************

The **Open student assignments directly from LMS** feature allows teachers to access their students' assignments directly from their Learning Management System (LMS) without needing to navigate to the teacher dashboard. This streamlines the grading and feedback process, making it more efficient.

LTI 1.1 
"""""""

**Custom parameters**


+-----------------------------------+---------------------------------------------------------------+--------------------------------------------------------+
| Parameter                         | Description                                                   | Example                                                |
+===================================+===============================================================+========================================================+
| custom_actual_user_id             | custom_actual_user_id= lms user identification                |                                                        |           
|                                   |                                                               | custom_actual_user_id=123                              |
|                                   | This is equivalent of user_id when the request is             |                                                        |  
|                                   | executed without changing thecurrent user.                    |                                                        |
+-----------------------------------+---------------------------------------------------------------+--------------------------------------------------------+
| custom_actual_user_email          | custom_actual_user_email= actual user email                   |                                                        |
|                                   |                                                               |                                                        |
|                                   | This will be used for registration if                         | custom_actual_user_email= lms-admin@email.com          |
|                                   | custom_actual_user_id is not matched to existing user.        |                                                        |
+-----------------------------------+---------------------------------------------------------------+--------------------------------------------------------+
| custom_actual_user_role           | custom_actual_user_role= actual user role                     |                                                        |             
|                                   |                                                               |                                                        |
|                                   | This should not be Student-like role.                         | custom_actual_user_role=Instructor                     |
+-----------------------------------+---------------------------------------------------------------+--------------------------------------------------------+
| custom_actual_user_name_family    | custom_actual_user_name_family= actual user family name       | custom_actual_user_name_family=Family                  |
+-----------------------------------+---------------------------------------------------------------+--------------------------------------------------------+
| custom_actual_user_name_given     | custom_actual_user_name_given= actual user given name         | custom_actual_user_name_given=Name                     |
+-----------------------------------+---------------------------------------------------------------+--------------------------------------------------------+
| custom_actual_user_name_full      | custom_actual_user_name_full= actual user full name           | custom_actual_user_name_full= Name Family              |
|                                   |                                                               |                                                        |
|                                   | This could be omitted if custom_actual_user_name_family and   |                                                        |
|                                   | custom_actual_user_name_given passed.                         |                                                        |
+-----------------------------------+---------------------------------------------------------------+--------------------------------------------------------+



LTI 1.3
"""""""

**Custom parameters claim object**
specified in https://purl.imsglobal.org/spec/lti/claim/custom

**actual_user**


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
|                  | This will be used for registration if                         | "actual_user_email": "lms-admin@email.com"       |
|                  | custom_actual_user_id is not matched to an existed user.      |                                                  |
+------------------+---------------------------------------------------------------+--------------------------------------------------+
| role             | role= actual user role                                        |                                                  |
|                  |                                                               |                                                  |
|                  | This should not be Student-like role.                         | "actual_user_role": "Instructor"                 |
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

.. important:: Canvas/Moodle/Blackboard do not support this feature.


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