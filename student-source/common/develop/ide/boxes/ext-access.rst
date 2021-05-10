.. meta::
   :description: External Access to Boxes and Ports

.. _external access:

External Access to Boxes and Ports
==================================

When a new project is created in Codio, a unique subdomain name is generated:

`word1-word2.codio.io`

where `word1` and `word2` are randomly generated words resulting in a unique domain name.

Recommended method for referencing box on specific port
-------------------------------------------------------
It is strongly recommended that you reference a Codio box running on a specific port using the unique domain name and port number: 

``word1-word2.codio.io``

If your PC is behind a firewall, access to external ports are often restricted. Using the unique domain name and port number allows the request to be made over port 80 so it's not blocked by the firewall. 

Using this approach allows both HTTP and HTTPS access over the full range of ports, `1024` to `9999`.


Standard method for referencing box on specific port
----------------------------------------------------
You can also reference a Codio box using ``word1-word2-<port>.codio.io`` but you should be aware of the following restrictions to avoid wasting valuable time diagnosing why your browser cannot talk to the Codio box:

- Port ranges are restricted to `1024` to `9499` for HTTP access.
- Port ranges are restricted to `9500` to `9999` for HTTPS access.
- If your PC is behind a firewall, access over non-standard ports is blocked and will fail if using ``word1-word2-3000.codio.io`` to reference a Codio box.

Original request header
-----------------------
The `X_FORWARDED_PROTO` header contains original request schema, should you need it.

Preview menu
------------
Codio offers a fully customizable **Preview** menu that allows you to preview both static files (.html) and server files (.php files, Ruby, Node apps, etc.). See :ref:`Preview documentation <preview>` for more information.

Using the **Preview** menu, you can set up any number of 'aliases' both for static files and box CLI commands.
