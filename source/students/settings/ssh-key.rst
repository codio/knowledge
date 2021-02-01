.. _ssh-key:

SSH Key
=======

An SSH public and private key pair is automatically generated for your account that can then be used when Codio attempts communication with an external server that requires authentication based on a public or private key, such as SSH terminal or SFTP. You access this key from the **SSH Key** tab on the **Settings** page.
[Ian, this screenshot is outdated] <Diana seems OK to me.. what is it you think needs to be changed>

.. image:: /img/prefs-account-ssh.png
   :alt: Codio SSH Key

Codio uses the public SSH key to connect to:
[Ian, I'm not sure where these topics will reside; need to insert cross-links] <Diana I can’t see in the ‘key use cases’ doc anything for deployment so something for Sharon i’d say. Currently is at https://docs.codio.com/project/ide/tools/deployment/ but I would say this is not something students would use so maybe if added in main docs just a link to 'more info on deploying to external locations and send them to that page rather than need to write all out here>

- [SFTP deployment target](/project/ide/tools/deployment/#sftp-target-type)
- [RSYNC deployment target](/project/ide/tools/deployment/#rsync-target-type)
- [SSH Terminal](/project/ide/tools/ssh/)
- [Git](/project/ide/editing/#git-mercurial-svn)

To connect to a remote server, you must :ref:`upload your SSH key to the remote server <upload-ssh-key-remote-server>`.