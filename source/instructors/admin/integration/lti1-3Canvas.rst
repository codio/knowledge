.. meta::
   :description: LTI 1.3 for Canvas

.. _lti1-3Canvas:

LTI 1.3 for Canvas
==================

On this page, you will find detailed step-by-step guidelines to help you integrate your Canvas and Codio accounts and connect assignments between the two applications.


LTI version 1.3 improves upon version 1.1 by moving away from the use of OAuth 1.0a-style signing for authentication and towards a new security model, using OpenID Connect, signed JWTs, and OAuth2.0 workflows for authentication.
For more information, see Learning Tools Interoperability Core Specification

The deep linking url is : https://apollo.codio.com/lti/resource_selection


Part 1: In Canvas - Create a Developer Key
------------------------------------------
The Canvas user who carries out these steps must be a system administrator.


+-----------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| .. raw:: html                                                                           |                                                                                                                                                              |
|                                                                                         |                                                                                                                                                              |
|     <div class="small">                                                                 |                                                                                                                                                              |
|      <strong>In Codio:</strong><br>                                                     |    |image1|                                                                                                                                                  |
|     1. Click your username in the                                                       |                                                                                                                                                              |
|        top-right corner, then select <strong>Organization</strong> from the menu.       |                                                                                                                                                              |
|        In the Organizations area, click the name of your organization.<br><br>          |                                                                                                                                                              |
|                                                                                         |                                                                                                                                                              |
|     2. Select the <strong>LTI Integrations</strong> tab.<br><br>                        |                                                                                                                                                              |
|     3. Scroll down to the <strong>LTI Integration 1.3</strong> section; you should      |                                                                                                                                                              |
|         see the following fields. Keep this page open.                                  |                                                                                                                                                              |
|     </div>                                                                              |                                                                                                                                                              |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| .. raw:: html                                                                           |                                                                                                                                                              |
|                                                                                         |                                                                                                                                                              |
|     <div class="small">                                                                 |                                                                                                                                                              |
|      <strong>In Canvas:</strong><br>                                                    |    |image2|                                                                                                                                                  |
|     4. Select <strong>Admin -> Developer</strong> Keys  <br><br>                        |                                                                                                                                                              |
|     5. Click on <strong>Developer Key</strong> and select <strong>+LTI key</strong>.    |                                                                                                                                                              |
|                                                                                         |                                                                                                                                                              |
|     </div>                                                                              |                                                                                                                                                              |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| .. raw:: html                                                                           |                                                                                                                                                              |
|                                                                                         |                                                                                                                                                              |
|     <div class="small">                                                                 |                                                                                                                                                              |
|                                                                                         |    |image3|                                                                                                                                                  |
|     6. Complete the <strong>Key Name, Title</strong> and <strong>Description</strong>   |                                                                                                                                                              |
|         fields. Make sure to set the <strong>method</strong> to <strong>Manual Entry    |                                                                                                                                                              |
|          </strong> <br><br>                                                             |                                                                                                                                                              |
|     7. From Codio, under <strong>LTI 1.3 Integration, copy the LTI URL</strong>         |                                                                                                                                                              |
|         and paste it into the <strong>Target Link URI field</strong> in Canvas.<br><br> |                                                                                                                                                              |
|     8. From Codio copy the <strong>Initiate Login URL</strong> and paste it into the    |                                                                                                                                                              |
|        <strong>OpenID Connect Initiation URL</strong>.<br><br>                          |                                                                                                                                                              |
|     9. Copy the <strong>Redirect URL</strong> and paste it into the                     |                                                                                                                                                              |
|      <strong>Canvas Redirect URI</strong> field.                                        |                                                                                                                                                              |
|                                                                                         |                                                                                                                                                              |
|     </div>                                                                              |                                                                                                                                                              |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| .. raw:: html                                                                           |                                                                                                                                                              |
|                                                                                         |                                                                                                                                                              |
|     <div class="small">                                                                 |                                                                                                                                                              |
|                                                                                         |    |image4|                                                                                                                                                  |
|     10. In Canvas, change <strong>JWK Method</strong> to                                |                                                                                                                                                              |
|          <strong>Public JWK URL</strong>. <br><br>                                      |                                                                                                                                                              |
|     11. From Codio, copy the <strong>Keyset URL</strong> and paste it into              |                                                                                                                                                              |
|          the <strong>Public JWK URL</strong> field.                                     |                                                                                                                                                              |
|     </div>                                                                              |                                                                                                                                                              |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| .. raw:: html                                                                           |                                                                                                                                                              |
|                                                                                         |                                                                                                                                                              |
|     <div class="small">                                                                 |                                                                                                                                                              |
|                                                                                         |    |image5|                                                                                                                                                  |
|     12. Expand the <strong>LTI Advantage Services</strong> section and toggle           |                                                                                                                                                              |
|         each field on.<br><br>                                                          |                                                                                                                                                              |
|     13. Expand the <strong>Additional Settings</strong> section<br><br>                 |                                                                                                                                                              |
|                                                                                         |                                                                                                                                                              |
|     14. Type "codio.com" in both the <strong>Domain</strong> and                        |                                                                                                                                                              |
|        <strong>Tool Id</strong> fields.<br><br>                                         |                                                                                                                                                              |
|     15. Select the <strong>Privacy level</strong> as <strong>Public</strong>.           |                                                                                                                                                              |
|                                                                                         |                                                                                                                                                              |
|                                                                                         |                                                                                                                                                              |
|     </div>                                                                              |                                                                                                                                                              |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| .. raw:: html                                                                           |                                                                                                                                                              |
|                                                                                         |                                                                                                                                                              |
|     <div class="small">                                                                 |                                                                                                                                                              |
|                                                                                         |    |image6|                                                                                                                                                  |
|     16. Scroll down to the <strong>Placements</strong> field. You can add a placement   |                                                                                                                                                              |
|          by starting to type the name and then selecting it when it appears.            |                                                                                                                                                              |
|          Placements that should be included (remove any others):                        |                                                                                                                                                              |
|          Link Selection, Editor Button,  Assignment Selection and Course Navigation.    |                                                                                                                                                              |
|     </div>                                                                              |                                                                                                                                                              |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+





