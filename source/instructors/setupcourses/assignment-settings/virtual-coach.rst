.. meta::
   :description: Hint-Bot is a quick AI solution for helping students with simple queries.


.. _virtual-coach:

Virtual Coach 
================

When Virtual Coach is enabled, students can use AI to assist them with their programming tasks. Codio's prompts to the AI ensure that only assistance is provided, not solutions. The Virtual Coach can help students understand error messages they have received, gain a better understanding of the assignment prompt, or receive a hint about the next possible steps.

In the assignments settings area, there are three settings you can toggle to enable the following features: **Summarize Prompt**, **Error Augmentation**, and **Next Steps Hint**.

.. image:: /img/Assignment-settings-Vc.png
   :alt: Assignment setting vc


When a student clicks on the Virtual Coach icon in the bottom right corner, a dialog opens, and they can see up to three options depending on the settings applied. If there is no :ref:`Guide<authoring>` in the assignment only error message augmentation will be available.



Students may select one of the options presented by the coach to receive more information.

.. image:: /img/Hint-Bot.png
   :alt: Hint-Bot


- **Summarize prompt**: This option summarizes the text in the guide on the page and provides students with an enumerated set of steps.

- **Error Augmentation**: Provides detailed explanations of error messages.

- **Next steps hint**: Provides students with ideas for the next steps they can take to complete their assignment.

.. image:: /img/Summarise-bot.png
   :alt: Summary-Hint



If error output is not directed to the guide, students will need to paste the text of the error message in the prompt field in Virtual Coach.


If an error message is not provided, the student will receive the following: "The provided text does not look like an error message. Please paste an error message below." If, on the second attempt, the student still does not provide an error message, they will be returned to the first screen with three buttons.

.. image:: /img/Explain-error.png
   :alt: Explain-Error


.. Note: Standard and Advanced Code tests have an additional "Explain this error" button that will appear if Error Augmentation is on and running a code test results in an error state.


The Virtual Coach window may be resized by dragging the circle in the upper left corner.