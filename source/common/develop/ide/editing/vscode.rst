.. meta::
   :description: Install VSCode as your code editor.
   
.. _vscode:

VSCode
======
You can set up your assignment to provide VSCode as the default code editor for your students. 

.. Note:: The :ref:`Code Playback <code-playback>` functionality will not work for code your students enter in VSCode.

Installing VSCode
-----------------
Use the **Tools > Install Software** :ref:`(more information) <box_parts>` menu item to easily install VSCode. If you want to run or debug your software you will also need to install language specific extensions. 
To do that follow the instructions on **Opening VSCode** below and then select the language extension you want to use from the **Extensions** tab in VSCode. 

   .. image:: /img/pyforvscode.png
      :alt: Selecting the Python language extension from the Marketplace tab in VSCode.

After you have completed installing the software you will need to :ref:`create a new stack <create-stack>` or a :ref:`new stack version <update-stack>` to provide this for your students.


Opening VSCode
--------------
There are multiple ways to provide your students with access to the VSCode editor once you have installed the software. The following are a couple of the possibilities.

- Modify the :ref:`Preview menu <preview>` so that students can access VSCode through the menu and open it in a new browser tab.

      To customize the Preview button, modify this section of the **.codio** file:

      .. code:: ini

               {
               // Preview button configuration
                  "preview": {
                        "Open Visual Studio": "https://{{domain4000}}/"
                  }
               }


- Use guides to :ref:`create a layout <page>` that automatically opens a pane containing VSCode. The example below shows a 2-Panel layout, you can create any number of panels and specify which panel should open VSCode.

      - Create a **2-Panel Layout**.
      - Add a tab and for type select - "Preview". 
      - Into the **Filename** field paste: ``https://{{domain4000}}/``

   .. image:: /img/vscodelayout.png
      :alt: Configuring the layout for VSCode

   This is the result, a 2-Panel Layout with the VSCode editor:

   .. image:: /img/vscodedisplay.png
      :alt: A two panel display with VSCode as the code editor