+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image7|                                                                                                                                                                                                                                                                                                    | 
|                                                                                                                                                                                                                                                                                                             |
| .. raw:: html                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                             |
|     <div class="small">                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                             |
|     17. Expand each of the following fields, and copy the static links below:<br><br>                                                                                                                                                                                                                       |
|     <strong>Link Selection</strong><br>                                                                                                                                                                                                                                                                     |
|     Select <strong>LtiDeepLinkingRequest</strong><br>                                                                                                                                                                                                                                                       |
|     <span style="color: teal;">Target Link URI:</span>                                                                                                                                                                                                                                                      |
|     https://apollo.codio.com/lti/resource_selection                                                                                                                                                                                                                                                         |
|     <button onclick="copyRSTUrl1()">Copy URL</button><br>                                                                                                                                                                                                                                                   |
|     <script> function copyRSTUrl1() {                                                                                                                                                                                                                                                                       |
|     const url = "https://apollo.codio.com/lti/resource_selection";                                                                                                                                                                                                                                          |
|     navigator.clipboard.writeText(url).then(() => {                                                                                                                                                                                                                                                         |
|      alert('URL copied to clipboard!'); }).catch(err => {                                                                                                                                                                                                                                                   |  
|      console.error('Failed to copy: ', err); }); } </script>                                                                                                                                                                                                                                                |
|     <span style="color: teal;">Icon Url:</span><br>                                                                                                                                                                                                                                                         |
|     https://static-assets.codio.com/dashboard/images/icons/favicon-16x16.da14ae918fd9bc3b.png                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                             |
|     <button onclick="copyRSTUrl2()">Copy URL</button><br>                                                                                                                                                                                                                                                   |
|     <script> function copyRSTUrl2() {                                                                                                                                                                                                                                                                       |
|     const url = "https://static-assets.codio.com/dashboard/images/icons/favicon-16x16.da14ae918fd9bc3b.png";                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                             |
|     navigator.clipboard.writeText(url).then(() => {                                                                                                                                                                                                                                                         |
|      alert('URL copied to clipboard!'); }).catch(err => {                                                                                                                                                                                                                                                   |  
|      console.error('Failed to copy: ', err); }); } </script>                                                                                                                                                                                                                                                |
|     </div>                                                                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image8|                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                             |
| .. raw:: html                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                             |
|     <div class="small">                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                             |
|     <strong>Editor button</strong><br>                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                             |
|     <span style="color: teal;">Target Link URI:</span>                                                                                                                                                                                                                                                      |
|     https://apollo.codio.com/lti/editor_button                                                                                                                                                                                                                                                              |
|     <button onclick="copyRSTUrl3()">Copy URL</button><br>                                                                                                                                                                                                                                                   |
|     <script> function copyRSTUrl3() {                                                                                                                                                                                                                                                                       |
|     const url = "https://apollo.codio.com/lti/editor_button";                                                                                                                                                                                                                                               |
|     navigator.clipboard.writeText(url).then(() => {                                                                                                                                                                                                                                                         |
|     alert('URL copied to clipboard!'); }).catch(err => {                                                                                                                                                                                                                                                    |  
|     console.error('Failed to copy: ', err); }); } </script>                                                                                                                                                                                                                                                 |
|     <span style="color: teal;">Icon Url:</span><br>                                                                                                                                                                                                                                                         |
|     https://static-assets.codio.com/dashboard/images/icons/favicon-16x16.da14ae918fd9bc3b.png                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                             |
|     <button onclick="copyRSTUrl4()">Copy URL</button><br>                                                                                                                                                                                                                                                   |
|     <script> function copyRSTUrl4() {                                                                                                                                                                                                                                                                       |
|     const url = "https://static-assets.codio.com/dashboard/images/icons/favicon-16x16.da14ae918fd9bc3b.png";                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                             |
|     navigator.clipboard.writeText(url).then(() => {                                                                                                                                                                                                                                                         |
|      alert('URL copied to clipboard!'); }).catch(err => {                                                                                                                                                                                                                                                   |  
|      console.error('Failed to copy: ', err); }); } </script>                                                                                                                                                                                                                                                |
|     </div>                                                                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image9|                                                                                                                                                                                                                                                                                                    |      
|                                                                                                                                                                                                                                                                                                             |
| .. raw:: html                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                             |
|     <div class="small">                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                             |
|     <strong>Assignment Selection</strong><br>                                                                                                                                                                                                                                                               |
|     Select <strong>LtiDeepLinkingRequest</strong><br>                                                                                                                                                                                                                                                       |
|     <span style="color: teal;">Target Link URI:</span>                                                                                                                                                                                                                                                      |
|     https://apollo.codio.com/lti/resource_selection                                                                                                                                                                                                                                                         |
|     <button onclick="copyRSTUrl5()">Copy URL</button><br>                                                                                                                                                                                                                                                   |
|     <script> function copyRSTUrl5() {                                                                                                                                                                                                                                                                       |
|     const url = "https://apollo.codio.com/lti/resource_selection";                                                                                                                                                                                                                                          |
|     navigator.clipboard.writeText(url).then(() => {                                                                                                                                                                                                                                                         |
|     alert('URL copied to clipboard!'); }).catch(err => {                                                                                                                                                                                                                                                    |  
|     console.error('Failed to copy: ', err); }); } </script>                                                                                                                                                                                                                                                 |
|     <span style="color: teal;">Icon Url:</span><br>                                                                                                                                                                                                                                                         |
|     https://static-assets.codio.com/dashboard/images/icons/favicon-16x16.da14ae918fd9bc3b.png                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                             |
|     <button onclick="copyRSTUrl6()">Copy URL</button><br>                                                                                                                                                                                                                                                   |
|     <script> function copyRSTUrl6() {                                                                                                                                                                                                                                                                       |
|     const url = "https://static-assets.codio.com/dashboard/images/icons/favicon-16x16.da14ae918fd9bc3b.png";                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                             |
|     navigator.clipboard.writeText(url).then(() => {                                                                                                                                                                                                                                                         |
|      alert('URL copied to clipboard!'); }).catch(err => {                                                                                                                                                                                                                                                   |  
|      console.error('Failed to copy: ', err); }); } </script>                                                                                                                                                                                                                                                |
|     </div>                                                                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image10|                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                             |
| .. raw:: html                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                             |
|     <div class="small">                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                             |
|     <strong>Course Navigation</strong><br>                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                             |
|     <span style="color: teal;">Target Link URI:</span>                                                                                                                                                                                                                                                      |
|     https://apollo.codio.com/lti/course_navigation                                                                                                                                                                                                                                                          |
|     <button onclick="copyRSTUrl7()">Copy URL</button><br>                                                                                                                                                                                                                                                   |
|     <script> function copyRSTUrl7() {                                                                                                                                                                                                                                                                       |
|     const url = "https://apollo.codio.com/lti/course_navigation";                                                                                                                                                                                                                                           |
|     navigator.clipboard.writeText(url).then(() => {                                                                                                                                                                                                                                                         |
|     alert('URL copied to clipboard!'); }).catch(err => {                                                                                                                                                                                                                                                    |  
|     console.error('Failed to copy: ', err); }); } </script>                                                                                                                                                                                                                                                 |
|     <span style="color: teal;">Icon Url:</span><br>                                                                                                                                                                                                                                                         |
|     https://static-assets.codio.com/dashboard/images/icons/favicon-16x16.da14ae918fd9bc3b.png                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                             |
|     <button onclick="copyRSTUrl8()">Copy URL</button><br>                                                                                                                                                                                                                                                   |
|     <script> function copyRSTUrl8() {                                                                                                                                                                                                                                                                       |
|     const url = "https://static-assets.codio.com/dashboard/images/icons/favicon-16x16.da14ae918fd9bc3b.png";                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                             |
|     navigator.clipboard.writeText(url).then(() => {                                                                                                                                                                                                                                                         |
|      alert('URL copied to clipboard!'); }).catch(err => {                                                                                                                                                                                                                                                   |  
|      console.error('Failed to copy: ', err); }); } </script>                                                                                                                                                                                                                                                |
|     </div>                                                                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| .. raw:: html                                                                             |                                                                                                                                                              |
|                                                                                           |                                                                                                                                                              |
|     <div class="small">                                                                   |                                                                                                                                                              |
|                                                                                           |    |image11|                                                                                                                                                 |
|     18. Press <strong>Save</strong> in bottom right corner<br><br>                        |                                                                                                                                                              |
|     19. You will be back at the list of developer keys.<br><br>                           |                                                                                                                                                              |
|     20. Update <strong>State</strong> to: on<br><br>                                      |                                                                                                                                                              |
|     21. Copy the number in the <strong>Details<strong> column (for use in Parts 2 and 3)  |                                                                                                                                                              |
|     </div>                                                                                |                                                                                                                                                              |
+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. |image1| image:: /instructors/admin/integration/CodioLTI1.3Integration.png
   :width: 1500px  
