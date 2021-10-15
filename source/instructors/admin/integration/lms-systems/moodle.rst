.. meta::
   :description: Integrating with Moodle

.. _moodle:

Moodle
======

Please be sure to check out the :ref:`Codio LTI App <lti-app>` which allows for an easy way to integrate and to map Codio course assignments to your LMS system. Moodle added support for LTI™ apps in version 2.2. The `following page <https://docs.moodle.org/32/en/External_tool_settings>`__ explains how to set up external apps in Moodle.

Setup and configuration
-----------------------

.. Important:: Codio needs the User Role, Email Address and Name of the Moodle user in order to work. It is important that you access the LTI security settings and ensure that these three fields are always enabled. If they are not available, contact Moodle support who can help you enable this. If enabled after you have mapped Codio content to Moodle, you may need to re publish for the changes to be implemented

**Video: Connect Moodle to Codio using the LTI Integration URL**

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/awib5ehvj0.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_awib5ehvj0 videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/awib5ehvj0/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

Common Cartridge
----------------

If using the Common Cartridge file you should first set up an External Tool in Moodle with the :ref:`LTI Key's and URL's <lti-keys-and-urls-information>` for your organisation.
When done then in the Moodle course you have created:

- go to the course settings and **Restore**, 
- select the **.ismcc** to upload it and proceed to restore, 
- and **Restore into this Course**.  
- Proceed through the steps.

.. Note:: It is Restore that is required as Moodle currently does not support importing of **.imscc** files

When completed, you can check all is correct by then selecting any of the assignments listed in Moodle. If all OK you will be taken to the **Teacher** view of the assignment in Codio

Authentication and account creation
-----------------------------------

To add students/teachers see :ref:`Users account creation <lms-users>`