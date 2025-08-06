.. meta::
   :description: LTI 1.3 for Blackboard

.. _lti1-3Blackboard:

LTI 1.3 for Blackboard
======================


Part 1: In Blackboard - Register an Advantage Tool
--------------------------------------------------
The Blackboard user who carries out these steps must be a system administrator.


In Blackboard:
~~~~~~~~~~~~~~

- On the administrator tools page select the **Register LTI1.3/Advantage Tool** tab.
- In the **Client ID** section enter:

    For codio.com - ``4eb78f1c-aae1-4d0f-843d-00eca4cbca18``

    For codio.co.uk - ``53e3fa08-0dd6-4b84-bb7d-5048bb7b32be``

.. Note:: If you get a message saying you are migrating your tool from LTI 1.1 to LTI 1.3 click **Ok**.

- At the bottom:

    - Click **Yes** for **Allow Grade Service Access**
    - Click **Yes** for **Allow Membership Service Access**

- Click **Submit** and the tool will be created.

- Copy the **Default Deployment ID** value from this page.


Part 2: In Codio - Create the configuration
-------------------------------------------

In Codio:
~~~~~~~~~
- Click your username in the top-right corner, then select **Organizations** from the menu.
- In the **Organizations** area, click the name of your organization.
- Select the **LTI Integrations** tab.
- Scroll down to the **LTI 1.3 Configurations** section.
- Click **Add Blackboard Integration**
- In the **Deployment Id:** field paste the value you copied above.
- Click **Create**.
- You will now see a new configuration in for Blackboard in your **LTI Integration 1.3** section.


Part 3: Connect the assignments
-------------------------------

In Codio enable LTI for Your Course
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Open the course you would like to connect or create a new course.
- Make sure you have at least one published assignment or add a new one. (see :ref:`Add and Remove Course Assignments <add-remove-assignment>`)
- Select the **LTI/LMS** tab.
- Toggle **ENABLE LTI** on.  

  .. image:: /img/lti/enable-lti.png
     :alt: enable lti
     
- Click **Save Changes**.

- Select an assignment you want to connect and click the 3 vertical dots to the right of that assignment.
- Select **LTI Integration URL**.
- Copy the LTI integration url to the clipboard by clicking on the clipboard icon.

.. figure:: /img/lti/LMS-Unit-URL.png
   :alt: Unit URL

In Blackboard:
~~~~~~~~~~~~~~

- Paste the **LTI Integration URL** you copied in the last step into the **Configuration URL** field for your assignments.


Blackboard LTI 1.x
-------------------

Please be sure to check out the :ref:`Codio LTI App <lti-app>` which allows for an easy way to integrate and to map Codio course assignments to your LMS system. The `following page <http://library.blackboard.com/ref/df5b20ed-ce8d-4428-a595-a0091b23dda3/Content/_admin_app_system/admin_app_basic_lti_tool_providers.htm>`_ explains how to set up external apps in Blackboard Learn.

In Codio:

Enable LTI for Your Course
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open the course you would like to connect or create a new course.
2. Make sure you have at least one published assignment or add a new one. (see :ref:`Add and Remove Course Assignments <add-remove-assignment>`)
3. Select the **LTI/LMS** tab.
4. Select the **ENABLE LTI** option.  

  .. image:: /img/lti/enable-lti.png
     :alt: enable lti
     
5. Click **Save Changes**.

Bring up the LTI Integration Information
----------------------------------------

6. Click your user name in the bottom left of your dashboard
7. Choose your Organization 
8. Click the **LTI Integrations** tab to bring up the following settings.

  .. image:: /img/lti/LTIintegrationinfo.png
     :alt: Org LTI info


In Blackboard
~~~~~~~~~~~~~

The Blackboard user who carries out these steps must be a Blackboard system administrator.