.. |image2| image:: /img/lti/canvasdeveloperkey.png
   :width: 1500px
.. |image3| image:: /img/lti/developerkeyvalues.png
   :width: 1500px
.. |image4| image:: /img/lti/canvasJWK.png
   :width: 1500px
.. |image5| image:: /img/lti/canvasadvantage.png
   :width: 1500px
.. |image6| image:: /img/lti/canvasplacements.png
   :width: 1500px
.. |image7| image:: /img/lti/canvaslinkselect.png
   :width: 1500px
.. |image8| image:: /img/lti/canvaseditorbutton.png
   :width: 1500px
.. |image9| image:: /img/lti/canvasassignment.png
   :width: 1500px
.. |image10| image:: /img/lti/canvasnavigation.png
   :width: 1500px
.. |image11| image:: /img/lti/canvasdetails.png
   :width: 1500px




Part 2: Create an application in your course in Canvas
------------------------------------------------------

In Canvas:
~~~~~~~~~~

+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| .. raw:: html                                                                             |                                                                                    |
|                                                                                           | .. image:: /img/lti/addlti13app.png                                                |
|     <div class="small">                                                                   |                                                                                    |
|     1. Select an existing course or create a new course.<br>                              |                                                                                    |
|      <strong>Optional</strong>: create a test course called Codio Test Course before      |                                                                                    |
|        you do it with a production course.<br><br>                                        |                                                                                    |
|      2. In your course, go to <strong>Settings → Apps → + App</strong><br><br>            |                                                                                    |
|      3. In Configuration Type, select: <strong>By Client ID</strong><br><br>              |                                                                                    |
|      4. Paste number you copied in Part 1 into <strong>Client ID</strong> field<br><br>   |                                                                                    |
|      5. <strong>Submit → Install</strong><br><br>                                         |                                                                                    |
|        </div>                                                                             |                                                                                    |
+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| .. raw:: html                                                                             |                                                                                    |
|                                                                                           | .. image:: /img/lti/canvasdeployment.png                                           |
|     <div class="small">                                                                   |                                                                                    |
|     6. After you click install, click the gear icon by the tool you just created<br><br>  |                                                                                    |
|     7. Select <strong>Deployment ID</strong><br><br>                                      |                                                                                    |
|                                                                                           |                                                                                    |
|      8. Copy the ID displayed, it will be used in Part 3                                  |                                                                                    |                                                                                                                           
|        </div>                                                                             |                                                                                    |
+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+



