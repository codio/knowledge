.. meta::
   :description: You can enable LLM's to use your own LLM Provider API keys in Codio
   
.. _org_llm:

Large Language Model
====================

You can add your own LLM API keys to your Codio organization to use in your :ref:`Course <course_llm>` from the **Organization > LLMs** page in Codio.

    .. image:: /img/llm_org_keys.png
       :alt: LLMs Keys
       
We support the following providers:


- `OpenAI <https://openai.com/api/>`_

- `Anthropic <https://console.anthropic.com/>`_

- `Azure OpenAI <https://azure.microsoft.com/en-us/products/ai-services/openai-service>`_

- `vLLM <https://docs.vllm.ai/en/stable/>`_

- `Deepinfra <https://deepinfra.com/docs/advanced/langchain>`_

.. _custom_llm_provider:

Custom LLM Providers
====================

You can add a custom LLM provider in Codio by entering API keys on the **Organization** > **LLMs** page. This allows you to use your chosen LLM provider in your courses.

.. image:: /img/custom_llm_provider.png
       :alt: Custom LLM Providers

Steps to Add a Custom LLM Provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Click **Add provider** and enter the following details:

- **Name:** A recognizable name for the provider.
- **Provider:** The name of the LLM service.
- **Endpoint:** The API endpoint URL for the provider.
- **API Key:** The authentication key needed to access the provider.
- **Authentication:** Select the authentication type (e.g., Header or Query Param).
- **Auth Template:** Specify the authorization format.
- **Endpoint Environment Variable:** Define an environment variable for the API endpoint.
- **API Key Environment Variable:** Define an environment variable for the API key.

2. Click **Create** to save and activate the provider.


Enabling LLM for Courses
------------------------

When keys are added, you can enable use of the key in a course. See :ref:`Course LLMs <course_llm>`.


To enable Codio LLM keys for your organization, please contact help@codio.com to initiate the process. Specify whether you require OpenAI or Anthropic keys.

.. Note:: These keys are currently free but may be subject to charges in the future.



LLM Organization Usage
----------------------

    .. image:: /img/llm_org_usage.png
       :alt: LLMs Usage


.. Note::  The names showing in this screenshot are example names.

Usage will be shown for:


- Daily, weekly, monthly and annual usage
- Daily and monthly top 10 consumers by course
- Each course total usage

.. Note:: The values shown are estimates and may not reflect the exact numbers.
