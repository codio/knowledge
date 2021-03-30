.. meta::
   :description: Page Editing

## Page editing overview
To create new content or to edit existing content, go to the **Tools->Guide->Edit** menu option.

Use the layout modes to switch between editor, preview, and split view modes.

When in preview mode, you can quickly switch back to editor mode by selecting the **Editor** button:

![Guides Edit Mode](/img/guides/editor.png)

**Video: Editing Existing Guides Content**

<p><a href="https://codio.wistia.com/medias/zqcpii19s6?wvideo=zqcpii19s6"><img src="https://embed-fastly.wistia.com/deliveries/245d383ed4a7ad83fb3addb91c089c17.jpg?image_play_button_size=2x&amp;image_crop_resized=960x540&amp;image_play_button=1&amp;image_play_button_color=1e71e7e0" width="400" height="225" style="width: 400px; height: 225px;"></a></p>


### Anatomy of the content editor
Below is a screenshot of the editor with the main components highlighted.
![overview](/img/guides/editbook.png)

### Editor settings
Editor settings gives you access to the key functions:

#### Page
  - **[Layout](/courses/settings-actions/#page)** allows you to specify the panel layout you want to choose for this section,
  - **[Show Folders](/courses/authoring/#hiding-folders)** allows you to define specific folders in your project that you wish to be visible when the current section is displayed,
  - **[Close Tabs](/courses/authoring/#openclose-tabs-from-content)** allows you to close all tabs open from previous section,
  - **Set Section as Chapter** allows you to set the section as a chapter in your content,
  - **[Teacher Only](/courses/authoring/#teacher-only-content)** allows you to show content that only teachers are able to see.
  - **Content Type** allows you to write your content in either [Markdown](/courses/authoring/#markdown-content-editing) or [HTML](/courses/authoring/#html-content-editing)

#### [Open Tabs](/courses/settings-actions/#open-tabs)
This allows you to specify:

  - which files you want to automatically open when the current section is displayed,
  - Preview (including external websites),
  - Open a Terminal window (including running a terminal command),
  - which lines (if any) you wish to highlight within each file.


#### [Assessments](/courses/assessments/#assessments)
This allows you to set up assessments.

#### [Media](/courses/authoring/#adding-media)
This allows you to play audio files within your project.


#### [Global](/courses/settings-actions/#global)
![Global Settings](/img/guides/globalsettings.png)

- **Scripts** allows you to point to one or more `.js` files in your project (usually you would have this somewhere within the `.guides` folder) that is run when the page is shown. This is especially useful when interacting with a button in a page of content.
- **Theme** allows you to select the default theme for people viewing the content. We currently have a light theme and will be adding a dark theme shortly. Dyslexic users can also choose a special theme from the Settings drop down in the content player.
- **[Lexicon Topic](/resources/Resource-Tools/lexikon/)**  if you use this option, an icon will appear in the toolbar that will load the Lexikon window with the selected topic automatically selected. Students can still access the Lexicon from the **Tools>Lexicon** menu (unless of course you are restricting the top menu available to them)
- **Suppress page numbering** allows you to suppress the section page numbers when in Play Mode.
- **Hide Menu** allows you to hide the main Codio menu items in the IDE (Codio/Project/File/Edit etc) when the assignment is run in a [course](/courses/classes/#assign-a-project-to-the-course).
- **Allow guide to be closed** allows students to be able to close the content. It can be restarted by selecting the Start icon in the file tree:

![StartGuides](/img/guides/startguides.png)

- **Use submit buttons** see [Student submission options](/courses/assessments/#student-submission-options) for more information
- **Use mark as completed** see [Student submission options](/courses/assessments/#student-submission-options) for more information
- **Collapsed on start** starts the assignment with the guides pane collapsed. Students can show the content clicking on the hamburger icon on the right
![OpenGuides](/img/guides/guidecollapse.png)
- **Hide Section List** hides the sections list in your content for the students. 
- **Hide Back to Dashboard button** hides this button that would otherwise show on the last page of the guides.
- **Protect Layout** prevents students from closing files in tabs.