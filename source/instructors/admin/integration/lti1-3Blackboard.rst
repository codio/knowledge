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

- On the administrator tools page select **LTI Tool Providers** under the **Integrations** section.
- Select **Register LTI1.3/Advantage Tool** tab.
- In the **Client ID** section enter:


.. tabs::


  .. code-tab:: text
     :caption: For codio.com


      0128e3c6-67a1-4bfb-9881-747baf0c7105


  .. code-tab:: text
     :caption: For codio.co.uk


      20d13eaa-8d29-4763-87ab-8137aa94129f




.. Note:: If you get a message saying you are migrating your tool from LTI 1.1 to LTI 1.3 click **Ok**.

- Click **Submit**.
- At the bottom of the new page:
- Click **Yes** for **Allow Grade Service Access**
- Click **Yes** for **Allow Membership Service Access**

- Copy the **Default Deployment ID** value from this page.

- Click **Submit** and the tool will be created.



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

- Paste the **LTI Integration URL** you copied in the last step into the **URL** field for your assignments.

  .. image:: /img/Blackboardweblink.png
     :alt: Blackboard Configuration URL field for LTI Integration URL
     :width: 750px




