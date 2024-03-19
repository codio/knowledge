.. meta::
   :description: Hint-Bot is a quick AI solution for helping students with simple queries.


.. _virtual-coach:

Virtual Coach 
================

Virtual Coach allows teachers to provide to students the ability to use AI to help them with programming tasks -- WITHOUT receiving answers (they would get an quick solution/hint which can reduce the possibility of getting stuck).This will help lower the burden of helping students with simple questions for TAs and teachers, All they need to do is just click on the icon in the bottom-right will allow students to trigger the chat bot.

In the assignments settings area, teachers would see a virtual coach option and three sub categories which they can enable  **Summarize prompt** , **Error Augmentation** and **Next steps hint** , once enabled these will be displayed in the bot.

.. image:: /img/Assignment-settings-Vc.png
   :alt: Assignment setting vc


.. Note:: The :ref:`Guides<authoring>` needs to be used otherwise students would see "guides player not opened" and can get confused. 

Once a student click on the virtual bot icon in the bottom right corner. 

.. image:: /img/Virtual-Coach.png
   :alt: AI Bot

This would open up the chat and they can see three discrete options.

- Summarize prompt: This option would help students to understand the question in an easier way as to what they need to do and the steps.

- Error Augmentation: Provides detailed error message explanations.

- Next steps hint: Helps students on how to complete, what steps would be followed to pass the test cases and requirements.


.. image:: /img/Hint-Bot.png
   :alt: Hint-Bot


When a button is pressed, the corresponding prompt is sent to Claude Instant and the response is displayed for the student:


.. image:: /img/Summarise-bot.png
   :alt: Summary-Hint



.. Note:: For error explanation, students will need to be able to paste in the error message, **The error message is validated using the validation prompt below**.


If an error message is not entered, this would throw  "The provided text does not look like an error message. Please paste an error message below." If on the second attempt the student still does not provide an error message, this would kick them back to the first screen with 3 buttons.


.. image:: /img/Explain-error.png
   :alt: Explain-Error


.. Note::   'Explain this error' button that will show for **Advance Code Test** in Guides and isn't same as for the 'bot' that shows 'explain an error' option if that was enabled by the teacher in the assignment - the middle option - error augmentation. 

.. Note::   Students can resize the window of the chatbox if they want to just they need to drag that circle that appears on the top left.