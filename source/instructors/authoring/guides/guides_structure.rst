.. meta::
   :description: This page explains how to create a guide structure that works in Codio.

.. _guides-structure:

Codio Guides Reference
======================

This page describes the structure, naming rules, and JSON fields used to create Codio Guides.

It is written for both of these workflows:

* authoring guides with AI assistance
* generating guide files programmatically outside Codio

In both cases, the output is the same: a normal guide definition stored in the project filesystem.

.. caution::

   We might change these settings from time to time. Use them at your own risk.


Guide structure
---------------

A Codio Guide is defined inside the ``.guides`` directory.

The standard structure is:

::

   .guides/
   ├── content/
   │   ├── index.json
   │   ├── <page-stem>.json
   │   ├── <page-stem>.md
   │   ├── <container-stem>/
   │   │   ├── index.json
   │   │   ├── index.md
   │   │   ├── <child-page-stem>.json
   │   │   ├── <child-page-stem>.md
   │   │   └── <child-container-stem>/
   │   │       ├── index.json
   │   │       └── ...
   ├── assessments/
   │   └── <assessment files>
   ├── img/
   │   └── <image assets>
   └── secure/
       └── <hidden files>

   <project files at repository root>

The key directories are:

.. list-table:: Guide directories
   :widths: 20 80
   :header-rows: 1

   * - Path
     - Purpose
   * - ``.guides/content/``
     - Stores the guide definition, including the root guide configuration, page metadata, container metadata, and Markdown content.
   * - ``.guides/assessments/``
     - Stores assessment definitions used by guide content.
   * - ``.guides/img/``
     - Stores image assets referenced by guide content.
   * - ``.guides/secure/``
     - Stores files hidden from students. This is a good place for secure resources, answer keys, or solutions that should not be exposed in the learner workspace.
   * - project root
     - Stores non-guide files used by the workspace, such as source files, scripts, notebooks, or starter code opened by guide steps.

Important notes
~~~~~~~~~~~~~~~

* Images used by guide content should be stored in ``.guides/img/``.
* When embedding images in Markdown, reference them from the project root, for example ``.guides/img/img1.png``. Do not use relative paths such as ``../img/img1.png``.
* Other files opened by the guide, such as ``.py`` files or project assets, should live at the project root or in normal project folders outside ``.guides``.
* Assessment definitions live in ``.guides/assessments/`` and are separate from normal guide content pages.
* Files that must remain hidden from students can be stored in ``.guides/secure/``.
* A guide can contain only pages, or it can also include sections, chapters, or both.
* Chapters and sections are fully optional organizational containers.
* Sections are not limited to chapters. They are organizational containers and can be used wherever they help structure content.

Content model
-------------

Codio Guides use three content item types:

* ``page``
* ``section``
* ``chapter``

These types serve different roles:

.. list-table:: Content item types
   :widths: 18 82
   :header-rows: 1

   * - Type
     - Description
   * - ``page``
     - A leaf item that displays instructional content from a Markdown file and can define a workspace layout.
   * - ``section``
     - An optional container used to group pages or other content items. It can also carry its own Markdown content and layout settings, but content is not required.
   * - ``chapter``
     - An optional higher-level container used to organize related sections or pages. It can also carry its own Markdown content and layout settings, but content is not required.

Pages are stored as paired ``.json`` and ``.md`` files.

Sections and chapters are stored as folders with an ``index.json`` file and, optionally, an ``index.md`` file.

In other words, chapters and sections are entirely optional, and when they are used, they do not need to contain their own Markdown content unless you want them to display content directly.

Naming conventions
------------------

Use readable file and folder names with a short unique suffix.

Recommended pattern:

* page files: ``intro-to-loops-a1b2.json`` and ``intro-to-loops-a1b2.md``
* section folders: ``python-basics-c3d4/``
* chapter folders: ``getting-started-e5f6/``

This convention makes the guide easier to read and keeps item names unique.

Why the suffix matters
~~~~~~~~~~~~~~~~~~~~~~

Every content item should have a stable stem that is both human-readable and unique. The short suffix at the end helps avoid collisions when two items have similar titles.

The same stem is used in three places:

* the file or folder name
* the parent ``order`` array
* the paired Markdown and JSON filenames for pages

For example:

* page metadata: ``intro-to-loops-a1b2.json``
* page content: ``intro-to-loops-a1b2.md``
* parent order entry: ``"intro-to-loops-a1b2"``

If you rename a page, section, or chapter, update every parent ``order`` entry that references it.

Recommended naming rules
~~~~~~~~~~~~~~~~~~~~~~~~

* use lowercase letters and hyphens for the readable part
* keep the suffix short and stable
* use the same stem for both the ``.json`` and ``.md`` page files
* avoid spaces in file and folder names
* make stems descriptive enough to remain readable in ``order`` arrays

Root guide file
---------------

The root configuration file is ``.guides/content/index.json``.

Example:

