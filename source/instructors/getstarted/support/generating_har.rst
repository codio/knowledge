.. meta::
   :description: Generating a HAR file for troubleshooting

.. _generating-har:

Generating a HAR file for troubleshooting
=========================================

Codio Team may occasionally need additional information about the network requests that are generated in your browser. A member of the team may ask you to record a HAR file, or a log of network requests, while that issue occurs. It's helpful to include any browser console logs in addition to a HAR file. Similarly, you may also collect Windows log files in addition to HAR files.

.. Note:: A HAR file includes data such as the content of your cookies and the pages you downloaded while making the recording. Anyone with access to the HAR file can view the data submitted while recording, which may include personal data or other sensitive data. Make sure that you secure your HAR files accordingly. Cloudflare has released a `HAR sanitizer <https://blog.cloudflare.com/introducing-har-sanitizer-secure-har-sharing/>`_ that can be used to strip any sensitive information.

Instructions for generating HAR files
-------------------------------------

Read the below instructions to generate a HAR file and console logs in the browser that you use. 

Generate a HAR file in Chrome
*****************************

1. Open Chrome and go to the page where the issue is occurring.
2. Look for the ⋮ button and select **More Tools > Developer Tools**.
3. From the panel that appears, select the **Network** tab. You must keep the menu open while you reproduce the issue. 

    Optional: If Codio Team requests a HAR file with WebSockets, select the WS option in the Network tab. Reload your browser to start seeing the traffic over the WebSocket.

4. Look for a round record button in the upper left corner of the tab, and make sure it is red. If it is grey, click the button once to start recording.
5. If it isn't, check the **Preserve log** box.
6. Click the grey crossed circle button to clear any existing logs from the network tab.
7. Reproduce the issue while the network requests are recorded.
8. Click the download button, **Export HAR**, to download, and save the file to your computer: **Save as HAR with Content**.
9. Send the HAR file to Codio for further investigation, see :ref:`Instructions for sending HAR files <sending-har>`.

To retrieve console logs in Chrome:

1. Open **Main Menu** for Chrome.
2. Navigate to **More Tools > Developer Tools**.
3. Open the **Console tab** and screenshot any errors that appear.


Generate a HAR file in Firefox
******************************

1. Open Firefox and go to the page where the issue is occurring.
2. Open the `Network Monitor <https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/#opening-the-network-monitor>`_.
3. Reproduce the issue while the network requests are recorded.
4. Right-click anywhere under the **File** column and click **Save All As HAR**.
5. Save the HAR file somewhere convenient.
6. Send the HAR file to Codio for further investigation, see :ref:`Instructions for sending HAR files <sending-har>`.

To retrieve console logs in Firefox:

1. In the **Tools** menu, select **Web Developer**.
2. Console logs will appear in a separate window.
3. Screenshot any errors that appear.


Generate a HAR file in Safari
*****************************

1. Open Safari and go to the Develop menu. If you don't see theDevelop menu, follow the instructions in this article from the Safari User Guide: Use the developer tools in the Develop menu in Safari on Mac.
2. Select Show Web Inspector.
3. Click the Network tab. You must keep it open while you reproduce the issue.
4. Reproduce the issue while the network requests are recorded.
5. Click the Export icon and save the HAR file.
6. Send the HAR file to Codio for further investigation, see :ref:`Instructions for sending HAR files <sending-har>`.

To retrieve console logs in Safari:

1. Open **Preferences** and navigate to the **Advanced** tab.
2. Select **Show Developer menu** in the menu bar.
3. Close Preferences.
4. In the menu bar, select **Developer > Show error console**.
5. Screenshot any errors that appear.


To generate a HAR file in Edge
******************************

1. Open Edge and go to the `Network tool <https://learn.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/network/#open-the-network-tool>`_ .
2. Reproduce the issue while the network requests are recorded.
3. Export captured traffic as a HAR file.
4. Send the HAR file to Codio for further investigation, see :ref:`Instructions for sending HAR files <sending-har>`.

To retrieve console logs in Edge:

1. Select the three dots in the upper-right corner of your browser window.
2. Click **More tools > Developer Tools**.
3. In the **DevTools** panel, click the **Console** tab.
4. Right-click the console and select **Clear Console** of any pre-existing logs.
5. Check the **Preserve Log** checkbox.
6. Replicate the issue that you experienced in the Edge browser.
7. Screenshot any errors that appear.


.. _sending-har:

Instructions for sending HAR files
----------------------------------

Before you send a HAR file to Codio Team, you should both rename AND zip or compress your HAR files. Uncompressed HAR files are often over standard attachment limits. Also, by default, HAR files use the page URL as the name of the file. Files with .com extensions look suspicious to spam and phishing filters. Give the HAR file a descriptive name that doesn't include their full URL.