.. meta::
   :description: The advanced code test assessment type allows you to easily implement unit tests, style checkers, or write custom code tests in any language that grades student-written code.
   
.. _advanced-code-test:

Advanced Code Test
==================
The advanced code test assessment type allows you to easily implement unit tests, style checkers, or write custom code tests in any language that grades student-written code. 

To ensure that your test scripts run securely and to prevent student access to your testing files or executables, place them in the **.guides/secure** folder. Create a folder if one does not already exist. This folder is not available to students in their assignments and they cannot access it from the command line. Only teachers with editing privileges have access to the **.guides/secure** folder.


.. Note::  If your assignment will contain multiple assessments, Code files and Test Cases for individual assessments should be placed in separate folders to avoid compiling all files. 


Complete each section to set up your advanced code test. For more information on **General**, **Metadata** and **Files** see :ref:`Assessments <assessments>`.

1. Complete **General**.

2. Click **Execution** in the navigation pane and complete the following information:

   - **Language Type** - Click the drop-down and choose the language. The following language-specific frameworks are explicitly supported:

     - **Custom**: for a `custom`_ auto-grading script in any language
     - **Ruby**: `RuboCop`_ or `RSpec`_
     - **Java**: `checkstyle`_ or `JUnit`_
     - **Python**: `pycodestyle`_ or `UnitTest`_
     - **JavaScript**: `JSHint and JSLint`_
     
.. Note:: For more information, see the :ref:`test-types` section or click any test name above to navigate directly to that section.

- **Language Assessment Subtype** - Click the drop-down and choose a subtype for the selected language type, if applicable.
   
- **Timeout** - You can amend the timeout setting for the code to execute. Arrows will allow you to set max 300 (sec). If you require longer, you can manually enter the timeout period.

3. Click **Grading** in the top navigation pane and complete the following fields:

   .. image:: /img/guides/ACTGradingScreen.png
      :alt: Grading
      :width: 500px

  - **Points** - The score given to the student if the code test passes. You can enter any positive numeric value. If this assessment should not be graded, enter 0 points.
  - **Partial Points** - Toggle to enable a percentage of total points to be given based on the percentage correctly answered. Note that it's not enough to turn partial points on; the advanced code test has to be written to handle partial points.  See :ref:`Partial Points <partial-points>` for more information.
  - **Define Number of Attempts** - enable to allow and set the number of attempts students can make for this assessment. If disabled, the student can make unlimited attempts.
  - **Show Rationale to Students** - Toggle to display the rationale for the answer to the student. This guidance information will be shown to students after they have submitted their answer and any time they view the assignment after marking it as completed. You can set when to show this selecting from **Never**, **After x attempts**, **If score is greater than or equal to a % of the total** or **Always**
  - **Rationale** - Enter guidance for the assessment. This is always visible to the teacher when the project is opened in the course or when opening the student's project. 
  - **Use maximum score** - Toggle to enable assessment final score to be the highest score attained of all runs.

5. **(Optional)** Complete **Metadata**.

6. **(Optional)** Complete **Files**.

7. Click **Create** to complete the process.


See a Working Example
----------------------
To see an example of a specific unit test or style checker, see the Starter Pack in the corresponding language: 

- Go to **Starter Packs** and search for **Advanced Features in Python** if not already loaded in your **My Projects** area. Click **Use Pack** and then **Create** to install it to your Codio account.

- Information about C++ unit testing using GoogleTest is available in the **C++ Unit Testing Using GoogleTest** Starter Pack.

- Additionally, Codio pre-populates a project in **My Projects** called **Demo Guides and Assessments** that contains examples for all assessment types and a guides authoring cheat sheet. If you do not see this project, go to **Starter Packs** and search for **Demo Guides and Assessments**. Click **Use Pack** and then **Create** to make a copy in your **My Projects** area.


.. _test-types:

Test Types
----------

----------------------
RuboCop
----------------------

`RuboCop (website link)`_ is a Ruby Linter.
 
To check if RuboCop is already installed on your stack, simply run `rubocop` from the command line. If it is not installed, you can easily install it either via the command line (`gem install rubocop`) or using **bundler** (by adding `gem 'rubocop', require: false` to your Gemfile). 
 
When using Rubocop in Codio, specify the Ruby files you'd like RuboCop to check under the **ADD CASE:** option.
 
The student will need to follow all style conventions to earn full credit on the assessment.
 
.. _RuboCop (website link): https://rubocop.org/


----------------------
RSpec
----------------------

`RSpec (website link)`_ is a Ruby testing suite.
 
To check if RSpec is already installed on your stack, simply run `rspec` from the command line. If it is not installed, you can easily install it either via the command line (`gem install rspec`) or using **bundler** by adding it to your Gemfile. 
 
When using RSpec in Codio, specify the ruby files containing RSpec tests you'd like to run under the **ADD CASE:** option.
 
If you have more than one test, by default, the student will need to pass all tests to earn the specified number of points. You can toggle on **ALLOW PARTIAL POINTS** to have Codio evenly weight each test.
 
.. _RSpec (website link): https://rspec.info/


