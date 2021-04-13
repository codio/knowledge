.. meta::
   :description: Using Auto-Grade Scripts
   
.. _auto-grade-scripts:

Using Auto-Grade Scripts
========================
You can use auto-grade scripts that evaluate the student code, and these scripts are added in the **Script Grading** field on the :ref:`**Script Grading** <grade-weights>` settings page. These scripts can then transfer the grading value into the grading field.

**Note:** The script must execute within 3 minutes or a timeout error occurs.

If you are using an LMS platform with Codio, be sure to enter a percentage value in the **Grade Weight** field to maintain compatibility with LMS gradebooks. This value is then transferred into your LMS gradebook once you :ref:`release the grades <release-grades>`.

Secure scripts
--------------
If you want your scripts to run securely, where students cannot view the script or other files that contain secure data, move the script files to the **.guides/secure** folder. Only the original project author can access this folder. 

Access authored content assessment results
------------------------------------------
You can get student scores for authored content-based, auto-graded assessments. You can get both summary data and data for each assessment. This data is in JSON format and can be accessed in the ``CODIO_AUTOGRADE_ENV`` environment variable. The following is an example:

.. code:: ini

    {
      "assessments": {
        "stats": {
          "total": 2,
          "answered": 2,
          "correct": 2,
          "totalPoints": 12,
          "points": 8
        },
        "info": [{
          "name": "Test 1",
          "points": 5,
          "answer": {
            "correct": true,
            "points": 5
          }
        }, {
          "name": "Test 2",
          "points": 7,
          "answer": {
            "correct": true,
            "points": 3
          }
        }]
      },
      "completedDate": "2017-02-07T09:47:54.471Z"
    }

Regrade an individual student's assignment
------------------------------------------
If students set their work to *complete* and the custom script is triggered, you can regrade their work by resetting the ``complete`` switch, and then set it to *complete* again, which triggers the custom script to run again.

Regrade all student's assignments
---------------------------------
You can regrade all student's assignments that have already been auto-graded from the **Actions** button on the assignment page.

1. Navigate to the assignment and open it.
2. Click the **Actions** button and then click **Regrade All**. This is useful if you have found a bug in your grading script. 

Test and debug your grading scripts
-----------------------------------
**IMPORTANT:**
Codio provides the ability to test your auto-grading scripts when creating your project, and it's important that this be done before publishing your project to a course. Once an assignment has been published to the course, any changes made to the assignment's source project are not automatically reflected in the published assignment. As a result, if you include your main grading logic in the project and the script has bugs, you cannot fix the bugs without deleting the assignment. All student data is lost. However, if all your scripts are stored in the **.guides/secure** folder, you can update and test the scripts and then publish the new version.

Test your script using bootstrap launcher
.........................................
You can also use a simple bootstrap launcher that loads and executes the script from a remote location so that you can edit and debug independently of the Codio box. The following example bash script shows a Python script that is located as a Gist on GitHub. This script might be called **.guides/secure/launcher.sh**.

.. code:: bash

    #!/bin/bash
    URL="https://gist.githubusercontent.com/MaximKraev/11cd4e43b0c43f79d9478efbe21ba1b9/raw/validate.py"
    curl -fsSL $URL | python - $@

It is important that this file is stored in the **.guides/secure** folder. You then specify the full filepath **.guides/secure/launcher.sh** in the **Set custom script path** field in the assignment settings.

You can now to debug the Python script and fix any bugs that you may have noticed once students have started work on the assignment.

Test your script in the IDE
...........................
You can also test your auto-grading script in the Codio IDE from the **Education > Test Autograde Script** on the menu bar. This option allows you to specify the location of your auto-grading script and run it against the current project content. It also allows you simulate scores attained by any auto-graded assessments located in the Codio Guide and select which autograded assessments to test.

.. image:: /img/autograde-test.png
   :alt: Autograde Test

Be sure to take the following into account when using this feature:

