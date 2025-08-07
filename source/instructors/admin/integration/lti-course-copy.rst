.. meta::
   :description: LTI Course copy

.. _lti-course-copy:

LTI Course copy
===============

Enabling this setting allows existing Codio course content used in your LMS to be copied into a new Codio course and a new course in your LMS. This should be enabled for the courses connected with the "Master" course in your LMS. The parameter will be disabled by default for all copied courses.

 .. note::
    The screenshots below are for implementation in Canvas but other LMS systems should be similar. Refer to their documentation for more assistance.
  


First enable :ref:`LTI Constant URLs <lti-keys-and-urls-information>` for your course.




+-----------------------------------------------+------------------------------------------------------------------------------+
| 1. In your existing Codio course, enable      | .. figure:: /img/lti/enable_class_fork.png                                   |
|    the **Enable LTI course copy** button,     |    :alt: Enable course copy field                                            |
|    and save your changes.                     |                                                                              |
|                                               |                                                                              |
| |                                             |                                                                              |
|                                               |                                                                              |
| 2. Both custom parameters should be added to  |                                                                              |
|    the tool in the Master course in Canvas.   |                                                                              |
|                                               |                                                                              |
| |                                             |                                                                              |
|                                               |                                                                              |
| 3. In your LMS "Copy this Course" (or         |                                                                              |
|    equivalent term for your LMS) and          |                                                                              |
|    create your new course.                    |                                                                              |
+-----------------------------------------------+------------------------------------------------------------------------------+
| 4. When completed go to **External Apps**     | .. figure:: /img/lti/copy_course.png                                         |
|    and edit the existing app connecting       |    :alt: Copy LMS Course                                                     |
|    Codio to your LMS.                         |                                                                              |
|                                               |                                                                              |
| |                                             |                                                                              |
|                                               |                                                                              |
| 5. Replace the existing custom field that     |                                                                              |
|    was set from your original Codio course    |                                                                              |
|    with an id of your own (e.g similar to     |                                                                              |
|    codio_course_target_id=semester-year)      |                                                                              |
|                                               |                                                                              |
| |                                             |                                                                              |
|                                               |                                                                              |
| 6. Submit                                     | .. figure:: /img/lti/parent_class.png                                        |
|                                               |    :width: 400                                                               |
| |                                             |    :alt: Parent course ID                                                    |
|                                               |                                                                              |
| 7. In the new course created in your LMS,     |                                                                              |
|    open one of the new assignments and this   |                                                                              |
|    will then create the new course in Codio   |                                                                              |
|    containing the content from your original  |                                                                              |
|    Codio course.                              |                                                                              |
+-----------------------------------------------+------------------------------------------------------------------------------+


.. note:: 
   If your LMS supports ``lis_course_offering_sourcedid`` you do not need to specify ``codio_course_target_id`` for the copied course, ``lis_course_offering_sourcedid`` will be used automatically to detect the course. For cases when ``lis_course_offering_sourcedid`` is needed for course copy but not available due to privacy settings in Canvas, a custom parameter ``custom_codio_course_offering_sourcedid=$CourseOffering.sourcedId`` can be tried.

