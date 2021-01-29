.. _ssh-key:

SSH Key
=======

An SSH public and private key pair is automatically generated for your account that can then be used when Codio attempts communication with an external server that requires authentication based on a public or private key, such as SSH terminal or SFTP. You access this key from the **SSH Key** tab on the **Settings** page.
[Ian, this screenshot is outdated]

.. image:: /img/prefs-account-ssh.png
   :Alt: Codio SSH Key

Codio uses the public SSH key to connect to:
[Ian, I'm not sure where these topics will reside; need to insert cross-links]

- [SFTP deployment target](/project/ide/tools/deployment/#sftp-target-type)
- [RSYNC deployment target](/project/ide/tools/deployment/#rsync-target-type)
- [SSH Terminal](/project/ide/tools/ssh/)
- [Git](/project/ide/editing/#git-mercurial-svn)

To connect to a remote server, you must :ref:`upload your SSH key to the remote server <upload-ssh-key-remote-server>`.