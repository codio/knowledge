.. meta::
   :description: Information about cpu, memory and disk resources in your assignment or project

System Resources
================
There following are system resources you may need to consider when designing your assignment or project. 
In most cases the default allocations Codio provides are sufficient but occasionally more may be required.

CPU
---
All Codio assignments/projects use shared CPU resources where there is fair balancing among users. You cannot configure the CPU usage for a process.

You can monitor running processes and CPU utilization in real time by typing the ``top`` command in the Terminal. A 100% CPU utilization means that your process is using only one vCPU (virtual CPU) core, a 200% utilization means your process is using two CPU cores. Long-running single-threaded processes do not usually affect the performance. 
If you have multithreaded, long-running processes, we recommend using :ref:`Virtual Machines <virtualmachine>` or limiting the number of threads. 

  .. image:: /img/guides/top-cpu.png
     :alt: A view of CPU usage using the top utility

Memory
------
The default memory configuration for asssignments/projects is 756Mb. If your usage requires more memory, you can purchase a larger :ref:`Gigabox <gigabox-usage>` configuration.
The ``top`` command can also be used to view how much memory is used by your processes. Note the value in the used column during the heaviest memory consumption as software is running. 
If the used memory, (highlighted below) is close to the limit, you will likely experience performance degradation.

  .. image:: /img/guides/top-memory.png
     :alt: A view of memory usage using the top utility

Disk space
----------
Codio assignments/projects have 5Gb of disk space available to them. You can check the disk space available and the disk space used by typing the ``df -h`` at the command prompt in the terminal. 

  .. image:: /img/guides/df-dsk.png
     :alt: A view of how much disk space is available in your Codio box

This number does not include stack size, which can be more than 5Gb. You can also easily check how much space your assignment is using by typing ``du -hs ./``. 
Smaller assignments can be provisioned more quickly and this becomes important for large online classes. For example, node modules can be very large and you might choose to not publish them to student assignments.
You can exclude the node modules by creating an ::ref:`.assignmentignore file <exclude>`. Your students will need to run ``npm install`` when they start the assignment.

We recommend caching the dependencies in the stack for large simultaneous user cohorts to avoid downloading the same dependencies multiple times from GitHub or npmjs.com.

You can do this by running `npm install` or `yarn install` and making a stack version after. That should cache the dependencies according to the lock file in ~/.npm/ folder.

