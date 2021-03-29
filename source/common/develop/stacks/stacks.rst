.. meta::
   :description: Stacks

.. _stacks:

Stacks
======
Codio projects are mounted to software configuration templates, known as Codio stacks. A stack refers to the software configuration of a project server (box), which includes everything on the server outside the code workspace (`/home/codio/workspace`) that you see in the IDE file tree. 

When you create a new Codio project or course assignment, you must specify a stack that contains the operating system (always) and other components such as languages, databases and tools. You can use our pre-configured stacks or create your own using the :ref:`project templates <projects>`. 

Codio’s templates deliver fully preconfigured servers in less than 5 seconds, no matter how complex the configuration. You can also snapshot a box's stack :ref:`create a stack <create-stack>` and add it to the **Stacks** template library.

**Note:** It is very important to understand how Stacks are used in Codio, especially when working with courses. Incorrect usage can result in being able to edit a project but then failing when it is run.

Stack modifications
-------------------
Any changes you or an application makes to the software on the server (box) outside the **Workspace** folder is considered a stack modification. Such modifications may include changes made using `sudo apt-get install`, manually editing a config file, or changes to a database due to application usage. 

If you modify a stack, be sure to keep the following in mind prior to assigning it to a course:

- **Projects** - If you have made any modifications to the project, you should :ref:`create a new stack <create-stack>` and :ref:`switch your project <switch-stack>` to the new stack after it is created to ensure maximum efficiency and speed. If you have not yet created a new stack to incorporate the modifications, go to **Project > Stack > Create New** to create a new stack before publishing the assignment. 

  It is good practice to go to your project and set it to point to this stack as soon as possible. It is however, much better practice to update the stack before you publish the assignment in the course module.

- **Course Assignments** - You should always :ref:`create a custom stack <create-stack>` first and then :ref:`switch the project's stack <switch-stack>` and any assignments that use the same configuration to the newly created stack. You can then assign a course module, which assigns all its assignments to the course.

See :ref:`Modifying a Stack <modify-stack>` for more information.

Stack versions
--------------
When a new stack or new version of an existing stack is created, the new versions are organized under the existing stack. Assigning a new version to a stack also resets all project content outside the workspace folder to those of the new stack version.

**Note:** When referring to a stack in our documentation, we are talking about a single stack or a stack version beneath it. 

Stack visibility and ownership
------------------------------
The following rules apply for visibility and ownership of stacks:

- By default, stacks are private to your account but you can make them public. When a stack is made public, it is displayed on the **Stacks** page under **All** and all Codio users can view it.

- If you are the owner of the stack for your organization, the stack is displayed on the **Stacks** page under **My Stacks** and all members of your organization can view it.

- If you are an owner in the organization, you can enable the setting that allows you to create public stacks. See :ref:`Public/Private Settings <public-private>`. 

- If you want to keep your Stack private to your organization, select the **Private** option and set the **Owner** option to your organization. These settings are recommended for collaborating with others when authoring and editing content.

  By default, you are the owner of the stack and only you can edit and :ref:`create new versions <update-stack>`. If you want to allow others to see and administer your stack, assign it to another organization.

**See Also:**

- :ref:`Creating a Stack <create-stack>`
- :ref:`Switching a Project to New Stack <switch-stack>`
- :ref:`Modifying a Stack <modify-stack>`
- :ref:`Updating a Stack <update-stack>`
- :ref:`Using Stacks <using-stacks>` 