.. meta::
   :description: LTI Keys

.. _lti-keys:

LTI Keys and URLs
=================

**LTI Keys** are used to integrate your LMS to Codio. These keys are required by your LMS administrator one time only so that Codio can be added as an LTI provider. Once Codio has been added as an LTI provider, you will not need them again and the remaining actions can be completed by LMS users who have Teacher/Instructor permissions.

**Course and assignment URLs** will be copied and pasted into your LMS system, once for the LMS course/course and once for each LMS assignment.

We have platform specific integration documentation for the following LMS platforms, although for most LMS systems you should be able to utilise the **:ref:`Codio LTI App <lti-app>`**

- :ref:`Canvas <canvas>`
- :ref:`Blackboard <blackboard>`
- :ref:`Moodle <moodle>`

LTI Keys
--------

LTI keys are accessible to `Codio Organization Owners <org-owners>` only.

To find these keys:

-  Go to your organization account settings by clicking on your user name in the bottom left of your dashboard and then selecting your organization within **My Organizations**.
-  Select the **LTI Integrations** tab.
-  Scroll down to the **LTI Integration 1.0** section. You should see the following fields.

.. figure:: /img/lti/lti-org-fields.png
   :alt: lti-keys


Course LMS URL
--------------

The **Course LMS URL** is used to map an LMS course to a Codio course. It ensures that Codio knows how to redirect students back to the correct course should they attempt to access the course through the Codio dashboard.

The LMS user who carries out these steps does not need to be a system administrator but must have suitable privileges to edit courses and assignments.

-  In Codio, go to the **Admin** tab near the top.
-  Select **Edit Details** in the bottom of the page.
-  Near the bottom is a switch **Enable LTI** which you should enable.
-  Below this is an empty field **Course LMS URL**. Switch back to your LMS and make sure you are on the Home page of the course. Copy the url in the address bar of your browser to the clipboard and paste it into the above mentioned field in Codio.

.. figure:: /img/lti/lti-class-url.png
   :alt: lti-class-url


Assignment URL
--------------

Please be sure to check out the :ref:`Codio LTI App <lti-app>` which allows for an easy way to integrate and to map Codio course assignments to your LMS system.

If you are unable to utilise the Codio LTI App, the **Assignment URL** is where you map each individual assignment within your Codio course to the corresponding assignment in your LMS. It directs a student to the correct Codio assignment and will automatically open the Codio assignment.

-  On the main course screen, click the icon with 3 blue dots for each of the assignments you wish to map and select **LTI Integration URL**.
-  You should copy the LTI integration url to the clipboard by clicking on the field (it will auto copy).

.. figure:: /img/lti/LMS-Unit-URL.png
   :alt: Assigment URL


-  Complete the mapping in your LMS.

Exporting LTI settings
----------------------

The LTI integration URLs for the assignments in a course can be exported.

-  Select the course, go to the Admin area and then press the **Export LTI Settings** button.

.. figure:: /img/class_lti_export.png
   :alt: Export LTI

