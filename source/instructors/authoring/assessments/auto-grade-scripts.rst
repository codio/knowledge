.. meta::
   :description: Assignment level scripts have access to data about all the assessments in an assignment.
   
.. _auto-grade-scripts:

Assignment Level Scripts
========================
You can use assignment level scripts to evaluate student code, normalize points, and mark for participation grading. Assignment level scripts are added in the **Script Grading** field on the :ref:`Script Grading <grade-weights>` settings page. These scripts can then transfer the grading value into the grading field. Assignment level scripts are run when an assignment is **Marked as Complete**.

.. Note:: The script must execute within 3 minutes or a timeout error occurs. There is a maximum size for the feedback that can be returned of 1Mb. If this limit is exceeded, the message **Payload content length greater than maximum allowed: 1048576** will be returned.

If you are using an LMS platform with Codio, be sure to enter a percentage value in the **Grade Weight** field to maintain compatibility with LMS gradebooks. This value is then transferred into your LMS gradebook once you :ref:`release the grades <release-grades>`.

Secure scripts
-------------- 
If you store grading scripts in the **.guides/secure** folder, they run securely and students cannot see the script or the files in the folder. Only instructors can access this folder.

Access authored content assessment results
------------------------------------------
You can access student scores for authored content-based, auto-graded assessments. You can get both summary data and data for each assessment. This data is in JSON format and can be accessed in the ``CODIO_AUTOGRADE_ENV`` environment variable. The following is an example of the format of this data:

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

.. _participation-grading:

Participation Grading
---------------------

You can implement participation grading using assignment level scripts. 

An example of participation grading:

- Add the script below as .py file to `.guides/secure` folder

.. code:: python

    import os
    import json

    # import grade submit function
    import sys
    sys.path.append('/usr/share/codio/assessments')
    from lib.grade import send_grade

    env = os.environ.get('CODIO_AUTOGRADE_ENV')

    parsed = json.loads(env)

    answered = parsed['assessments']['stats']['answered']

    total=parsed['assessments']['stats']['total']

    grade=answered*100/total
    res = send_grade(int(round(grade)))
    exit( 0 if res else 1)


- Add the file to **Education>Test Autograde Script**. If your file is not a bash script or other type of file that runs independently, you will need to specify the program that will run it, for example "python3 autograde.py".
- Note: The JSON is not updated until the assignment is marked as complete. If you are testing values from inside the assignment - you will not see the updated values.
- Make sure to **Publish** the assignment.
- In the course assignment settings :ref:`Grade Weights <grade-weights>` section, enable **Script Grading** set **Set custom script path** to that file and disable **Assessments Grading**.

Regrade an individual student's assignment
------------------------------------------
If students have clicked **Mark as Complete** and the custom script is triggered, you can regrade their work by resetting the `complete` switch, and then set it to *complete* again, which triggers the custom script to run again.

Regrade all student's assignments
---------------------------------
You can regrade all student's assignments that have already been auto-graded from the **Actions** button on the assignment page.

1. Navigate to the assignment and open it.
2. Click the **Actions** button and then click **Regrade Completed**. This is useful if you have found a bug in your assignment level grading script. **Regrade Completed** does not run individual code test assessments.

Test and debug your grading scripts
-----------------------------------
.. Note:: Codio provides the ability to test your auto-grading scripts when creating your project, this should be done before publishing your project to a course. Once an assignment has been published to the course, any changes made to the assignment's source project are not automatically reflected in the published assignment. As a result, if you include your main grading logic in the project and the script has bugs, you cannot fix the bugs without deleting the assignment. All student data is lost. However, if all your scripts are stored in the **.guides/secure** folder, you can update and test the scripts and then publish the new version.

Test your script using bootstrap launcher
.........................................
You can also use a simple bootstrap launcher that loads and executes the script from a remote location so that you can edit and debug independently of the Codio box. The following example bash script shows a Python script that is located as a Gist on GitHub. This script might be called **.guides/secure/launcher.sh**.

.. code:: bash

    #!/bin/bash
    URL="https://gist.githubusercontent.com/MaximKraev/11cd4e43b0c43f79d9478efbe21ba1b9/raw/validate.py"
    curl -fsSL $URL | python - $@

It is important that this file is stored in the **.guides/secure** folder. You then specify the full filepath **.guides/secure/launcher.sh** in the **Set custom script path** field in the assignment settings.

It is now possible to debug the Python script and fix any bugs that you may have noticed once students have started work on the assignment.

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
This section provide some example assignment level scripts.

Python auto-grading script
..........................
Below is an example Python file that can be loaded by a bootstrap script.

.. Note:: The only code you need to modify is near the bottom. The other functions are helpers and can be used for any test in any assignment.

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

- **Grade** (```CODIO_AUTOGRADE_V2_URL```) - return 0-100 percent. This is the percent correct out of total possible points.
- **Feedback** - text
- **Format** - html, md, txt - txt is default

If the grade is submitted to the URL, the script output is saved as a debug log. This means that all information you want to pass to students must use the **Feedback** mechanism.

If the script fails:

- The attempt is recorded.
- The assignment is not locked (if due date is not passed).
- An email  notification with information about the problem is sent to the course instructor(s) containing the debug output from the script.

Example Python auto-grading script 
..................................

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