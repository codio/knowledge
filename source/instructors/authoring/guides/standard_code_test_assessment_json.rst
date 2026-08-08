.. meta::
   :description: This page explains how to create a Standard Code Test assessment that works in Codio.

.. _standard-code-test-assessment-json:

Standard Code Test assessment JSON
==================================

A Standard Code Test assessment in Codio is stored as a JSON file in the
``.guides/assessments`` directory.

This assessment type runs a command, optionally passes command-line arguments
or standard input, and compares the program output against expected output.

In the assessment JSON, Standard Code Tests use the assessment type
``code-output-compare``.

File location and naming
------------------------

Store each assessment in:

.. code-block:: text

   .guides/assessments/

Use this filename pattern:

.. code-block:: text

   code-output-compare-<unique-id>.json

The ``<unique-id>`` portion is a numeric string made of random numbers, for
example:

.. code-block:: text

   code-output-compare-1075712907.json

Examples may use 9-digit or 10-digit numeric strings. Do not use consecutive
numbers for this value.

The ``taskId`` value should match the filename stem exactly:

.. code-block:: json

   {
     "type": "code-output-compare",
     "taskId": "code-output-compare-1075712907",
     "source": {
       "name": "Fibonacci sequence"
     }
   }

For example, this file:

.. code-block:: text

   .guides/assessments/code-output-compare-1075712907.json

should use this value:

.. code-block:: json

   "taskId": "code-output-compare-1075712907"

To embed this Standard Code Test assessment in a guide, use:

.. code-block:: md

   {Check It!|assessment}(code-output-compare-1075712907)

Use ``{Check It!|assessment}`` exactly as shown, with no spaces before the closing brace.

Structure
---------

A Standard Code Test assessment uses this structure. This example uses the
default values shown in the available settings for this assessment type.

.. code-block:: json

   {
     "type": "code-output-compare",
     "taskId": "code-output-compare-1075712907",
     "source": {
       "name": "Assessment name",
       "showName": true,
       "instructions": "Submit your code to the auto-grader.",
       "command": "python fib.py",
       "preExecuteCommand": "",
       "options": {
         "timeout": 30,
         "ignoreCase": true,
         "ignoreWhitespaces": true,
         "ignoreNewline": true,
         "matchSubstring": false
       },
       "metadata": {
         "tags": [
           {
             "name": "Assessment Type",
             "value": "Standard Code Test"
           }
         ],
         "files": [],
         "opened": []
       },
       "bloomsObjectiveLevel": "",
       "learningObjectives": "",
       "guidance": "",
       "showGuidanceAfterResponseOption": {
         "type": "Never"
       },
       "maxAttemptsCount": 0,
       "points": 20,
       "showExpectedAnswerOption": {
         "type": "Always"
       },
       "arePartialPointsAllowed": true,
       "useMaximumScore": false,
       "sequence": [
         {
           "arguments": "5",
           "input": "",
           "output": "0 1 1 2 3 \n",
           "showFeedback": false,
           "feedback": ""
         }
       ]
     }
   }

Field reference
---------------

Top-level fields
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 16 64

   * - Field
     - Type
     - Description
   * - ``type``
     - string
     - Required assessment type. Use ``"code-output-compare"``.
   * - ``taskId``
     - string
     - Assessment identifier. Uses the pattern
       ``code-output-compare-<numeric-id>`` and should match the filename stem
       exactly.
   * - ``source``
     - object
     - Contains the assessment content, command, comparison options, test
       sequence, rationale settings, and scoring options.