Part 3: Create an LTI configuration in Codio
--------------------------------------------

In Codio:
~~~~~~~~~

+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| .. raw:: html                                                                             |                                                                                    |
|                                                                                           |                                                                                    |
|     <div class="small">                                                                   |                                                                                    |
|     1. In your org → <strong>LTI Integrations</strong><br>                                |     .. image:: /img/lti/addlti13integration.png                                    |
|            - Scroll down to <strong>LTI 1.3 Configurations</strong><br>                   |                                                                                    |
|            - Click <strong>Add Integration</strong><br><br>                               |                                                                                    |                                                                                                                         
|        </div>                                                                             |                                                                                    |
+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| .. raw:: html                                                                             |                                                                                    |
|                                                                                           |                                                                                    |
|     <div class="small">                                                                   |                                                                                    |
|     Updating the fields in Platform Information<br><br>                                   |                                                                                    |
|     <strong>Note: replace [CANVAS DOMAIN] with your institution’s                         |                                                                                    |
|       domain in steps 5-7. Make sure to remove the brackets. Example:                     |                                                                                    |
|       https://Codio.instructure.com/api/lti/security/jwks      </strong><br><br>          |    .. image:: /img/lti/canvasplatform25.png                                        |    
|     2. <span style="color: teal;">Platform ID:</span>                                     |                                                                                    |
|         https://canvas.instructure.com                                                    |                                                                                    |
|                                                                                           |                                                                                    |
|       <button onclick="copyRSTUrl9()">Copy URL</button><br>                               |                                                                                    |
|       <script> function copyRSTUrl9() {                                                   |                                                                                    |
|       const url = "https://canvas.instructure.com";                                       |                                                                                    |
|       navigator.clipboard.writeText(url).then(() => {                                     |                                                                                    |
|       alert('URL copied to clipboard!'); }).catch(err => {                                |                                                                                    |
|        console.error('Failed to copy: ', err); }); } </script><br><br>                    |                                                                                    |
|                                                                                           |                                                                                    |
|      3. <strong>Client ID:</strong> copied from Developer Keys at end of Part 1<br><br>   |                                                                                    |
|      4. <strong>Deployment Id:</strong> copied in Part 2<br><br>                          |                                                                                    |
|                                                                                           |                                                                                    |
|      5. <span style="color: teal;">Public Keyset URL:</span>                              |                                                                                    |
|         https://[CANVAS DOMAIN]/api/lti/security/jwks                                     |                                                                                    |
|                                                                                           |                                                                                    |
|         <button onclick="copyRSTUrl10()">Copy URL</button><br>                            |                                                                                    |
|         <script> function copyRSTUrl10() {                                                |                                                                                    |
|         const url = "https://[CANVAS DOMAIN]/api/lti/security/jwks";                      |                                                                                    |
|         navigator.clipboard.writeText(url).then(() => {                                   |                                                                                    |
|        alert('URL copied to clipboard!'); }).catch(err => {                               |                                                                                    |
|        console.error('Failed to copy: ', err); }); } </script><br><br>                    |                                                                                    |
|                                                                                           |                                                                                    |
|      6. <span style="color: teal;">Access Token URL:</span>                               |                                                                                    |
|         https://[CANVAS DOMAIN]/login/oauth2/token                                        |                                                                                    |
|                                                                                           |                                                                                    |
|         <button onclick="copyRSTUrl11()">Copy URL</button><br>                            |                                                                                    |
|         <script> function copyRSTUrl11() {                                                |                                                                                    |
|         const url = "https://[CANVAS DOMAIN]/login/oauth2/token";                         |                                                                                    |
|         navigator.clipboard.writeText(url).then(() => {                                   |                                                                                    |
|        alert('URL copied to clipboard!'); }).catch(err => {                               |                                                                                    |
|        console.error('Failed to copy: ', err); }); } </script><br><br>                    |                                                                                    |
|                                                                                           |                                                                                    |
|      7. <span style="color: teal;">Authentication Request URL:</span>                     |                                                                                    |
|         https://[CANVAS DOMAIN]/api/lti/authorize_redirect                                |                                                                                    |
|                                                                                           |                                                                                    |
|         <button onclick="copyRSTUrl12()">Copy URL</button><br>                            |                                                                                    |
|         <script> function copyRSTUrl12() {                                                |                                                                                    |
|         const url = "https://[CANVAS DOMAIN]/api/lti/authorize_redirect";                 |                                                                                    |
|         navigator.clipboard.writeText(url).then(() => {                                   |                                                                                    |
|        alert('URL copied to clipboard!'); }).catch(err => {                               |                                                                                    |
|        console.error('Failed to copy: ', err); }); } </script><br><br>                    |                                                                                    |
|                                                                                           |                                                                                    |
|      8. Click <strong>Create</strong>                                                     |                                                                                    |                                                                                                                              
|                                                                                           |                                                                                    |                                                                                                                                                                  
|        </div>                                                                             |                                                                                    |
+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+


