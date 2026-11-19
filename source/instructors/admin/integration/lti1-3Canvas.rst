.. meta::
   :description: LTI 1.3 for Canvas

.. _lti1-3Canvas:


LTI 1.3 for Canvas
==================

On this page, you will find detailed step-by-step guidelines to help you integrate your Canvas and Codio accounts and connect assignments between the two applications.

LTI version 1.3 improves upon version 1.1 by moving away from the use of OAuth 1.0a-style signing for authentication and towards a new security model, using OpenID Connect, signed JWTs, and OAuth2.0 workflows for authentication.
For more information, see `Learning Tools Interoperability Core Specification <https://www.imsglobal.org/spec/lti/v1p3/>`__


Part 1: In Canvas - Create a Developer Key
------------------------------------------
The Canvas user who carries out these steps must be a system administrator.

.. important::
   When copying links, please use the copy button adjacent to each link to ensure accuracy and prevent linking errors.

There are two ways to create the Developer Key. Choose **one** and follow its steps from start to finish:



.. tab-set::

   .. tab-item:: Option 1: JSON configuration URL

      :bdg-success:`Recommended` Canvas configures most settings automatically from a JSON URL.

      **In Codio:**

      #. Click your username in the top-right corner, then select **Organization** from the menu. In the Organizations area, click the name of your organization.

      #. Select the **LTI Integrations** tab.

      #. Scroll down to the **LTI Integration 1.3** section. Keep this page open; you will copy values from it.

      **In Canvas:**

      4. Select **Admin -> Developer Keys**.

         |image1|

      #. Click on **Developer Key** and select **+LTI key**.

      #. Set the **Method** to **Enter URL**.

         .. image:: /img/lti-json-url.png
            :alt: Canvas configuration for JSON configuration Url
            :width: 80%

      #. Complete the following fields:

         .. list-table::
            :header-rows: 1
            :widths: 30 70

            * - **Field**
              - **What to add**
            * - **Key Name**
              - A name for the tool, for example: "Codio"
            * - **Owner Email**
              - An email address; you can use your own.
            * - **Redirect URIs**
              - Copy and paste this URL:

                .. tab-set::

                   .. tab-item:: Redirect URI

                      .. code-block:: text
                         :class: no-header

                         https://apollo.codio.com/lti/oidc_redirect

            * - **JSON URL**
              - Paste the URL from **Canvas JSON configuration Url** in Codio.

      #. Click **Save** in the bottom-right corner. You will be back at the list of developer keys.

         |image5|

      #. Update **State** to: **On**.

      #. Copy the number in the **Details** column. This is your **Client ID**, which you will use in Parts 2 and 3.

      When you're done, continue to **Part 2**.

   .. tab-item:: Option 2: Manual configuration
      
      :bdg-info:`Full control` Set each value in Canvas yourself.

      **In Codio:**

      #. Click your username in the top-right corner, then select **Organization** from the menu. In the Organizations area, click the name of your organization.

      #. Select the **LTI Integrations** tab.

      #. Scroll down to the **LTI Integration 1.3** section. Keep this page open; you will copy values from it.

      **In Canvas:**

      4. Select **Admin -> Developer Keys**.

         |image1|

      #. Click on **Developer Key** and select **+LTI key**.

      #. Complete the **Key Name**, **Title** and **Description** fields. Make sure to set the **Method** to **Manual Entry**.

         |image2|

      #. Copy each value from the Codio **LTI 1.3 Integration** section and paste it into the matching Canvas field:

         .. list-table::
            :header-rows: 1
            :widths: 50 50

            * - **Copy from Codio**
              - **Paste into Canvas**
            * - **Redirect URL**
              - **Redirect URIs**
            * - **LTI URL**
              - **Target Link URI**
            * - **Initiate Login URL**
              - **OpenID Connect Initiation URL**

      #. In Canvas, change **JWK Method** to **Public JWK URL**.

      #. From Codio, copy the **Keyset URL** and paste it into the **Public JWK URL** field.

         |image3|

      #. Expand the **LTI Advantage Services** section and enable the desired fields. Ensure all gradebook-related services are enabled for grades to pass back to Canvas.

      #. Expand the **Additional Settings** section.

      #. Type "codio.com" in both the **Domain** and **Tool Id** fields.

      #. Select the **Privacy level** as **Public**.

      #. Scroll down to the **Placements** field. You can add a placement by starting to type the name and then selecting it when it appears. Placements that should be included (remove any others): Link Selection, Editor Button, Assignment Selection and Course Navigation.

         |image4|

      #. Expand each placement and copy in the static links below. Each placement needs a **Target Link URI** and an **Icon URL**; use the images as a reference guide.

         **Link Selection and Assignment Selection**

         .. image:: /img/canvaslinkassignmentselect.png
            :alt: Canvas Link Selection placement
            :width: 750px

         .. tab-set::

            .. tab-item:: Target Link URI

               .. code-block:: text
                  :class: no-header

                  https://apollo.codio.com/lti/resource_selection

         .. tab-set::

            .. tab-item:: Icon URL

               .. code-block:: text
                  :class: no-header

                  https://static-assets.codio.com/dashboard/images/icons/favicon-16x16.da14ae918fd9bc3b.png

         **Editor Button**

         .. image:: /img/canvascourseeditortselect.png
            :alt: Canvas Editor Button placement
            :width: 750px

         .. tab-set::

            .. tab-item:: Target Link URI

               .. code-block:: text
                  :class: no-header

                  https://apollo.codio.com/lti/editor_button

         .. tab-set::

            .. tab-item:: Icon URL

               .. code-block:: text
                  :class: no-header

                  https://static-assets.codio.com/dashboard/images/icons/favicon-16x16.da14ae918fd9bc3b.png

         **Course Navigation**

         .. image:: /img/canvascoursecoursetselect.png
            :alt: Canvas Course Navigation placement
            :width: 750px

         .. tab-set::

            .. tab-item:: Target Link URI

               .. code-block:: text
                  :class: no-header

                  https://apollo.codio.com/lti/course_navigation

         .. tab-set::

            .. tab-item:: Icon URL

               .. code-block:: text
                  :class: no-header

                  https://static-assets.codio.com/dashboard/images/icons/favicon-16x16.da14ae918fd9bc3b.png

      #. Click **Save** in the bottom-right corner. You will be back at the list of developer keys.

         |image5|

      #. Update **State** to: **On**.

      #. Copy the number in the **Details** column. This is your **Client ID**, which you will use in Parts 2 and 3. When you're done, continue to **Part 2**.


