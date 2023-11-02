.. meta::
   :description: The advanced code test assessment type allows you to easily implement unit tests, style checkers, or write custom code tests in any language that grades student-written code.
   
.. _advanced-code-test:

Advanced Code Test
==================
The advanced code test assessment type allows you to easily implement unit tests, style checkers, or write custom code tests in any language that grades student-written code. 

To ensure that your test scripts run securely and to prevent student access to your testing files or executables, place them in the **.guides/secure** folder. This folder is not available to students in their assignments and they cannot access it from the command line. Only teachers with editing privileges have access to the **.guides/secure** folder.


    .. Note::  If your assignment will contain multiple assessments, Code files and Test Cases for individual assessments should be placed in separate folders to avoid compiling all files. 

Complete each section to set up your advanced code test.

1. On the **General** page, enter the following information:

   .. image:: /img/guides/assessment_general.png
      :alt: General

   - **Name** - Enter a short name that describes the test. This name is displayed in the teacher dashboard so the name should reflect the challenge and thereby be clear when reviewing.

     Toggle the **Show Name** setting to hide the name in the challenge text the student sees.
     
   - **Instructions** - Enter text that is shown to the student using optional Markdown formatting.

2. Click **Execution** in the navigation pane and complete the following information:

   - **Language Type** - Click the drop-down and choose the language. The following language-specific frameworks are explicitly supported:

     - **Ruby**: `RuboCop`_ or `RSpec`_
     - **Java**: `JUnit`_ or `checkstyle`_
     - **Python**: `pycodestyle`_ or `UnitTest`_
     - **JavaScript**: `JSHint and JSLint`_
     - **Custom**: for a `custom`_ auto-grading script in any language
     
   - **Language Assessment Subtype** - Click the drop-down and choose a subtype for the selected language type, if applicable.
   
   - **Timeout** - Where you can amend the timeout setting for the code to execute. Arrows will allow you to set max 300 (sec), if you require longer, you can manually enter the timeout period.

4. Click on the **Parameters** tab if you wish to set up **Parameterized Assessments**. See :ref:`Parameterized Assessments <parameterized>` for more information.

3. Click **Grading** in the left navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_grading.png
      :alt: Grading

  - **Points** - The score given to the student if the code test passes. You can enter any positive numeric value. If this assessment should not be graded, enter 0 points.
  - **Allow Partial Points** - Toggle to enable a percentage of total points to be given based on the percentage correctly answered. See :ref:`Allow Partial Points <partial-points>` for more information.
  - **Define Number of Attempts** - enable to allow and set the number of attempts students can make for this assessment. If disabled, the student can make unlimited attempts.
  - **Show Rationale to Students** - Toggle to display the rationale for the answer to the student. This guidance information will be shown to students after they have submitted their answer and any time they view the assignment after marking it as completed. You can set when to show this selecting from **Never**, **After x attempts**, **If score is greater than or equal to a % of the total** or **Always**
  - **Rationale** - Enter guidance for the assessment. This is always visible to the teacher when the project is opened in the course or when opening the student's project. 

5. Click **Metadata** in the left navigation pane and complete the following fields:

   .. image:: /img/guides/assessment_metadata.png
      :alt: Metadata

  - **Bloom's Level** - Click the drop-down and choose the level of Bloom's Taxonomy: https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/ for the current assessment.
  - **Learning Objectives** The objectives are the specific educational goal of the current assessment. Typically, objectives begin with Students Will Be Able To (SWBAT). For example, if an assessment asks the student to predict the output of a recursive code segment, then the Learning Objectives could be *SWBAT follow the flow of recursive execution*.
  - **Tags** - The **Content** and **Programming Language** tags are provided and required. To add another tag, click **Add Tag** and enter the name and values.

6. Click **Files** in the left navigation pane and check the check boxes for additional external files to be included with the assessment when adding it to an assessment library. The files are then included in the **Additional content** list.

   .. image:: /img/guides/assessment_files.png
      :alt: Files

7. Click **Create** to complete the process.

Example Grading Scripts for Unit Testing
----------------------------------------------

As mentioned before, you can use multiple languages for your Unit Testing. Codio natively supports Java, Python and Ruby. You can also use any other language setting the ``LANGUAGE TYPE`` to **Custom**, in this example we will use JavaScript.

