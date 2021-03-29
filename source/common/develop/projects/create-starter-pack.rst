.. meta::
   :description: Create Starter Pack

.. _create-starter-pack:

Create Starter Pack
===================
You can create your own Starter Pack and upload it for others to use. Follow these steps to create a Starter Pack:

1. In the navigation pane, click **Starter Packs**.

2. On the **Packs** page, click **New Pack**.

3. Click the **Workspace Source**. The following options are available:

   - **Codio** - Use a Codio project that contains your code.
   - **Git** - Specify a Git repo; use the HTTPS URL to the repository.
   - **Mercurial** - Specify a Mercurial repo; use the HTTPS URL to the repository.

   **Note:** When you specify a Git or Mercurial repo, the repos is pulled into the project each time someone uses your Starter Pack. 

4. Specify the **Stack** to be used. If you only need a base Ubuntu Box, you do not need to specify a Stack.

   **Note:** A Starter Pack is simply a Codio Stack and code workspace. If your Starter Pack is based on a project that has had the Box modified (additional Box components installed, npm global install etc.), these are not present in the project created from the Starter Pack.

5. Enter a **Name** and **Description**, and optionally an **Image** and **Tags** that allow searchability.

6. Specify the Visibility of the Starter Pack. By default, a Starter Pack is private to your account until you make it public, at which point it is displayed in the **Popular** and **All** pages where all Codio users can access it.

  ** Note:** The organization owner can disable the ability for you to create public starter packs. See :ref:Enable or Disable Public/Private Settings <public-private>`.

  **Important** - Do not make your Starter Pack public unless you have fully tested it.

7. Click **Create**.