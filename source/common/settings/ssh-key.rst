.. meta::
   :description: Access your SSH Key

.. _ssh-key:

SSH Key
=======

An SSH public and private key pair is automatically generated for your account that can then be used when Codio attempts communication with an external server that requires authentication based on a public or private key, such as SSH terminal or SFTP. You access this key from the **SSH Keys** tab.

    .. image:: /img/prefs-account-ssh.png
       :alt: Codio SSH Key


If you wish to regenerate the SSH public and private key in your Codio account, you can do so clicking the Regenerate icon (see arrow above). If you would like to use your own custom key, click the **Replace Key** button. Any external servers that have used the original key will need to be updated to use the newly created key.

To connect to a remote server, you must :ref:`upload your SSH key to the remote server <upload-ssh-key-remote-server>`.