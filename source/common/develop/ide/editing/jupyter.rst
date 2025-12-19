.. meta::
   :description: Using JupyterLab for your assignments.
   
.. _jupyter:

JupyterLab
==========
You can set up your assignment to provide your students with the `JupyterLab <https://jupyterlab.readthedocs.io/en/latest/>`_ IDE. 

.. Note:: 
   :ref:`Code Playback <code-playback>` does not work with JupyterLab Notebooks. 
      
   To view a timeline of events in a notebook, see :ref:`jupyter-collaboration-extension` below. 

Using JupyterLab in Codio
--------------------------------
If you plan to use JupyterLab and optionally nbgrader, you must use a stack configured to support them. As these items are often difficult to configure, we recommend that you select the JupyterLab stack from our list of Certified Stacks.

For information about grading notebook assignments, see :ref:`nbgrader <notebooks>`.

.. Note:: Notebook files are only supported in the root (`/home/codio/workspace` or `~/workspace`) folder.

Opening JupyterLab
------------------
There are multiple ways to provide your students with access to JupyterLab.  

The following are a few of the possibilities.

- Modify the :ref:`Preview menu <preview>` so that students can access the Jupyter server through the menu and open it in Codio or in a new browser tab.
   To customize the Preview button, modify this section of the **.codio** file:

   .. code:: ini

      {
      // Preview button configuration
         "preview": {
               "JupyterLab": "https://{{domain3000}}/"
         }
      }


- Use guides to :ref:`create a layout <page>` that automatically opens a pane containing JupyterLab and a particular Notebook file. The example below shows a 2-Panel layout.
    - Create a **2-Panel Layout**.
    - Add a tab and select the "JupyterLab" type. 
    - Enter the name of your file into the **Filename** field or drag it from the file tree.
    - You can change the :ref:`guide settings <global>` to **Collapsed on Start** and the Jupyter pane will open with the Guides collapsed.

.. image:: /img/jlablayout.png
   :alt: Configuring the layout for JupyterLab

If you don't use Guides, consider creating a README.md file with instructions on accessing JupyterLab. When there are no guides, the README.md will auto-open for students. You can tell students to click on the file in the file tree if you haven't configured another way to open it.

JupyterLab Extensions
---------------------

The following two features require JupyterLab. The Codio Certified Jupyter stacks based on Ubuntu 22.04 all come with JupyterLab pre-installed, so you can access these extension features immediately after opening JupyterLab.

If you are using a custom stack, you can check if JupyterLab is installed by running ``jupyter --version`` in the terminal. If it is not installed, you will not be able to use these features.

Virtual Coach and JupyterLab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An extension will allow :ref:`Virtual Coach <virtual-coach>` to access the contents of your Jupyter Notebook and detect errors when running Jupyter cells. This extension is already installed in all the Codio Certified Jupyter stacks. You can add the extension if you have your own custom Jupyter stack.

Use the **Tools > Install Software** :ref:`(more information) <box_parts>` menu item to install the **Jupyter Codio Extension**. 

After you have completed installing the software you will need to :ref:`create a new stack <create-stack>` or a :ref:`new stack version <update-stack>` to provide this for your students.


.. _jupyter-collaboration-extension:


Collaboration and Timeline
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. Important:: You must have JupyterLab 4.4 or greater to use the Jupyter Collaboration Extension.

This extension will allow multiple students to collaborate on a single Jupyter Notebook. You can set up groups using the :ref:`Pair Programming <group-work>` feature to facilitate notebook sharing; note that this extension does not support the Driver/Navigator and Shared Focus functionality (described in the same section).

Use the **Tools > Install Software** :ref:`(more information) <box_parts>` menu item to install the **Jupyter Collaboration Extension**. 

After you have completed installing the software you will need to :ref:`create a new stack <create-stack>` or a :ref:`new stack version <update-stack>` to provide this for your students.

For more information about the Jupyter Collaboration Extension, see the `official documentation <https://jupyterlab-realtime-collaboration.readthedocs.io/en/latest/>`_. This extension also provides a timeline of events in a Jupyter Notebook; learn more in this `blog post about timeline viewing <https://blog.jupyter.org/exploring-a-documents-timeline-in-jupyterlab-6084f96db263>`_.

.. image:: /img/guides/timeline.gif
    :alt: An animated GIF showing a review of Jupyter Notebook edits
    :align: center