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
- Go to your organization account settings by clicking on your user name in the bottom left of your dashboard and then selecting your organization within **Organizations**.
- Select the **LTI Integrations** tab.
- Scroll down to the **LTI Integration 1.3** section.
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
- Select the **ENABLE LTI** option.  

  .. image:: /img/lti/enable-lti.png
     :alt: enable lti
     
- Click **Save Changes**.

- Select an assignment you want to connect and click the icon with 3 blue dots and select **LTI Integration URL**.
- Copy the LTI integration url to the clipboard by clicking on the clipboard icon.

.. figure:: /img/lti/LMS-Unit-URL.png
   :alt: Unit URL

In Blackboard:
~~~~~~~~~~~~~~

- Paste the **LTI Integration URL** you copied in the last step into the **Configuration URL** field for your assignments.