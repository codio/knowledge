.. meta::
   :description: LTI 1.3 Dynamic Registration

.. _lti1-3DynReg:

LTI 1.3 Dynamic Registration
============================

The Dynamic Registration specification automates the exchange of configuration information between Tools and LMS systems. This standard has not been implemented for all LMS systems but for those that support it you can set it up as follows.
The instructions below are for the Moodle LMS system but should be similar in other systems that have implemented this feature.

Access LTI Integration settings in Codio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Go to your organization account settings by clicking on your user name in the bottom left of your dashboard and then selecting your organization within **Organizations**.
2. Select the **LTI Integrations** tab.
3. Scroll down to the **LTI Integration 1.3** section. 
4. The **Dynamic Registration URL** is at the bottom of the list, you can copy it by clicking on the **Dynamic Registration URL** button.

The LTI 1.3 area of your LTI Integrations settings for your organization.
  .. image:: /img/lti/codiolti13settings.png
     :alt: LTI 1.3 settings in Codio

Adding the tool in Moodle
~~~~~~~~~~~~~~~~~~~~~~~~~
1. Navigate to the **Manage Tools** section of your Site Administration and select the Plugins tab.

The location where you paste the Dynamic Registration URL
  .. image:: /img/lti/moodlepastedynreg.png
     :alt: Where you paste your Dynamic Registration URL in Moodle
    
2. Paste the value you copied in the Tool URL field and click **Add LTI Advantage**.
3. It will present you with the Codio Organizations you are associated with, likely just one choice, but if there is more than one, select the organization you want to associate this tool with and click continue. It should be the organization that contains the courses you want to connect to the LMS system.
4. It will ask you to confirm that you want to register Codio as an external tool in the organization you selected. Click **Yes**. You will receive a confirmation from Codio that the action was completed.
5. The tool will appear at the bottom of the screen, click the Activate button.


Activating the tool you are creating
  .. image:: /img/lti/LTI13dynregactivate.png
     :alt: Where you activate the tool

Return to Codio and refresh the **Integrations** page, you will see the integration you created in the bottom section if everything has been set up properly.

Using the tool in Moodle
~~~~~~~~~~~~~~~~~~~~~~~~
1. Navigate to your **My Courses** page and select the course you want to use.
2. Turn on **Edit Mode**.
3. From the **More** dropdown select **LTI External Tools**.
4. You will see the Codio tool, toggle **Show in activity chooser** on.

Toggling on show in activity chooser for the Codio tool.
  .. image:: /img/lti/LTI13dynregshow.png
     :alt: Toggling on show in activity chooser for the Codio tool.
     
5. Go to your course and click on **Add an activity or resource**.
6. Click on the **All** tab to show all the tools and select Codio.
7. Click **Select Content** and that will bring up your list of Codio courses, select the course and assignment you want to connect.