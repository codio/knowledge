.. meta::
   :description: The Open Tab settings specify what will display in the panels of a Codio window

.. _open-tabs:

Open Tabs
==========
You can automatically perform any of the following actions when a page is shown:

- Reconfigure the overall IDE panel layout.
- Open files.
- Open a url preview including external websites.
- Open a terminal window and optionally run a terminal command.
- Select lines you wish to highlight within each file.
- Open a :ref:`virtual machine <virtualmachine>` when set up for students.

**Opening Files Automatically**

Files can be opened automatically to present students with relevant content. You have several options for adding files:

- Use the **Add Tab** button to create multiple configuration lines for different scenarios
- Drag and drop files from your project file tree directly onto the **Open Tabs** section
- Drag and drop files onto the Open Tabs area in the content

**Alternative Method**

You can achieve the same functionality using Markdown directives on a page. :ref:`Click here <open-close>` for details.

.. note:: Image files dragged onto a page will be automatically tagged to display within the content rather than in a new panel. If you wish to have an image file open in a panel, you need to add it directly in the Open Tabs area. You can also drag and drop from the file tree. The correct path to the file will be included automatically.


Opening Files
*************
To open files, select the file type from the drop down and enter the file name, including the path to the file if not in the root (`/home/codio/workspace` or `~/workspace`) of the project workspace.

.. image:: /img/guides/type_file.png
   :alt: open file
     

To open multiple files in the same panel, enter in the following format:

```
index.html, main.css
```

Previewing
**********
To preview your project, select the **Preview** type from the drop down. If you wish to show a workspace or external website page, use the **Preview** option and enter the appropriate URL.

.. image:: /img/guides/type_preview.png
   :alt: Preview
     


.. note:: If the URL you are previewing does not allow embedding in an `<iframe>`, then you won't be able to use `https` addresses. You would have to use an `http` address instead, in which case it will automatically open in a new browser tab and not within Codio.

Opening the Terminal and Running System Commands
************************************************

Opening a Terminal Window
^^^^^^^^^^^^^^^^^^^^^^^^^

To open a terminal window, select **Terminal** from the type dropdown menu.

Running Commands Automatically
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can specify a terminal command to run automatically when a section is displayed. This is useful for setup tasks such as:

- Copying files from the hidden `/.guides` folder into the project root (`/home/codio/workspace` or `~/workspace`)

.. image:: /img/guides/type_terminal.png
   :alt: terminal

- Running bash scripts to prepare the environment
- Executing any necessary setup commands at specific points in your content

.. image:: /img/guides/terminal_command.png
   :alt: terminal command



Highlighting Lines in Your Code
********************************

Setting Up Code Highlighting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To highlight one or more lines within an auto-opened file:

1. Select **Highlight** from the type dropdown menu
2. Enter a piece of reference text from your target file into the **Reference...** field
3. Specify the number of lines to highlight from that reference point

.. image:: /img/guides/type_highlight.png
   :alt: Highlight

Why Use Reference Text?
^^^^^^^^^^^^^^^^^^^^^^^

Using reference text instead of line numbers makes your highlighting more resilient to changes. If you add or remove lines elsewhere in your file, Codio automatically adjusts the highlighted block based on the reference text. 

.. note:: If you insert or remove lines *within* the highlighted block, you'll need to adjust the line count manually.

Ensuring Unique References
^^^^^^^^^^^^^^^^^^^^^^^^^^

If there's any potential ambiguity with your reference text, insert a unique comment in your code and reference that instead.

Additional Options
^^^^^^^^^^^^^^^^^^

- Multiple highlight configurations are supported and will be applied in the order specified
- To highlight code while preventing student edits, you can :ref:`freeze code <freezecode>` in code files

.. _code-visualizer:

Visualizer
**********

Codio supports `Python Tutor <http://pythontutor.com>`_, allowing students to overcome a fundamental barrier to learning programming: understanding what happens as the computer executes each line of a program's source code.
Select `Visualizer` and enter the path to your file.

**Supported languages:** Python, Java, JavaScript, TypeScript, Ruby, C, C++


Students can visualize what the computer is doing step-by-step as it executes those programs.

.. image:: /img/guides/pythontutor.png
   :alt: python tutor


Visualizer Examples
^^^^^^^^^^^^^^^^^^^

**Python**

.. code:: python

    nested = ['spam', 1, ['Brie', 'Roquefort', 'Pol l Veq'], [1, 2, 3]]
    for temp in nested:
      print(temp)

.. image:: /img/guides/PythonVisualizerExample.png
   :alt: Python Visualizer Example

**Java**

.. code:: java

    public static void countdown(int n) {
      if (n == 0) {
        System.out.println("Blastoff!");
      } else {
        System.out.println(n);
        countdown(n - 1);
      }
    }


.. image:: /img/guides/JavaVisualizerExample.png
   :alt: Java visualizer Example

     


For more information and examples see `Python Tutor <http://pythontutor.com>`_.

Open Computed VM
****************

Select this option to automatically open the virtual machine for the students.

.. image:: /img/guides/guides_vm.png
   :alt: Open VM

.. note:: If selected but the assignment is not set up for :ref:`virtual machine <virtualmachine>` nothing will happen for the student.

.. _specify-panel:



Panel Selection
***************

If your :ref:`layout <page>` includes multiple panels, you can specify which panel to display the file in using the panel letter designation.

.. image:: /img/guides/panel.png
   :alt: Panel

Panel Ordering
^^^^^^^^^^^^^^

Panels are ordered from left to right, then top to bottom. The file tree is always last in the sequence.

Default Panel Behavior
^^^^^^^^^^^^^^^^^^^^^^

- The Guide defaults to the right panel unless **Guides Left** is specified in **Page Layout**

