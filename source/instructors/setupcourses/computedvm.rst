.. meta::
   :description: Instructions for using Computed VMs.


.. _computedvm:

Computed VMs
============

Codio supports Windows OS in **Computed VM** boxes . To enable this send an email to help@codio.com with details of the number of students who will require access to computed VMs.

.. Note:: Codio are not responsible for licensing issues in regard to any software you install to use.

The computed VM's can support 1, 4, 8 or 16Gb memory.   VM's are enabled for the organisation and then set up at the **Course** level. All assignments in the course would then be able to utilise the computed VM boxes, so we would recommend setting up a new course for those assignments that require them.


When Computed VM's have been enabled for your organisation, follow these steps:

Enabling VM for the Course
**************************

- On the **Courses** page, select the course and then click the **Course Details** tab.

- In the **Computed VM** section, toggle the **Enable Computed VM** button to **On**.

- Select **OS type** (currently supported: Windows OS).

- Select **VM type** to allocate the memory required.

- Select **VM Stack** - the default is **Windows Codio Ami** but once you have published your own VM Stack (see below), you will be able to select those as required.

- Save the changes.

Setting up the assignment(s)
****************************

- Create an assignment and open the working copy in the usual manner.

- Go to **Tools>Virtual Machine** to open the VM.

.. Note::  It will take a short while for the VM to activate and start.

- When activated, proceed to setup/install all you require.

- When all is installed and tested go to **Tools>Virtual Machine>Publish** to publish the changes as an updated VM stack assignment your own name for the VM Stack.

.. Note::  It can take around 10 minutes for the new stack to be created and be available for use.

- When the stack has been fully published go to **Courses>Computed VM>VM Stack** and you can then select the newly published stack that will then be avaiable to students as they start the assignment(s).

- Save the changes.

- Return to the assignment in **Edit Assignments** and publish the assignment either from the publish button that shows or from **Education>Publish Assignment** to make the assignment accessible to your students in the course.

Updating the VM Stack after students have started the assignment(s)
*******************************************************************

Students that have already started assignment(s) before a new/updated VM stack has been published will need to terminate the Virtual Machine in their assignment(s) and restart it to use the VM stack if the VM does not restart itself. There are buttons available for this purpose in the VM tab.

.. Note:: Termination and restart for students can take a substantial period of time (around 20mins on average) so would recommend that you fully test all is as you require before making available/accessible to students to avoid as much as possible the need for them to have to terminate/restart.

Automatically starting/opening Computed VM
******************************************

You can automatically start/open the **Computed VM** for students using :ref:`Open tab <open-tabs>` setting for **VM** or direct them to **Tools>Virtual Machine>Open** to start themselves.

Pair Programming
****************

:ref:`Pair Programming <group-work>` is not supported for **Computed VMs**.