.. meta::
   :description: Exam Proctoring settings are used to enable options such as time limit, shuffle question order, navigation and login for exams.


.. _exam-proctoring:

Exam Proctoring
===============
The Exam Proctoring settings are used to enable various options for assignment exams. After you have completed your selections, click **Save Changes**.

.. image:: /img/examproctoring.png
   :alt: Exam Proctoring Settings

- **Time Limit** - If enabled, assignments are marked as complete after the indicated amount of time has passed since the student started the assignment or the **End Time** of the assignment has been reached. 
 
  - Click **Time Limit** to enable it and then enter the value for **Days**, **Hours**, and **Minutes**.
  
  - To disable, uncheck **Time Limit**.
  
  - Students can be granted additional time if required. Select the 3 blue dot menu for the students assignment and **Extend Time**
  
.. image:: /img/extendtime.png
   :alt: Extend Time

- **Shuffle Question Order** - If enabled, each student receives the pages of the assignment in a random order to avoid students having exact duplicate assignments.
  
   - Click **Shuffle Question Order** to enable it.
  
   - To disable, uncheck **Shuffle Question Order**.


- **Forward Only Navigation** - If enabled, navigation buttons and menus that allow students to re-visit questions are hidden; students can only move forward through the pages. Students are advised of this restriction as they start the assignment.

- **Single Login** - If enabled, once a student has started the assignment and until they mark it as complete, all other account login attempts are blocked. As students start the assignment, they are advised that it is restricted to single login and to ensure that they have:

  - Closed other tabs or browsers where Codio is open.
  - A stable internet connection.
  - Enough power in their device.
  - Sufficient time to complete the assignment.

  If students attempt to access the assignment from a different IP address or browser, they will be restricted and advised to contact their course instructor for assistance. 

  If students try to log out of Codio before the assessment is fully completed, they will be advised that if they continue, they will not be able to access it again. 

  Instructors can reset the single login restriction if they feel it is appropriate:

  On the **Students** tab in the course, click the menu icon (3 horizonatal dots) and choose **Reset Single Login**.

- **Authentication** - If enabled, your students will need to authenticate before they can open the assignment. This option can only be used if you have configured :ref:`SSO Integration <sso-integration>` for the organisation.
