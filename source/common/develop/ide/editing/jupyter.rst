.. meta::
   :description: Using Jupyter Notebooks for your assignments.
   
.. _jupyter:

Jupyter
=======
You can set up your assignment to provide your students with a Jupyter Notebook as the default code editor or to open JupyterLab. More information about `Jupyter Notebook <https://jupyter.org/>`_ and `Jupyter Lab <https://jupyterlab.readthedocs.io/en/latest/>`_.

The :ref:`Code Playback <code-playback>` functionality will not work for code your students enter in a Jupyter Notebook. If you install the Jupyter Collaboration Extension (see `Using the Jupyter Collaboration Extension`_ below), you can view a timeline of events in the notebook.

Using Jupyter Notebooks in Codio
--------------------------------
If you plan to use Jupyter Notebook and optionally nbgrader, you must use a stack configured to support them. As these items are often difficult to configure, we recommend that you select the Jupyter Lab stack from our list of Certified Stacks.

More information about grading using :ref:`nbgrader <notebooks>`.

.. Note:: Notebook files are only supported in the root (`/home/codio/workspace` or `~/workspace`) folder.

Opening a Jupyter Notebook or JupyterLab
----------------------------------------
There are multiple ways to provide your students with access to their Jupyter Notebook.  

The following are a few of the possibilities.

- Modify the :ref:`Preview menu <preview>` so that students can access the Jupyter server through the menu and open it in Codio or in a new browser tab.
   To customize the Preview button, modify this section of the **.codio** file:

   .. code:: ini

            {
            // Preview button configuration
               "preview": {
                     "Jupyter Notebook": "https://{{domain3000}}/"
               }
            }


- Use guides to :ref:`create a layout <page>` that automatically opens a pane containing JupyterLab or a particular Jupyter NoteBook file. The example below shows a 2-Panel layout.
    - Create a **2-Panel Layout**.
    - Add a tab and for type select - "File" or select the "Jupyter Lab" type. 
    - Enter the name of your file into the **Filename** field or drag it into it from the file tree.
    - You can change the :ref:`guide settings <global>` to **Collapsed on Start** and the Jupyter pane will open with the Guides collapsed.

.. image:: /img/jlablayout.png
   :alt: Configuring the layout for Jupyter Lab

If you don't use Guides, consider creating a README.md file with instructions on accessing the Jupyter Notebook. When there are no guides, the README.md will auto-open for students. You can tell students to click on the file in the file tree if you haven't configured another way to open it.

Virtual Coach and Jupyter Notebook
----------------------------------
An extension will allow :ref:`Virtual Coach <virtual-coach>` to access the contents of your Jupyter Notebook and detect errors when running Jupyter cells. This extension is already installed in all the Codio Certified Jupyter stacks. You can add the extension if you have your own custom Jupyter stack.

Use the **Tools > Install Software** :ref:`(more information) <box_parts>` menu item to install the **Jupyter Codio extension**. 

After you have completed installing the software you will need to :ref:`create a new stack <create-stack>` or a :ref:`new stack version <update-stack>` to provide this for your students.

The Codio Jupyter stacks based on Ubuntu 22.04 all utilize JupyterLab, and you should open the file as a JupyterLab (see above) to use all the features of the extension. 

You can check if JupyterLab is installed in your stack by entering the command ``jupyter --version`` in the terminal. This command will inform you which Jupyter packages are installed. If JupyterLab is not installed, you should open the Jupyter Notebook as a file.

.. _jupyter-collaboration-extension:

Using the Jupyter Collaboration Extension
-----------------------------------------

.. Note:: You must have JupyterLab 4.4 or greater to use Jupyter collaboration.

This extension will allow multiple students to collaborate on a single Jupyter Notebook. You can set up the groups using the :ref:`Pair Programming <group-work>` feature to facilitate the sharing of notebooks. This extension does not support the Driver/Navigator and Shared Focus functionality (see :ref:`Pair Programming <group-work>` for details on these features).

Use the **Tools > Install Software** :ref:`(more information) <box_parts>` menu item to install the **Jupyter Collaboration extension**. 

After you have completed installing the software you will need to :ref:`create a new stack <create-stack>` or a :ref:`new stack version <update-stack>` to provide this for your students.

For more information about the Jupyter Collaboration Extension, see the `official documentation <https://jupyterlab-realtime-collaboration.readthedocs.io/en/latest/>`_. This extension also provides a timeline of events in a Jupyter Notebook; learn more in this `blog post about timeline viewing <https://blog.jupyter.org/exploring-a-documents-timeline-in-jupyterlab-6084f96db263>`_.


.. image:: /img/guides/jupyterhistoryofedits.gif
    :alt: An animated GIF showing a review of Jupyter Notebook edits
    :align: center