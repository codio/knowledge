.. meta::
   :description: Hint-Bot is a quick AI solution for helping students with simple queries.


.. _virtual-coach:

Virtual Coach 
================

This new exciting feature has been introduced where students would get an AI which can help them in their programming tasks (they would get an quick solution/hint which can reduce the possibility of getting stuck).This will help lower the burden of helping students with simple questions for TAs and teachers, All they need to do is just click on the icon in the bottom-right will allow students to trigger the chat bot.

.. image:: /img/Virtual-Coach.png
   :alt: AI Bot



This would open up the chat and they can see three discrete options as of now and can't enter the text (as it's in beta version now). 


.. image:: /img/Hint-Bot.png
   :alt: Hint-Bot


When a button is pressed, the corresponding prompt is sent to Claude Instant and the response is displayed for the student:


.. image:: /img/Summarise-bot.png
   :alt: Summary-Hint



.. Note:: For error explanation, students will need to be able to paste in the error message, **The error message is validated using the validation prompt below** .
If an error message is not entered, this would throw  "The provided text does not look like an error message. Please paste an error message below." If on the second attempt the student still does not provide an error message, this would kick them back to the first screen with 3 buttons.


.. image:: /img/Explain-error.png
   :alt: Explain-Error