9.  Create a new Course in Blackboard. We suggest you create a test course called **Codio Blackboard** before you do it with a production course.
10.  Look for the **System Admin** tab near the top right of the page and select it.
11.  Look for the **Building Blocks** section and select it.
12.  Click on **LTI tool providers**.
13.  Click on **Register Provider Domain** in the menu bar.
14.  In the **Provider Domain** field, enter ``apollo.codio.com``.
15.  In the **Default Configuration** section, set **Default Configuration** to be **Set globally**.
16.  In the **Organization Policies** section you should
17.  set **Send User Data** to **Send user data only over SSL**.
18.  in **User Fields to Send** you should set all 3 fields (Constituency in Course, Name, Email Address).

In Codio and Blackboard
~~~~~~~~~~~~~~~~~~~~~~~

19. Now return to the **Default Configuration** section in Blackboard. We will now copy the following global integration fields from Codio to Blackboard.

-  LTI Consumer -> Tool Provider Key
-  LTI Secret -> Tool Provider Secret

Codio course setup
------------------

You need to perform the following actions one time only for a course. The Blackboard user who carries out these steps does not need to be a system administrator but must have suitable privileges to edit courses and assignments.

20.  In Codio, go to your course and click on the **LTI/LMS** tab.
21.  Go to the **LTI/LMS Settings** area.
22.  At the top is a switch **Enable LTI** which you should check is enabled.
23.  Below this is an empty field **Course LMS URL**. Switch back to Blackboard and make sure you are on the main the Codio Blackboard course you created earlier. Copy the url in the address bar of your browser to the clipboard and paste it into the above mentioned field in Codio.

This URL ensures that Codio knows how to redirect students back to the correct Blackboard course should they attempt to access the course through their dashboard.

Mapping an assignment to Blackboard Content
-------------------------------------------

The final mapping step needs to be taken for each individual assignment within Codio. It maps a piece of Blackboard content to a Codio assignment.

In Codio
~~~~~~~~

24.  On the main course screen, make sure the **Edit Assignments** tab is selected.
25.  Click the **Add Assignment** button and select **Project Based**.
26.  Select a project that has some autograded assessments. The **My First Project** that you created earlier in the Onboarding Guide has some auto-graded assessments. You can also assign another project but you will need to manually grade the assignment so there are some scores to pass back to the Blackboard gradebook.
27.  Once the assignment has been added to the course, you should click the 3 dots to the rigth of that assignment and select **LTI Integration URL**.
28.  You should copy the LTI integration url to the clipboard by clicking on the field (it will auto copy).

.. figure:: /img/lti/LMS-Unit-URL.png
   :alt: Unit URL

In Blackboard
~~~~~~~~~~~~~

We now return to Blackboard complete the mapping.

29.  Make sure you have selected the Blackboard course.
30.  Click **Content** in the left hand menu.
31.  Select or hover over **Build Content** in the menu bar
32.  Select **Web Link**.
33.  In the **Web Link Information** section ...
34.  Enter a name for the content
35.  Paste in the **LTI Integration URL** that you just copied to the clipboard from Codio
36.  Check the box **Ths is a link to a tool provider**
37.  Select **Yes** for the field **Enable Evaluation** after which more fields will appear
38.  Set the points you want to award for this content (Codio will automatically scale the percentage value it uses to the points you specify here)
39.  Save the content settings.

Authentication and account creation
-----------------------------------

To add students/teachers see :ref:`Users account creation <lms-users>`

LTI 1.3 Dynamic Registration
-----------------------------


Dynamic Registration simplifies the setup process by automatically sharing configuration information between Tools and LMS systems. 


Access LTI Integration Settings in Codio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. image:: /img/lti/codiolti13settings.png
    :alt: LTI 1.3 settings in Codio
    :align: right
    :width: 350px
    :class: img-responsive


1. Click your username in the top-right corner, then select **Organizations** from the menu.
2. In the **Organizations** area, click the name of your organization.
3. Select the **LTI Integrations** tab.
4. Scroll down to the **LTI Integration 1.3** section.
5. The **Dynamic Registration URL** is at the bottom of the list, you can copy it by clicking on the **Dynamic Registration URL** button.










