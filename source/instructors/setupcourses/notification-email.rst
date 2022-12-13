.. meta::
   :description: Notification Emails

.. _notification-emails:

Automated Emails
================

Automatic email notifications can be set up in your courses to send emails to your students. Go to the **Automated Emails** tab in your course to create automatic email notifications. Not available for **Read only** teachers in the course.

   .. image:: /img/notificationdetails.png
      :alt: Notifications

Automated Email details
***********************

- **Not Started Assignment:** you can schedule the notifications to be sent to all students in the course that have never opened the assignment that is due soon
- **Incomplete Assignment:** you can schedule the notifications to be sent to all students who have started but not finished an assignment that is due soon. Students that have also not started will also be notified
- **Started and Incomplete Assignment** you can schedule the notifications to be sent to all students who have started but not finished an assignment that is due soon. Students that have not started will not be notified
- **New Feedback:** the email notification will be sent when new feedback is available for the student
  

Before
******

- **Due Date (before late penalties)** where :ref:`penalties deadlines <penalties>` are set and the **Closing Date** is set to the final date of completion, the **Due Date** is taken from the penalty deadline date
- **Closing Date** is taken from the **Closing Date** set for the assignment duration

**Reply to Email Address:** enter an email address that students can then reply to if they have questions or require further assistance.

Automated Email Template
************************

We prefill a default title name and the body text including links (in the ```<<<  >>>``` tags) that will assist the students.

You may edit this as you wish.

**Supported tags**

- Student name ```<<<student name>>>``` : Students name
- Assignment name ```<<<assignment name>>>```: Assignment name
- Course name ```<<<course name>>>```: Codio course name
- Course link ```<<<course link>>>```: link to Codio course for non LTI and for LTI enabled courses the ```COURSE LMS URL```
- Assignment link ```<<<assignment link>>>```: link to students project (if the project is not started then the course link as above used)
- Feedback link ```<<<feedback link>>>```: Link to assignment feedback
- Due In ```<<<due in>>>```: when the assignment is due for completion relative to current date/time


**Please note:** we have plans to develop this feature in the future but if you have ideas/suggestions please raise in our `Feedback area <https://feedback.codio.com/>`_

