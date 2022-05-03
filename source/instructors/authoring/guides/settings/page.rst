.. meta::
   :description: Use page settings to control the appearance of your instructional materials

.. _page:


Guides Settings and Page actions
================================

.. toctree::
   :caption: Guides Settings and Page actions
   :hidden:
   
   opentabs
   assessments
   media
   global

Layout settings
---------------

Access **Layout** settings by clicking on **Layout** while editing a Guide.

  .. image:: /img/guides/page.png
     :alt: Page settings
     
.. _layout:

Use layout to control the appearance of your panels
***************************************************
You can choose from a variety of panel layouts to control the display inside the window for each page of content.

  .. image:: /img/guides/layouts.png
     :alt: Layouts


The dropdown list contains the available layouts.

:ref:`click here <specify-panel>` for information on how to reference these panels when auto opening code files, url previews or terminal windows.

The top-most entry in the Layout dropdown is **Previous**. This means it will use the same panel layout as specified on the previous page.


.. _show-hide-folders:

Show/Hide Folders
*****************
You can place code samples for each page in separate directories and then you can show only the relevant folders for a specific page. On the **Layout** settings when **Show File Tree** is enabled you can specify that folder and all non-specified folders are hidden from view in the file tree.

The benefit of hiding folders is that the student is not distracted by other folders and files that are not relevant to the page.

Full File Tree:
***************

  .. image:: /img/guides/project_1.png
     :alt: Full File Tree


Hiding of Folders:
******************

  .. image:: /img/guides/project_2.png
     :alt: Hiding Folders


Defining folders to hide:
*************************
1. From edit mode on the page you wish to hide folders, access **Layout** settings by clicking on **Layout**.
2. Enable **Show File Tree** and then in the **Show Folders** field, specify the folder or folders which should be shown in the file tree. Use the `;` character to separate multiple folders.

  .. image:: /img/guides/project_3.png
     :alt: Defining folders


If you have several pages that show the same folders, you only need define the folders on the first page of the set of pages. All subsequent pages will use the same **Show Folders** setting until a new one is encountered.

Guides on Left
--------------

If you wish the guides content to show on the left, enable this option.

.. _close-tabs:

Close Tabs
----------

Enable this to close all panels open from the previous page.

- **Close Terminal Session** when Close tabs enabled, allows you the option to retain terminal session from previous section. By default, terminal session will close.

Content Type
------------
You can specify whether the page content type is Markdown or HTML. If you choose HTML, you will need to set the page HTML header and footer in :ref:`Settings <global>`.

Teacher only content
--------------------
If this switch is enabled then the page contents will not be show to students. Teachers will be able to see it when they open an assignment in a course or when opening a students assignment.

Learning Objectives
-------------------
A tag field that can be used for data analysis.

