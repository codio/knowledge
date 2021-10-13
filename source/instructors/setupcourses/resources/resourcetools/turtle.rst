.. meta::
   :description: Turtle graphics setup & usage

.. _turtle:

Turtle
======

With Turtle Graphics, students can produce animations and graphical output. Lines are drawn following the turtle movement. 

  .. image:: /img/turtlepreview.png
     :alt: turtle graphics

In Python
*********
We have a Turtle Graphics in Python Starter Pack to help you get started. 

You can find this by either searching for "turtle" in the starter pack area or:

-  For Codio.com users, `click here <https://codio.com/home/starter-packs/6ff2e3ab-6e02-45fc-9ed8-26793aa77336>`__
-  For Codio.co.uk users, `click here <https://codio.co.uk/home/starter-packs/6ff2e3ab-6e02-45fc-9ed8-26793aa77336>`__

Turtle is pre-installed in the Python library, so manul installation is simple:

1. Start by creating either a new project or assignment in your course and selecting the **Python Trajectory** stack. 

2. Select **Tools** at the top and click **Install software.** Search for **X server** and select install.

3. Once the software has downloaded, go to **Project > Restart Box** in the menu. 

4. Create two files:

- ``.py``: This is the student code file. 
- ``bg.sh``: This is the bash script. 

4. Within the ``bg.sh`` file, write the following bash script:

    | ``#!/bin/bash``
    | ``set -e``
    | ``set -o pipefail``
    | ``. /etc/profile.d/codio-xserver.sh``
    | ``$1 -m py_compile $2``
    | ``nohup $@ > /dev/null 2>&1&``

5. Set up your page panels by selecting the **settings wrench** from inside your Guide Editor. Select 3-panels without tree, and then navigate to **Open Tabs.**

6. Under **Open Tabs,** drag in your ``.py`` file and position it in panel 0. 

7. Press the **Add Tab** button and specify the type as **Preview.** Paste the following in the URL field:  ``https://{{domain3000}}/`` Position this in panel 1. 

8. Select **Save and close settings.**

9. The last thing you need to do is set up a **Try It** button so that once code is written in the code file, it can be executed in the server. In the Guide Editor, write the following: ``{Try it}(bash .guides/bg.sh python3 file.py)``

   .. Note:: You need to import the turtle library with ``import turtle`` as the first line of your code and end your code by calling ``turtle.mainloop()``.

In Java
*******

We have a Turtle Graphics in Java Starter Pack to help you get started. 

You can find this by either searching for "turtle" in the starter pack area or:

-  For Codio.com users, `click here <https://codio.com/home/starter-packs/5b707965-4353-4e23-9ce1-09a574475f58>`__
-  For Codio.co.uk users, `click here <https://codio.co.uk/home/starter-packs/5b707965-4353-4e23-9ce1-09a574475f58>`__

In C++
******

We have a Turtle Graphics in C++ Starter Pack to help you get started. 

You can find this by either searching for "turtle" in the starter pack area or:

-  For Codio.com users, `click here <https://codio.com/home/starter-packs/16556076-d721-4b11-a466-1820eccafd04>`__
-  For Codio.co.uk users, `click here <https://codio.co.uk/home/starter-packs/16556076-d721-4b11-a466-1820eccafd04>`__
