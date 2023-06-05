.. meta::
   :description: LTI 1.3 for Canvas

.. _lti1-3Canvas:

LTI 1.3 for Canvas
==================

See this page for a video demonstration:

:ref:`LTI 1.3 integration <lti1-3>`

Part 1: In Canvas - Create a Developer Key
------------------------------------------
The Canvas user who carries out these steps must be a system administrator.


In Codio:
~~~~~~~~~

1. Go to your organization account settings by clicking on your user name in the bottom left of your dashboard and then selecting your organization within **Organizations**.
2. Select the **LTI Integrations** tab.
3. Scroll down to the **LTI Integration 1.3** section; you should see the following fields. Keep this page open.


  .. image:: /img/lti/codiolti13settings.png
     :alt: LTI 1.3 settings in Codio

In Canvas:
~~~~~~~~~~

4. Select **Admin -> Developer** Keys.
5. Click on **+Developer Key** and select **+LTI key**.


  .. image:: /img/lti/canvasdeveloperkey.png
     :alt: Creating a Canvas Developer key

6. Complete the **Key Name**, **Title** and **Description** fields.
7. From Codio, under **LTI 1.3 Integration**, copy the **LTI URL** and paste it into the **Target Link URI field** in Canvas.
8. From Codio copy the **Initiate Login URL** and paste it into the **OpenID Connect Initiation URL**.
9. Copy the **Redirect URL** and paste it into the **Canvas Redirect URI** field.


  .. image:: /img/lti/developerkeyvalues.png
     :alt: Adding the Developer key values


10. In Canvas, change **JWK Method** to **Public JWK URL**.
11. From Codio, copy the **Keyset URL** and paste it into the **Public JWK URL** field.


  .. image:: /img/lti/canvasJWK.png
     :alt: JWK URL

12. Expand the **LTI Advantage Services** section and toggle each field on.
13. Expand the **Additional Settings** section

- Type ``codio.com`` in both the **Domain** and **Tool Id** fields.
- Select the **Privacy level** as **Public**.



  .. image:: /img/lti/canvasadvantage.png
     :alt: LTI Advantage Services

14. Scroll down to the **Placements** field. You can add a placement by starting to type the name and then selecting it when it appears.
Placements that should be included (remove any others): Link Selection, Editor Button, Assignment Selection and Course Navigation. 



  .. image:: /img/lti/canvasplacements.png
     :alt: LTI Placements

15. Expand each of the following fields, and copy the static links below:

- **Link Selection**
    - Select **LtiDeepLinkingRequest**
    - **Target Link URI:** ``https://apollo.codio.com/lti/resource_selection``
    - **Icon Url:** ``https://static-assets.codio.com/dashboard/images/icons/favicon-16x16.da14ae918fd9bc3b.png``


  .. image:: /img/lti/canvaslinkselect.png
     :alt: Link Selection

- **Editor button**
    - **Target Link URI:** ``https://apollo.codio.com/lti/editor_button``
    - **Icon Url:** ``https://static-assets.codio.com/dashboard/images/icons/favicon-16x16.da14ae918fd9bc3b.png``


  .. image:: /img/lti/canvaseditorbutton.png
     :alt: Editor Button

- **Assignment Selection**
    - Select **LtiDeepLinkingRequest**
    - **Target Link URI:** ``https://apollo.codio.com/lti/resource_selection``
    - **Icon Url:** ``https://static-assets.codio.com/dashboard/images/icons/favicon-16x16.da14ae918fd9bc3b.png``


  .. image:: /img/lti/canvasassignment.png
     :alt: Assignment Selection

- **Course Navigation** 
    - **Target Link URI:** ``https://apollo.codio.com/lti/course_navigation``
    - **Icon Url:** ``https://static-assets.codio.com/dashboard/images/icons/favicon-16x16.da14ae918fd9bc3b.png``


  .. image:: /img/lti/canvasnavigation.png
     :alt: Course Navigation


16. Press **Save** in bottom right corner

17. You will be back at the list of developer keys.

- Update **State** to: on
- Copy the number in the **Details** column (for use in Parts 2 and 3)


  .. image:: /img/lti/canvasdetails.png
     :alt: Developer Key

Part 2: Create an application in your course in Canvas
------------------------------------------------------

In Canvas:
~~~~~~~~~~


1. Select an existing course or create a new course. 
    - Optional: create a test course called Codio Test Course before you do it with a production course.

2. In your course, go to **Settings → Apps → + App**

3. In Configuration Type, select: **By Client ID**

4. Paste number you copied in Part 1 into **Client ID** field

- **Submit → Install**


  .. image:: /img/lti/addlti13app.png
     :alt: Add App

5. After you click install, click the gear icon by the tool you just created

- Select **Deployment ID**

6. Copy the ID displayed, it will be used in Part 3


  .. image:: /img/lti/canvasdeployment.png
     :alt: Deployment ID


Part 3: Create an LTI configuration in Codio
--------------------------------------------

In Codio:
~~~~~~~~~

1. In your org → **LTI Integrations**

    - Scroll down to **LTI 1.3 Configurations**
    - Click **Add Integration**


  .. image:: /img/lti/addlti13integration.png
     :alt: LTI 1.3 Configurations

Updating the fields in Platform Information
  .. Note:: replace [CANVAS DOMAIN] with your institution’s domain in steps 5-7

2. **Platform ID:** ``https://canvas.instructure.com``
3. **Client ID:** copied from Developer Keys at end of Part 1
4. **Deployment Id:** copied in Part 2
5. **Public Keyset URL:** ``https://[CANVAS DOMAIN]/api/lti/security/jwks``
6. **Access Token URL:** ``https://[CANVAS DOMAIN]/login/oauth2/token``
7. **Authentication Request URL:** ``https://[CANVAS DOMAIN]/api/lti/authorize_redirect``
8. Click **Create**

  .. image:: /img/lti/canvasplatform.png
     :alt: Create LTI Integration

Part 4: Adding a resource
-------------------------
In Canvas:
~~~~~~~~~~

1. Go to Assignments in your course, select **+Assignment**.
2. Give your assignment a name.
3. Select a number of points.
4. Under **Submission Type**, select **External Tool**.
5. Select Find.

  .. Note:: Do not use LTI Integration URL to assign an assignment

6. Select the tool created in Part 1.
- Choose the Course and Assignment to connect to
- Recommended: Select Load in a new tab

  .. image:: /img/lti/createassignment.png
     :alt: Create an Assignment

7. Select **Save** at bottom of the page

Note: these settings are not final and can be edited in Canvas at a later time.


Important Notes on Course Copy in Canvas:
-----------------------------------------

- In Canvas, once you copy the course, you must enter a unique SIS ID in Course Settings.
    - An SIS ID that is different from the Blueprint Course (Canvas’ Parent Course) is required for Codio to spawn a corresponding child course.
    - An SIS ID is optional for the Blueprint Course.
