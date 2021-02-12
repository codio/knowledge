.. _parts-coding:

Add Your Own Software Packages
==============================

If you cannot find the software you want to install in the list, you can add your own package to the **Install Software** list by forking our GitHub repository, making the necessary modifications, submitting a pull request.

The repository can be found at https://github.com/codio/install_software

Software packages are installed by running a script. You can code your own install package using the concepts in this topic.

Scripts
-------
A script is typically, but not necessarily, a bash script that runs a series of commands as you would on the command line to install or configure software on your Codio box. However, it can be any executable code you choose.

The scripts written by Codio typically use Ansible, a very friendly deployment management system that greatly reduces complexity.

package_list.json
^^^^^^^^^^^^^^^^^
The **package_list.json** file is is the manifest that lists the entire contents of the publicly available scripts. Each script has an entry in this file, and you must add a new item to the list when coding your own install package. Whenever you open the **Install Software** page (**Tools > Install Software**), this Install Software manifest is retrieved from our GitHub repo.

Here's a example of the MySQL entry:

.. code:: json

    "mysql": {
      "name": "MySQL",
      "description": "MySQL is an open-source relational database management system (RDBMS)",
      "script": "mysql/install.sh",
      "version": "5.5.49",
      "category": "data_stores"
    }
where:

- ``script`` - is the path, relative to the root of the repo, where the installation script can be found.
- ``category`` - is the category that the component belongs to; you can update the category field field with any of the following categories:

  - data_stores
  - deployment
  - development_tools
  - libraries
  - shells
  - programming_languages
  - utilities
  - web_development

Example :MySQL
..............
The following example shows how to install MySQL from the **Install Software** page in a few seconds. Run the **MySQL** installation on a new box. The MySQL entry in the `package_list.json` file looks like this:

.. code:: json

      "mysql": {
      "name": "MySQL",
      "description": "MySQL is an open-source relational database management system (RDBMS)",
      "script": "mysql/install.sh",
      "version": "5.5.49",
      "category": "data_stores"
    }

You can see the reference to the ``mysql/install.sh`` script.

Bash script
^^^^^^^^^^^
This script calls our standard Ansible loader script, which in turn loads the relevant playbook.

.. code:: bash

    #!/bin/bash

    bash -c "$(curl -fsSL https://raw.github.com/codio/install_software/master/tools/ansible.sh)" mysql

    echo "Mysql password root user password is 'codio'"


Ansible playbook script
^^^^^^^^^^^^^^^^^^^^^^^
Ansible simplifies installations and configurations, as easier to read and maintain than using the main bash script with standard Ubuntu commands. For more information about Ansible playbooks, `click here <http://docs.ansible.com/>`_.

.. code:: json

    ---
    - name: Install MySQL
      hosts: 127.0.0.1
      sudo: True
      vars:
        MySQL_root_pass: codio
      tasks:
        - name: Set MySQL root password before installing
          debconf: name='mysql-server' question='mysql-server/root_password' value='{{MySQL_root_pass | quote}}' vtype='password'
        - name: Set MySQL root again password before installing
          debconf: name='mysql-server' question='mysql-server/root_password_again' value='{{MySQL_root_pass | quote}}' vtype='password'
        - name: Install MySQL
          apt: name={{ item }} state=present
          with_items:
            - mysql-server
            - mysql-client
            - python-mysqldb
        - copy: src=my.cnf dest=/home/codio/.my.cnf


