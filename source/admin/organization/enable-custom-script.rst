.. _enable-custom-script:

Enable Custom Script
====================
You can enable custom scripts to integrate third-party systems, such as :ref:`Sense Network <sense-network>` to help and track students from the **Organization > Custom Scripts** page in Codio. The script passes the ``userid``, ``email``, and ``user type`` (Student/Teacher).

If required by the third-party system, custom js code can be included in the **Custom Script** section. This code should be entered without script tags, for example:

```javascript
var http = new XMLHttpRequest();
var url = 'https://userdomain/url'; //Change to valid URL for your third-party system
var params = 'userId=' + codio.userId ;
http.open('POST', url, true);
http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
http.onreadystatechange = function() {//Call a function when the state changes.
    if(http.readyState == 4 && http.status == 200) {
        alert(http.responseText);
    }
}
http.send(params);
```

You can also add ``console.log`` entries to be able to test and view output, for example:

```javascript
console.log('params', codio);
console.log('params', window);
console.log('params', document)
console.log(window.codio.currentPage)
console.log(window.codio.totalNumberOfPages)
```

.. image:: /img/manage_organization/customscript.png
   :alt: Custom Script

If you require any assistance enabling custom scripts, contact Codio.
