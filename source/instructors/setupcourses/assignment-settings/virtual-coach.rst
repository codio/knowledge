.. meta::
   :description: Virtual Coach is an AI tool for assisting students with explanations, error messages, and hints.


.. _virtual-coach:

Virtual Coach 
*************

When Virtual Coach is enabled, students can use AI to assist them with their programming tasks. Codio's prompts to the AI ensure that only assistance is provided, not solutions. The Virtual Coach can help students understand error messages, gain a better understanding of the assignment prompt, or receive a hint about the next possible steps.

Codio conducts extensive research in the field of AI use in computing education, with error messages, summaries, and hints representing well-researched use cases for AI-assisted learning. Our Virtual Coach feature, which generates AI-powered explanations, demonstrates positive benefits for learners through improved completion rates and higher median grade attainment.

.. note::
    Coach is powered by Anthropic's Claude model. No student's personally identifiable information (PII) is stored by Anthropic, ensuring student privacy protection. 

In the assignment settings, there are three settings you can toggle to enable the following features: **Summarize Prompt**, **Error Augmentation**, and **Next Steps Hint**.

.. image:: /img/vc-and-extensions/coach-assignment-settings.png
   :alt: Assignment settings for Virtual Coach


When a student clicks on the Virtual Coach icon in the bottom right corner, a dialog opens, and they can see the assistants you have enabled. If there is no :ref:`Guide <authoring>` in the assignment, only error message augmentation will be available.



Students may select one of the options presented by the Coach to receive more information.

.. image:: /img/vc-and-extensions/student-view-coach.png
   :alt: The student view of Virtual Coach


- **Summarize Prompt**: This option summarizes the text in the guide on the page and provides students with an enumerated set of steps.

- **Error Augmentation**: Provides detailed explanations of error messages.

- **Next Steps Hint**: Provides students with ideas for the next steps they can take to complete their assignment.

.. image:: /img/vc-and-extensions/student-vc-summary.png
   :alt: The student view of an assignment summary in Virtual Coach



If error output is not directed to the guide, students will need to paste the text of the error message in the prompt field in Virtual Coach.


If an error message is not provided, the student will receive the following: "The provided text does not look like an error message. Please paste an error message below." If the student still does not provide an error message, they will be returned to the first screen with three buttons.

.. image:: /img/vc-and-extensions/student-vc-error.png
   :alt: The student view of an error explanation in Virtual Coach


.. Note:: Standard and Advanced Code tests have an additional "Explain this error" button that will appear if Error Augmentation is on and running a code test results in an error state.

Students can provide feedback on the Virtual Coach’s responses by using the thumbs up or thumbs down icon.
The Virtual Coach window may be resized by dragging the resize handle in the upper left corner.

There are two ways to review how the Virtual Coach interacts with students:

1. Export Virtual Coach logs using the Codio API ``codio.course.exportCoachData(courseId)``. For more information on Codio APIs see: `Codio JS API <https://github.com/codio/codio-api-js>`_

2. Export the Course Coach Log Data from **Export** tab for the course. For more information, see :ref:`Course Coach Log Data <export-course-coach-logs>`

.. _enable-vc-bulk:

Using Bulk Settings to Enable or Disable Assistants
===================================================

You can enable or disable assistants for all assignments in a course using a CSV file, see :ref:`Bulk Assignment Update<bulk-assignment-update>`

- The CSV template for bulk assignment settings upload includes columns for each Virtual Coach assistant and any custom extensions you have.
- The column values in the CSV file can be set to TRUE to enable assistants for any assignments in the course, and FALSE to disable them.

Using Course Settings to Enable or Disable Assistants
=====================================================

You can enable or disable assistants at the :ref:`course level <course-coach-settings>`. Course-level settings override assignment-level settings—if you activate an extension at the course level, you cannot disable it for individual assignments.


.. Note:: For more information about creating custom Virtual Coach assistants see :ref:`Custom Assistants for Virtual Coach <custom-coach-extensions>`.