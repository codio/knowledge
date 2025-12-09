.. meta::
   :description: Allow webhoooks to support passing of student data to extenal servers

.. _webhooks:

Webhooks
========

Webbhooks provide a way to receive Codio events at an endpoint you specify. 

The system does not retry webhook calls for missed events. You can query the API event object using the ``loadEvents`` function.

You can add Webhooks for your Codio organization from the **Organization > Integrations** page.

1. Click your username in the top-right corner, then select **Organization** from the menu.

2. In the **Organizations** tab, click the name of your organization.

   .. image:: /img/class_administration/createanorganization/organizations.png
      :alt: My Organizations

3. Click the **Integrations** tab and go to the **Webhooks** area and click **Add Webhook**.

Enter the URL of your server and click **Create**, the system will send a test request to check endpoint validity.


All requests contain a JWT signature you can verify using Codio keys https://apollo.codio.com/lti/oidc/certs (or https://apollo.codio.co.uk/lti/oidc/certs if you are working on codio.co.uk).

View an example here: https://github.com/iyashtykov/webhook-server

