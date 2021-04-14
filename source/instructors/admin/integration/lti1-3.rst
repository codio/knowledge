.. meta::
   :description: Working with LTI 1.3 systems

.. _lti1-3:

LTI version 1.3
===============

LTI version 1.3 improves upon version [LTI-1.1] by moving away from the use of OAuth 1.0a-style signing for authentication and towards a new security model, using OpenID Connect, signed JWTs, and OAuth2.0 workflows for authentication. As we have implemented the majority of these improvements already in Codio, it can be better to work with
Codio, LT1 1.1 integration especially considering the ease to set up using the:ref:`Codio LTI App <lti-app>`.

For more information, see `Learning Tools Interoperability Core Specification <https://www.imsglobal.org/spec/lti/v1p3/>`__

Canvas
------

There are a number of ways to integrate Codio with Canvas with LTI 1.3. Check out the following videos to see the option that best suits you.

How to configure lti1.3 tool in Canvas manually - part 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/vEW03zJGTNA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

How to configure lti1.3 tool in Canvas manually -part 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/1d-aumU5sxo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Tool configuration data for canvas lms in canvas.cod.io:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These paramaters cannot be found in canvas.cod.io (found by search only)

-  **platformid**: https://canvas.instructure.com
-  **PUBLIC KEYSET URL**: https://canvas.cod.io/api/lti/security/jwks
-  **ACCESS TOKEN URL**: https://canvas.cod.io/login/oauth2/token
-  **AUTHENTICATION REQUEST URL**:  https://canvas.cod.io/api/lti/authorize_redirect

clientId and deploymentId can be found in tool settings in canvas.cod.io after configuration is completed

How to configure lti1.3 tool in Canvas by paste json object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/Ff0WUjp5Yuo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

How to configure lti1.3 tool in Canvas by paste json url
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/UAZRyE8FUYI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Connecting/mapping assignments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are also a number of ways you can connect/map assignments. Check out the following videos to see the option that best suits you.

How to connect assignment and unit by lti integration url of assignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/BzdqCvFEz5s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

How to connect assignment and assignment by resource selection preview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/aR8kh3Jwjrg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

How to connect assignment and assignment by endpoint url
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/9dgDwsjnY9k" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

How to connect assignment and assignment with custom param
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/VkLYOY19Eu0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

If you require any assistance, please don't hesitate to :ref:`contact us <codio-support>`

Moodle
------

How to configure lti1.3 tool in Moodle manually
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/ZszXM6Ppsgs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Connecting/mapping assignments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a number of ways you can connect/map assignments. Check out the following videos to see the option that best suits you.

How to connect assignment and assignment by lti integration url of assignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/BV1zsXxaUpU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

How to connect assignment and assignment by resource selection preview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/rDFpErXo_-w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

How to connect assignment and assignment by endpoint url
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/AlR18uqU4Pk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

How to connect assignment and assignment with custom param
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/Oy7VjuFXlls" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

If you require any assistance, please don't hesitate to :ref:`contact us <codio-support>`