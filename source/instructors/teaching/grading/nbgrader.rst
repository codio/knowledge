.. meta::
   :description: Auto-Grade Jupyter notebook assignments using nbgrader.
   
.. _notebooks:

Auto-Grade with nbgrader
========================
Codio supports `Jupyter notebook <https://jupyter.org/>`_ auto-grading functionality through `nbgrader <http://nbgrader.readthedocs.io/en/stable/index.html>`_. Assignments are created with `Jupyter notebook <https://jupyter.org/>`_ and when the assignment is published to a course, the release version is created for the student. If the assignment is updated and republished, it overwrites all tests and read-only cells with the new version and the release version for the students is updated. If you change the jupyter version or nbgrader version or any other nbgrader metadata in the assignment, it will not reflect automatically for students who have already started the assignment, instructor need to reset their assignment to reflect those changes. Students who haven't started the assignment will receive the updated version of assignment.

When a student submits the assignment by marking the assignment as complete, the assignment is automatically graded. However, manual grading is also possible if desired. 

User configurations for nbgrader can be stored in a **nbgrader_config.py** or in **.codio-jupyter** file. A .codio-jupyter file must be present in a project to let Codio know that nbgrader should be used to grade Jupyter assessments.  

.. Important:: If using **nbgrader_config.py** for your configurations, the **.codio-jupyter** is still required but can be empty/blank

.. Note:: If both files are used the settings in the **nbgrader_config.py** take precedence. This file is not visible to students in their assignments 

.. Note:: Notebook files are only supported if in the root (`/home/codio/workspace` or `~/workspace`) folder


.. Note:: Instructors can be notified of Jupyter Notebook grading failures by enabling the :ref:`Autograde Failure Notification <autograde-failure-notification>` feature in the course settings.

.. Warning:: :ref:`Pair Programming <group-work>` should not be used for Jupyter Notebook

Configuration
-------------
Use the following configuration information when setting up nbgrader in a **.codio-jupyter** file. If using **nbgrader_config.py**, see :ref:`example <nb-conf-example>` below.

- **Extend Timeout period** - To extend the time required for completion (to 90 seconds in this example), you can add the following to the **.codio-jupyter** file:

.. code:: yaml

  nbgrader:
     ExecutePreprocessor.timeout: 90
 

- **Lock all cells** - To lock all cells (Default: False), add the following to the **.codio-jupyter** file:

.. code:: yaml

  nbgrader:
     LockCells.lock_all_cells: True



- **Lock all grade cells** - To lock all grade cells (Default: True) where grade cells are locked (non-deletable), add the following to the **.codio-jupyter** file:

.. code:: yaml

  nbgrader:
     LockCells.lock_grade_cells: True


- **Lock all read-only cells** - To lock all grade cells (Default: True) where read only cells are locked (non-deletable and non-editable), add the following to the **.codio-jupyter** file:

.. code:: yaml

  nbgrader:
     LockCells.lock_readonly_cells: True


- **Lock all solution cells** - To lock all solution cells (Default: True) where solution cells are locked (non-deletable and non-editable), add the following to the **.codio-jupyter** file:

.. code:: yaml

  nbgrader:
     LockCells.lock_solution_cells: True


- **Execute preprocessor on timeout** - If execution of a cell times out, interrupt the kernel and continue executing other cells rather than throwing an error and stopping by adding the following to the **.codio-jupyter** file:

.. code:: yaml

  nbgrader:
     ExecutePreprocessor.interrupt_on_timeout: True


- **Run custom grading with Jupyter** - To avoid execution of autograder with nbgrader and allow Codio script autograder to be executed, add the following to the **.codio-jupyter** file. When this is set, Jupyter files do not display as assessments in Codio and are not submitted through nbrader after the assignment is marked as completed (no assessments and points are set in the assignment).

.. code:: yaml

  codio:
    grader: false


- **ClearSolutions.code_stub** - Add the following to the **.codio-jupyter** file:

.. code:: yaml

  nbgrader:
      ClearSolutions.code_stub:
          R: |
              # BEGIN YOUR CODE
              # END YOUR CODE
          python: |
              # YOUR CODE HERE
              raise NotImplementedError()
          ruby: |
              # BEGIN YOUR CODE
              raise NotImplementedError.new()
              #END YOUR CODE
  
.. _postgrading:

- **Postgrader**       

You can add a post-grading hook to Jupyter to alter the result html for the student. You can do this to remove and/or replace text from the notebook file that the students will see in their feedback.

.. code:: yaml

  codio:
    postGrader: .guides/secure/postgrader.py

To enable this, create a file **postgrader.py** in .guides/secure folder. This file needs to be executable.
Running ```chmod +x .guides/secure/postgrader.py``` will make this file executable.

Example postgrader.py file
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    #!/usr/bin/env python3
    import sys

    START_HIDDEN_TEST_TEXT = '### BEGIN HIDDEN TESTS'
    END_HIDDEN_TEST_TEXT = '### END HIDDEN TESTS'

    html_path = sys.argv[1].rstrip()
    with open(html_path, 'r') as content_file:
        content = content_file.read()


    def search_surrounding_html(original_text, position, left):
        index_to = len(original_text)
        text_position = position

        if not left:
            for i in range(position, index_to):
                if original_text[i] == '>':
                    return i + 1
        
        if left:
            for i in range(position, -1, -1):
                print(i, original_text[i])
                if original_text[i] == '<':
                    return i

        return text_position


    def replace_text_between(original_text, delimeter_a, delimter_b, replacement_text):
        index_from = 0
        index_to = len(original_text)
        if delimeter_a in original_text:
            index_from = original_text.index(delimeter_a)
            index_from = search_surrounding_html(original_text, index_from, True)

        if delimter_b in original_text:
            index_to = original_text.index(delimter_b) + len(delimter_b)
            index_to = search_surrounding_html(original_text, index_to, False)

        return original_text[0:index_from] + replacement_text + original_text[index_to:]


    while START_HIDDEN_TEST_TEXT in content:
        content = replace_text_between(content, START_HIDDEN_TEST_TEXT, END_HIDDEN_TEST_TEXT, '')


    with open(html_path, 'w+') as stream:
        stream.write(content)


In this example anything between the ### BEGIN HIDDEN TESTS and ### END HIDDEN TESTS in the **.ipynb** file will not be shown to the students 
  
If using the **nbgrader_config.py**, see example below

.. _nb-conf-example:

Example nbgrader_config.py
--------------------------

.. code:: python

    c = get_config()
    c.ClearHiddenTests.begin_test_delimeter = "BEGIN HIDDEN TESTS"
    c.ClearHiddenTests.end_test_delimeter = "END HIDDEN TESTS"
    c.LockCells.lock_all_cells = True
    c.LockCells.lock_grade_cells = True
    c.LockCells.lock_readonly_cells = True
    c.LockCells.lock_solution_cells = True
    c.ExecutePreprocessor.interrupt_on_timeout = True
    c.ExecutePreprocessor.timeout = 20
    c.ClearSolutions.code_stub = {
    "R": "# your R code here\n# end of R code\n",
    "python": "# your python code here\n# end of python code\n",
    "ruby": "# your ruby code here            \n# end of ruby code"
    }
    