``source`` fields
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 16 56

   * - Field
     - Type
     - Description
   * - ``name``
     - string
     - Assessment name.
   * - ``showName``
     - boolean
     - Controls whether the assessment name is shown to learners. Default:
       ``true``.
   * - ``instructions``
     - string
     - The prompt, task description, or instructions shown to learners.
   * - ``command``
     - string
     - Command Codio runs for each test case, such as ``"python fib.py"`` or
       ``"python3 simple_interest.py"``.
   * - ``preExecuteCommand``
     - string
     - Optional command to run before the assessment command. Use ``""`` when
       no setup command is required.
   * - ``options``
     - object
     - Output comparison settings, including timeout and matching behavior.
   * - ``metadata``
     - object
     - Metadata container, including the Standard Code Test tag and optional
       file-opening information.
   * - ``bloomsObjectiveLevel``
     - string
     - Bloom's objective level. Default: ``""``. Available values shown here
       include ``""`` and ``"3"``.
   * - ``learningObjectives``
     - string
     - Optional learning objective text. Default: ``""``.
   * - ``guidance``
     - string
     - Rationale, hint, or solution text shown according to
       ``showGuidanceAfterResponseOption``. Default: ``""``.
   * - ``showGuidanceAfterResponseOption``
     - object
     - Controls when rationale or guidance is shown. Only one ``type`` value
       can be used at a time. Default shown here: ``{"type": "Never"}``.
   * - ``maxAttemptsCount``
     - integer
     - Maximum number of attempts. ``0`` allows unlimited attempts. Available
       values shown here include ``0`` and ``5``.
   * - ``points``
     - number
     - Points awarded for a correct response. Default shown here: ``20``.
   * - ``showExpectedAnswerOption``
     - object
     - Controls when the expected output is shown. Default shown here:
       ``{"type": "Always"}``.
   * - ``arePartialPointsAllowed``
     - boolean
     - Enables partial scoring across test cases. Default shown here:
       ``true``.
   * - ``useMaximumScore``
     - boolean
     - Enables maximum-score behavior across attempts. Default shown here:
       ``false``.
   * - ``sequence``
     - array
     - Array of test case objects. Each item defines arguments, input,
       expected output, and optional feedback.

``options`` fields
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 16 56

   * - Field
     - Type
     - Description
   * - ``timeout``
     - integer
     - Maximum runtime in seconds for each test command. Default shown here:
       ``30``.
   * - ``ignoreCase``
     - boolean
     - Ignores letter case during output comparison when ``true``. Default:
       ``true``.
   * - ``ignoreWhitespaces``
     - boolean
     - Ignores whitespace differences during output comparison when ``true``.
       Default: ``true``.
   * - ``ignoreNewline``
     - boolean
     - Ignores newline differences during output comparison when ``true``.
       Default: ``true``.
   * - ``matchSubstring``
     - boolean
     - When ``true``, the expected output can be matched as a substring of the
       learner's output. When ``false``, the output must match according to
       the other comparison options. Default shown here: ``false``.

``metadata`` fields
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 24 16 60

   * - Field
     - Type
     - Description
   * - ``tags``
     - array
     - Tag array for the assessment metadata. Default:
       ``[{"name": "Assessment Type", "value": "Standard Code Test"}]``.
   * - ``files``
     - array
     - Optional list of project files associated with the assessment. Default:
       ``[]``.
   * - ``opened``
     - array
     - Optional list of files Codio opens in the workspace for this assessment.
       Default: ``[]``.

``opened`` objects
~~~~~~~~~~~~~~~~~~

Each item in ``metadata.opened`` is an object that describes a file Codio should
open.

.. list-table::
   :header-rows: 1
   :widths: 24 16 60

   * - Field
     - Type
     - Description
   * - ``type``
     - string
     - The opened item type. Use ``"file"`` for files.
   * - ``panelNumber``
     - integer
     - The workspace panel where the file should open, such as ``0``.
   * - ``content``
     - string
     - File path to open, such as ``"exercise3.py"`` or ``"ex1/ex1.py"``.

``sequence`` objects
~~~~~~~~~~~~~~~~~~~~

Each item in ``sequence`` is one test case. Codio runs the assessment command
for each test case and compares the result to ``output``.

