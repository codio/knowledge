SSH and code access
===================

Codio box SSH keys
------------------
Codio generates a key-pair that can be used for services like Github, so you can upload your public key to those systems (read [this section](/dashboard/account/#github) for details on how to upload Github and Bitbucket public keys with a single button press).

You can find your Codio public key as [described here](/dashboard/account/#public-key).

When you create a new Codio project, your user keys are automatically copied into your project and can be found in the `~/.ssh` folder. You will need to open up a Terminal window to access this folder and the keys stored in the `id_rsa` file.

.. _ssh into your box: 

SSH into your box
-----------------
Unless your project is utilising :ref:`Always on Boxes <Always on Boxes>` you will need to open your Codio Project in order for the Box to be started and ready to receive incoming SSH connections.

Generating Key Pairs
--------------------
There are several sites that explain generating SSH keys.

- Windows: https://www.techrepublic.com/blog/10-things/how-to-generate-ssh-keys-in-openssh-for-windows-10/
- Mac : https://help.github.com/articles/generating-ssh-keys#platform-mac
- Linux: https://help.github.com/articles/generating-ssh-keys#platform-linux

Find your local machine's SSH public Key
----------------------------------------
This is pretty easy to do. On a Mac or Linux box you can get your public key in one of two ways

- **either** copy your local machine's public key to the clipboard from your local machine's terminal using `pbcopy < ~/.ssh/id_rsa.pub`
- **or** on your local machine, open the file `~/.ssh/id_rsa.pub` and copy it to the clipboard. Be careful with some editors that include control characters that you don't want to be copied across.

On a Windows machine you'll probably be using putty, so grab your key from there.

Uploading your Public Key to your Codio Box
-------------------------------------------
You need to upload the public key you just found in the above steps. Once you have it copied to the clipboard, open a terminal tab in your Codio project and enter this key into the `.ssh/authorized_keys` file. The easiest way to do this is to enter `nano .ssh/authorized_keys` which will open this file in the nano editor and you can paste it in.

You can view/check to see all/any Public key(s) you have uploaded into your project by opening the terminal and running `cat ~/.ssh/authorized_keys`.

Enabling and Connecting to your Box from your local machine's Terminal
----------------------------------------------------------------------

1. Go to **Project>Settings** and to the [Forwarding Settings](/project/ide/settings/#project-settings) tab and click the 'Enable SSH Forwarding' button
1. The connection string you need to use is shown there

You will see connection details like this
`SSH Forwarding: ssh codio@forwarding.codio.com:29119`

You can now connect to your Box from any Terminal window using (in the above example)
`ssh codio@forwarding.codio.com -p 29119`

If you get a message `Permission denied (publickey)` then you have not uploaded your SSH Public Key correctly.

You cannot connect to a Codio Box without using a Public Key.

