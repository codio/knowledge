.. meta::
   :description: LTI 1.3 for Brightspace and D2L

.. _lti1-3BS-D2L:

LTI 1.3 for Brightspace/D2L
===========================

In Brightspace - Register a Tool
--------------------------------
1. Name - Codio
2. In the **Domain** field enter - ``https://apollo.codio.com``

Access your LTI Integration settings in Codio
---------------------------------------------
1.  Go to your organization account settings by clicking on your user name in the bottom left of your dashboard and then selecting your organization within **Organizations**.
2.  Select the **LTI Integrations** tab.
3.  Scroll down to the **LTI Integration 1.3** section. You should see the following fields. Remain on this screen for the time being.

The LTI 1.3 area of your LTI Integrations settings for your organization.
  .. image:: /img/lti/codiolti13settings.png
     :alt: LTI 1.3 settings in Codio

Copy the following fields from Codio to Brightspace/D2L
-------------------------------------------------------
1. Copy **Initiate Login URL** to the **OpenID Connect Login URL** field.
2. Copy **Redirect URL** to the **Redirect URL** field.
3. Copy **Keyset URL** to the **Keyset URL** field.
4. Press **Register** - leave the pop-up on the screen, you will be copying values from it.

Now add the Integration you created
-----------------------------------
1. In Codio on the LTI Integrations screen scroll down to the LTI 1.3 Configurations field and click **Add Integration**

  .. image:: /img/lti/addlti13integration.png
     :alt: LTI 1.3 Configurations

2. From the pop-up in Brightspace/D2L copy the **Issuer ID** and place in the **PLATFORM ID** field

  .. image:: /img/lti/codioplatformlti1-3.png
     :alt: LTI 1.3 Platform information in Codio


Copy the following fields from the Brightspace/D2L pop-up to Codio
------------------------------------------------------------------
1. Copy the **Client ID** to the **Client ID** field in Codio.
2. Copy the **Keyset URL** to **Public Keyset URL** field.
3. Copy the **Brightspace OAuth2 Access Token URL** to the **Access Token URL** field in Codio
4. Copy the **OpenID Connect Authentication Endpoint** to the **Authentication Request URL** field in Codio
5. Click on **View Deployments** and create a **New Deployment**
6. In the Tool field select the tool you just created
7. Name it Codio Deployment or something similar.
8. Toggle **Open as External Resource** if you want to open the tool in a new tab, otherwise it will open as an iFrame.
9. Toggle **Grades created by LTI will be included in Final Grade** if you are using grades passed from Codio.
10. Add **Org Units** as you need for your setup.
11. Click **Create Deployment**.
12. Copy the deployment ID that is generated and paste it into Codio into the **Deployment ID** field.
13. Click **Create** in Codio.

Create the new link in Brightspace/D2L
--------------------------------------
1. In your Brightspace/D2L environment you can dismiss the pop up.
2. In the deployment tool click **View Links** and then create a **New Link**
3. Name it Codio.
4. In the URL field paste: ``https://apollo.codio.com/lti/resource_selection``
5. Change type to **Deep Linking Quicklink**
6. Click **Save and Close**



Connect your Brightspace/D2L Modules to your Codio Assignments
==============================================================

The final mapping step needs to be taken for each individual assignment within Codio. It maps a Brightspace/D2L assignment to a Codio assignment.

In Brightspace/D2L
------------------

1. Select the **Content** tab from the top of the page. 
2. Add a new module in your D2L course.
3. Select **Add Existing Activities** (1) -> **External Learning Tools** (2)

  .. image:: /img/lti/D2Lconnectassignment.png
     :alt: D2L view 3

4. From the list of available LTI links, select the Codio tool you created earlier.
5. Click on the Codio link to bring up all the Codio courses for which you have enabled LTI.
6. Select the Codio assignment you want to connect.

LTI Course copy for Brightspace/D2L
===================================

Enabling this setting allows existing Codio course content used in your LMS to be copied into a new Codio course and a new course in your LMS. This should be enabled for the courses connected with the "Master" course in your LMS. The parameter will be disabled by default for for all copied courses.

First enable :ref:`LTI Constant URLs <lti-constant>` for your course.

1.  In your existing Codio course, enable the **Enable LTI course copy** button, and save your changes

.. figure:: /img/lti/enable_class_fork.png
   :alt: Enable course copy field

Add custom parameters to your course in Brightspace/D2L
-------------------------------------------------------
2. In the Course Tools menu click on the tool you created in the LTI advantage menu.
3. In the Custom Parameters section click **Add Custom parameter** and copy the ``codio_parent_course_id`` name and value from Codio.  