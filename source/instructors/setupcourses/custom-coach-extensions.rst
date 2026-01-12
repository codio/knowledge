.. meta::
   :description: Virtual Coach is an AI tool for assisting students with explanations, error messages, and hints.


.. _custom-coach-extensions:

Custom Assistants for Virtual Coach
===================================

You can extend the current capabilities of Coach by adding your own custom assistants as JavaScript extensions. You will need a Github account to get started. If you don't have one, follow the steps in the `GitHub documentation <https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github>`_.

Once you're signed in to your Github account, you will be able to create, install and test your custom AI assistant with Coach.

Customize or Use an Existing Custom Assistant as a JavaScript Extension
-----------------------------------------------------------------------

1. Click this link to view the `Codio Extensions GitHub repository <https://github.com/codio-extensions>`_ and scroll down to the Repositories section.

.. image:: /img/codio-extension-virtual-coach.png
   :alt: Codio-extensions

2. Choose one of the repositories that starts with **custom-assistant-example-<example_name>**

.. Note:: These examples are experimental and may receive small improvements and updates. If you're using them as is, please check the respective github repositories for the latest release available.

3. Click on the green **Use This Template** button or the `Fork <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo>`_ button, in the top right corner, to create a copy of the example repo, and give it a unique name - This will be your own copy of the custom assistant where you can make edits to the example code to customize your assistant.
    You'll see two files in your repo:
        -  **metadata.json**: This file will contain some basic information about your extension:
            1. **name**: The name of your extension - rename this field to describe what your assistant will do
            2. **type**: For any Coach extension, the default value is “helper”
            3.  **user_type**: Describes who will be able to see the extension - one of 3 possible values: “learner”, “instructor”, “all”
            4. **component**: For any Coach extension, the default value is "all"
        -  **index.js**: This file will contain the Javascript code for the extension.

    The **index.js** file has example code of how you can use the `Coach API <https://codio.github.io/client/codioIDE.coachBot.html>`_ to create your own assistant.

4. Edit the **metadata.json** file (rename the extension, choose **user_type**). Save and commit the changes to your branch.

5. Refer to the `API documentation <https://codio.github.io/client/codioIDE.coachBot.html>`_ and edit the **index.js** file with the Javascript code for your assistant.

.. _create-a-release:

Creating a Release
~~~~~~~~~~~~~~~~~~

When the code for the extension is complete, you'll need to create a **Release** for your repository, making it deployable and ready to use.
   
1. Navigate back to your repository and on the right panel, click on “Create a new release”.

.. image:: /img/creating-a-release-virtual-coach.png
   :alt: create-release-example

2. On this page, in the tags field, write and create a new tag by referring to the tagging suggestions on the right panel. Enter a name and description for this release, and click on the **Publish release** button at the very bottom of the page.

.. image:: /img/publish-release-virtual-coach.png
   :alt: publish-release-example


.. Note:: If you've made any changes, updates or edits to your code files (**index.js** or **metadata.js**) after creating a release, you need to create a new release to propagate those changes to your custom assistant.

.. _deploy-your-assistant:

Deploying a custom assistant to your organization
-------------------------------------------------

Now that you have authored and tested your custom AI assistant, follow these steps to deploy it in your organization:

1. Navigate to your extension's Github repository and copy the webpage URL: it should look something like this: `https://github.com/<your-github-username>/<extension-repository-name>`

2. Login to your Codio account, and click on your username in the upper right corner and select **Organizations** from the menu.

3. Choose an Organization that you're an owner of - this is how you'll set up your assistant as an extension. If you're not an owner, contact your Organization Admin to help you set it up.

4. Now click on :ref:`Extensions <org-extensions>`, and then click on the **Add extension** button.

5. Paste the URL of your Github repository's webpage that you copied in step 1, and click **Ok**. You should now see it pop up as an Inactive Extension. To deploy the assistant to your account, click the plug icon. Now it is active and deployed in your organization.


.. Note:: **This is an experimental feature**. Adding an assistant to your organization will make it available to be toggled on or off in every course in that organization. 

Applying updates to a custom assistant after creating a new release
-------------------------------------------------------------------

Once you've made more edits to your code files and created a new release, here's how you can apply the updates to your assistant:

1. Login to your Codio account, and click on your username in the upper right corner of your screen and select **Organizations**.
2. Choose an Organization that you're an owner of - this is how you'll be able to set up your assistant as an extension. If you're not an owner, contact your Organization Admin to help you set it up.
3. Now click on :ref:`Extensions <org-extensions>`. You should be able to see your Custom Assistant under Active Extensions.
4. Click on the **Check for Updates** button in the top right corner.
5. If there are any updates to be applied, you will be prompted to do so.

Using your own LLMs in custom assistants via Codio's LLM Proxy
--------------------------------------------------------------

If you'd prefer sending API requests to your own LLM (commercial or open-source) instead of Codio's built-in Anthropic LLM, you can do so by leveraging your Organization Level LLM API keys via Codio's LLM Proxy.

Please refer to our documentation on adding LLM API keys to your Codio Organization and enabling it for a course.
`Large Language Models in Codio <https://docs.codio.com/instructors/admin/organization/llms.html>`_

Once the API keys are set up and LLMs are enabled in your course, refer to the Coach Custom Assistants `API Reference <https://codio.github.io/client/codioIDE.coachBot.html#.getLlmProxyDetails>`_  to send requests and fetch responses from your own LLMs!

Testing your custom assistant using Development Mode
----------------------------------------------------

If you'd like to test your assistant before deploying it to your organization, you can use the Extension Development Mode to test it.


1. Navigate to your extension's GitHub repository, click on the green **Code** button, then click on SSH and copy the displayed URL.

2. Now, go back to your repository's home page, click on the **metadata.json** file and copy its contents.

3. Login to your Codio account, select **My Projects** from the **Build** menu and click the **New Project** button.

4. In the **Select your Starting Point** section, click **Import** and then paste the URL you copied in Step 1 in the URL field, and give your project a name in the **Add Details** section.

5. In the **Select the visibility** section, choose **Public**, and click **Create**. Your project will be opened.

6. Now, you should see the ``index.js`` file in the filetree on the left. Right-click (or ctrl-click) on it, and select **Preview Static** in the drop down menu.

7. This will open the file and display a web URL. Copy this web URL.

8. Go back to the homepage of your Codio account and click on your username in the upper right corner of your screen and select **Preferences**.

9. Now click on **Extensions** at the bottom of the list, and scroll down to the Development mode section.

.. image:: /img/vc-and-extensions/preference-extensions.png
    :alt: Development Mode for testing extensions

10. Paste the **index.js** webpage URL that you copied in Step 7 in the Source Code URL field.

11. Paste the contents of the metadata.json file that you copied in Step 2 in the **metadata** section, and click **Save changes**.

Now you can open any of your assignments or projects and your extension will be visible as a menu item in Coach. You can test and make changes and once you're happy with it, :ref:`create a release<create-a-release>` and :ref:`deploy your assistant<deploy-your-assistant>`.


.. Note:: By adding an extension to your account or testing it in Development mode, it will only be visible to you and not your students—regardless of the **user_type** in **metadata.json**. This allows you to test and refine your assistant before deploying it to your organization.


