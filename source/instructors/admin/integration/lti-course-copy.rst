.. meta::
   :description: LTI Course copy

.. _lti-course-copy:

LTI Course copy
===============

Enabling this setting allows existing Codio course content used in your LMS to be copied into a new Codio course and a new course in your LMS. This should be enabled for the courses connected with the "Master" course in your LMS. The parameter will be disabled by default for all copied courses.

**Video - LTI Course Copy:**

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/x99lsbx801.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_x99lsbx801 seo=false videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/x99lsbx801/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

.. Note:: the screenshots below are for implementation in Canvas but other LMS systems should be similar. Refer to their documentation for more assistance

First enable :ref:`LTI Constant URLs <lti-keys-and-urls-information>` for your course.

1.  In your existing Codio course, enable the **Enable LTI course copy** button, and save your changes

.. figure:: /img/lti/enable_class_fork.png
   :alt: Enable course copy field


2.  Both custom parameters should be added to the tool in the Master course.
3.  In your LMS "Copy this Course" (or equivalent term for your LMS) and create your new course

.. figure:: /img/lti/copy_course.png
   :alt: Copy LMS Course

3.  When completed go to **External Apps** and edit the existing app connecting Codio to your LMS
4.  Replace the existing custom field that was set from your original Codio course with an id of your own (e.g something like codio_course_target_id=semester-year)

.. Note:: If your LMS supports ``lis_course_offering_sourcedid`` you do not need to specify ``codio_course_target_id`` for the copied course, ``lis_course_offering_sourcedid`` will be used automatically to detect the course.  For cases when ``lis_course_offering_sourcedid`` is needed for course copy but not available due to privacy settings in Canvas, a custom parameter ``custom_codio_course_offering_sourcedid=$CourseOffering.sourcedId`` can be tried.

.. figure:: /img/lti/parent_class.png
   :width: 400
   :alt: Parent course ID

6.  Submit

7.  In the new course created in your LMS, open one of the new  assignments and this will then create the new course in Codio containing the content from your original Codio course. 