.. list-table::
   :header-rows: 1
   :widths: 24 16 60

   * - Field
     - Type
     - Description
   * - ``arguments``
     - string
     - Command-line arguments appended to the assessment command for this test
       case. Use ``""`` when no arguments are needed.
   * - ``input``
     - string
     - Standard input passed to the program for this test case. Use newline
       characters, such as ``"John\n10"``, for multiple input lines.
   * - ``output``
     - string
     - Expected output for this test case. Preserve required newline
       characters with ``\n``.
   * - ``showFeedback``
     - boolean
     - Shows the test-case feedback to learners when ``true``.
   * - ``feedback``
     - string
     - Feedback text for this test case. Use ``""`` when no feedback is
       needed.

Rationale display options
~~~~~~~~~~~~~~~~~~~~~~~~~

``showGuidanceAfterResponseOption`` is an object with a ``type`` field. Only
one ``type`` value can be used at a time.

.. list-table::
   :header-rows: 1
   :widths: 28 24 48

   * - ``type`` value
     - Additional field
     - Behavior
   * - ``"Attempts"``
     - ``passedFrom``
     - Show rationale starting from a specific attempt number.
   * - ``"Score"``
     - ``passedFrom``
     - Show rationale when the learner reaches the specified score threshold.
   * - ``"Always"``
     - None
     - Always show rationale.
   * - ``"Never"``
     - None
     - Never show rationale.
   * - ``"WhenGradesReleased"``
     - None
     - Show rationale when grades are released.

Expected answer display options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``showExpectedAnswerOption`` is an object with a ``type`` field.

.. list-table::
   :header-rows: 1
   :widths: 32 68

   * - ``type`` value
     - Behavior
   * - ``"Always"``
     - Always show the expected answer.
   * - ``"Never"``
     - Never show the expected answer.
   * - ``"WhenGradesReleased"``
     - Show the expected answer when grades are released.

Command-line arguments
----------------------

Use ``arguments`` when the learner's program should receive values through
``sys.argv`` or another command-line argument mechanism.

In this example, Codio runs ``python3 simple_interest.py`` and appends the
arguments from each test case.

.. code-block:: json

   {
     "type": "code-output-compare",
     "taskId": "code-output-compare-165558969",
     "source": {
       "name": "Simple Interest Calculator",
       "showName": true,
       "instructions": "Write a program that calculates the simple interest earned on an investment.",
       "command": "python3 simple_interest.py",
       "preExecuteCommand": "",
       "options": {
         "timeout": 30,
         "ignoreCase": true,
         "ignoreWhitespaces": true,
         "ignoreNewline": true,
         "matchSubstring": false
       },
       "metadata": {
         "tags": [
           {
             "name": "Assessment Type",
             "value": "Standard Code Test"
           }
         ],
         "files": [],
         "opened": []
       },
       "bloomsObjectiveLevel": "3",
       "learningObjectives": "SWBAT apply mathematical formulas in programming to solve real-world financial problems involving simple interest calculations.",
       "guidance": "This solution implements the simple interest calculation using basic arithmetic operations and string formatting.",
       "showGuidanceAfterResponseOption": {
         "type": "Never"
       },
       "maxAttemptsCount": 0,
       "points": 20,
       "showExpectedAnswerOption": {
         "type": "Always"
       },
       "arePartialPointsAllowed": true,
       "useMaximumScore": false,
       "sequence": [
         {
           "arguments": "1000 5 3",
           "input": "",
           "output": "Interest earned: $150.00\nFinal amount: $1150.00\n",
           "showFeedback": true,
           "feedback": "Check your simple interest formula and ensure you're formatting the output correctly with 2 decimal places."
         },
         {
           "arguments": "500 4.5 2",
           "input": "",
           "output": "Interest earned: $45.00\nFinal amount: $545.00\n",
           "showFeedback": true,
           "feedback": "Verify that your program handles decimal interest rates correctly and formats the output properly."
         }
       ]
     }
   }

Standard input
--------------

Use ``input`` when the learner's program should receive values through standard
input, such as Python's ``input()`` function.

Use ``\n`` between input values that should be entered on separate lines.