Part 4: Adding a resource
-------------------------
In Canvas:
~~~~~~~~~~
+-------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| .. raw:: html                                                                                   |      .. image:: /img/lti/createassignment.png                                                                                                        |
|                                                                                                 |                                                                                                                                                      |
|     <div class="small">                                                                         |                                                                                                                                                      |
|      1. Go to Assignments in your course, select <strong>Assignment</strong><br><br>.           |                                                                                                                                                      |
|      2. Give your assignment a name.<br><br>                                                    |                                                                                                                                                      |
|      3. Select a number of points.<br><br>                                                      |                                                                                                                                                      |
|      4. Under <strong>Submission Type</strong>, select <strong>External Tool</strong>.<br><br>  |                                                                                                                                                      |
|      5. Select Find.<br><br>                                                                    |                                                                                                                                                      |
|                                                                                                 |                                                                                                                                                      |
|  <strong>Note: Do not use LTI Integration URL to assign an assignment</strong><br><br>          |                                                                                                                                                      |
|                                                                                                 |                                                                                                                                                      |
|     6. Select the tool created in Part 1.<br>                                                   |                                                                                                                                                      |
|         - Choose the Course and Assignment to connect to<br>                                    |                                                                                                                                                      |
|         - Recommended: Select Load in a new tab<br><br>                                         |                                                                                                                                                      |
|      7. Select <strong>Save</strong> at bottom of the page                                      |                                                                                                                                                      |
|       </div>                                                                                    |                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

