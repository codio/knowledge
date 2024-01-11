.. meta::
   :description: The Prime Assignment Containers settings is useful when you have a large number of students looking to start an assignment at the same time.

.. _prime-assignment-containers:

Prime Assignment Containers 
===========================

The Prime Assignment Containers settings is useful when you have a large number of students scheduled to start an assignment at the same time. You do not need to do this for cohorts of less than 500 simultaneous starts.
After enabling this setting, Codio will make the specified number of containers available at the scheduled time.  
When your students open the assignment the containers will already be set up and they will not face any performance issues even when thousands of students begin at the same time.

.. image:: /img/prime-assignment.png
   :alt: Prime Assignment Options


You can specify the **Start Time** when you want the containers available and the **Number of Students** that will start the assignment at the same time.

The Start Time must be at least 4 hours in the future so Codio will have enough time to ensure that the containers are available and can be started at your specified time.


We recommend priming for large assignments, like ones that contain node modules or extensive data sets, or for assignments that have 100+ students starting at the same time, 
like a large exam. Instructors can also prime smaller assignments with starter code files for thousands of students beginning simultaneously.

.. Note::  Both the Prime Assignment setting and the :ref:`Pair Programming<group-work>` setting can not be enabled at the same time.