- When you click **Test Script**:

  - All output to ``stdout`` and ``stderr`` are displayed in the dialog.
  - The grade returned by your test script is at the bottom of the output section.

- ``stdout`` and ``stderr`` output is not available when running the actual auto-grading script (not in test mode) because it runs invisibly when the assignment is marked as complete. Because of this, you should only generate output for testing and debugging.
- If you want your script to provide feedback to the student, you should output it to a file that can be accessed by the student when opening the project at a later date. In this case, you should allow read-only access to the project from the assignment settings after being marked as complete.

Example grading scripts
-----------------------
This section provide some example auto-grading scripts.

Python auto-grading script
..........................
Below is an example Python file that can be loaded by a bootstrap script.

**Note:** The only code you need to modify is near the bottom. The other functions are helpers and can be used for any test in any assignment.

.. code:: python

    import os
    import random
    import requests
    import json
    import datetime

    # import grade submit function
    import sys
    sys.path.append('/usr/share/codio/assessments')
    from lib.grade import send_grade

    ##################
    # Helper functions #
    ##################


    # Get the url to send the results to
    CODIO_AUTOGRADE_URL = os.environ["CODIO_AUTOGRADE_URL"]
    CODIO_UNIT_DATA = os.environ["CODIO_AUTOGRADE_ENV"]

    def main():
      # Execute the test on the student's code
      grade = validate_code()
      # Send the grade back to Codio with the penatly factor applied
      res = send_grade(int(round(grade)))
      exit( 0 if res else 1)

    ########################################
    # You only need to modify the code below #
    ########################################

    # Your actual test logic
    # Our demo function is just generating some random score
    def validate_code():
      return random.randint(10, 100)

    main()



Bash auto-grading script
........................
Below is an example bash script file that can be stored in the **.guides/secure** folder:

.. code:: bash

    #!/bin/bash
    set -e
    # Your actual test logic
    # Our demo function is just generating some random score
    POINTS=$(( ( RANDOM % 100 )  + 1 ))
    # Show json based passed environment
    echo $CODIO_AUTOGRADE_ENV
    # Send the grade back to Codio
    curl --retry 3 -s "$CODIO_AUTOGRADE_URL&grade=$POINTS"


Auto-grading enhancements
-------------------------
To provide instructors with more robust auto-grade scripts, you can also:

- Send feedback in different formats such as HTML and Markdown/plaintext.
- Allow separate debug logs.
- Notify (instructors and students) and reopen assignments for a student on grade script failure.

To support this additional feedback, this URL (passed as an environment variable) can be used:```CODIO_AUTOGRADE_V2_URL```

These variables allow POST and GET requests with the following parameters:

- **Grade** (```CODIO_AUTOGRADE_V2_URL```) - 0-100 grade result
- **Feedback** - text
- **Format** - html, md, txt - txt is default

If the grade is submitted to the URL, the script output is saved as debug log.

If the script fails:
- The attempt is recorded.
- The assignment is not locked (if due date is not passed).
- An email  notification with information about the problem is sent to the course instructor(s) containing the debug output from the script.

Example Python auto-grading script
...................................

.. code:: python

    import os
    import random
    import requests
    import json
    # import grade submit function
    import sys
    sys.path.append('/usr/share/codio/assessments')
    from lib.grade import send_grade_v2, FORMAT_V2_MD, FORMAT_V2_HTML, FORMAT_V2_TXT
    def main():
      # Execute the test on the student's code
      grade = random.randint(10, 100)
      # Send the grade back to Codio with the penatly factor applied

      res = send_grade_v2(int(round(grade)), '### Hi here', FORMAT_V2_MD)
      exit( 0 if res else 1)

    main()


Example Bash auto-grading script
................................

.. code:: bash

    #!/bin/bash
    set -e
    POINTS=$(( ( RANDOM % 100 )  + 1 ))
    curl --retry 3 -s "$CODIO_AUTOGRADE_V2_URL" -d grade=$POINTS -d format=md -d feedback=test

