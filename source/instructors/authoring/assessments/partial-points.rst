.. meta::
   :description: Awarding partial points in your test script.
   
.. _partial-points:

Partial Points
==============
You can award partial points for student assessments in your testing scripts. Use the following Bash and Python grading scripts to enable partial points. You must toggle **Allow Partial Points** on in the **Grading** section of the Advanced Code Test dialog.

Feedback for Partial Points
---------------------------
In addition to the red **x** and green **checkmark** indicators for correctness there is a third indicator that displays when the student gets only a portion of the available points, an orange **percent** sign.

.. image:: /img/guides/indicators.png
   :alt: Indicators for assessment correctness

Autograding Enhancements for Partial Points
-------------------------------------------
To provide you with more robust auto-grade scripts, you can send back feedback in different formats HTML, Markdown, or plaintext and a URL is passed as an environment variable ``CODIO_PARTIAL_POINTS_V2_URL``. These variables allow POST and GET requests with the following parameters:


- **Score** (``CODIO_PARTIAL_POINTS_V2_URL``) - a percentage of total points possible between 0-100. 
- **Feedback** - text - this is limited to 1 Mb
- **Format** - html, md, or txt (default)

If you use Python, you can also use the function ``send_partial_v2``. Also, through HTTP requests you can use any other language you feel comfortable with.

As a general rule, your script should always exit with ``0``; otherwise, the grade will be 0. If the student receives partial points, the results will display an orange percent sign rather than a green check mark or red x.

Example Auto-Grading Scripts With Partial Points
------------------------------------------------

The following examples in Python and JavaScript show how you can write your scripts in any language. 

The Python script parses the student's file and then assigns points based on specific criteria. In the JavaScript version, it uses Unit Testing through Mocha, a popular `node` library and it is invoked with ``mocha 2>&1 || true`` to force the exit code to be 0. 

.. tabs::

      .. code-tab:: javascript

            const assert = require('assert');

            const CODIO_PARTIAL_POINTS_V2_URL = process.env.CODIO_PARTIAL_POINTS_V2_URL;
            var points = 0;
            var total_tests = 2;
            var feedback = "";

            describe('Operations', function () {
              describe('Sum', function () {
                it('should return 2 for 1 + 1', function () {
                  assert.equal(1 + 1, 2);
                  points++;
                  feedback += "<h2>Test 1 passed!</h2>"
                });
              });

              describe('Multiplication', function () {
                it('should return 4 for 2 x 2', function () {
                  assert.equal(2 * 2, 4);
                  points++;
                  feedback += "<h2>Test 2 passed!</h2>"
                });
              });

              after(function () { // Runs once after all tests
                if (CODIO_PARTIAL_POINTS_V2_URL) {
                  percentage = points/total_tests*100
                  fetch(CODIO_PARTIAL_POINTS_V2_URL, {
                    method: 'POST',
                    headers: {
                      'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: 'points=' + percentage + '&format=html&feedback=' + feedback,
                  })
                }
              });
            });

      .. code-tab:: python 
            :selected:

            import os, random, re, io, subprocess, shutil, sys
            from subprocess import Popen, PIPE, STDOUT

            sys.path.append('/usr/share/codio/assessments')
            from lib.grade import send_partial_v2, FORMAT_V2_MD, FORMAT_V2_HTML, FORMAT_V2_TXT

            score = 0
            feedback = ""

            # Get student code

            with open('code/quizquestion2.c') as response:
              answer = response.read()

            # Check student code

            if re.search('pi.*=.*3.14',answer) and re.search('r.*=.*8',answer):
              feedback+="Correct variable initialization.\n"
              score+=5
            else:
              feedback+="Incorrect variable initialization.\n"

            if re.search('float.*pi',answer) and re.search('float.*r',answer):
              feedback+="Correct variable declaration.\n"
              score+=5
            else:
              feedback+="Incorrect variable declaration.\n"

            # Give final feedback to the student and scale up score to be out of 100

            feedback+= "<h2>On this question you earned " + str(score) + " out of 10</h2>"
            percent = (score/10)*100

            # Send grades back to Codio

            res = send_partial_v2(percent, feedback, FORMAT_V2_HTML)
            exit(0 if res else 1)

 
Example Grading Script for Partial Points
-----------------------------------------
These are examples of the older method of partial points reporting.

.. tabs::

    .. code-tab:: bash

        POINTS=5
        curl -s "$CODIO_PARTIAL_POINTS_URL&points=${POINTS}" > /dev/null

    .. code-tab:: python 
        :selected:

        #!/usr/bin/env python

        import random
        import sys
        # import grade submit function
        sys.path.append('/usr/share/codio/assessments')
        from lib.grade import send_partial
        def main():
          # Execute the test on the student's code
          grade = random.randint(10, 50) 

          # Send the grade back to Codio 
          res = send_partial(int(round(grade)))
          exit( 0 if res else 1)

        main()


.. important::
   The score you award should be any value between 0 and the maximum score you specified when defining the assessment in the Codio authoring editor.