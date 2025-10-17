.. meta::
   :description: LTI 1.3 for Brightspace and D2L

.. _lti1-3BS-D2L:

LTI 1.3 for Brightspace/D2L
===========================

In Brightspace - Register a Tool
--------------------------------
The following is created in Manage Extensibility, LTI Advantage - Register a Tool, select Standard.
1. Name - Codio
2. In the **Domain** field enter - ``https://apollo.codio.com``

Access LTI Integration settings in Codio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/lti/codiolti13settings.png
   :alt: LTI 1.3 settings in Codio
   :width: 500px    

1. Click your username in the top-right corner, then select **Organizations** from the menu.
2.  In the **Organizations** area, click the name of your organization.
3.  Select the **LTI Integrations** tab.
4.  Scroll down to the **LTI Integration 1.3** section. You should see the following fields. Remain on this screen for the time being.


Copy fields from Codio to Brightspace/D2L
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 .. important::
    When copying links, please use the copy button adjacent to each link to ensure accuracy and prevent linking errors.


1. Copy **Initiate Login URL** to the **OpenID Connect Login URL** field.
2. Copy **Redirect URL** to the **Redirect URL** field.
3. Copy **Keyset URL** to the **Keyset URL** field.
4. In the **Extensions** section enable **Assignment and Grader Services**, **Deep Linking** and **Names and Role Provisioning Services**.
5. Press **Register** - leave the pop-up on the screen, you will be copying values from it.

|
|

Add the Integration you created
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. In Codio on the LTI Integrations screen scroll down to the LTI 1.3 Configurations field and click **Add Integration**

.. image:: /img/lti/addlti13integration.png
     :alt: LTI 1.3 Configurations
    
|

2. From the pop-up in Brightspace/D2L copy the **Issuer ID** and place in the **PLATFORM ID** field


Copy fields from Brightspace/D2L pop-up to Codio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/lti/codioplatformlti1-3.png
     :alt: LTI 1.3 Platform information in Codio
     :width: 325px
     :align: center


1. Copy the **Client ID** to the **Client ID** field in Codio.
2. Copy the **Keyset URL** to **Public Keyset URL** field.
3. Copy the **Brightspace OAuth2 Access Token URL** to the **Access Token URL** field in Codio
4. Copy the **OpenID Connect Authentication Endpoint** to the **Authentication Request URL** field in Codio
5. Click on **View Deployments** and create a **New Deployment**
6. In the Tool field select the tool you just created
7. Name it Codio Deployment or something similar.
8. In the **Security Settings** section you need to send at least the **Name** and the **Email** if you aren't choosing to enroll your students anonymously.
9. Toggle **Open as External Resource** if you want to open the tool in a new tab, otherwise it will open as an iFrame.
10. Toggle **Grades created by LTI will be included in Final Grade** if you are using grades passed from Codio.
11. Add **Org Units** as you need for your setup.
12. Click **Create Deployment**.
13. Copy the deployment ID that is generated and paste it into Codio into the **Deployment ID** field.
14. Click **Create** in Codio.

Create the new link in Brightspace/D2L
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. In your Brightspace/D2L environment you can dismiss the pop up.
2. In the deployment tool click **View Links** and then create a **New Link**
3. Name it Codio.
4. In the URL field paste: ``https://apollo.codio.com/lti/resource_selection``
5. Change type to **Deep Linking Quicklink**
6. Click **Save and Close**



Connect Brightspace/D2L and Codio assignments
---------------------------------------------

The final mapping step needs to be taken for each individual assignment within Codio. It maps a Brightspace/D2L assignment to a Codio assignment.

In Brightspace/D2L
~~~~~~~~~~~~~~~~~~

1. Select the **Content** tab from the top of the page. 
2. Add a new module in your D2L course.
3. Select **Add Existing Activities** 
4. From the list of available LTI links, select the Codio tool you created earlier.
5. Click on the Codio link to bring up all the Codio courses for which you have enabled LTI.
6. Select the Codio assignment you want to connect.

LTI Course copy for Brightspace/D2L
-----------------------------------

.. image:: /img/lti/enable_class_fork.png
   :alt: Enable course copy field
   :width: 375px
   :align: center

Enabling this setting allows existing Codio course content used in your LMS to be copied into a new Codio course and a new course in your LMS. This should be enabled for the courses connected with the "Master" course in your LMS. The parameter will be disabled by default for all copied courses.

First enable :ref:`LTI Constant URLs <lti-keys-and-urls-information>` for your course.

1.  In your existing Codio course, enable the **Enable LTI course copy** button, and save your changes






