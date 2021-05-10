.. meta::
   :description: Awarding partial points in your test script.
   
.. _partial-points:

Partial Points
==============
You can award partial points for student assessments in your testing scripts. Use the following Bash and Python grading scripts to enable partial points.


Example Bash grading script for partial points
----------------------------------------------
If your test was written using a bash script, enable partial points similar to the following:

.. code:: bash

     POINTS=5
     curl -s "$CODIO_PARTIAL_POINTS_URL&points=${POINTS}" > /dev/null


Example Python grading script for partial points
------------------------------------------------
If your test was written using a Python script, enable partial points similar to the following:

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
