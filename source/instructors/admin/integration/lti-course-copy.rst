.. meta::
   :description: LTI Course copy

.. _lti-course-copy:


LTI Course Copy
===============

Enabling this setting allows existing Codio course content used in your LMS to be copied into a new Codio course and a new course in your LMS. Enable this for courses connected to the "Master" course in your LMS. The parameter will be disabled by default for all copied courses.

.. note::
   Screenshots below show Canvas, but other LMS platforms should be similar. Refer to their documentation for more assistance.

.. important::
   Codio can automatically detect the course to copy from using LMS-provided source identifiers, removing the need to manually specify ``codio_course_target_id`` in most cases. This applies to both LTI 1.3 and LTI 1.1.

   - If your LMS provides ``lis_course_offering_sourcedid``, Codio will use it automatically to detect the parent course.
   - Codio also supports ``lis_course_section_sourcedid`` for course copy detection. If both are present, ``lis_course_offering_sourcedid`` takes priority.
   - Not all LMS platforms supply these identifiers. When neither is available, ``codio_course_target_id`` must be set manually.
   - In Canvas, if ``lis_course_offering_sourcedid`` is unavailable due to privacy settings, use the custom parameter ``custom_codio_course_offering_sourcedid=$CourseOffering.sourcedId`` as a fallback.


LTI 1.3 Course Copy
--------------------

First enable :ref:`LTI Constant URLs <lti-keys-and-urls-information>` for your course.

1. In your existing Codio course, enable **Enable LTI course copy**, save your changes.

   .. figure:: /img/lti/enable_class_fork.png
      :alt: Enable course copy field

2. In your LMS, use "Copy this Course" (or equivalent) to create your new course.

3. In the new LMS course, go to settings and add a unique SIS ID (e.g. ``Fall2026``).

4. Open one of the new assignments in the copied LMS course. This will create the new course in Codio with content from your original course.


LTI 1.1 Course Copy
--------------------

First enable :ref:`LTI Constant URLs <lti-keys-and-urls-information>` for your course.


1. In your existing Codio course, enable **Enable LTI course copy** and save your changes.

   .. figure:: /img/lti/enable_class_fork.png
      :alt: Enable course copy field

2. Add both custom parameters to the tool in the Master course in Canvas.

3. In your LMS, use "Copy this Course" (or equivalent) to create your new course.

4. Go to **External Apps** and edit the existing app connecting Codio to your LMS.

   .. figure:: /img/lti/copy_course.png
      :alt: Copy LMS Course

5. Replace the existing custom field with a unique ID of your own (e.g. ``codio_course_target_id=semester-year``).

   .. figure:: /img/lti/parent_class.png
      :width: 400
      :alt: Parent course ID

6. Submit.

7. Open one of the new assignments in the copied LMS course. This will create the new course in Codio with content from your original course.