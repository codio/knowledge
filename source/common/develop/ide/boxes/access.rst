.. _ssh:

Access Codio Box via SSH
========================

You can SSH into your Codio box from code using SSH public keys. Understanding how Codio uses SSH keys is important to accessing your box via ssh.

**Note:** You cannot connect to a Codio box without using a Public Key.


Codio box SSH keys
------------------
Codio generates a key-pair that can be uploaded to connect to applications such as Github and BitBucket. See :ref:`SSH Keys <ssh-key`> for information on uploading your public key to Github and Bitbucket.

When you create a new Codio project, your user keys are automatically copied into your project and can be found in the **~/.ssh** folder. To access this folder, open a terminal window and navigate to the **id_rsa** file.

SSH into your box
-----------------
Unless your project has the :ref:`Always-on Box <Always on Boxes>` feature enabled, you must open your Codio project to start the box so that it is ready for receiving incoming SSH connections.

To prepare your box for external access, follow these guidelines:

Generate key pairs
^^^^^^^^^^^^^^^^^^
To gain an understanding of how to generate SSH keys, see the following documentation:

- Windows - https://www.techrepublic.com/blog/10-things/how-to-generate-ssh-keys-in-openssh-for-windows-10/
- Mac - https://help.github.com/articles/generating-ssh-keys#platform-mac
- Linux - https://help.github.com/articles/generating-ssh-keys#platform-linux

Find your local machine's SSH public key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To find your local machine's SSH public key, use one of the following methods depending on your operating system:

- Mac or Linux - Copy your local machine's public key to the clipboard from your local machine's terminal using ``pbcopy < ~/.ssh/id_rsa.pub``.
- Mac or Linux - On your local machine, open the **~/.ssh/id_rsa.pub** file and copy it to the clipboard. Be careful not to copy unwanted control characters.
- Windows - Use Putty to obtain your key.

Upload your public key to your Codio box
----------------------------------------
Once you have obtained your local machine's SSH public key, follow these steps to upload it your Codio box: 
1. Copy the public key to your clipboard.
2. Open a terminal tab in your Codio project and enter the key into the **.ssh/authorized_keys** file. The easiest way to do this is to enter ``nano .ssh/authorized_keys`` to open the **.ssh/authorized_keys** file in the nano editor and paste the key into the file.

You can view all uploaded public keys in your project by opening the terminal and running ``cat ~/.ssh/authorized_keys``.

Enable SSH forwarding and connect to your box
---------------------------------------------
You can now enable SSh forwarding in Codio and then connect to you box from you local machine's terminal window:

1. Click the **Project** tab on the menu bar and choose **Settings**.
2. Click the **Forwarding Settings** tab.
3. Click **Enable SSH Forwarding** to display the connection string, similar to:

   ``SSH Forwarding: ssh codio@forwarding.codio.com:29119``

4. Connect to your box from any terminal window using the connection string that is displayed:
   
   ``ssh codio@forwarding.codio.com -p 29119``

If you get a message `Permission denied (publickey)`, you have incorrectly entered your SSH public key.


