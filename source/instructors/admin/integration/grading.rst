.. meta::
   :description: LTI Grading Process

.. _lti-grading:

LMS Grading
============
Codio passes grades back to the LMS as a percentage earned out of the available points designated in Codio. 

By default, grades are passed when assignment is completed and **Release Grades** setting is enabled, but if you want to customize this behavior you can in the **custom fields parameter** in the integration. You can set the **CUSTOM_CODIO_SEND_GRADE** custom parameter and here is list of possible values (case insensitive):


+-------------------+---------------------------------------------------------------------------------+
| **GRADE_RELEASE** | Default behavior, grades are sent when the grades are released and the          |
|                   | assignment is graded.                                                           |
+-------------------+---------------------------------------------------------------------------------+
| **ALWAYS**        | Grades (even if incomplete) are sent every time on assignment submission or     |
|                   | manual grade action even if the grade hasn't changed.                           |
+-------------------+---------------------------------------------------------------------------------+
| **CHANGED**       | Every time grade is different from the previous state.                          |
+-------------------+---------------------------------------------------------------------------------+


Example:

.. code:: ini

   CUSTOM_CODIO_SEND_GRADE=GRADE_RELEASE

When grades are :ref:`released <release-grades>` a URL is passed to the LMS where students/teachers can access the grading information for the assignment in the grading area of the LMS. By default, only the course teachers and the individual student can access the grading preview URL.

In order to pass a different URL back to your LMS system allowing anyone who knows the URL to access the students grading information, enable the **Provide Feedback Link** option for the course. You can find this at the botton of the **LTI/LMS Settings** on the **LTI/LMS** tab.

  .. image:: /img/lmssharedfeedback.png
     :alt: LMS Shared Feedback