Note: these settings are not final and can be edited in Canvas at a later time.


Part 5: Customizing Iframe Width/Height
---------------------------------------

You can customize the width and height of the Codio window embedded in the Canvas. The default width is 1000 pixels and height is 800 pixels, change those values if you need and press **Save Changes**.

  .. image:: /img/lti/iframe-width-height.png
     :alt: Iframe Width and Height settings


Important Notes on Course Copy in Canvas:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- In Canvas, once you copy the course, you must enter a unique SIS ID in Course Settings.
    - An SIS ID that is different from the Blueprint Course (Canvas’ Parent Course) is required for Codio to spawn a corresponding child course.
    - An SIS ID is optional for the Blueprint Course.






Connecting/mapping assignments in Canvas
------------------------------------------

There are also a number of ways you can connect/map assignments. Check out the following videos to see the option that best suits you.

How to connect assignment by lti integration url of assignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/bzowzoyfz1.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_bzowzoyfz1 seo=false videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/bzowzoyfz1/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

How to connect assignment by resource selection preview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/ksdwvd0z3i.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_ksdwvd0z3i seo=false videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/ksdwvd0z3i/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

How to connect assignment by endpoint url
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/fvyglizd2l.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_fvyglizd2l seo=false videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/fvyglizd2l/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

How to connect assignment with custom param
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/4hacq8dpos.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_4hacq8dpos seo=false videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/4hacq8dpos/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>