.. tabs::

    .. code-tab:: Java

         package demo.tests;
         import static org.junit.Assert.*;
         import org.junit.AfterClass;
         import org.junit.BeforeClass;
         import org.junit.Test;

         public class JUnitProgram {

            @BeforeClass
            public static void BeforeTests() {
               /*
               Use this space to create objects and definitions.
               This code will run once before all tests.
               */
            }

            @Test
            public void Test1() {
               // Do something with your students' code.
               String str1 = "This is first the testcase in this class";
               assertEquals("This is first the testcase in this class", str1);
            }

            @Test
            public void Test2() {
               // Do something with your students' code.
               String str2 = "This is the second testcase in this class";
               assertEquals("This is the second testcase in this class", str2);
            }

            @AfterClass
            public static void AfterTests() {
               /*
               Use this space to clean your execution or execute final instructions.
               */
            }
         }

    .. code-tab:: JavaScript

         const assert = require('assert');

         describe('TestProgram', function() {
            before(function() {
               // Use this space to create objects and definitions.
               // This code will run once before all tests.
            });

            it('test_1', function() {
               // Do something with your students' code.
               const str1 = "This is first the testcase in this class";
               assert.strictEqual(str1, "This is first the testcase in this class");
            });

            it('test_2', function() {
               // Do something with your students' code.
               const str2 = "This is the second testcase in this class";
               assert.strictEqual(str2, "This is the second testcase in this class");
            });

            after(function() {
               // Use this space to clean your execution or execute final instructions.
            });
         });


    .. code-tab:: Python 

         import unittest

         class TestProgram(unittest.TestCase):

            @classmethod
            def setUpClass(cls):
               """
               Use this space to create objects and definitions.
               This code will run once before all tests.
               """
               pass

            def test_1(self):
               # Do something with your students' code.
               str1 = "This is first the testcase in this class"
               self.assertEqual(str1, "This is first the testcase in this class")

            def test_2(self):
               # Do something with your students' code.
               str2 = "This is the second testcase in this class"
               self.assertEqual(str2, "This is the second testcase in this class")

            @classmethod
            def tearDownClass(cls):
               """
               Use this space to clean your execution or execute final instructions.
               """
               pass

         if __name__ == '__main__':
            unittest.main()

    .. code-tab:: Ruby

         RSpec.describe "TestProgram" do
            before(:all) do
               # Use this space to create objects and definitions.
               # This code will run once before all tests.
            end

            it 'test_1' do
               # Do something with your students' code.
               str1 = "This is first the testcase in this class"
               expect(str1).to eq("This is first the testcase in this class")
            end

            it 'test_2' do
               # Do something with your students' code.
               str2 = "This is the second testcase in this class"
               expect(str2).to eq("This is the second testcase in this class")
            end

            after(:all) do
               # Use this space to clean your execution or execute final instructions.
            end
         end

For each language, you have multiple methods and attributes you can use. The examples above are using two tests, together with the two methods that are executed at the beginning and at the end of the execution of the tests.

As a general rule, make sure that your code always exits with code ``0``. That way Codio can assign partial points. If your code exits with an error, Codio will grade the assessment with ``0``.

Keep in mind that each language has its own syntax, here you have some notes about them:

----------------------
JUnit
----------------------
 `JUnit (website link)`_ is a Java testing framework. Currently Codio supports JUnit 4 and JUnit 5 so you can choose any one of them as per your requirement.
  
 When using JUnit in Codio, specify the Java files containing JUnit tests you'd like to run under the **ADD CASE:** option.
 
 If you have more then one test, by default, the student will need to pass all tests to earn the specified number of points. You can toggle on **ALLOW PARTIAL POINTS** to have Codio evenly weight each test.
 
 There are 4 *optional* configurations for more complex file structures:
 
 - **SOURCE PATH** - specifies where the student code being tested is
 - **TESTS SOURCE PATH** - specifies where non-test-case test helper files are
 - **LIBRARY PATH** - specifies where .jar files needed to run the student code or test code at
 - **WORKING DIRECTORY** - specifies where in the file tree the actual test will run

 All code files **Source path** will be compiled. Files that fail to compile successfully will cause the tests to fail, even if they are not used.
 Codio has a :ref:`JUnit <junit>` runner for building JUnit tests.

 .. _Junit (website link): https://junit.org/junit4/

----------------------
Custom
----------------------

In the example above, we are using a JavaScript example, but you can use any language and any framework. To execute this code we are using ``Mocha``, a popular node library for Unit Testing.

If you choose **Custom**, enter the following information:

   .. image:: /img/guides/assessment_act_exec_custom.png
      :alt: Custom

   - **Command** - Enter the command that executes the student code. 

    .. Note:: If you store the assessment scripts in the **.guides/secure** folder, they run securely and students cannot see the script or the files in the folder. 
      
    The files can be dragged and dropped from the File Tree into the field to automatically populate the necessary execution and run code.
      
  - **Timeout** - Enter the time period (in seconds) that the test runs before terminating.

  - **Allow Partial Points** - Toggle to enable partial points, the grade is then based on the percentage of test cases the code passes. See :ref:`Allow Partial Points <partial-points>` for more information.

