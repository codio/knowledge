.. meta::
   :description: Stack planning

Stack planning
==============


You should be familiar with the concept of :ref:`stack <stacks>` before creating content.

Minimize the number of stacks
-----------------------------

It is important to think about the :ref:`stack <stacks>` that your course uses. You should avoid creating a new stack for each assignment. There are very few cases where this is needed. If you unnecessarily create new stacks for each assignment, you will be be less efficient and waste unnecessary time with stack builds/rebuilds.


You should look to use as few stacks as possible, ideally just one, and use that stack for all assignments. There are perfectly valid exceptions, but this is the rule.

Single stack example
--------------------

To illustrate a single stack situation, let's assume you are teaching a course "Programming in Java". You could either use our default Java stack or you start with the Java stack and then add additional tools so it has all the components you require to teach all parts of your course.

Whether you have created your own stack or used a default one, you would then point all your assignments to that one, same stack.

If, as you create more assignments in your course, you find you need to install more tools, then you should :ref:`update the stack with a new version <update-stack>`.

By default, when you choose a stack for your new assignment, it will point to the latest version. So if the underlying stack is updated from any location at all, then any assignment that uses that stack will automatically be set to use it. Students who are using a assignment in a course will also automatically use the latest version when it is updated.

It follows that you should be very careful when pointing to a specific version of a stack, rather than the latest version. If you do this, then you will need to update all assignments that are not set to use the latest version.


Multiple stack example
----------------------

Let's say you are teaching a course "Introduction to Programming" and it has 3 modules "Java", "Python" and "Haskell" and each module contains a good number of assignments. In this case, you could still choose the single stack approach, but you would need to install all three languages and their toolsets and then create a stack from it.

A simpler approach would be to use three separate stacks, one for each language. You set the assignments for each language to point to the appropriate language stack.

Other than that, the principles described above still apply.

Switching stacks
----------------
It is possible to change the stack for an assignment. This can be done from either the assignment listing area from within the IDE. However, if this change were to be needed for all assignments then you would have to repeat this for each assignment individually.

It is therefore highly recommended that you start with a stack and stick with it wherever possible.

Stacks not owned by you
-----------------------

If you were to use one of Codio's default stacks then you are not able to update these yourself as you don't have permissions. However, you might want to start off with, say, the Java stack and then install new components.

In this case, you should plan this ahead of time. You would

- first create the assignment from Codio's Java stack
- install your components

- create a new stack from your assignment (:ref:`in the IDE <updating-from-the-ide>`) or from the :ref:`stacks dashboard <updating-from-the-dashboard>`)

- make sure your stack is switched to that newly created stack

You now own this stack and so you can update whenever you like down the line. When you create new assignments, you would then choose this new stack.

Use Latest Version
------------------

When you assign a stack to a assignment, it will be set by default to the **Use Latest Version**. You can view the stack settings from the IDE (**Project-Stack Settings**)

Understanding what **Use Latest Version** means is important. When you work with a assignment as a course author, that assignment is actually using a fixed version. It does not automatically switch to the latest version each time a new version of a stack is created. This could be dangerous as switching a stack resets everything outside the workspace folder. If you want to update to the latest version then you need to go to the stack settings dialog and press the save button.

Where **Use Latest Version** is useful is when you assign a course module and its assignments to a course. In this case, students who have not yet started a assignment **will** get the latest version of the stack.