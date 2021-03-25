.. _nbgrader:

Auto-Grade with nbgrader
========================
Codio supports <Jupyter notebook> (https://jupyter.org/) auto-grading functionality through <nbgrader> (http://nbgrader.readthedocs.io/en/stable/index.html). Assignments are created with [Jupyter notebook](https://jupyter.org/) and when the assignment is published to a course, the release version is created for the student. If the assignment is updated and republished, it overwrites all tests and read-only cells with the new version and the release version for the students is updated.

When a student submits the assignment by marking the assignment as complete, the assignment is automatically graded. However, manual grading is also possible if desired. 

**Note:** Any user configurations for nbgrader should be stored in a **.codio-jupyter** file. If a **.codio-jupyter** file is used in a project, Codio assumes it is the Jupyter based grader so only **nbgrader** can be selected for the assessment scripts in the assignment.

Configuration
-------------
Use the following configuration information when setting up nbgrader:

- **Extend Timeout period** - To extend the time required for completion (to 90 seconds in this example), you can add the following to the **.codio-jupyter** file:

  ```yaml
  nbgrader:
     ExecutePreprocessor.timeout: 90
  ```

- **Lock all cells** - To lock all cells (Default: False), add the following to the **.codio-jupyter** file:

  ```yaml
  nbgrader:
     LockCells.lock_all_cells: True
  ```

- **Lock all grade cells** - To lock all grade cells (Default: True) where grade cells are locked (non-deletable), add the following to the **.codio-jupyter** file:

  ```yaml
  nbgrader:
     LockCells.lock_grade_cells: True
  ```

- **Lock all read-only cells** - To lock all grade cells (Default: True) where read only cells are locked (non-deletable and non-editable), add the following to the **.codio-jupyter** file:

  ```yaml
  nbgrader:
     LockCells.lock_readonly_cells: True
  ```

- **Lock all solution cells** - To lock all solution cells (Default: True) where solution cells are locked (non-deletable and non-editable), add the following to the **.codio-jupyter** file:

  ```yaml
  nbgrader:
     LockCells.lock_solution_cells: True
  ```

- **Execute preprocessor on timeout** - If execution of a cell times out, interrupt the kernel and continue executing other cells rather than throwing an error and stopping by adding the following to the **.codio-jupyter** file:

  ```yaml
  nbgrader:
     ExecutePreprocessor.interrupt_on_timeout: True
  ```

- **Run custom grading with Jupyter** - To avoid execution of autograder with nbgrader and allow Codio script autograder to be executed, add the following to the **.codio-jupyter** file. When this is set, Jupyter files do not display as assessments in Codio and are not submitted through nbrader after the assignment is marked as completed (no assessments and points areset in the assignment).

  ```yaml
  codio:
    grader: false
  ```

- **ClearSolutions.code_stub** - Add the following to the **.codio-jupyter** file:

  ```yaml
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
  ```