----------------------
UnitTest
----------------------

 `UnitTest (website link)`_ is a python testing framework.
  
 When using python UnitTest in Codio, specify the python files containing UnitTest tests you'd like to run under the **ADD CASE:** option.
 
 Specify whether you are running python 2 (`python`) or python 3 (`python3`) under **PYTHON EXECUTABLE**.
 
 If you have more then one test, by default, the student will need to pass all tests to earn the specified number of points. You can toggle on **ALLOW PARTIAL POINTS** to have Codio evenly weight each test.
 
 There are 2 *optional* configurations for more complex file structures:
 
 - **PYTHON WORKING DIRECTORY** - specifies where in the file tree the actual test will run
 - **STUDENT FOLDER** - specifies where the student code being tested is
 
.. _UnitTest (website link): https://docs.python.org/3/library/unittest.html

----------------------
RSpec
----------------------

 `RSpec (website link)`_ is a Ruby testing suite.
 
 To check if RSpec is already installed on your stack, simply run `rspec` from the command line. If it is not installed, you can easily install it either via the command line (`gem install rspec`) or using **bundler** by adding it to your Gemfile. 
 
 When using RSpec in Codio, specify the ruby files containing RSpec tests you'd like to run under the **ADD CASE:** option.
 
 If you have more then one test, by default, the student will need to pass all tests to earn the specified number of points. You can toggle on **ALLOW PARTIAL POINTS** to have Codio evenly weight each test.
 
.. _RSpec (website link): https://rspec.info/

Grading Code Using Linters
----------------------------------------------

As a general rule, all linters will give either all or zero points. Since linters are not native to the language, it is very likely that you will need to install them (with the exception of pycodestyle that is already installed in our Codio certified Python stack). 

Linters usually don't require configuration files or definitions. You just need to the add the files you want to check and they will automatically give feedback to the student. 

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
  
.. _checkstyle (website link): https://checkstyle.sourceforge.io/
.. _Google configuration: https://github.com/checkstyle/checkstyle/blob/2954d8723003ef229f5825510a433ab8c60f2774/src/main/resources/google_checks.xml
.. _Sun configuration: https://github.com/checkstyle/checkstyle/blob/13481f2c410e4944ecf5ab93ec49948a523a0c82/src/main/resources/sun_checks.xml
.. _create your own configuration: https://checkstyle.sourceforge.io/config.html

----------------------
JSHint and JSLint
----------------------

**JSHint** or **JSLint** must first be installed as a Node.js global package using the following command:

``sudo npm install -g jshint jslint``

To add individual JavaScript source files for style checking, either enter their relative path to `~/namespace` or drag them from the File Tree into the **Add Case** text box and click **Add Case**. You may add as many cases as needed. 

You can also choose **JSLint** or **JSHint** in the **Language Assessment Subtype** drop-down menu. When the assessment executes, each added file is inspected and outputs all styling issues that were found.

----------------------
pycodestyle
----------------------

.. image:: /img/guides/assessment_act_exec_pycodestyle.png
   :alt: Pycodestyle

To add individual Python source files whose style should be checked, either enter their relative path to `~/namespace` or drag them from the File Tree into the **Add Case** text box and click **Add Case**. You may add as many cases as needed. When the assessment executes, ``pycodestyle`` inspects each added file and outputs all styling issues.

----------------------
RuboCop
----------------------

 `RuboCop (website link)`_ is a Ruby Linter.
 
 To check if RuboCop is already installed on your stack, simply run `rubocop` from the command line. If it is not installed, you can easily install it either via the command line (`gem install rubocop`) or using **bundler** (by adding `gem 'rubocop', require: false` to your Gemfile). 
 
 When using Rubocop in Codio, specify the Ruby files you'd like RuboCop to check under the **ADD CASE:** option.
 
 The student will need to follow all style conventions to earn full credit on the assessment.
 
.. _RuboCop (website link): https://rubocop.org/

See More Working Examples
----------------------
To see an example of a specific unit test or style checker, see the Starter Pack in the corresponding language: 

Go to **Starter Packs** and search for **Advanced Features in Python** if not already loaded in your **My Projects** area. Click **Use Pack** and then **Create** to install it to your Codio account.

Information about C++ unit testing using GoogleTest is available in the **C++ Unit Testing Using GoogleTest** Starter Pack.

Additionally, Codio pre-populates a project in **My Projects** called **Demo Guides and Assessments** that contains examples for all assessment types and a guides authoring cheat sheet. If you do not see this project, go to **Starter Packs** and search for **Demo Guides and Assessments**. Click **Use Pack** and then **Create** to make a copy in your **My Projects** area.

