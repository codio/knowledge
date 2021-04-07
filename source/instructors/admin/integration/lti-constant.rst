.. meta::
   :description: LTI Constant URLs

.. _lti-constant:

LTI Constant URLs
=================

Enabling this setting enables constant URL for course assignments, course detection will be done based on the custom parameter your LMS should pass.

Constant URL's allows the transfer of learning content without modifying LTI links and they are also required if you wish to copy Codio courses and LMS Courses. See :ref:`LTI Course Copy <lti-course-copy>` for more on this.

**Video - LTI Constant URL:**

.. raw:: html

    <iframe width="620" height="349" src="https://codio.wistia.com/medias/8asg6lncd3?wvideo=8asg6lncd3" allowtransparency="true" frameborder="0" scrolling="no" class="wistia_embed" name="wistia_embed" allowfullscreen mozallowfullscreen webkitallowfullscreen oallowfullscreen msallowfullscreen width="620" height="349"></iframe>


**Please note the screenshots below are for implementation in Canvas but other LMS systems should be similar. Refer to their documentation for more assistance**

-  Create an External app in your LMS using the configuration type: By URL

.. figure:: /img/lti/canvas_url.png
   :alt: LTI URL config

-  Enter in the Consumer Key and Shared Secret from your Codio organisation

.. figure:: /img/lti/lti-org-fields.png
   :alt: LTI Fields

-  Copy the XML URL into the Config URL field
-  Submit
-  Return to your Codio course and enable the **Enable LTI constant URL's** button, and save your changes
-  Copy the **LTI constant URL's enabled** link

**N.B. If your LMS supports it, ``lis_course_offering_sourcedid`` is also supported as a unique course identifier so you can replace``codio_class_target_id`` if required**

.. figure:: /img/lti/constant_url.png
   :alt: Enable Constant URL

-  Return to your LMS external app and 'edit'
-  Paste the **LTI constant URL's enabled** link into the Custom Field
-  Submit