::

   {
     "title": "my-guide",
     "theme": "light",
     "scripts": [],
     "suppressPageNumbering": true,
     "useSubmitButtons": true,
     "useMarkAsComplete": true,
     "hideMenu": false,
     "allowGuideClose": false,
     "collapsedOnStart": false,
     "hideSectionsToggle": false,
     "hideBackToDashboard": false,
     "protectLayout": false,
     "order": [
       "intro-a1b2",
       "python-basics-c3d4",
       "assessment-e5f6"
     ]
   }

.. list-table:: Root ``index.json`` fields
   :widths: 24 18 58
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``title``
     - string
     - Display name of the guide.
   * - ``theme``
     - string
     - Fixed to ``"light"``.
   * - ``scripts``
     - array
     - Guide-level scripts configuration.
   * - ``suppressPageNumbering``
     - boolean
     - Hides page numbering in the guide UI.
   * - ``useSubmitButtons``
     - boolean
     - Enables submit buttons.
   * - ``useMarkAsComplete``
     - boolean
     - Enables the mark-as-complete action.
   * - ``hideMenu``
     - boolean
     - Hides the guide menu when set to ``true``.
   * - ``allowGuideClose``
     - boolean
     - Controls whether learners can close the guide.
   * - ``collapsedOnStart``
     - boolean
     - Starts navigation in a collapsed state when set to ``true``.
   * - ``hideSectionsToggle``
     - boolean
     - Hides the sections toggle when set to ``true``.
   * - ``hideBackToDashboard``
     - boolean
     - Hides the back-to-dashboard control when set to ``true``.
   * - ``protectLayout``
     - boolean
     - Prevents layout changes when set to ``true``.
   * - ``order``
     - array of strings
     - Defines the top-level reading order. Each entry must match the stem of a top-level page file or the name of a top-level chapter or section folder.

Pages
-----

A page is defined by two files with the same stem:

* ``<page-stem>.json``
* ``<page-stem>.md``

The JSON file defines metadata and workspace behavior. The Markdown file contains the visible page content.

Example page JSON:

::

   {
     "id": "91173adf-f264-7e53-aada-aaf497a54450",
     "title": "New Page",
     "files": [
       {
         "path": "example.py",
         "panel": 0,
         "action": "open"
       }
     ],
     "layout": "2-panels-tree",
     "path": [],
     "type": "page",
     "contentType": "markdown",
     "teacherOnly": false,
     "closeTerminalSession": true,
     "learningObjectives": ""
   }

.. list-table:: Page JSON fields
   :widths: 24 18 58
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``id``
     - string
     - Unique UUID identifier for the page.
   * - ``title``
     - string
     - Display title shown in the guide UI.
   * - ``files``
     - array
     - Files, tabs, and terminal actions to apply when the page opens.
   * - ``layout``
     - string
     - Workspace layout to use for the page.
   * - ``path``
     - array
     - Path metadata for the item. In the current format this is represented as an array.
   * - ``type``
     - string
     - Fixed to ``"page"`` for page files.
   * - ``contentType``
     - string
     - Fixed to ``"markdown"``.
   * - ``teacherOnly``
     - boolean
     - Restricts visibility to teachers when set to ``true``.
   * - ``closeTerminalSession``
     - boolean
     - Controls whether terminal sessions are closed when navigating away from the item.
   * - ``learningObjectives``
     - string
     - Learning objectives text for the item.

Sections and chapters
---------------------

Sections and chapters are directory-based content items.

They are optional. You can build a guide using only pages, or introduce sections, chapters, or both when they improve organization.

A section or chapter folder contains:

* ``index.json``
* optionally, ``index.md``
* child pages, child sections, or both

Minimal example:

::

   {
     "id": "5d58b1fa-8496-6737-42b8-79b1ea87db57",
     "type": "section",
     "title": "Section",
     "order": [
       "intro-to-loops-a1b2"
     ]
   }

Extended example:

::

   {
     "id": "fae10178-28cf-9d65-7308-ef99c43efb27",
     "type": "chapter",
     "title": "Another Chapter",
     "order": [
       "another-section-c3d4"
     ],
     "files": [
       {
         "path": "#tabs",
         "action": "close"
       }
     ],
     "layout": "1-panel",
     "path": [],
     "contentType": "markdown",
     "teacherOnly": false,
     "closeTerminalSession": true,
     "learningObjectives": ""
   }

By default, sections and chapters are often used as organizational containers only. In that case, an ``index.md`` file is not required.

.. list-table:: Section and chapter fields
   :widths: 24 18 58
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``id``
     - string
     - Unique UUID identifier for the item.
   * - ``type``
     - string
     - ``"section"`` or ``"chapter"``.
   * - ``title``
     - string
     - Display title shown in the guide UI.
   * - ``order``
     - array of strings
     - Child item order for pages, sections, or both.
   * - ``files``
     - array
     - Optional workspace actions applied when the item opens.
   * - ``layout``
     - string
     - Optional workspace layout applied to the item.
   * - ``path``
     - array
     - Path metadata for the item.
   * - ``contentType``
     - string
     - Fixed to ``"markdown"``.
   * - ``teacherOnly``
     - boolean
     - Restricts visibility to teachers when set to ``true``.
   * - ``closeTerminalSession``
     - boolean
     - Controls terminal cleanup behavior.
   * - ``learningObjectives``
     - string
     - Learning objectives text for the item.

