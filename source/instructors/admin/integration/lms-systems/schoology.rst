.. meta::
   :description: Integrating with Schoology

.. _schoology:

Schoology
*********

Enable LTI for Your Course
--------------------------
In Codio
~~~~~~~~

The Schoology system administrator should install a Codio external tool for the course so that it is quick and easy for instructors to add material. The Schoology system administrator should follow these directions to install Codio as an external tool:

1. Open the course you would like to connect or create a new course.
2. Make sure you have at least one published assignment or add a new one. (see :ref:`Add and Remove Course Assignments <add-remove-assignment>`)
3. Select the **LTI/LMS** tab.
4. Select the **ENABLE LTI** option.  
5. Select the **ENABLE LTI CONSTANT URLS** option.  
6. Note the **Codio Course Target ID**, you will need that in subsequent steps. 
7. Click **Save**.

  .. image:: /img/lti/enable-lti-new.png
     :alt: enable lti and urls
        
Bring up the LTI Integration Information
----------------------------------------

8. Click your user name in the bottom left of your dashboard.
9. Select your Organization. 
10. Click the **LTI Integrations** tab to bring up the following settings. You will need to enter these into Schoology in the subsequent steps.

  .. image:: /img/lti/LTIintegrationinfo.png
     :alt: Org LTI info
     
In Schoology
~~~~~~~~~~~~

11. In your System Administrator account, click **Tools** in the header.
12. Select **School Management**.
13. Click **Integration** on the left. 
14. Click **External Tools**.
15. Click **Add External Tool Provider** and fill out the form:

  .. image:: /img/lti/external-tool-form.png
     :alt: External Tool Form

* **Tool name**: this is the name educators see when adding external tools to their courses, so call this **Codio**
* **Consumer Key**: this is the **LTI consumer key** from Codio (reference step 10 above)
* **Shared Secret**: this is the **LTI secret key** from Codio (reference step 10 above)
* **Privacy**: Schoology suggests **Name and email of the user who launches the tool**
* **Configuration Type**: choose Manual > Matchy By > URL
* **Domain/URL**: this is the **XML URL** from Codio (reference step 10 above)
* **Custom Parameters**: this is the **Codio Course Target ID** from Codio (reference step 6 above)

  .. Note:: If you are teaching more than one course in Codio, your system administrator will need to enter each course's **Codio Course Target ID** in the Custom Parameters field. Each **Codio Course Target ID** should be on a new line. 

16. Click submit.
     
Mapping an Assignment to a Schoology Assignment
-----------------------------------------------
In Schoology
~~~~~~~~~~~~

Once the system administrator has configured the external tool at the system level, return to your Materials page in Schoology. Then, to add the tool into your course:

17. Click **Add Materials**.
18. Select **Add File/Link/External Tool**.
19. Select **External Tool**.
20. Enter the required information in the External Tool Form: 

* **Tool Provider**: select Codio if it has been configured beforehand
* **Title**: name your assignment
* **URL**: you will need to go back into Codio for this information (see steps 21-24 below)

  .. image:: /img/lti/add-external-tool.png
     :alt: Add External Tool

In Codio
~~~~~~~~

21. Navigate to the course you would like to integrate with Schoology and go to the **Overview** area. 
22. Click the icon with 3 blue dots for each assignment you wish to map and select **LTI Integration URL.** Select the clipboard to copy the link.

    .. figure:: /img/lti/LMS-Unit-URL.png
       :alt: Unit URL

   .. Note:: If you would like to access all the LTI integration URLs at once, navigate to the course, then the **LTI/LMS** in the Admin section. Select **Assignment URLS** and a CSV will download that provides the information for the course in one place. 

In Schoology
~~~~~~~~~~~~

23. Go back to Schoology and paste the **LTI Integration URL** into the URL field of the Add External Tool form from step 20. 
24. You can enable grading on external tool items which adds the material to your Gradebook so that you can assign a grade for each student who completes the assignment launched via the external tool.

   .. Note:: LTI and external tool materials that have grading enabled in Schoology do not trigger submission notifications, grading reminders, or overdue notifications because Schoology does not automatically detect submissions from external tools. 