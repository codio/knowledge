.. meta::
   :description: Sandboxes allow instructors to set safe AWS environments.

.. _sandboxes:

Sandboxes
=========

About Sandboxes
---------------

Sandboxes provide time-boxed, ephemeral **AWS Management Console environments** that expire automatically. A sandbox's permissions are defined by a template and can range from full administrator access to least-privileged roles, depending on need. When a sandbox's duration ends, access is revoked and all resources created inside the sandbox are cleaned up automatically—no user action required.

.. important::

   **Sandboxes are not enabled by default.** They require a signed agreement because they incur additional costs for your organization. To enable Sandboxes for your organization, please reach out to Support.

.. note::

   **AWS region:** Sandboxes currently run in ``us-east-1`` only. Additional regions can be added if needed.

Key Concepts
------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Concept
     - Description
   * - **Sandbox**
     - A short-lived AWS environment defined by a ``sandbox.yml`` template. It grants time-boxed access and (optionally) provisions resources for hands-on work.
   * - **Type**
     - The sandbox runtime. Two types are illustrated in the examples below:

       - ``aws_cloud`` — console-first sessions that assume an AWS role defined by a policy (optionally orchestrated by an Infrastructure-as-Code engine).

       - ``aws_ec2`` — a session that provisions an EC2 instance with parameters like instance type, image, disk size, and connection mode (``ssh`` or ``vnc``).
   * - **Lifetime**
     - The initial duration of the sandbox (e.g., ``15m``, ``30m``). Access and resources automatically expire at the end of the lifetime.
   * - **Lifetime Extension**
     - Optional, on-demand increments (e.g., ``5m``, ``10m``) that can be applied to a running sandbox, up to ``lifetime_max``.
   * - **Policy**
     - The permissions definition attached to the sandbox (for example, an IAM policy file like ``lab.policy``). This controls the permission level from full to least-privileged.
   * - **Provision Engine**
     - The engine used to orchestrate resources defined by the sandbox (e.g., ``terraform``, ``bash``, or CloudFormation).
   * - **Billing Limit**
     - A numeric cap used by the platform to help control costs attributed to the sandbox (e.g., ``5.0``).
   * - **Parameters**
     - Resource-specific inputs for the sandbox type (for example, EC2 instance settings: ``instance_type``, ``image``, ``volume_size``, ``connection_mode``).
   * - **Region**
     - The AWS region in which sandboxes are created. Currently fixed to ``us-east-1``.
   * - **Prime**
     - Optional pre-warming configuration for sandboxes. When enabled, the platform creates "primed" sandboxes ahead of time to reduce wait time for learners.

Lifecycle, Duration, and Cleanup
--------------------------------

- **Start:** Launch a sandbox from a ``sandbox.yml`` template. The environment and its access are created for the configured ``lifetime``.
- **Extend:** While running, you may extend the lifetime in ``lifetime_extension`` increments, **not exceeding** ``lifetime_max``.
- **Expire & Clean:** When the lifetime ends, access is revoked and resources created by the sandbox are cleaned up automatically—no user action required.

Creating a Sandbox and a Collection
-----------------------------------

1. Select **Sandboxes** from the Build menu, if that option is not available, Sandboxes are not enabled for your organization.

.. image:: /img/sandbox_build.png
    :width: 90%
    :align: center
    :alt: Select Sandboxes on the top menu.

2. Then click the **New Collection** button in the top right. Give your collection a name and click `Create Collection`. 

.. image:: /img/sandbox_newcollection.png
    :width: 70%
    :align: center
    :alt: New Collection screenshot.

3. Once created, your new collection will open automatically. Click `Edit` to start creating sandboxes. The section below explains how to get started quickly. 

.. image:: /img/sandbox_overview.png
    :width: 90%
    :align: center
    :alt: View of Sandboxes Overview.

Sandbox Configuration (``sandbox.yml``)
---------------------------------------

Define sandboxes in YAML, one sandbox per folder. The best starting point is using this command to get four **working examples** you can adapt:

.. code-block:: bash

    git clone https://github.com/codio-content/sandboxes_examples.git .

.. important::

    The command above will copy the repository to your current directory. Make sure your folder is empty.

Configuration Reference
-----------------------

Top-level keys
~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 15 10 55
   :header-rows: 1

   * - Key
     - Type
     - Required
     - Description
   * - ``version``
     - string
     - Yes
     - Schema version of the sandbox definition (e.g., ``"1.0"`` or ``1.0``).
   * - ``type``
     - enum
     - Yes
     - Sandbox runtime type. Supported in examples: ``aws_cloud`` or ``aws_ec2``.
   * - ``settings``
     - mapping
     - Yes
     - Configuration block that defines lifetime behavior, permissions, provisioning engine, and resource parameters.
   * - ``prime``
     - mapping
     - No
     - Optional pre-warming configuration for **any** sandbox type. Supports priming continuously or on scheduled UTC start dates.

