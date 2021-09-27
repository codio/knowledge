.. meta::
   :description: Awarding partial points in your test script.
   
.. _partial-points:

Partial Points
==============
You can award partial points for student assessments in your testing scripts. Use the following Bash and Python grading scripts to enable partial points. You must toggle **Allow Partial Points** on in the **Grading** section of the Advanced Code Test dialog.


Example Bash grading script for partial points
----------------------------------------------
If your test was written using a bash script, report partial points similar to the following:

.. code:: bash

     POINTS=5
     curl -s "$CODIO_PARTIAL_POINTS_URL&points=${POINTS}" > /dev/null


Example Python grading script for partial points
------------------------------------------------
If your test was written using a Python script, report partial points similar to the following:

.. code:: python

    #!/usr/bin/env python

    import random
    import sys
    # import grade submit function
    sys.path.append('/usr/share/codio/assessments')
    from lib.grade import send_partial
    def main():
      # Execute the test on the student's code
      grade = random.randint(10, 50) 

      # Send the grade back to Codio with the penalty factor applied
      res = send_partial(int(round(grade)))
      exit( 0 if res else 1)

    main()


The score you award should be any value between 0 and the maximum score you specified when defining the assessment in the Codio authoring editor.

Autograding enhancements for partial points
-------------------------------------------
To provide you with more robust auto-grade scripts, you can send back feedback in different formats HTML, Markdown, or plaintext) and a URL is passed as an environment variable ```CODIO_PARTIAL_POINTS_V2_URL```. These variables allow POST and GET requests with the following parameters:

- **Score** (```CODIO_PARTIAL_POINTS_V2_URL```) - 0-100 percent for assessment, should be a percentage of total points possible. 
- **Feedback** - text
- **Format** - html, md, or txt (default)

Example Python auto-grading script with partial points
......................................................

.. code:: python

    import os, requests, random, re, io, subprocess, shutil, sys
    from subprocess import Popen, PIPE, STDOUT

    sys.path.append('/usr/share/codio/assessments')
    from lib.grade import send_partial_v2, FORMAT_V2_MD, FORMAT_V2_HTML, FORMAT_V2_TXT

    score = 0
    feedback = ""

    # get student code

    with open('code/quizquestion2.c') as response:
      answer = response.read()

    #check student code

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

    feedback+= "<h2>On this question you earned " + str(score) + " out of 10</h2>"
    # scale up score to be out of 100
    percent = (score/10)*100
    res = send_partial_v2(percent, feedback, FORMAT_V2_HTML)
    exit(0 if res else 1)