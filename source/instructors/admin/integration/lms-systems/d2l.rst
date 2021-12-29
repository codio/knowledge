.. meta::
   :description: Connecting your Codio course with your D2L Learning Management System.


.. _d2l:

D2L
===


**In Codio:**

Enable LTI for Your Course
--------------------------

1. Open the course you would like to connect or create a new course.
2. Make sure you have at least one published assignment or add a new one. (see :ref:`Add and Remove Course Assignments <add-remove-assignment>`)
3. Select the **LTI/LMS** tab.
4. Select the **ENABLE LTI** option.  

  .. image:: /img/lti/enable-lti.png
     :alt: enable lti
     
5. Click **Save Changes**.

Bring up the LTI Integration Information
----------------------------------------

1. Click your user name in the bottom left of your dashboard.
2. Choose your Organization. 
3. Click the **LTI Integrations** tab to bring up the following settings.

  .. image:: /img/lti/LTIintegrationinfo.png
     :alt: Org LTI info

In D2L:

Create an External Learning Tools Link in D2L
---------------------------------------------

1. From the course homepage, select the **Edit Course** tab.
2. Under Site Resources, select **External Learning Tools**. 
3. Click the **New Link** button.
4. Under *"Title"* write Codio.
5. Paste ``https://apollo.codio.com/lti/link_endpoint`` in (1) the URL field.
6. Under the **Key/Secret** heading, first ensure that *"Sign messages with key/secret with"* and *"Link key/secret"* are selected. 
7. Copy the **LTI Consumer** information from Codio into (2).
8. Copy the **LTI Secret** information from Codio into (3).

  .. image:: /img/lti/D2Lscreenone.png
     :alt: D2L view

9. Fill in the Security fields as depicted in (4) below.

  .. image:: /img/lti/D2LScreen2.png
     :alt: D2L view 2
     
10. Click **Save**. 

Connect your D2L Modules to your Codio Assignments
--------------------------------------------------
1. Select the **Content** tab from the top of the page. 
2. Add a new module in your D2L course.
3. Select **Add Existing Activities** (1) -> **External Learning Tools** (2)

  .. image:: /img/lti/D2Lconnectassignment.png
     :alt: D2L view 3

4. From the list of available LTI links, select the Codio tool you created earlier.
5. Click on the Codio link to bring up all the Codio courses for which you have enabled LTI.
6. Select the Codio assignment you want to connect.
7. Refresh your page to view the rendered connection. You will see the Teacher view of the course with the connected assignment selected. Students will see the assignment opened in student mode.

Common Cartridge
----------------

If using the Common Cartridge file you should first set up an External Tool in Brightspace with the :ref:`LTI Key's and URL's <lti-keys-and-urls-information>` for your organization.

When done then in the Brightspace course you have created go to **Course Admin** and **Import/Export/Copy Components** and **Import Components** and proceed to upload the **.ismcc** file.

When completed, **View Content** and then **External Learning Tools** where you will see all the assignments listed.

Then go to **Content**, select **Existing Activities**, **External Learning Tools**, select your assignment from the list to add as an activity to the course. Repeat for each Codio assignment you wish to create an activity for


Single sign-in and account creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Codio maps D2L users to Codio users by using the D2L email address to identify the user and create the Codio account. In all subsequent access, the D2L userID will be used. In the event the user changes their email address in D2L, the user will be mapped to the same Codio account.

-  If the user does not have a Codio account, a new user account will be created in the background and the user will enter directly into the Codio content. The D2L user role is carried into Codio.
-  If the user already has an account they will enter into the Codio content without any sign-in required. If they already have a Codio account, but are not a member of the organization, they will be required to complete an email verification.


Teacher Roles
~~~~~~~~~~~~~

Based on the LMS role, if teachers join Codio via the LMS, the following will apply:

+----------------------+-----------------------------------------------------------------------------------------------------+
| LMS Role             | Will be added to Codio with these rights                                                            |
+======================+=====================================================================================================+
| Teaching Assistant   | TEACHER                                                                                             |
+----------------------+-----------------------------------------------------------------------------------------------------+
| Content Developer    | TEACHER                                                                                             |
+----------------------+-----------------------------------------------------------------------------------------------------+
| Mentor               | TEACHER (with :ref:`read only <add-teachers>` access to the course}                                 |
+----------------------+-----------------------------------------------------------------------------------------------------+
