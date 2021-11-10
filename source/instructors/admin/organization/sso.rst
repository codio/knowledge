.. meta::
   :description: You can enable SSO integration to allow you to configure SSO engines and for your users to login through your SSO
   
.. _sso-integration:

Enable SSO Integration
======================

You can enable sso integration to integrate with your own SSO engine from the **Organization > Integrations** page in Codio.

    .. image:: /img/sso-integration.png
       :alt: SSO Integration
       
.. Important:: Your SSO Custom User fields need to be set up with **FirstName**,**LastName**,**Email Address** and **Role** (Teacher/Mentor or Student).

SSO Roles
---------

The SSO roles you set will determine whether the user accesses Codio as either a student or teacher. If your SSO supports Mentor role, that can also be set for teachers who you wish to access with :ref:`Read Only <add-teachers_org>` access.

Login URL
---------
       
When set up with your SSO, the login URL can then be used by your users to login through your SSO.  

.. Note:: Your users will still be able to access Codio from the usual login URL but will not be authenticated through your SSO.

Changing Email address in SSO
-----------------------------

If the users email address is changed in the future, the SSO userID will be used and the user will be mapped to the same Codio account.