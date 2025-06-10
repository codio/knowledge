.. meta::
   :description: Integrating with Moodle

.. _moodle:

Moodle
======

Please be sure to check out the :ref:`Codio LTI App <lti-app>` which allows for an easy way to integrate and to map Codio course assignments to your LMS system. Moodle added support for LTI™ apps in version 2.2. The `following page <https://docs.moodle.org/32/en/External_tool_settings>`__ explains how to set up external apps in Moodle.

Setup and Configuration
------------------------

.. raw:: html

    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Important Notice</title>
    </head>
    <body style="font-family: Arial, sans-serif; padding: 20px;">
        <div style="margin: 0 0 10px 20px; padding: 10px; background: #ffffff; border: 5px solid #2baeff;">
            <div style="background: #e6f5ff; padding: 5px 8px; margin: -10px -10px 8px -10px; border-radius: 2px;">
                <span style="color: #2baeff; font-weight: bold;">!</span> <strong>Important</strong>
            </div>
            Codio needs the User Role, Email Address and Name of the Moodle user in order to work. It is important that you access the LTI security settings and ensure that these three fields are enabled. If they are not available, contact Moodle support who can help you enable this. If enabled after you have mapped Codio content to Moodle, you may need to re publish for the changes to be implemented.
        </div>
    </body>
    </html>


**Video: Connect Moodle to Codio using the LTI Integration URL**

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/awib5ehvj0.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_awib5ehvj0 videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/awib5ehvj0/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

Common Cartridge
----------------

If using the Common Cartridge file you should first set up an External Tool in Moodle with the :ref:`LTI Key's and URL's <lti-keys-and-urls-information>` for your organization.
Then in the Moodle course you have created:

- Go to the course settings and **Restore**.
- Select the **.ismcc** to upload it and proceed to restore. 
- **Restore into this Course**.  
- Proceed through the steps.


.. raw:: html

    <div style= " margin: 0 0 10px 20px; padding: 10px; background: #f0f0f0; border: 3px solid #00ece5;">
    <strong>Note:</strong> Restore is required as Moodle currently does not support importing of <strong>.imscc </strong> files.
    </div>


To confirm your setup, just click on any assignment available in Moodle. If all configurations are correct, you will be redirected straight to the Teacher view of that assignment in Codio.

Authentication and Account Creation
------------------------------------

To add students/teachers see :ref:`Users account creation <lms-users>`






LTI 1.3 Dynamic Registration
-----------------------------

Dynamic Registration simplifies the setup process by automatically sharing configuration information between Tools and LMS systems. For LMS platforms that are compatible with this standard, you can enable it by following these steps.


Access LTI Integration Settings in Codio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/lti/codiolti13settings.png
     :alt: LTI 1.3 settings in Codio
     :align: right
     :width: 350px
     :class: img-responsive

1. Go to your organization account settings by clicking on your user name in the bottom left of your dashboard and then selecting your organization within **Organizations**.
2. Select the **LTI Integrations** tab.
3. Scroll down to the **LTI Integration 1.3** section. 
4. The **Dynamic Registration URL** is at the bottom of the list, you can copy it by clicking on the **Dynamic Registration URL** button.




Adding the Tool in Moodle
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/lti/moodlepastedynreg.png
     :alt: Where you paste your Dynamic Registration URL in Moodle
     :align: right
     :width: 500px
     :class: img-responsive

1. Navigate to the **Manage Tools** section of your Site Administration and select the Plugins tab.
2. Paste the value you copied in the Tool URL field and click **Add LTI Advantage**.
3. It will present you with the Codio Organizations you are associated with, likely just one choice, but if there is more than one, select the organization you want to associate this tool with and click continue. It should be the organization that contains the courses you want to connect to the LMS system.
4. It will ask you to confirm that you want to register Codio as an external tool in the organization you selected. Click **Yes**. You will receive a confirmation from Codio that the action was completed.
5. The tool will appear at the bottom of the screen, click the Activate button.



Activating the Tool You are Creating

  .. image:: /img/lti/LTI13dynregactivate.png
     :alt: Where you activate the tool

Return to Codio and refresh the **Integrations** page, you will see the integration you created in the bottom section if everything has been set up properly.

Using the Tool in Moodle
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/lti/LTI13dynregshow.png
     :alt: Toggling on show in activity chooser for the Codio tool.
     :align: right
     :width: 500px
     :class: img-responsive

1. Navigate to your **My Courses** page and select the course you want to use.
2. Turn on **Edit Mode**.
3. From the **More** dropdown select **LTI External Tools**.
4. You will see the Codio tool, toggle **Show in activity chooser** on.
5. Go to your course and click on **Add an activity or resource**.
6. Click on the **All** tab to show all the tools and select Codio.
7. Click **Select Content** and that will bring up your list of Codio courses, select the course and assignment you want to connect.



LTI Version 1.3
----------------

LTI version 1.3 improves upon version [LTI-1.1] by moving away from the use of OAuth 1.0a-style signing for authentication and towards a new security model, using OpenID Connect, signed JWTs, and OAuth2.0 workflows for authentication. As we have implemented the majority of these improvements already in Codio, we recommend using the LT1 1.1 integration instead of 1.3 unless your LMS specifically requires it, since it is much easier to set up using the :ref:`Codio LTI App <lti-app>`.


For more information, see `Learning Tools Interoperability Core Specification <https://www.imsglobal.org/spec/lti/v1p3/>`__

The deep linking url is : ``https://apollo.codio.com/lti/resource_selection``



How to Configure lti1.3 Tool in Moodle Manually
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/24smkegju4.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_24smkegju4 seo=false videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/24smkegju4/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>




Connecting/Mapping Assignments in Moodle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a number of ways you can connect/map assignments. Check out the following videos to see the option that best suits you.

How to Connect Assignment by lti Integration url 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/u6r8zfk9nc.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_u6r8zfk9nc seo=false videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/u6r8zfk9nc/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

How to Connect Assignment by Resource Selection Preview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/e7jx2wdpyq.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_e7jx2wdpyq seo=false videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/e7jx2wdpyq/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

How to Connect Assignment by Endpoint url
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/g10ydg4cs2.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_g10ydg4cs2 seo=false videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/g10ydg4cs2/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

How to Connect Assignment with Custom Param
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/493c2q31t5.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_493c2q31t5 seo=false videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/493c2q31t5/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

If you require any assistance, please don't hesitate to :ref:`contact us <codio-support>`
