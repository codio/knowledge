.. meta::
   :description: Integrating with Canvas

.. _canvas:

Canvas
======

Integrating with Canvas using LTI App
-------------------------------------
**This method is recommended.**

The **Codio LTI App** method allows for an easy way to integrate and to map Codio course assignments to Canvas. Access the directions at :ref:`LTI App <lti-app>` page. If you are not able to use the LTI App, follow the manual integration directions below. 

Integrating with Canvas Manually
--------------------------------

In Codio
~~~~~~~~ 

Enable LTI for Your Course
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open the course you would like to connect or create a new course.
2. Make sure you have at least one published assignment or add a new one. (see :ref:`Add and Remove Course Assignments <add-remove-assignment>`)
3. Select the **Admin** tab and click on the blue **Edit Details** button at the bottom.
4. Select the **ENABLE LTI** option.  

  .. image:: /img/lti/enable-lti.png
     :alt: enable lti
     
5. Click **Save**.

Bring up the LTI Integration Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

6. Click your user name in the bottom left of your dashboard
7. Choose your Organization 
8. Click the **LTI Integrations** tab to bring up the following settings.

  .. image:: /img/lti/LTIintegrationinfo.png
     :alt: Org LTI info

In Canvas, adding Codio as an App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Canvas user who carries out these steps must be a system administrator.

9.  Create a new Course in Canvas. We suggest you create a test course called **Codio Canvas** before you do it with a production course.
10.  Select the Course.
11.  Click on **Settings** in the left set of options.
12.  In the top links, select **Apps**.
13.  Click the large button **View App Configurations**.
14.  Click on the blue **+ App** button.

In Codio and Canvas
~~~~~~~~~~~~~~~~~~~

15. We will now copy the following global integration fields from Codio to Canvas.

-  LTI Consumer -> Consumer Key
-  LTI Secret -> Shared Secret
-  LTI URL -> Launch URL

16. In Canvas you should then use one of the following steps:

Option 1: By URL
~~~~~~~~~~~~~~~~

-  Enter a suitable name (Codio Canvas LTI) in the **Name** field.
-  In Codio select the **Copy Consumer** button to copy in to the **Consumer Key** field.
-  Select the **Copy Secret Key** to copy in to the **Shared Secret** field.
-  Select the **Copy XML URL** to copy in the to the **Config URL** field.
-  Submit

Option 2: Paste XML
~~~~~~~~~~~~~~~~~~~

-  Enter a suitable name (Codio Canvas LTI) in the **Name** field.
-  In Codio select the **Copy Consumer** button to copy in to the **Consumer Key** field.
-  Select the **Copy Secret Key** to copy in to the **Shared Secret** field.
-  Click on the ``XML Configuration`` link to open the XML and then copy in the to the **XML Configuration** field.
-  Submit.

Option 3: Manual Entry
~~~~~~~~~~~~~~~~~~~~~~

-  Paste the 3 keys above into the appropriate fields.
-  Enter a suitable name (Codio Canvas LTI) in the **Name** field.
-  Enter **apollo.codio.com** into the **Domain** field.
-  In the **Privacy** field, select **Public**.

You should end up with something like this.

.. figure:: /img/lti/canvas-global.png
   :alt: Canvas Global

Course LMS URL
--------------
This URL ensures that Codio knows how to redirect students back to the correct Canvas course should they attempt to access the course through their dashboard. You need to perform the following actions one time only for a course. The Canvas user who carries out these steps does not need to be a system administrator but must have suitable privileges to edit courses and assignments.

17.  In Codio, go to your course and click on the **Admin** tab near the top.
18.  Select **Edit Details** in the bottom of the page.
19.  Near the bottom is a switch **Enable LTI** which you should check is enabled.
20.  Below this is an empty field **Course LMS URL**. Switch back to Canvas and make sure you are on the Home page of the course. Copy the url in the address bar of your browser to the clipboard and paste it into the above mentioned field in Codio. The url format should end with something like ``/courses/1121212`` although the number will be different.

Mapping an Assignment to a Canvas Assignment
--------------------------------------------

The final mapping step needs to be taken for each individual assignment within Codio. It maps a Canvas assignment to a Codio assignment.

In Canvas
~~~~~~~~~

21.  Make sure you are in the Courses area.
22.  Click on the **Assignments** link in the left hand side.
23.  Provide a name for the Assignment.
24.  Set the points for the Assignment. When the grades get passed back later, the Codio percentage score will be scaled to the points value you specify here.
25.  Scroll down and look for the **Submission Type** field.

.. figure:: /img/lti/canvas-submission-type.png
   :alt: Canvas Submission

26.  You should now click on the dropdown list and select **External Tool**.
27.  Specify the assignment using one of the two options: 

    - **Add by Resource Selection Preview (recommended)**
        
        - Click the **Find** button.
        - Click the Codio tool.
        - Select the assignment you want to map to your course in Canvas. 
        
    - **Add by LTI Integration URL**
    
        - Return to Codio and navigate to the course. Ensure you are in **Teach** mode. 
        - To the right of the assignment, click the icon with 3 blue dots and select **LTI Integration URL**. You should copy the LTI integration url to the clipboard by clicking on the field (it will auto copy).
        - Paste the **LTI Integration URL** in the URL field under **Enter or find an External Tool URL.**

28.  Select **Load This Tool In a New Tab**.
29.  Click the **Save and Publish** button.
30.  Make sure the Canvas course is published.

Common Cartridge
----------------

In the Canvas course you have created go to **Settings** and **Import Course Content** and select **Common Cartridge 1 x Package** and proceed to upload the **.ismcc** file.

If using the Common Cartridge file to import the Codio course assignment details into Canvas, each assignment needs mapping as above using the **Add by Resource Selection Preview (recommended)** method noted above.

Authentication and account creation
-----------------------------------

To add students/teachers see :ref:`Users account creation <lms-users>`