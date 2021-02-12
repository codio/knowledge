.. _customizable-run-menu:

Customize Run Button
=====================
The Codio IDE offers the ability to customize the **Run** button, similar to using the ``alias command in the command line. When you click **Run**, a new terminal window opens to run the command. You can also force the command to run in an existing terminal window instead of opening a new window.

Configure Run to open new terminal window
-----------------------------------------

To customize the **Run** button to open a new terminal window where you can see the output, you must edit the **.codio** file in the root of your project. 

.. image:: /img/run-menu.png
   :alt: Run Menu

In the .codio file, locate the lines below, and then copy and paste the following code:

.. code:: json

    {
      // Configure your Run and Preview buttons here.

      // Run button configuration
      "commands": {
        "Install Learnyounode" : "npm install -g learnyounode",
        "Run Lesson" : "./ns-executes.sh run {{filename_no_ext}} {{path}}",
        "Verify Lesson" : "./ns-executes.sh verify {{filename_no_ext}} {{path}}",
        "Completed Lessons" : "learnyounode",
        "Run with Node" : "node {{filepath}} 3 4 5"
      }
    }

When you click the **Run** button, it executes the last selected command.

Configure to run in current terminal window
-------------------------------------------
If you want to configure the Run button to run commands in the current terminal window, modify the **id** field in the **.codio** file as follows:

.. code:: json

    {
      "commands": {
            "Node version": {
                "id": "terminal_1",
                "cmd": "node --version"
            },
            "ls": {
                "id": "terminal_1",
                "cmd": "ls"
            }
      },

    // Preview button configuration
      "preview": {
            "Project Index (static)": "http://{{domain}}/{{index}}",
            "Current File (static)": "http://{{domain}}/{{filepath}}",
            "Box URL": "http://{{domain3000}}/"
      }
    }

**Notes:**

- Commands with the same **id** will share the same terminal window.
- The terminal id should be "backend-guide" to execute a command in the terminal window opened by guides.

When modifying the **.codio** file, you can also use the following tokens in the shell commands:

- ``{filepath}}`` - inserts the path and full file name (/path/to/file.ext).
- ``{{path}}`` - inserts only the path to the selected file (/path/to/).
- ``{{filename}}`` - inserts the filename with its extension (file.ext).
- ``{{filename_no_ext}}`` - inserts the filename without the extension (file).
- ``{{domain3000}}`` - inserts the public url to your box; **word1-word2-3000.codio.io** to access over port 80, which is useful if your corporate firewall blocks ports other than 80 and 443.
- ``{{domain}}`` - inserts the alternate public url to your box; **word1-word2.codio.io**; be aware that you will usually need to specify a port to reach a service running on your box (for example, **word1-word2-<port>.codio.io**).