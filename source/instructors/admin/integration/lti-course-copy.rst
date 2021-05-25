.. meta::
   :description: LTI Course copy

.. _lti-course-copy:

LTI Course copy
===============

Enabling this setting allows existing Codio course content used in your LMS to be copied into a new Codio course and a new course in your LMS. This should be enabled for the courses connected with the "Master" course in your LMS. The parameter will be disabled by default for for all copied courses.

**Video - LTI Course Copy:**

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/x5lwfhay39.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_x5lwfhay39 videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/x5lwfhay39/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>



.. Note:: This video was created before a recent naming change from LTI Course Fork to LTI Course Copy

.. Note:: the screenshots below are for implementation in Canvas but other LMS systems should be similar. Refer to their documentation for more assistance**

First enable :ref:`LTI Constant URLs <lti-constant>` for your course.

-  In your existing Codio course, enable the **Enable LTI course copy** button, and save your changes

.. figure:: /img/lti/enable_class_fork.png
   :alt: Enable course copy field


-  In your LMS "Copy this Course" (or equivalent term for your LMS) and create your new course

.. figure:: /img/lti/copy_course.png
   :alt: Copy LMS Course

-  When completed go to **External Apps** and edit the existing app connecting Codio to your LMS
-  Replace the existing custom field that was set from your original Codio course with an id of your own (e.g something like codio_class_target_id=my_class_id_10)

.. Note:: If your LMS supports ``lis_course_offering_sourcedid`` you do not need to specify ``codio_class_target_id`` for the copied course,``lis_course_offering_sourcedid`` will be used automatically to detect the course**

.. figure:: /img/lti/fork_class_id.png
   :alt: course fork id

-  In your existing Codio course, copy the content of the LTI course copy enabled field into a new line in the 'Edit App' custom field

.. figure:: /img/lti/parent_class.png
   :alt: Parent course ID

-  Submit

-  In the new course created in your LMS, open one of the new  assignments and this will then create the new course in Codio containing the content from your original Codio course. 

