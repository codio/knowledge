.. meta::
   :description: LTI Keys & URLs

.. _lti-keys-and-urls-information:

LTI Keys and URLs 
=================
This page provides an overview of some of the key settings allowing for LTI integration. For more specific directions, access your LMS under system-specific directions. 

LTI Constant URLs
-----------------

Enabling this setting enables constant URL for course assignments, course detection will be done based on the custom parameter your LMS should pass.

Constant URL's allows the transfer of learning content without modifying LTI links and they are also required if you wish to copy Codio courses and LMS Courses. See :ref:`LTI Course Copy <lti-course-copy>` for more on this.




LTI Keys
--------

**LTI Keys** are used to integrate your LMS to Codio. Your LMS administrator will use these keys once to integrate Codio as an LTI provider in your system. Once Codio has been added as an LTI provider, you will not need them again and the remaining actions can be completed by LMS users who have Teacher/Instructor permissions. LTI keys are accessible to :ref:`Codio Organization Owners <org-owners>` only.

To find these keys:

+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+   
| 1. Click your user name in the top right corner,              |    .. figure:: /img/lti/LTI1.1IntegrationCodio.png                                          |
|    then select **Organization** from the menu.                |       :alt: lti-keys                                                                        |
|                                                               |                                                                                             |
| 2. In the **Organizations** area, click the name              |                                                                                             |
|    of your organization.                                      |                                                                                             |
|                                                               |                                                                                             |
| 3. Click the **LTI Integrations** section on the              |                                                                                             |
|    left to bring up the following settings.                   |                                                                                             |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+


Course LMS URL
--------------

The **Course LMS URL** is used to map a LMS course to a Codio course. This ensures that students are automatically redirected to the correct course when they access it through the Codio dashboard.

**Note: The LMS user who carries out these steps does not need to be a system administrator but must have suitable privileges to edit courses and assignments.**


+---------------------------------------------------------------+--------------------------------------------------------------------------------+
| 1. In Codio, go to the **LTI/LMS** section.                   | .. figure:: /img/lti/lti-class-url.png                                         |
|                                                               |    :alt: lti-class-url                                                         |
| 2. At the top is a switch **Enable LTI** which you should     |                                                                                |
|    enable.                                                    |                                                                                |
|                                                               |                                                                                |
| 3. Below this is an empty field **Course LMS URL**. Switch    |                                                                                |
|    back to your LMS and make sure you are on the Home page    |                                                                                |
|    of the course. Copy the url in the address bar of your     |                                                                                |
|    browser to the clipboard and paste it into the above       |                                                                                |
|    mentioned field in Codio.                                  |                                                                                |
|                                                               |                                                                                |
| 4. Save your changes.                                         |                                                                                |
+---------------------------------------------------------------+--------------------------------------------------------------------------------+



.. _lti-integration-assignment-urls:

LTI Integration Assignment URLs
-------------------------------

The **Assignment URL** is needed to map each individual assignment within your Codio course to the corresponding assignment in your LMS. It directs a student to the correct Codio assignment and will automatically open the Codio assignment.

1.  On the main course screen, click the icon with 3 blue dots for each of the assignments you wish to map and select **LTI Integration URL**.
2.  You should copy the LTI integration url to the clipboard by clicking on the field (it will auto copy).

.. figure:: /img/lti/LMS-Unit-URL.png
   :alt: Assigment URL


.. Note:: The LTI integration URLs for the assignments in a course can be exported, see instructions below. 






Export LTI Settings
===================

The LTI integration URLs for the assignments in a course can be exported.

- Select the course, go to the **LTI/LMS** area and then press the **Assignment URLs** button.

  .. image:: /img/class_lti_export.png
     :alt: Export LTI settings








LTI Enroll to Course Only
=========================

LTI Enrollment provides single sign-on access to an entire course without linking each assignment. **It does not allow for automatic grade passback**.

To use this feature, first generate a link from your Codio course and then add it to your LMS course as an **External Tool** in an assignment or module. When students click the link, they are enrolled in the Codio course and redirected to the Codio dashboard. On there dashboards they will see all the assignments for the course. 
Students do not need to begin each assignment using the LMS system.

To generate an **LTI Enroll Link**, follow the steps below:

.. image:: /img/lti/LTIenrolllink.png
   :alt: Export LTI settings
   :align: right
   :width: 490px

1. Navigate to the **Courses** page and select the course you wish to connect.
2. Click the **LTI/LMS** tab and toggle the **Enable LTI** setting on from the LTI/LMS Setting area.
3. Enable the **Enroll to course only** setting to generate the link.
4. Copy the link and paste it as an **External Tool** in your LMS system.


|  

.. Note:: With the **Enroll to course only** setting, grades are not passed back to the LMS. Refer to :ref:`Webhook <webhooks>` for more information about passing grades back.


Common Cartridge
=================

Allows you to export the `Common Cartridge 1.3 <http://www.imsglobal.org/cc/ccv1p3/imscc_Overview-v1p3.html>`_ data for the course to then use within your LMS system to import details of the assignments in your Codio courses.

1. Navigate to the **Courses** page and select the course to open it.
2. Click the **LTI/LMS** tab and then in the **LTI/LMS Connections** area, click to **Common Cartridge** the common cartridge information.

   .. image:: /img/common-cartridge.png
      :alt: Common Cartridge Export

.. Important:: If working with Canvas, each assignment within your LMS still needs to be configured. Refer to the :ref:`system specific instructions <system-specific-directions>` for your LMS system.