.. |image1| image:: /img/lti/canvasdeveloperkey.png
   :alt: Canvas Developer Keys page
   :width: 750px

.. |image2| image:: /img/developerkeyvaluessample1.png
   :alt: Canvas LTI key configuration fields
   :width: 500px

.. |image3| image:: /img/canvasadvantagesample.png
   :alt: LTI Advantage Services toggles in Canvas
   :width: 750px

.. |image4| image:: /img/canvasplacementssample.png
   :alt: Canvas placements configuration
   :width: 500px

.. |image5| image:: /img/lti/canvasdetails.png
   :alt: Canvas Developer Key list with details
   :width: 1500px


Part 2: Create an application in your course in Canvas
------------------------------------------------------

In Canvas:
~~~~~~~~~~

1. Select an existing course or create a new course. **Optional**: create a test course called Codio Test Course before you do it with a production course.

2. In your course, go to **Settings → Apps → + App**.

   .. image:: /img/addlti13app.png
      :width: 450px

3. In Configuration Type, select: **By Client ID**.

4. Paste the Client ID you copied in Part 1 into the **Client ID** field.

5. **Submit → Install**.


Part 3: Create an LTI configuration in Codio
--------------------------------------------

In Codio:
~~~~~~~~~

.. image:: /img/lti/addlti13integration.png
   :width: 750px

1. In your org → **LTI Integrations**

   - Scroll down to **LTI 1.3 Configurations**
   - Click **Add Integration**

Updating the fields in Platform Information

.. note::
   Replace [CANVAS DOMAIN] with your institution's domain in steps 5–7. Remove the brackets. Example: https://yourinstitution.instructure.com/api/lti/security/jwks

.. image:: /img/canvasplatform25.png
   :width: 500px

2. **Platform ID:**

   .. tab-set::

      .. tab-item:: Platform ID

         .. code-block:: text
            :class: no-header

            https://canvas.instructure.com

3. **Client ID:** copied from Developer Keys at the end of Part 1.

4. **Deployment ID:** leave blank.

   .. note::
      Leave the Deployment ID empty if you plan to deploy the LTI tool at the course level.

5. **Public Keyset URL:**

   .. tab-set::

      .. tab-item:: Public Keyset URL

         .. code-block:: text
            :class: no-header

            https://[CANVAS DOMAIN]/api/lti/security/jwks

6. **Access Token URL:**

   .. tab-set::

      .. tab-item:: Access Token URL

         .. code-block:: text
            :class: no-header

            https://[CANVAS DOMAIN]/login/oauth2/token

7. **Authentication Request URL:**

   .. tab-set::

      .. tab-item:: Authentication Request URL

         .. code-block:: text
            :class: no-header

            https://[CANVAS DOMAIN]/api/lti/authorize_redirect

8. Click **Create**.


Part 4: Adding a resource
-------------------------

In Canvas:
~~~~~~~~~~

1. Go to **Assignments** in your course, then click **Assignment**.

   .. image:: /img/createassignment.png
      :width: 500px

2. Give your assignment a name.

3. Select a number of points.

4. Under **Submission Type**, select **External Tool**.

5. Select **Find**.

   .. note::
      Do not paste the LTI Integration URL directly into the Canvas External Tool URL field when creating an assignment. Instead, use the deep link "Find" flow (recommended).

6. Select the tool created in Part 1.

   - Choose the Course and Assignment to connect to
   - Recommended: Select **Load in a new tab**

7. Select **Save** at the bottom of the page.

.. note::
   These settings are not final and can be edited in Canvas at a later time.


Part 5: Customizing Iframe Width/Height
---------------------------------------

You can customize the width and height of the Codio window embedded in Canvas. The default width is 1000 pixels and height is 800 pixels; change those values if needed and press **Save Changes**.

.. image:: /img/lti/iframe-width-height.png
   :alt: Iframe Width and Height settings


Important Notes on Course Copy in Canvas:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- In Canvas, once you copy the course, you must enter a unique SIS ID in Course Settings.

  - An SIS ID that is different from the Blueprint Course (Canvas' Parent Course) is required for Codio to spawn a corresponding child course.
  - An SIS ID is optional for the Blueprint Course.