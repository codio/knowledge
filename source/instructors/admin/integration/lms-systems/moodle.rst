.. meta::
   :description: Integrating with Moodle

.. _moodle:

Moodle
======

Please be sure to check out the :ref:`Codio LTI App <lti-app>` which allows for an easy way to integrate and to map Codio course assignments to your LMS system. Moodle added support for LTI™ apps in version 2.2. The `following page <https://docs.moodle.org/32/en/External_tool_settings>`__ explains how to set up external apps in Moodle.


.. important:: 
   Codio needs the User Role, Email Address and Name of the Moodle user in order to work. It is important that you access the LTI security settings and ensure that these three fields are enabled. If they are not available, contact Moodle support who can help you enable this. If enabled after you have mapped Codio content to Moodle, you may need to re publish for the changes to be implemented.



LTI 1.3 Dynamic Registration
-----------------------------

Dynamic Registration simplifies the setup process by automatically sharing configuration information between Tools and LMS systems. For LMS platforms that are compatible with this standard, you can enable it by following these steps. For more information on how to find the values in Codio please visit :ref:`Dynamic Registration <lti1-3DynReg>` .


Adding the Tool in Moodle
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/moodlepastedynreg.png
     :alt: Where you paste your Dynamic Registration URL in Moodle
     :width: 500px
     

1. Navigate to the **Manage Tools** section of your Site Administration and select the Plugins tab.
2. Paste the value you copied in the Tool URL field and click **Add LTI Advantage**.
3. It will present you with the Codio Organizations you are associated with, likely just one choice, but if there is more than one, select the organization you want to associate this tool with and click continue. It should be the organization that contains the courses you want to connect to the LMS system.
4. It will ask you to confirm that you want to register Codio as an external tool in the organization you selected. Click **Yes**. You will receive a confirmation from Codio that the action was completed.
5. The tool will appear at the bottom of the screen, click the Activate button.


.. image:: /img/LTI13dynregactivate.png
   :alt: Where you activate the tool
   :width: 200px

Return to Codio and refresh the **Integrations** page, you will see the integration you created in the bottom section of **LTI 1.3 Configurations** if everything has been set up properly.

Using the Tool in Moodle
~~~~~~~~~~~~~~~~~~~~~~~~

1. Navigate to your **My Courses** page and select the course you want to use.
2. Click the **More** tab.
3. From the **More** dropdown select **LTI External Tools**.
4. You will see the Codio tool, toggle **Show in activity chooser** on.

.. image:: /img/LTI13dynregshow.png
     :alt: Toggling on show in activity chooser for the Codio tool.
     :width: 600px
     :class: img-responsive

5. Go to your course and toggle on **Edit Mode** on the top right corner of screen.

.. image:: /img/editmodemoodle.png
     :alt: Toggling on edit mode.
     :width: 200px

6. Navigate to the module you would like to add an assignment and click the plus.
7. Click **Add an activity or resource**.
8. Click on the **All** tab to show all the tools and select Codio.
9. Click **Add**.
10. Click **Select Content** and that will bring up your list of Codio courses, select the course and assignment you want to connect.
 

Common Cartridge
----------------

If you are using a Common Cartridge file, you’ll first need to configure an External Tool in Moodle using your organization’s  :ref:`LTI Key's and URL's <lti-keys-and-urls-information>`.

Once the External Tool is set up, you can proceed with importing your Common Cartridge file by following the instructions provided on that same page.

Then in the Moodle course you have created:

1. Go to your course and click the **More** tab.
2. From the **More** dropdown select **Course reuse**.
3. Click **Restore**
4. Select the **.ismcc** to upload it and proceed to restore. 
5. **Restore**.  
6. Proceed through the steps.


.. note::
   Restore is required as Moodle currently does not support importing of **.imscc** files.
    


To confirm your setup, just click on any assignment available in Moodle. If all configurations are correct, you will be redirected straight to the Teacher view of that assignment in Codio.

Authentication and Account Creation
------------------------------------

To add students/teachers see :ref:`Users account creation <lms-users>`



LTI Version 1.3
----------------

LTI version 1.3 improves upon version [LTI-1.1] by moving away from the use of OAuth 1.0a-style signing for authentication and towards a new security model, using OpenID Connect, signed JWTs, and OAuth2.0 workflows for authentication. 


For more information, see `Learning Tools Interoperability Core Specification <https://www.imsglobal.org/spec/lti/v1p3/>`__

The deep linking url is : ``https://apollo.codio.com/lti/resource_selection``

