.. meta::
   :description: Use the Codio Bookstore Portal to sign up your bookstore and order Codio access codes for your students.

.. _bookstore-portal:

Bookstore Portal
================

About the Bookstore Portal
--------------------------

The **Codio Bookstore Portal** lets campus bookstores order Codio access codes for their students. From the portal, you can sign up your bookstore, place orders for access codes, and follow the status of each order.

The portal is available at https://bookstore-portal.codio.com.

.. image:: /img/bookstore/bookstore_home.png
    :width: 80%
    :align: center
    :alt: Codio Bookstore Portal home page with the Sign In and Sign Up Your Bookstore buttons.

.. note::

   **Password-less sign-in:** The Bookstore Portal does not use passwords. Each time you sign in, the portal emails you a single-use **magic link** that signs you in.

Signing Up Your Bookstore
-------------------------

Before you can place orders, your bookstore needs an approved account. Codio reviews every signup before activating the account.

1. Go to https://bookstore-portal.codio.com and click **Sign Up Your Bookstore**. You can also click the **Sign up your bookstore** link on the **Sign in** page.

2. Complete the form. The fields are described in the table below.

   .. image:: /img/bookstore/bookstore_signup_form.png
       :width: 70%
       :align: center
       :alt: Sign up your bookstore form.

3. Click **Submit Signup**.

4. A confirmation message appears. Codio reviews your signup within one business day and emails you once your account is approved.

   .. image:: /img/bookstore/bookstore_signup_wait.png
       :width: 70%
       :align: center
       :alt: Signup confirmation message.

.. important::

   You cannot sign in until Codio approves your account. Wait for the approval email before you request a magic link.

Signup fields
~~~~~~~~~~~~~

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Field
     - Required
     - Description
   * - **Bookstore name**
     - Yes
     - The name of your bookstore.
   * - **Institution you serve**
     - Yes
     - The university or school your students belong to. This value appears as the institution on every order.
   * - **Country**
     - Yes
     - The country of your bookstore. It is used for your account record only and does not set your Bookstore ID.
   * - **State**
     - Conditional
     - Required when **Country** is United States.
   * - **Address**
     - No
     - The street address of your bookstore.
   * - **ZIP code**
     - Conditional
     - Required for United States addresses. Optional for international addresses, where the field is labeled **ZIP / postal code (optional)**.
   * - **Your email**
     - Yes
     - The email address you use to sign in and manage the account. Magic links are sent to this address.
   * - **Your name**
     - Yes
     - The name of the account contact.
   * - **Phone**
     - No
     - A contact phone number.
   * - **Anything we should know?**
     - No
     - Any additional information for the Codio review team.

Signing In
----------

1. Go to https://bookstore-portal.codio.com and click **Sign In**.

2. Enter the email address associated with your bookstore account and click **Send Magic Link**.

   .. image:: /img/bookstore/bookstore_signin.png
       :width: 70%
       :align: center
       :alt: Sign in page with the email field and the Send Magic Link button.

3. The **Check your email** page appears. For security reasons, this page looks the same whether or not an account exists for the email you entered. If no email arrives, make sure you used the correct address and that your account has been approved.

   .. image:: /img/bookstore/bookstore_signin_checkemail.png
       :width: 60%
       :align: center
       :alt: Check your email page.

4. Open the email from Codio and click the magic link. Your dashboard opens.

.. important::

   The magic link expires after **15 minutes** and can be used **only once**. If your link has expired, or you have already used it, return to the **Sign in** page and request a new one. If you don't see the email, check your spam folder.

Dashboard
---------

After you sign in, the dashboard shows your bookstore name, address, and **Bookstore ID**. From the dashboard you can:

- Click **Place New Order** to order access codes.
- Click **Refund Access Codes** to request a refund.
- Review your previous orders under **Recent orders**.

.. image:: /img/bookstore/bookstore_dashboard.png
    :width: 90%
    :align: center
    :alt: Bookstore Portal dashboard.

Placing a New Order
-------------------

1. On the dashboard, click **Place New Order**. If you have not placed any orders yet, you can also click **Place Your First Order** under **Recent orders**.

2. On the **Upload your PO** step, choose one of the following options:

   - **Upload a purchase order (PO):** Click the upload area, choose your PO file, and click **Extract with AI**. The portal reads the PO and fills in the order details for you. The file must be a PDF of up to 4 MB.
   - **Enter the details yourself:** Click **Skip and Enter Manually**.

   .. image:: /img/bookstore/bookstore_neworder_po.png
       :width: 90%
       :align: center
       :alt: Upload your PO step with the Extract with AI and Skip and Enter Manually buttons.

   .. note::

      The **Extract with AI** button is available only after you choose a PDF. Always review the extracted details before you submit the order.

3. Complete the **Review order details** section. The fields are described in the table below.

   .. image:: /img/bookstore/bookstore_neworder_form.png
       :width: 90%
       :align: center
       :alt: Review order details section with the Subscription type list open.

4. Scroll down to the **Confirmation** section and review the order summary, including the **Unit price** and **Total**.

5. Click **Submit Order**.

6. The **Order details** page opens with the status **Processing**. Codio prepares your access codes and invoice, and the page updates automatically.

   .. image:: /img/bookstore/bookstore_order_details.png
       :width: 90%
       :align: center
       :alt: Order details page showing the order summary.

From the **Order details** page, click **Back to Dashboard** to return to the dashboard, or **Place Another Order** to start a new order.

Order fields
~~~~~~~~~~~~

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Field
     - Required
     - Description
   * - **Institution served**
     - Read-only
     - Set on your account during signup. To change it, contact accounts@codio.com.
   * - **Quantity of codes needed**
     - Yes
     - The number of access codes to order.
   * - **Subscription type**
     - Yes
     - The product to order. Each option shows the product name and its ISBN.
   * - **PO reference number**
     - No
     - Your purchase order number, for your records.
   * - **Recipient email**
     - Yes
     - The email address that receives the access codes.
   * - **Billing contact email**
     - Yes
     - The email address that receives the invoice.
   * - **Notes for Codio**
     - No
     - Any additional information about the order.