.. code-block:: json

   {
     "type": "code-output-compare",
     "taskId": "code-output-compare-454810909",
     "source": {
       "name": "Other settings",
       "showName": true,
       "instructions": "Write a program that asks the user for their name and age, then tells them how old they'll be in 10 years.",
       "command": "python ex1/ex1.py",
       "preExecuteCommand": "",
       "options": {
         "timeout": 30,
         "ignoreCase": true,
         "ignoreWhitespaces": true,
         "ignoreNewline": true,
         "matchSubstring": true
       },
       "metadata": {
         "tags": [
           {
             "name": "Assessment Type",
             "value": "Standard Code Test"
           }
         ],
         "files": [],
         "opened": []
       },
       "bloomsObjectiveLevel": "",
       "learningObjectives": "",
       "guidance": "Consider getting what the user inputs in variables and then printing the result in the console.",
       "showGuidanceAfterResponseOption": {
         "type": "Attempts",
         "passedFrom": 3
       },
       "maxAttemptsCount": 5,
       "points": 20,
       "showExpectedAnswerOption": {
         "type": "Never"
       },
       "arePartialPointsAllowed": true,
       "useMaximumScore": true,
       "sequence": [
         {
           "arguments": "",
           "input": "John\n10",
           "output": "Hello, John!\nIn 10 years, you will be 20 years old.\n",
           "showFeedback": false,
           "feedback": ""
         },
         {
           "arguments": "",
           "input": "Mary\n24",
           "output": "Hello, Mary!\nIn 10 years, you will be 34 years old.\n",
           "showFeedback": false,
           "feedback": ""
         }
       ]
     }
   }

Matching a substring
--------------------

Set ``matchSubstring`` to ``true`` when the expected output only needs to
appear somewhere in the learner's output. This can be useful when a program
prints prompts before the final answer.

.. code-block:: json

   "options": {
     "timeout": 30,
     "ignoreCase": true,
     "ignoreWhitespaces": true,
     "ignoreNewline": true,
     "matchSubstring": true
   }

Set ``matchSubstring`` to ``false`` when the learner's output should match the
expected output more strictly, subject to the other comparison options.

Assessment files and opened files
---------------------------------

Use ``metadata.files`` to associate project files with the assessment, and use
``metadata.opened`` to open specific files in the workspace.

.. code-block:: json

   "metadata": {
     "tags": [
       {
         "name": "Assessment Type",
         "value": "Standard Code Test"
       }
     ],
     "files": [
       "fib.py",
       "ex1/ex1.py",
       "exercise3.py",
       "simple_interest.py"
     ],
     "opened": [
       {
         "type": "file",
         "panelNumber": 0,
         "content": "fib.py"
       },
       {
         "type": "file",
         "panelNumber": 0,
         "content": "ex1/ex1.py"
       },
       {
         "type": "file",
         "panelNumber": 0,
         "content": "exercise3.py"
       },
       {
         "type": "file",
         "panelNumber": 0,
         "content": "simple_interest.py"
       }
     ]
   }

Guide embedding example
-----------------------

A guide Markdown page can embed one or more Standard Code Test assessments.
Each embedded assessment uses the ``taskId`` without the ``.json`` extension.

.. code-block:: md

   # Practice checks

   {Check It!|assessment}(code-output-compare-1075712907)

   {Check It!|assessment}(code-output-compare-454810909)

   {Check It!|assessment}(code-output-compare-1600352608)

   {Check It!|assessment}(code-output-compare-165558969)

Authoring notes
---------------

* Keep the ``taskId`` and filename stem identical.
* Store the assessment JSON in ``.guides/assessments/``.
* Put learner-editable source files at the project root or in normal project folders outside ``.guides``.
* Use ``arguments`` for command-line input and ``input`` for standard input.
* Include trailing ``\n`` characters in ``output`` when the expected program output ends with a newline.
* Use ``showFeedback`` and ``feedback`` for per-test-case guidance.
* Use ``arePartialPointsAllowed`` when learners should receive credit for passing some, but not all, test cases.
