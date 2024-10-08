.. meta::
   :description: LTI Enrol to Course Only

.. _lti-enrol:

LTI Enroll to Course Only
=========================

LTI Enrollment provides single sign-on access to an entire course without linking each assignment. **It does not allow for automatic grade passback**.

To use this feature, you first generate a link from your Codio course and then add it to your LMS course as an **External Tool** in an assignment or module. When students click the link, they are enrolled in the Codio course and redirected to the Codio dashboard, where they will see all the assignments for the course. 
Students do not need to begin each assignment using the LMS system.

To generate an **LTI Enroll Link**, follow the steps below:

1. Navigate to the **Courses** page and select the course you wish to connect.
2. Click **LTI/LMS** tab and turn ON the **Enable LTI** setting from LTI/LMS Setting area.
3. Enable the **Enroll to course only** setting to generate the link.
4. Copy the link and paste it as an **External Tool** in your LMS system.




.. Note:: With the **Enroll to course only** setting, grades are not passed back to the LMS. Refer to :ref:`Webhook <webhooks>` for more information about passing grades back.