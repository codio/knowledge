.. meta::
   :description: Guidelines for creating a Starter Pack including configuring menu items, providing a read me file and creating a Stack forthe software configuration.

.. _starter-pack-guidelines:

Starter Pack Guidelines
=======================
The following guidelines may help you When creating a Starter Pack.

Stack
-----
When you create a Starter Pack, you should first create a new project from a stack that meets your requirements. You can also use the Base Stack and then :ref:`install your own components <box_parts>`.

.codio file
-----------
Create a **.codio** file in the root (`/home/codio/workspace` or `~/workspace`) of your project so you can easily run common terminal commands and preview the code. 

To enable your project to preview inside a **Codio** tab, you must configure the preview to run over https. We recommend this as being the default behavior as it will run both inside Codio and in a new browser tab. You should configure any services to run on any port between 9500 and 9000, depending on the server technology being used.

The following **.codio** file is typical:

.. code:: ini

    {
    // Configure your Run and Preview buttons here.

    // Run button configuration
      "commands": {
            "Start Express Server": "npm start"
      },

    // Preview button configuration
      "preview": {
            "Preview": "https://{{domain}}:9500/"
      }
    }


Create a new stack
------------------
If you have installed or configured any components that are not a part of the code workspace, then you may want to create a special Stack that your Starter Pack uses. If you don't do this, then Projects that are created from the Starter Pack will need to have these modifications performed after Project creation. This might be an `npm install` if you are using Node.

Use GitHub
-----------
Although you can use Codio as the source for your Starter Pack, we recommend pushing your Project to a Git remote. This gives better version control over time. The creation process is also somewhat faster.

When you create the Starter Pack, you can specify the Git url.

Long Description
----------------
You should include a full description of your Starter Pack that appears when someone clicks on it within the Starter Packs listing. Check out some of Codio Certified Pack long descriptions.


README.md file
--------------
You should create a **README.md** file in the root (`/home/codio/workspace` or `~/workspace`) of your project that displays helpful information the user can see when they open the project.

Below is a template that can be used:

.. code:: markdown

    # Title
    Put the name of your Pack here containing the primary technology or technologies with a version number, along with a short description.

    ## Using the Pack
    Describe how the user should get started. Point to your `.codio` menu options if you have created any.

    ## How the Pack was prepared
    It can be helpful to others or even to you later on to describe how you built the Pack. What we often do is to include a set of instructions that can be pasted into a Bash script to recreate the Pack with a single command.

    **Example** : This Starter Pack was built on the Node+Grunt+MongoDB Stack. We than ran the following commands before creating the Pack.

    npm install -g express
    npm install -g express-generator
    express .
    npm install

    ## Useful Links

    - [Express site](http://expressjs.com/)
    - [Node](http://nodejs.org/)
    - [npm](https://www.npmjs.org/)
    - [Grunt](http://gruntjs.com/)
    - [MongoDB](https://www.mongodb.org)

