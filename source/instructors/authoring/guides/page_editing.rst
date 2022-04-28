.. meta::
   :description: Editing the content of a Guides page

.. _page-editing:

Page editing overview
=====================
To create new content or to edit existing content, go to the **Tools->Guide->Edit** menu option.

Use the **Split View** button to switch into split view mode.

Use the **Preview** button to switch into  preview mode.

When in preview mode, you can quickly switch back to editor mode by selecting the **Edit** button:

.. image:: /img/guides/editor.png
     :alt: Guides Edit Mode



**Video: Editing Existing Guides Content**


.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/p1d771yk2v.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_p1d771yk2v seo=false videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/p1d771yk2v/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>


Anatomy of the content editor
*****************************
Below is a screenshot of the editor with the main components highlighted.

  .. image:: /img/guides/editbook.png
     :alt: overview



Layout
******


  .. image:: /img/guides/guideslayout.png
     :alt: Layout settings


Layout settings gives you access to the key functions:


  - :ref:`Layout <layout>` allows you to specify the number of panels/columns you want to choose for this section, or set to **Previous** to inherit the layout settings from the previous page.
  - **Show File Tree** allows you to define whether to show or hide the file tree.
     - :ref:`Show Folders <show-hide-folders>` allows you to define specific folders in your project that you wish to be visible when the current section is displayed.
  - **Content Type** allows you to write your content in either :ref:`Markdown <markdown-content-editing>` or :ref:`HTML <html-content>`.
  - **Guides on Left** allows you to define whether the guides content shows on the left or right.
  - :ref:`Teacher Only <teacher-only>` allows you to show content that only teachers are able to see.      
  - :ref:`Close Tabs <close-tabs>` allows you to close all tabs open from previous section.
      - **Close Terminal Session** when Close tabs enabled, allows you the option to retain terminal session from previous section. By default, terminal session will close.
  - :ref:`Teacher Only <teacher-only>` allows you to show content that only teachers are able to see.
  - **Learning Objectives** allows you to define learning objectives for this section.
  - :ref:`Open Tabs <open-tabs>` allows you to specify:
      - which files you want to automatically open when the current section is displayed,
      - Preview (including external websites),
      - Open a Terminal window (including running a terminal command),
      - which lines (if any) you wish to highlight within each file.



:ref:`Assessments <assessments>`
********************************

  .. image:: /img/guides/guidesassessments.png
     :alt: Assessment settings

This allows you to set up assessments and view all assessments in the assignment/project



:ref:`Settings <global>`
************************

  .. image:: /img/guides/guidessettings.png
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

- **Hide Section Toggle** hides the sections list in your content for the students. 
- **Hide Back to Dashboard button** hides this button that would otherwise show on the last page of the guides.
- **Protect Layout** prevents students from closing files in tabs.