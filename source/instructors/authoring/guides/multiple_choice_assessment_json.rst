.. meta::
   :description: This page explains how to create a multiple choice assessment that works in Codio.

.. _multiple-choice-assessment-json:

Multiple choice assessment JSON
===============================

A multiple choice assessment in Codio is stored as a JSON file in the
``.guides/assessments`` directory.

This assessment type supports both:

* single-answer multiple choice, where learners select one option
* multiple selection, where learners select more than one correct option

Use the same assessment type for both. The difference is controlled by the
``multipleResponse`` setting.

File location and naming
------------------------

Store each assessment in:

.. code-block:: text

   .guides/assessments/

Use this filename pattern:

.. code-block:: text

   multiple-choice-<unique-id>.json

The ``<unique-id>`` portion is a 10-digit numeric string made of random
numbers, for example:

.. code-block:: text

   multiple-choice-1214417678.json

Do not use consecutive numbers for this value.

The ``taskId`` value should match the filename stem exactly:

.. code-block:: json

   {
     "type": "multiple-choice",
     "taskId": "multiple-choice-1214417678",
     "source": {
       "name": "Programming basics"
     }
   }

For example, this file:

.. code-block:: text

   .guides/assessments/multiple-choice-1214417678.json

should use this value:

.. code-block:: json

   "taskId": "multiple-choice-1214417678"

To embed this multiple choice assessment in a guide, use:

.. code-block:: md

   {Text |assessment}(multiple-choice-1214417678)

Use ``|assessment}`` exactly as shown, with no spaces before the closing brace.

Structure
---------

A multiple choice assessment uses this structure. This example uses the
default values shown in the available settings for this assessment type.

.. code-block:: json

   {
     "type": "multiple-choice",
     "taskId": "multiple-choice-1214417678",
     "source": {
       "name": "Assessment name",
       "showName": true,
       "instructions": "Question text or instructions.",
       "multipleResponse": false,
       "isRandomized": false,
       "answers": [
         {
           "_id": "195edb63-54dd-51e6-29e0-ba5266450ef4",
           "correct": true,
           "answer": "Answer text"
         }
       ],
       "metadata": {
         "tags": [
           {
             "name": "Assessment Type",
             "value": "Multiple Choice"
           }
         ],
         "files": [],
         "opened": []
       },
       "bloomsObjectiveLevel": "",
       "learningObjectives": "",
       "guidance": "",
       "showGuidanceAfterResponseOption": {
         "type": "Attempts",
         "passedFrom": 1
       },
       "maxAttemptsCount": 1,
       "showExpectedAnswerOption": {
         "type": "Always"
       },
       "points": 20,
       "incorrectPoints": 0,
       "arePartialPointsAllowed": false,
       "useMaximumScore": false
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
     - Required assessment type. Use ``"multiple-choice"``.
   * - ``taskId``
     - string
     - Assessment identifier. Uses the pattern
       ``multiple-choice-<10-digit-number>`` and should match the filename
       stem exactly.
   * - ``source``
     - object
     - Contains the assessment content, answers, rationale settings, and
       scoring options.

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
     - The prompt, question text, or instructions shown to learners.
   * - ``multipleResponse``
     - boolean
     - Set to ``false`` for single-answer multiple choice. Set to ``true``
       for multiple selection. Default: ``false``.
   * - ``isRandomized``
     - boolean
     - Randomizes the order of answer options when ``true``. Default:
       ``false``.
   * - ``answers``
     - array
     - Array of answer objects. Each answer should have a unique ``_id``.
   * - ``metadata``
     - object
     - Metadata container.
   * - ``bloomsObjectiveLevel``
     - string
     - Bloom's objective level. Default: ``""``. Available values shown here
       are ``""``, ``"1"``, and ``"2"``.
   * - ``learningObjectives``
     - string
     - Optional learning objective text. Default: ``""``.
   * - ``guidance``
     - string
     - Rationale text shown according to
       ``showGuidanceAfterResponseOption``. Default: ``""``.
   * - ``showGuidanceAfterResponseOption``
     - object
     - Controls when rationale is shown. Only one ``type`` value can be used
       at a time. Default: ``{"type": "Attempts", "passedFrom": 1}``.
   * - ``maxAttemptsCount``
     - integer
     - Maximum number of attempts. Default: ``1``. Available values shown here
       include ``0``, ``1``, and ``9``.
   * - ``showExpectedAnswerOption``
     - object
     - Controls when the expected answer is shown. Default:
       ``{"type": "Always"}``.
   * - ``points``
     - number
     - Points awarded for a correct response. Default: ``20``. Available
       values shown here include ``0``, ``20``, and ``50``.
   * - ``incorrectPoints``
     - number
     - Score applied for an incorrect response. Default: ``0``. Available
       values shown here include ``0`` and ``25``.
   * - ``arePartialPointsAllowed``
     - boolean
     - Enables partial scoring. This is especially relevant when
       ``multipleResponse`` is ``true``. Default: ``false``.
   * - ``useMaximumScore``
     - boolean
     - Enables maximum-score behavior. Default: ``false``.

Answer objects
~~~~~~~~~~~~~~

Each item in ``answers`` is an object with the following fields.

.. list-table::
   :header-rows: 1
   :widths: 20 16 64

   * - Field
     - Type
     - Description
   * - ``_id``
     - string
     - Answer identifier. This is a 36-character UUID-format string using
       lowercase hexadecimal characters and hyphens, in the form
       ``8-4-4-4-12``.
   * - ``correct``
     - boolean
     - Marks whether the answer is correct.
   * - ``answer``
     - string
     - The answer text shown to learners.

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
       ``[{"name": "Assessment Type", "value": "Multiple Choice"}]``.
   * - ``files``
     - array
     - Default: ``[]``.
   * - ``opened``
     - array
     - Default: ``[]``.

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

Multiple selection
------------------

Set ``multipleResponse`` to ``true`` when more than one answer can be correct.
This uses the same assessment type and file structure.

.. code-block:: json

   {
     "type": "multiple-choice",
     "taskId": "multiple-choice-3914419031",
     "source": {
       "name": "Solar system objects",
       "showName": true,
       "instructions": "**Which of the following are found in the solar system?**",
       "multipleResponse": true,
       "isRandomized": true,
       "answers": [
         {
           "_id": "2e14860f-3179-75b1-b41f-b8a339c47871",
           "correct": true,
           "answer": "Planets"
         },
         {
           "_id": "a0bf5603-02dc-e47e-3e97-03bdf8d61c02",
           "correct": true,
           "answer": "Moons"
         },
         {
           "_id": "e55d6b9e-d839-bb48-c570-4cff2dc0393f",
           "correct": true,
           "answer": "Asteroids"
         },
         {
           "_id": "c7ba4087-c95c-806a-a8e6-1d2742b445f7",
           "correct": false,
           "answer": "Traffic lights"
         }
       ],
       "metadata": {
         "tags": [
           {
             "name": "Assessment Type",
             "value": "Multiple Choice"
           }
         ],
         "files": [],
         "opened": []
       },
       "bloomsObjectiveLevel": "2",
       "learningObjectives": "SWBAT identify common objects in the solar system",
       "guidance": "Planets, moons, and asteroids are all part of the solar system. Traffic lights are human-made objects found on Earth.",
       "showGuidanceAfterResponseOption": {
         "type": "Always"
       },
       "maxAttemptsCount": 1,
       "showExpectedAnswerOption": {
         "type": "Always"
       },
       "points": 20,
       "incorrectPoints": 0,
       "arePartialPointsAllowed": true,
       "useMaximumScore": true
     }
   }