----------------------
JUnit
----------------------
`JUnit (website link)`_ is a Java testing framework. Currently Codio supports JUnit 4 and JUnit 5 so you can choose any one of them as per your requirement.
  
When using JUnit in Codio, specify the Java files containing JUnit tests you'd like to run under the **ADD CASE:** option.
 
If you have more than one test, by default, the student will need to pass all tests to earn the specified number of points. You can toggle on **ALLOW PARTIAL POINTS** to have Codio evenly weight each test.
 
There are 4 *optional* configurations for more complex file structures:
 
 - **SOURCE PATH** - Specifies the location of the student code being tested.
 - **TESTS SOURCE PATH** - Specifies the location of non-test-case test helper files.
 - **LIBRARY PATH** - Specifies the location of .jar files needed to run the student code or test code.
 - **WORKING DIRECTORY** - Specifies where in the file tree the test will run.

All code files **SOURCE PATH** will be compiled. Files that fail to compile successfully will cause the tests to fail, even if they are not used.
Codio has a :ref:`JUnit <junit>` runner for building JUnit tests.
 
-----------------------------------
Custom Feedback with JUnit in Codio
-----------------------------------
When using JUnit in Codio, you can add your own custom feedback to the standard feedback Junit returns to students. The feedback message is passed to the assert method as the first parameter. 

`assertEquals(feedback, expected, actual)`
 
.. _Junit (website link): https://junit.org/junit5/

----------------------
checkstyle
----------------------

`checkstyle (website link)`_ is a Java linter.
  
When using checkstyle in Codio, specify the configuration file under **CONFIG PATH** -- you can use the `Google configuration`_, `Sun configuration`_, or `create your own configuration`_.
 
Select the **CHECKSTYLE VERSION**, by default the appropriate version is selected according to your installed Java version but you can also select one of the available options:

  - Checkstyle v10.12(JRE 11 and above)

  - Checkstyle v8.24(JRE 8 and above)

  - Checkstyle v8.9(JRE 8)

  - Checkstyle v6.6(JRE 6 and 7)


Specify the Java files you'd like Checkstyle to check under the **ADD CASE:** option.
 
The student will need to follow all style conventions to earn full credit on the assessment.
  
.. _checkstyle (website link): https://checkstyle.sourceforge.io/
.. _Google configuration: https://github.com/checkstyle/checkstyle/blob/2954d8723003ef229f5825510a433ab8c60f2774/src/main/resources/google_checks.xml
.. _Sun configuration: https://github.com/checkstyle/checkstyle/blob/13481f2c410e4944ecf5ab93ec49948a523a0c82/src/main/resources/sun_checks.xml
.. _create your own configuration: https://checkstyle.sourceforge.io/config.html

----------------------
pycodestyle
----------------------

If you want to use pycodestyle, you must first install it. Use the following commands to install pycodestyle:

.. code:: ini

  sudo apt update
  sudo apt install python3-pip
  sudo python3 -m pip install pycodestyle

.. image:: /img/guides/assessment_act_exec_pycodestyle.png
   :alt: Pycodestyle

To add individual Python source files whose style should be checked, either enter their relative path to `~/namespace` or drag them from the File Tree into the **Add Case** text box and click **Add Case**. You may add as many cases as needed. When the assessment executes, ``pycodestyle`` inspects each added file and outputs all styling issues.

----------------------
UnitTest
----------------------

`UnitTest (website link)`_ is a python testing framework.


**Configuration**

1. Under **ADD CASE**, specify the Python files containing your UnitTest tests.

2. Under **PYTHON EXECUTABLE**, specify whether you are running Python 2 (``python``) or Python 3 (``python3``).

3. **Scoring**: By default, students must pass all tests to earn the specified points. Toggle on **ALLOW PARTIAL POINTS** to evenly weight each test.

**Optional Configurations**

For more complex file structures, you can configure:

- **PYTHON WORKING DIRECTORY** - Specifies where in the file tree the test will run
- **STUDENT FOLDER** - Specifies the location of the student code being tested

**Working Example:** Advanced Features in Python `Starter Pack <https://docs.codio.com/develop/develop/packs/packs.html>`_

.. _UnitTest (website link): https://docs.python.org/3/library/unittest.html


----------------------
JSHint and JSLint
----------------------

**JSHint** or **JSLint** must first be installed as a Node.js global package using the following command:

``sudo npm install -g jshint jslint``

To add individual JavaScript source files for style checking, either enter their relative path to `~/namespace` or drag them from the File Tree into the **Add Case** text box and click **Add Case**. You may add as many cases as needed. 

You can also choose **JSLint** or **JSHint** in the **Language Assessment Subtype** drop-down menu. When the assessment executes, each added file is inspected and outputs all styling issues that were found.

----------------------
Custom
----------------------

If you choose **Custom**, enter the following information:

.. image:: /img/guides/assessment_act_exec_custom.png
   :alt: Custom
   :width: 500px

- **Command** - Enter the command that executes the student code. 
      
The files can be dragged and dropped from the File Tree into the field to automatically populate the necessary execution and run code.
      
- **Timeout** - Enter the time period (in seconds) that the test runs before terminating.


