.. _junit:

JUnit Testing Framework
=======================

Codio provides a simple way to test Java in your project using [JUnit](https://junit.org/junit4/). To use JUnit, your project requires Java. Use one of the following methods to make sure your project uses Java:

- Use the [Java 8](https://codio.com/home/stacks/cf71b65b-ab7a-4f9b-9885-34009fccb476/?tab=details) stack.
- Manually install Java on your box.
- Install Java from **Tools > Install Software**. See :ref:`Install Software Packages <box_parts>` for more information.

Configure JUnit
---------------
To configure to use JUnit for Java testing, follow these steps:

1. Click **Tools** on the menu bar and choose **JUnit**. You can also use the shortcut **Shift+Alt+J**.

   ..image:: /img/junit.png
     :alt: JUnit Settings

2. Complete the fields on the **JUnit Settings** page:

   - **JUnit version** - Select the version from the drop-down list.   
   - **Source path** - Location of the source code.
   - **Test source path** - Location of the test cases source folder.
   - **Library path** - Path to any libraries used by the project.
   - **Working directory** - Path where the compiled code should execute.
   - **Add test case** - Specify the paths to a file with JUnit tests or drag and drop the file into the JUnit field.

**Notes:** 

- All paths are relative to the root of the workspace folder.
- If using multiple cases in an assignment/project, the files for each should all be in separate folders for them to work independently of each other. This applies to student code files as well as the code used for the cases.

Timeout settings
----------------

The default timeout for JUnit execution is 30 seconds. You can change the timeout and default hotkey in :ref:`User Preferences <user-prefs>` or :ref:`Project Preferences <project-prefs>`. To ensure that the same settings apply to all students using the same project, we recommend changing the timeout and hotkey in Project Preferences.

.. image:: /img/junitsettings.png
   :alt: JUnit Preferences

Execute JUnit Test
------------------
You execute the tests from the **JUnits Execution** page (**Tools > JUnit > Junit Executions**). Once completed, the results are shown on the page.

.. image:: /img/junitexecution.png
   :alt: JUnit Execute

If you publish your project as a unit to a class, the JUnit configurations you set up are included in the unit for students.
