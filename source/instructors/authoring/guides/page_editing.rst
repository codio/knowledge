.. meta::
   :description: Editing the content of a Guides page

.. _page-editing:

Page editing overview
=====================
To create new content or to edit existing content, go to the **Tools->Guide->Edit** menu option.

Use the layout modes to switch between editor, preview, and split view modes.

When in preview mode, you can quickly switch back to editor mode by selecting the **Editor** button:

.. image:: /img/guides/editor.png
     :alt: Guides Edit Mode



**Video: Editing Existing Guides Content**


.. raw:: html

    <iframe width="620" height="349" src="https://codio.wistia.com/medias/zqcpii19s6?wvideo=zqcpii19s6" allowtransparency="true" frameborder="0" scrolling="no" class="wistia_embed" name="wistia_embed" allowfullscreen mozallowfullscreen webkitallowfullscreen oallowfullscreen msallowfullscreen width="620" height="349"></iframe>



Anatomy of the content editor
*****************************
Below is a screenshot of the editor with the main components highlighted.

  .. image:: /img/guides/editbook.png
     :alt: overview



Editor settings
***************
Editor settings gives you access to the key functions:

Page
----
  - :ref:`Layout <layout>` allows you to specify the panel layout you want to choose for this section,
  - :ref:`Show Folders <show-hide-folders>` allows you to define specific folders in your project that you wish to be visible when the current section is displayed,
  - :ref:`Close Tabs <close-tabs>` allows you to close all tabs open from previous section,
      - **Close Terminal Session** when Close tabs enabled, allows you the option to retain terminal session from previous section. By default, terminal session will close
  - **Set Section as Chapter** allows you to set the section as a chapter in your content,
  - :ref:`Teacher Only <teacher-only>` allows you to show content that only teachers are able to see.
  - **Content Type** allows you to write your content in either :ref:`Markdown <markdown-content-editing>` or :ref:`HTML <html-content>`



:ref:`Open Tabs <open-tabs>`
----------------------------
This allows you to specify:

  - which files you want to automatically open when the current section is displayed,
  - Preview (including external websites),
  - Open a Terminal window (including running a terminal command),
  - which lines (if any) you wish to highlight within each file.


:ref:`Assessments <assessments>`
--------------------------------
This allows you to set up assessments.


:ref:`Media <add-media>`
------------------------
This allows you to play audio files within your project.


:ref:`Global <global>`
----------------------

  .. image:: /img/guides/globalsettings.png
     :alt: Global Settings


- **Scripts** allows you to point to one or more `.js` files in your project (usually located within the `.guides` folder) that is run when the page is shown. This is especially useful when interacting with a button in a page of content.
- **Theme** allows you to select the default theme for people viewing the content. There is currently a light theme and a dark theme will be added at a later time. Dyslexic users can also choose a special theme from the Settings drop down in the content player.
- :ref:`Lexicon Topic <lexikon>`  if you use this option, an icon will appear in the toolbar that will load the Lexikon window with the selected topic automatically selected. Students can still access the Lexicon from the **Tools>Lexicon** menu (unless of course you are restricting the top menu available to them)
- **Suppress page numbering** allows you to suppress the section page numbers when in Play Mode.
- **Hide Menu** allows you to hide the main Codio menu items in the IDE (Codio/Project/File/Edit etc) when the assignment is run in a :ref:`course <add-remove-assignment>`).
- **Allow guide to be closed** allows students to be able to close the content. It can be restarted by selecting the Start icon in the file tree:

  .. image:: /img/guides/startguides.png
     :alt: StartGuides


- **Use Submit Buttons** see :ref:`Student submission options <student-submission>` for more information
- **Use Mark as Complete** see :ref:`Student submission options <student-submission>` for more information
- **Collapsed on start** starts the assignment with the guides pane collapsed. Students can show the content by clicking on the index icon on the right

  .. image:: /img/guides/guidecollapse.png
     :alt: OpenGuides

- **Hide Section List** hides the sections list in your content for the students. 
- **Hide Back to Dashboard button** hides this button that would otherwise show on the last page of the guides.
- **Protect Layout** prevents students from closing files in tabs.