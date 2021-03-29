.. meta::
   :description: Switch Project to New Stack

.. _switch-stack:

Switch Project to New Stack
===========================

There are various reasons for switching your project's stack to a new one, including:

- When you :ref:`create a new stack <create-stack>`. This is the most important and common use case. If you have modified your stack and then created a new stack (or a new version) from it, you need to point your project to the new stack.
- If you mistakenly specified the wrong stack when you created the project.
- If a new stack version has been created and you want to point your project to the latest version.

You can switch a project's stack from **Project > Stack > Settings** on the menu bar or from the Settings (gear) icon on the project in the main project listing.

When you switch the stack from **Project > Stack > Settings**, all stack modifications that were made relative to the original stack are replaced by the new stack. Normally this is fine if you created a new stack from the project before switching it.

**Important:**
When you switch a stack, everything outside the workspace folder in the tree (`/home/codio/workspace`) is replaced by the new stack. See :ref:`Stacks <stacks>` for more information.
