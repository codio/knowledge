.. meta::
   :description: Cookies, Firewalls, Browser support
   


Web Security and Browser Capabilities
=======================================
On this page you will find instructions on how to configure your **cookies**, **firewalls**, and **browser support**.


.. _cookie-requirements:


Cookie Requirements
-------------------


To ensure Codio works properly, you must enable cookies in your web browser. Below you will find instructions on how to enable cookies for all sites.
If you have any questions about how Codio uses cookies, please check our `Privacy policy <https://www.codio.com/legal-stuff#pii>`_.




Enabling Cookies in Chrome:
****************************


1. Click the three-dot menu in the top right corner.
2. Go to Settings.
3. Click "Privacy and Security" tab in the main menu.
4. Select "Third-party cookies".
5. Choose "Allow third-party cookies".




.. image:: /img/ChromeCookies25.png
  :alt: Chrome Cookies








Enabling Cookies in Firefox:
*****************************


1. Open the menu (three horizontal lines) in the top right.
2. Go to Settings.
3. Select "Privacy & Security".
4. Under "Enhanced Tracking Protection", choose "Standard" or select "Custom" and uncheck "Cookies".
5. Ensure third-party cookies are not blocked.


.. image:: /img/FirefoxCookies25.png
  :alt: Firefox Cookies






.. Note:: Ensure third-party cookies are not blocked by checking the box "Allow Firefox to automatically trust third-party..."


.. image:: /img/FirefoxThirdPartyCookies.png
  :alt: Firefox Cookies






Enabling Cookies in Safari:
****************************




1. Open the menu by clicking Safari in the top left.
2. Click on Settings.
3. Click the "Advanced" tab.
4. Uncheck "Block all cookies".




.. image:: /img/SafariCookies25.png
  :alt: Safari Cookies
 


If using an earlier version of Safari, check **Always Allow** in the Cookies and website data section


Enabling Cookies in Microsoft Edge:
***********************************


1. Open Microsoft Edge on your computer.
2. Click the three dots (...) in the top-right corner to open the menu.
3. Select "Settings".
4. In the left sidebar, click on "Cookies and site permissions".
5. Click "Cookies and site data"
6. Make sure the toggle for "Block third-party cookies" is turned OFF.
7. Ensure "Allow sites to save and read cookie data (recommended)" is turned ON.


.. image:: /img/edgecookeis.png
  :alt: Edge Cookies


.. _firewalls:


Firewall and Network Settings
-----------------------------


Codio is designed to work in most browsers without special configuration. However, if you're accessing it from a K-12 school or university network, certain firewall settings may require additional setup to function properly.


Below you will find more information about:


- Network system administrators
- Students and teachers who may be using Codio from home


Firewall Settings
*****************


The following is a list of ports and URLs that Codio accesses from time to time. We have put these in priority order.


   - `*.codio.com` the main Codio site and application
  
   - `*.codio.io` domains that are auto-generated for each user project


   - `*.codio.co.uk` the main site for Codio services in the UK.


   - `*.codio-box.uk` domains that are auto-generated for user projects in the UK.
  
   - `api.keen.io` statistics gathering to measure student time spent in units   (stats)
  
   - `*.typekit.net` web fonts
  
   - `fonts.gstatic.com` web fonts
  
   - `fast.fonts.net` web fonts
  
   - `*.cloudfront.net` our CDN for speeding up static content
  
   - `*.youtube.com` & `*.vimeo.com` for videos included in Course content
  
   - `gravatar.com` used for user gravatars (pictures)


   - `*.intercom.io`, `cdnjs.cloudflare.com` and `*.pubnub.com` are highly recommended as they relate to  the help and support application (Intercom) built into Codio.


If your institution blocks access to YouTube as a general rule, your IT department can whitelist YouTube access that only allows access to content from registered and accredited educational content repositories. See `here <https://support.google.com/youtube/answer/2695317?hl=en-GB>`_ for more information on this.




Ports
*****


We recommend opening the following ports


- **80 and 443** for standard communications


Working from home
*****************


Your anti-virus software or firewall settings on personal devices might occasionally interfere with Codio, potentially causing slower performance during home use. Temporarily adjusting these security settings may improve your experience.
You should check your settings and ensure that items in the above **Firewall Settings** list are added to your exclusion list.


Connectivity Test
*****************


If you continue to experience difficulties, visit the `Connection Diagnostics <https://codio.com/connectivity/index.html>`_ page and send us back the generated output.


Steps for sending us the generated output:


1. Go to your Codio dashboard.
2. Click on **Support Chat** found on the bottom left corner under "Help".
3. Attach the output file using the paperclip icon.
4. Send the message.


.. _browser-support:


Browser support
---------------
While Codio works with most browsers we recommend using the most recent versions of our fully supported browsers below:


- **Chrome**
- **Firefox**
- **Edge**
- **Safari**


**Note(s)**:


- If using **Safari** be aware that it can block preview cookies with their 'Intelligent Tracking Prevention 2.0' and cause assignments not to load.


- If using **Safari** and accessing Codio via an LMS (Canvas/Blackboard/D2L/Moodle etc), disable "Prevent cross-site tracking" to ensure access.


.. image:: /img/SafariTracking.png
  :alt: Safari Settings






If you continue to experience any disruptions in Codio, please send an email to `help@codio.com <https://help@codio.com>`_.


.. _disable-ie-compatibility-view:


Disable Microsoft Edge Compatibility View
******************************************


It's possible that if you have Microsoft Edge, we detect an older version of the browser(For example Internet Explorer).


This is due to the *Compatibility Mode* of the Browser which enables old features we no longer support.


To disable Compatibility View in Microsoft Edge, follow these steps:


1. Open Microsoft Edge.
2. Click on the three dots menu (⋯) in the top-right corner.
3. Select "Settings".
4. In the left sidebar, click on "Default browser".
5. Under "Internet Explorer compatibility," look for the "Allow sites to be reloaded in Internet Explorer mode" option.
6. Click the dropdown menu on the right.
7. Click "Don't allow".




.. image:: /img/MicrosoftCompadability.png
  :alt: Microsoft Edge Settings


**Note: Make sure to reload your browser after editing the setting.**