``settings`` (common)
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 22 14 10 54
   :header-rows: 1

   * - Key
     - Type
     - Required
     - Description
   * - ``lifetime``
     - string
     - Yes
     - Initial duration of the sandbox (e.g., ``"15m"``, ``"30m"``). Sandboxes are **ephemeral** and expire after this time.
   * - ``lifetime_extension``
     - string
     - No
     - Increment applied when extending a running sandbox (e.g., ``"5m"``, ``"10m"``). Extensions cannot push the total beyond ``lifetime_max``.
   * - ``lifetime_max``
     - string
     - No
     - Maximum total runtime allowed for the sandbox (e.g., ``"20m"``, ``"60m"``). Once reached, the sandbox cannot be extended further.
   * - ``policy``
     - string
     - Conditional
     - Path or reference to the IAM policy that defines the sandbox's permissions. Controls access level from full to **least-privileged**.
   * - ``provision_engine``
     - string
     - Conditional
     - Infrastructure-as-Code engine used to orchestrate resources (e.g., ``terraform``). Include when the sandbox provisions resources.
   * - ``billing_limit``
     - number
     - Optional
     - Organizational cost control value associated with the sandbox.
   * - ``parameters``
     - mapping
     - Conditional
     - Type-specific inputs. Required for ``aws_ec2`` (see below).

.. _ec2type-sandboxes:

``settings.parameters`` for ``aws_ec2``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After setting ``type`` to ``aws_ec2``, configure the following ``parameters``:

.. list-table::
   :widths: 22 14 10 54
   :header-rows: 1

   * - Key
     - Type
     - Required
     - Description
   * - ``instance_type``
     - string
     - Yes
     - EC2 instance type to provision (e.g., ``t3.medium``). Supported instance types include:

       - ``t3.nano`` ``t3.micro`` ``t3.small`` ``t3.medium`` ``t3.large`` ``t3.xlarge`` ``t3.2xlarge``
       - ``t3a.nano`` ``t3a.micro`` ``t3a.small`` ``t3a.medium`` ``t3a.large`` ``t3a.xlarge`` ``t3a.2xlarge``
       - ``c5a.large`` ``c5a.xlarge`` ``c5a.2xlarge`` ``c5a.4xlarge`` ``c5a.8xlarge`` ``c5a.12xlarge`` ``c5a.16xlarge`` ``c5a.24xlarge``
       - ``c6a.large`` ``c6a.xlarge`` ``c6a.2xlarge`` ``c6a.4xlarge`` ``c6a.8xlarge`` ``c6a.12xlarge`` ``c6a.16xlarge`` ``c6a.24xlarge``
       - ``g4dn.xlarge`` ``g4dn.2xlarge`` ``g4dn.4xlarge`` ``g4dn.8xlarge`` ``g4dn.16xlarge``
   * - ``image``
     - string
     - Yes
     - AMI name or ID for the VM image. Examples:

       - Ubuntu: ``codio-aws-ubuntu-base`` (or Ubuntu Codio AMI)
       - Windows: ``codio-aws-windows-base`` (or Windows Codio AMI)
   * - ``volume_size``
     - integer (GB)
     - Yes
     - Root volume size in GiB for the instance (e.g., ``30``).
   * - ``connection_mode``
     - enum
     - Optional
     - Default access channel for the instance. Supported values in examples: ``ssh`` or ``vnc``.
       If omitted, both connection modes are available.

``prime`` (common)
~~~~~~~~~~~~~~~~~~

Optionally prime (pre-warm) sandboxes to reduce learner wait time. Priming can be:

- **Continuous:** Maintain a steady pool of primed sandboxes.
- **Date-based:** Prime a specific number of sandboxes at specific UTC start times. 

.. note::

    For **Continuous**, sandboxes will start priming immediately after publishing the Collection. For **Date-based** this date specifies the time sandboxes will start priming, not when they will be ready.

.. list-table::
   :widths: 22 14 10 54
   :header-rows: 1

   * - Key
     - Type
     - Required
     - Description
   * - ``type``
     - enum
     - Yes
     - Priming mode. Supported values: ``continuous`` or ``date``.
   * - ``count``
     - integer
     - Conditional
     - Required when ``prime.type`` is ``continuous``. Number of primed sandboxes to keep available.
   * - ``start_dates``
     - list
     - Conditional
     - Required when ``prime.type`` is ``date``. List of scheduled priming entries (UTC).
   * - ``start_dates[].date``
     - string (datetime, UTC)
     - Conditional
     - Required within each ``start_dates`` entry. Date/time (UTC) when priming should occur (e.g., ``2025-11-24T11:40:00Z``).
   * - ``start_dates[].count``
     - integer
     - Conditional
     - Required within each ``start_dates`` entry. Number of primed sandboxes to create at the scheduled date/time.

Permissions (Full to Least-Privileged)
--------------------------------------

Sandbox **permissions are chosen by you** via the attached ``policy``:

- To grant **broad administrative capabilities**, point ``policy`` to an IAM policy that allows those actions.
- To enforce **least-privileged** access, supply a narrowly scoped policy granting only the minimum actions required.

This design lets you run anything from **full AWS** environments to tightly constrained labs, all with the same sandbox mechanism.

.. admonition:: How can I create a policy?

   Policies are an AWS concept. If you want to read more, please visit AWS' guide to
   `Policies and permissions`__ and the
   `IAM tutorial: Delegate access across AWS accounts using IAM roles`__.

   __ https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html
   __ https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html
