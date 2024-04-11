.. meta::
   :description: Hint-Bot is a quick AI solution for helping students with simple queries.


.. _virtual-coach:

Virtual Coach 
*************

When Virtual Coach is enabled, students can use AI to assist them with their programming tasks. Codio's prompts to the AI ensure that only assistance is provided, not solutions. The Virtual Coach can help students understand error messages they have received, gain a better understanding of the assignment prompt, or receive a hint about the next possible steps.

In the assignments settings area, there are three settings you can toggle to enable the following features: **Summarize Prompt**, **Error Augmentation**, and **Next Steps Hint**.

.. image:: /img/Assignment-settings-Vc.png
   :alt: Assignment setting vc


When a student clicks on the Virtual Coach icon in the bottom right corner, a dialog opens, and they can see up to three options depending on the settings applied. If there is no :ref:`Guide<authoring>` in the assignment only error message augmentation will be available.



Students may select one of the options presented by the coach to receive more information.

.. image:: /img/Hint-Bot.png
   :alt: Hint-Bot


- **Summarize prompt**: This option summarizes the text in the guide on the page and provides students with an enumerated set of steps.

- **Error Augmentation**: Provides detailed explanations of error messages.

- **Next steps hint**: Provides students with ideas for the next steps they can take to complete their assignment.

.. image:: /img/Summarise-bot.png
   :alt: Summary-Hint



If error output is not directed to the guide, students will need to paste the text of the error message in the prompt field in Virtual Coach.


If an error message is not provided, the student will receive the following: "The provided text does not look like an error message. Please paste an error message below." If, on the second attempt, the student still does not provide an error message, they will be returned to the first screen with three buttons.

.. image:: /img/Explain-error.png
   :alt: Explain-Error


.. Note: Standard and Advanced Code tests have an additional "Explain this error" button that will appear if Error Augmentation is on and running a code test results in an error state.


The Virtual Coach window may be resized by dragging the circle in the upper left corner.


Customize Assistants for Virtual Coach
======================================

You can extend the current capabilities of Coach by adding your own custom assistants as Javascript extensions. You're going to need a Github account to get started. If you don’t have one, follow the steps by visiting this web page to create: https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github

Once you’re signed in to your Github account, you will be able to create, install and test your very own custom AI assistant with Coach.

Authoring your own custom assistant as a Javascript extension
-------------------------------------------------------------

1. Click this link to head over to the Coach extensions example Github repository - https://github.com/codio-extensions/coach-callback-demo


   .. image:: /img/coach-extensions-repo.png
      :alt: Coach extensions example Github repository

2. Click on the `Fork <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo>`_ button, in the top right corner, to fork your own copy of the example repo, and give it a unique name - This is where you will be making the edits to the example code to create your custom assistant

   - You'll see 2 files in your forked repo:

      - **metadata.json**: This file will contain some basic information about your extension:

            - **name**: The name of your extension - rename this field to describe what your assistant will docs
            - **type**: For any Coach extension, the default value is “helper”
            - **user_type**: Describes who will be able to see the extension - choose one of 3 possible values: “learner”, “instructor”, “all”
            - **component**: For any Coach extension, the default value is "assignment"

      - **index.js**: This file will contain the Javascript code for the extension.

   - The index.js file has a simple example of how you can use the `Coach API <https://codio.github.io/client/codioIDE.coachBot.html>`_ to create your own assistant.


3. Edit the metadata.json file (rename the extension, choose user_type). Save and commit the changes to your branch.

4. Refer to the `API documentation <https://codio.github.io/client/codioIDE.coachBot.html>`_ and edit the index.js file with the Javascript code for your assistant. The example gives some context about the API elements and how you can use them. Save and commit the changes to your branch.

5. Now that the code for the extension is complete, you’ll have to create a Release for your repository, making it deployable and ready to use. Navigate back to your repository and on the right panel, click on “Create a new release”.


   .. image:: /img/coach-release-repo.png
      :alt: Showing how to create a new release for your repository



6. On this page, in the tags field, write and create a new tag by referring to the tagging suggestions on the right panel. Enter a name and description for this release, and click on the **Publish release** button at the very bottom of the page.


   .. image:: /img/coach-publish-release.png
      :alt: Publish Release button




Testing your custom assistant in Coach
--------------------------------------

If you’d like to test your assistant before deploying it to your organization, you can add it to your Codio account first, as follows:

1. Navigate to your extension's Github repository and copy the webpage URL: it should look something like this: `https://github.com/<your-github-username>/<extension-repository-name>`

2. Login to your Codio account, and click on your username or Avatar on the bottom left corner of your screen to open Account Settings.

3. Now click on Extensions at the bottom of the list, and then click on the Add extension button.


   .. image:: /img/add-extension-button.png
      :alt: Add extension from Extensions tab in Codio



4. Paste the URL of your Github repository’s webpage that you copied in step 1, and click Add Extension. You should now see it pop up as an Inactive Extension. To deploy the assistant to your account, click Use. Now it is active and you’ll be able to test it by opening any assignment in a course where you’re a teacher.

   .. Note::  By adding an extension to your account, it will **only be visible to you**, and not your students, even If you’ve chosen “learner” or “all” as the user_type in the metadata.json file. This will let you test your assistant, giving you the ability to make changes to it before deploying it for your organization.


   .. image:: /img/add-extension-url.png
      :alt: Enter external URL and press Add Extension



Deploying a custom assistant to your organization
-------------------------------------------------

Now that you have authored and tested your very own custom AI assistant, let’s look at the steps to deploy it in your organization:

1. Navigate to your extension’s Github repository and copy the webpage URL: it should look something like this: `https://github.com/<your-github-username>/<extension-repository-name>`

2. Login to your Codio account, and click on your username or Avatar on the bottom left corner of your screen to open Account Settings.

3. Click on Organizations and choose an Organization that you’re an owner of - this is how you’ll be able to set up your assistant as an extension. If you’re not an owner, contact your Organization Admin to help you set it up.

4. Now click on Extensions, and then click on the Add extension button.

5. Paste the URL of your Github repository’s webpage that you copied in step 1, and click Add Extension. You should now see it pop up as an Inactive Extension. To deploy the assistant to your account, click Use. Now it is active and deployed in your organization.


.. Note::  **This is an experimental feature**. By adding an assistant to your organization, it will automatically be deployed to every course in that organization. We’re currently working on a way for instructors to have more flexibility and control over deploying custom assistants to specific courses and assignments.
