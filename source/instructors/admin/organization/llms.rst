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

Examples of how to use a custom LLM provider
--------------------------------------------
**OpenAI:**

- name: your openai custom name (custom value)
- provider: openai (custom value)
- endpoint: https://api.openai.com
- api key: your api key from openai
- authentication: Header
- auth template: Authorization: Bearer {{apikey}}
- endpoint environment variable: OPENAI_CUSTOM_KEY (custom value)
- api key environment variable: OPENAI_CUSTOM_KEY (custom value)

After saving the parameters in the organization and enabling the provider in the course, run the script below in the assignment.

.. code-block:: bash

   #!/bin/bash

   SUB_PATH=/v1/chat/completions
   LLM_URL=$OPENAI_CUSTOM_URL$SUB_PATH

   curl -X POST $LLM_URL -H "Authorization: Bearer $OPENAI_CUSTOM_KEY" -H "Content-Type: application/json" -d '{"model": "gpt-3.5-turbo", "messages": [{"role": "system", "content": "your question here" }]}'


**Gemini:**

- name: your gemini custom name (custom value)
- provider: gemini (custom value)
- endpoint: https://generativelanguage.googleapis.com
- api key: your api key from gemini
- authentication: Query param
- auth template: key={{apikey}}
- endpoint environment variable: GEMINI_CUSTOM_URL (custom value)
- api key environment variable: GEMINI_CUSTOM_KEY (custom value)

The script:

.. code-block:: bash

   #!/bin/bash

   SUB_PATH=/v1beta/models/gemini-2.0-flash:generateContent
   LLM_URL=$GEMINI_CUSTOM_URL$SUB_PATH?key=$GEMINI_CUSTOM_KEY

   curl -X POST $LLM_URL  -H "Content-Type: application/json" -d '{"contents": [{"parts":[{"text": "your question here"}]}]}'

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
