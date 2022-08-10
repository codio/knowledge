.. meta::
   :description: Instructions for using Computed VMs.


.. _computedvm:

Computed VMs
============

Codio supports Windows and Ubuntu OS in **Computed VM** boxes. To enable this for your organization, send an email to help@codio.com with approximate details of the number of students who will require access to computed VMs.

.. Note:: Codio is not responsible for licensing issues in regard to any software you install to use.

The computed VM's can support 1, 4, 8 or 16Gb memory. VM's are enabled for the organization and then set up at the **Course** level. All assignments in the course can utilize the computed VM boxes, so we would recommend setting up a new course for those assignments that require them.  All assignments in the course would use the same **VM Stack**.


Computed VM's are not available for individual projects (ie when created in **My Projects** area).

 **Please note:** we have plans to develop this feature in the future but if you have ideas/suggestions please raise in our `Feedback area <https://feedback.codio.com/>`_


When Computed VM's have been enabled for your organization, follow these steps:

Enabling VM for the Course
**************************

- On the **Courses** page, select the course and then click the **Course Details** tab.

- In the **Computed VM** section, toggle the **Enable Computed VM** button to **On**.

- Select **OS type** (currently supported: Windows & Ubuntu).

- Select **VM type** to allocate the memory required.

- Select **VM Stack** - select either **Windows Codio Ami** or **Ubintu Codio Ami** depending on the OS type selected above but once you have published your own VM Stack (see below), you will be able to select those as required.

- Save the changes.

Setting up the assignment(s)
****************************

- Create an assignment and open the working copy in the usual manner.

- Go to **Tools>Virtual Machine** to open the VM.  If using **Ubuntu** OS you can use **open ssh** to be able to open the same instance of the main ubuntu vm if you'd prefer to install/set up your VM that way.   You can have both options active at the same time

.. Note::  It takes some time for the VM to activate and start.

- Once the VM has started you can setup or install any items you need. If using **Ubuntu** OS you can also use **Tools>Virtual Machine>open ssh** to be able to open the same instance of the main ubuntu vm if you'd prefer to install/set up your VM that way.   You can have both options active at the same time

- Once you have completed setting up your environment and tested everything select **Tools>Virtual Machine>Publish** from the menu to publish the changes as an updated VM stack assignment providing your own name for the VM Stack.

.. Note::  It can take around 10 minutes for the new stack to be created and available for use.

- When the stack has been fully published go to **Courses>Computed VM>VM Stack** and select the newly published stack to make it available to students for their assignment(s).

- Save the changes.

- Return to the assignment in **Edit Assignments** and publish the assignment either from the publish button in the upper right corner or from **Education>Publish Assignment** to make the assignment accessible to your students.

.. Note::  Publishing the assignment should be done as the last step to avoid students starting the assignments before the required VM Stack is saved to the course.

Updating the VM Stack after students have started the assignment(s)
*******************************************************************

Students that have already started working before a new/updated VM stack has been published will need to terminate the Virtual Machine in their assignment(s) and restart it to use the updated VM stack if the VM does not restart itself. There are buttons available for this purpose in the VM tab.

.. Note:: Termination and restart for students can take a substantial period of time (around 20mins on average) so we recommend that you fully test the VM stack you create before making it available to students.

Updating the assignment content after initial publish
*****************************************************

Any changes to the actual assignment (ie in Guides or the file structure) only require the assignment to be published in the usual manner either from the publish button in the upper right corner or from **Education>Publish Assignment** menu item..

Automatically starting/opening Computed VM
******************************************

You can automatically start/open the **Computed VM** for students using :ref:`Open tab <open-tabs>` setting for **VM** or direct them to **Tools>Virtual Machine>Open** to start themselves.

Pair Programming
****************

:ref:`Pair Programming <group-work>` is not supported for **Computed VMs**.