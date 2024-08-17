.. meta::
   :description: Audio, Images and Videos can be added to a Guide page.

.. _add-media:

Adding media
============

Audio, Images and Videos can be added to a Guide page.

Audio
*****
Audio files can be added to and played from your project.

To add Audio: select **Media** icon in the guides editor ribbon where you can define the source audio file along with any actions the should be triggered at specific times during playback.


  .. image:: /img/guides/ribbon-media.png
     :alt: Media



- **Source Name** - select the source file either from `.guides/media` folder if already uploaded to the project or upload directly from your PC and it will be stored in the `.guides/media` folder.
- **Add Action** - specifies actions that are triggered at specific times during playback. The following options are available.

  Open file
  Close file
  Open Terminal
  Close Terminal
  Run command
  Highlight
  Close all tabs
  Pause


.. _record-audio:

Recording Audio inside Guide
****************************

You can record audio using a guide button and save that audio in a file. To add record button, select Record Audio icon in the guides editor ribbon. 

  .. image:: /img/guides/ribbon-record-audio.png
     :alt: Record audio button

Once the button code appears on the guide page, you can change the button text and the file location as per your requirement. If you want to hide the generated audio file from students then save the file in .guides folder.

To record the audio, permission for your microphone is required and your browser will prompt you to allow permission. If permission has been denied, you can re enable in your browser, if you do not know how then see :ref:`Permissions <permissions>`.


Images
******
Inserting an image is similar. You can use the **Image** icon in the guides editor ribbon or write in markdown within your content area. Here are some examples. PNG and JPG image types are supported. Note that the 2nd and 3rd examples point to images within your project.

Store your images in the `.guides/img` folder if you do not want them to be readily accessible to students.

.. code:: markdown

    ![optional alt tag](http://any-url-you-like.png)
    ![](image-in-project-root.jpg)
    ![](.guides/img/best-place-for-images.png)



You can drag/drop images from your project file tree into your content. They will automatically contain the correct path.

For Markdown pages:

.. code:: markdown

    ![.guides/img/displayimage](.guides/img/displayimage.png)


For HTML pages:

.. code:: html

    ![.guides/img/displayimage](.guides/img/displayimage.png)



Videos
******

You can use the **Image** icon in the guides editor ribbon defining the URL to the video or you can manually add to your content.

Include embedded videos using the standard `<iframe>` html tag.


YouTube
-------

If you wish to embed a YouTube video, go to the Share option and select **Embed** to obtain the code snippet.

  .. image:: /img/guides/guides_youtube.png
     :alt: You Tube embed



```
<iframe width="560" height="315" src="//www.youtube.com/embed/1JNhoVbmNAo" frameborder="0" allowfullscreen></iframe>
```

Vimeo
-----

  If you wish to embed a Vimeo video, go to the Share option and select **Embed** to obtain the code snippet.

  .. image:: /img/guides/guides_vimeo.png
     :alt: Vimeo embed



```
<iframe src="//player.vimeo.com/video/110479088" width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> <p><a href="http://vimeo.com/110479088">Codio - Innovation in Computer Programming Education</a> from <a href="http://vimeo.com/user20752628">Codio</a> on <a href="https://vimeo.com">Vimeo</a>.</p>
```

Hyperlinks
**********
Creating a hyperlink on a piece of text is easy.

.. code:: markdown

    Go to [Google](google.com) to look stuff up.




iframes
*******

You can embed content in an iframe using the `<iframe>` html tag.

To embed from Google Docs, go to **File>Publish** to Web and select **Embed** to get the code snippet

  .. image:: /img/guides/guides_publish.png
     :alt: iframe embed