Shared item settings
--------------------

Layout-related settings are shared across pages, sections, and chapters.

This means that the following fields can appear on any of those item types:

* ``files``
* ``layout``
* ``path``
* ``contentType``
* ``teacherOnly``
* ``closeTerminalSession``
* ``learningObjectives``

In practice, this allows both container items and leaf pages to carry their own content, workspace setup, and instructional metadata.

Layout options
--------------

The following layout values are some of the available options in the current format:

.. list-table:: Layout values
   :widths: 28 72
   :header-rows: 1

   * - Layout value
     - Description
   * - ``1-panel``
     - Single-panel layout.
   * - ``2-panels-tree``
     - Two-panel layout with the file tree visible.
   * - ``3-cell``
     - Three-cell layout.
   * - ``3-columns-guides-left``
     - Three-column layout with the guide on the left.
   * - ``4-cell``
     - Four-cell layout.

Files actions
-------------

The ``files`` array controls workspace state when an item opens.

Example:

::

   "files": [
     {
       "path": "#tabs",
       "action": "close"
     },
     {
       "path": "anotherfile.py",
       "panel": 0,
       "action": "open"
     },
     {
       "path": "example.py",
       "panel": 2,
       "action": "open"
     },
     {
       "path": "#terminal: python example.py",
       "panel": 3,
       "action": "open"
     }
   ]

.. list-table:: ``files`` entry fields
   :widths: 24 18 58
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``path``
     - string
     - Target to open or close. This can be a workspace file path or a special token such as ``#tabs`` or ``#terminal: ...``.
   * - ``panel``
     - integer
     - Target panel index. Available values shown in the current format are ``0``, ``1``, ``2``, and ``3``.
   * - ``action``
     - string
     - Action to perform. Available values are ``"open"`` and ``"close"``.

Special ``path`` values
~~~~~~~~~~~~~~~~~~~~~~~

The following ``path`` patterns are supported in the current format:

.. list-table:: Special path patterns
   :widths: 28 72
   :header-rows: 1

   * - Path value
     - Purpose
   * - ``#tabs``
     - Targets open editor tabs. Commonly used with ``"action": "close"``.
   * - ``#terminal:``
     - Opens a terminal without a startup command.
   * - ``#terminal: <command>``
     - Opens a terminal and starts it with the given command.
   * - normal file path
     - Opens a file from the project workspace, such as ``example.py``.

Markdown content
----------------

Guide content is authored in Markdown. For more information see :ref:`Content Editing <markdown-content-editing>`.

For pages, the Markdown content lives in the paired ``<page-stem>.md`` file.

For sections and chapters, Markdown content can live in ``index.md`` inside the item folder. This is optional.

Programmatic generation
-----------------------

Codio Guides can be generated outside Codio as long as the filesystem structure and JSON conventions are respected.

This makes it possible to:

* generate guides from templates
* build guides from structured data
* use AI to draft content and metadata
* store guides in version control and update them through automation

When generating guides programmatically:

* keep stems stable and unique
* make sure every ``order`` entry matches a real file or folder stem
* generate both the ``.json`` and ``.md`` file for every page
* place images in ``.guides/img/``
* reference embedded images from the project root, for example ``.guides/img/img1.png``
* place assessment files in ``.guides/assessments/``
* place secure or hidden resources in ``.guides/secure/`` when appropriate
* place workspace files outside ``.guides`` in the normal project structure
* use ``contentType: "markdown"`` and ``theme: "light"`` as fixed values

Authoring recommendations
-------------------------

A reliable workflow is:

#. create the root ``.guides/content/index.json``
#. add top-level pages, sections, or chapters as needed
#. create paired ``.json`` and ``.md`` files for every page
#. create ``index.json`` and optional ``index.md`` files for sections and chapters when using them
#. define each parent ``order`` array using exact child stems
#. add workspace files at the project root
#. add assessments to ``.guides/assessments/`` when needed
#. add images to ``.guides/img/``
#. add hidden resources or solutions to ``.guides/secure/`` when needed
#. validate that every referenced stem, file path, panel, and layout value is correct

Minimal examples
----------------

Single page at the root level:

::

   .guides/content/
   ├── index.json
   ├── intro-a1b2.json
   └── intro-a1b2.md

Section used as an organizational container:

::

   .guides/content/
   ├── index.json
   └── python-basics-c3d4/
       ├── index.json
       ├── variables-e5f6.json
       └── variables-e5f6.md

Chapter containing a section and page:

::

   .guides/content/
   ├── index.json
   └── getting-started-g7h8/
       ├── index.json
       ├── index.md
       └── setup-i9j0/
           ├── index.json
           ├── first-run-k1l2.json
           └── first-run-k1l2.md
