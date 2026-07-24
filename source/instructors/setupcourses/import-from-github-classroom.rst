.. meta::
   :description: Importing your GitHub classroom into Codio.

.. _importfromgithubclassroom: 


Importing from GitHub Classroom
===============================

You can import an existing GitHub Classroom into Codio. Each assignment repository in the classroom is created as an assignment in a new Codio course.

Choose an Import Method
-----------------------

There are two ways to migrate your assignments from GitHub into Codio:

- **GitHub Classroom Import** — Import your entire classroom as is.
- **Smart Import** — Import individual assignments and automatically add Codio native features (Guides).

Use the table below to decide which method fits your course.

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :widths: 20 40 40

   * -
     - :ref:`GitHub Classroom Import <githubclassroomimportsteps>`
     - :ref:`Smart Import <smartimport>`
   * - **What it does**
     - Imports your entire classroom as is. Each repository becomes a Codio assignment.
     - Imports repositories one at a time and automatically converts them into assignments with Codio Guides.
   * - **Guides**
     - No — content stays as README files.
     - Yes — README content becomes interactive Guide pages.
   * - **Best for**
     - Moving a whole course over quickly.
     - Getting the most out of Codio's native features.

To use Smart Import, see :ref:`smartimport`. To import your entire classroom, follow the steps below.


.. _githubclassroomimportsteps:

Steps
-----

1. Go to `codio.com <https://www.codio.com>`_ and click the user icon at the top of the page.

2. Sign in with your Codio credentials.

   .. note::
      If you do not have a Codio account, click **Free Instructor Account**, enter your
      information, and indicate that you are an instructor and a GitHub Classroom user.
      Once your account is created, sign in to Codio.

3. Click **Import** in the top right corner.

4. Sign in to your GitHub account when prompted. If you are already signed in to GitHub
   in this browser session, your classroom organizations populate automatically.

5. Select the classroom you want to import.

6. In the pop-up window, select the organization to import to. If you belong to only
   one organization, it is the only option shown.

7. Select the technology stack that matches the coding language of your content.

8. Click **Import** in the bottom right corner. Each assignment repository is created
   as an assignment in the Codio course.

9. To import additional classrooms, return to the **Courses** dashboard and repeat Steps 3–8.