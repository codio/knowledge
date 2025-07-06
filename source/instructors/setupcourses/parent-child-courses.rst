.. meta::
   :description: When a course is created by cloning or using a share code, the course (child) is tied to the original (parent) course so that any updates to an assignment in the parent course are also updated in the child course. 


.. _parent-child-courses:

Working with Parent/Child Courses
=================================
When a course is created by cloning or using a share code, the course (child) is tied to the original (parent) course and any updates to an assignment in the parent course may also be updated. Details of the parent course for any child assignments can be seen from the :ref:`version history button <relationship>` and individual child assignments as well as the entire course can  be :ref:`disconnected <disconect>` if required.

Update & pull updates
---------------------
After an update in the parent course has been published, from **Edit Assignments** area, a **Pull** icon will appear next to assignments that have changed. Follow these steps to pull the updates.

1. In the Dashboard, select the course to open it and click on the **Edit Assignments** tab. The assignments that have changed show a **Pull** icon.

   .. image:: /img/pullarrow.png
      :alt: Pull

2. Click the Pull icon to view the details of the update.

   .. image:: /img/manage_classes/updatedialog.png
      :alt: Update Details

3. Click Update to pull the updates into the cloned (child) course.

   .. Note:: You can also click **Pull All** to pull all available updates for the module but you cannot view the details.

   .. image:: /img/pullallarrow.png
      :alt: Pull

  .. Note:: Pulling updates from the parent course overwrites changes made in the child course. 
  
Update & pull updates - with notification sent to child courses
---------------------------------------------------------------
Some people prefer to **send notifications** to alert child courses of updates. After an update in the parent course has been published, you can send a notification that displays a banner in the child course(s) informing all instructors that there are available updates.

To send notifications, follow these steps:

1. In the Dashboard, select the course to open it and then click the **Notifications** tab.

2. Click the **Send Notification** button.

3. In the **Notification Message** text box, enter the message to instructors that explains the changes that have been made to the parent course and are now available in the child course. 

   .. image:: /img/manage_classes/sendnotification.png
      :alt: Notification Message 

   The message can include details of all the changes made in each assignment or just be a summary. If a summary is included, instructors can pull the assignments and review the information in the publish assignment changelog. 

  .. Note:: To view a history of all notifications sent for published updates in the parent course, click the **View Sent Notifications** button.

4. After a notification has been sent, a **Download** icon is displayed in the upper right corner of the course.

   .. image:: /img/manage_classes/courseupdatelist.png
      :alt: Course Update Icon 

   If you open the course, a banner is displayed indicating that the course has been updated.

   .. image:: /img/courseupdatebanner2.png
      :alt: Course Update Banner 

5. Click **Show Changes** to view the updates, including the tagged parts of the assignment that has updates.

   .. image:: /img/manage_classes/detailcourseupdates.png
      :alt: Course Update Details

   To view the notification message that was send with the update, click **Updates History**.

   .. image:: /img/manage_classes/updatehistory.png
      :alt: View update notification history

6. Check the check box next to the assignments you want to update and then click **Apply**. 

7. On the confirmation dialog, confirm that you want to update the assignments.

  .. Note:: Pulling updates from the parent course overwrites changes made in the child course. 


Add new assignments from parent to child courses
------------------------------------------------
When a new assignment has been added in the parent course, it will not automatically be added to child courses. Rather, child courses will need to add it manually to allow future updates to be pulled. Follow these steps to add an assignment from the parent course to the child course:

1. In the Dashboard, select the child course to open it and go to the **Edit Assignments** tab.

2. Select the module and from the **Add assignment** dropdown select **Add Copy From Existing**.

   .. image:: /img/manage_classes/addchild.png
      :alt: Add Assignment 

3. Select the parent course, module and assignment(s) to be added to the child course. The assignment in the child course is automatically published.

Revert to earlier version
-------------------------
You can revert back to earlier published versions of your courses. However, reverting automatically publishes the course and it's available to your students.

1. In the Dashboard, select the course to open it and go to the **Edit Assignments** tab.

2. On the **Assignments** page, click the **Versions** button.

   .. image:: /img/manage_classes/viewversions.png
      :alt: View Versions

3. View the list of all previous versions and click Revert for the version to which you want to revert. 

   .. image:: /img/manage_classes/revertversion.png
      :alt: Revert Version 

4. When other instructors open the assignment (in Edit mode), they can click **Latest Published Version** to update their working copy to the currently published version.

   .. image:: /img/publishedversion.png
      :alt: Latest Published Version
      
.. _relationship:
      
Parent/Child relationship information
-------------------------------------

Details of the parent course associated with child assignments can be seen from the **Versions** button.



   .. image:: /img/manage_classes/parentdetails.png
      :alt: Linked Parent Course 
      
.. _disconect:      


Disconnecting assignments or an entire course from a parent course
------------------------------------------------------------------

Individual assignments
^^^^^^^^^^^^^^^^^^^^^^

Assignments in child courses can be disconnected from the parent assignment so any future updates released for the parent assignment will not be available to update.

   .. image:: /img/manage_classes/disconnect.png
      :alt: Disconnect assignment

Entire Course
^^^^^^^^^^^^^

The entire course can be disconnected from the parent course so any future updates released for the parent course will not be available to update. 

 - Select the course, and then click the **Course Management** tab and click the **Disconnect** button in the **Course Management** section.

   .. image:: /img/manage_classes/disconnectcourse.png
      :alt: Linked Parent Course 



.. _send-announcements:

Send announcements
------------------
Announcements can be sent to instructors that display a banner all child courses informing instructors of an announcement. 

To send an announcement, follow these steps:

1. In the Dashboard, select the course to open it and then click the **Notifications** tab.

2. Click the **Send Announcement** button.

3. In the **Announcement Message** text box, enter the message to instructors you wish to send.

   .. image:: /img/manage_classes/announcement.png
      :alt: Announcement Message 


  .. Note:: To view a history of all announcements sent in the parent course, click the **View Sent Announcements** link.


4. When an instructor opens the course, a banner is displayed indicating that there is an announcement for the course.

   .. image:: /img/manage_classes/announcebanner.png
      :alt: Course Announcement Banner 