.. meta::
   :description: Parameterized assessments
   
.. _parameterized:

Parameterized assessments
=========================
For all assessment types except Gradebook and Random, you can generate parameters by writing **python** code on the **PARAMETERS** tab.

   .. image:: /img/guides/parameterized2.png
      :alt: Parameterized Assessment

Parameters tab
**************
The **PARAMETERS** tab has a large built-in code editor to enter **python** code that generates parameters.

   .. image:: /img/guides/ParametersTab.png
      :alt: Parameters Tab UI

On the right-hand side, the **Add Code Example** button will generate 3 lines of code which (1) import the python ``random`` library, (2) declare the ``codio_parameters`` dictionary you will store parameters and their values in, and (3) provide a sample parameter.

The **Generate Sample Parameters** button on the right-hand side will run the code in the editor and display in the small box below the button a sample set of generated parameters. If there is an error with the code, the box will turn red and the error message will be displayed.

Creating and using parameters
*****************************
To create a parameter, store a value in the ``codio_parameters`` dictionary. You can then refer to the parameter throughout the assessment within double curly brackets (otherwise known as mustache templating).

   .. image:: /img/guides/paramterSyntax.png
      :alt: Syntax for parameters in Codio

See the first image on this page for an example of creating parameters. Once created, you can then refer to parameters throughout the other fields in your assessment (e.g. instructions on the **General** tab, fields on the **Execution** tab, rationale on the **Grading** tab).

   .. image:: /img/guides/param_instructions2.png
      :alt: Parameters in question field

   .. image:: /img/guides/param_execution.png
      :alt: Parameters in fields of multiple choice assessment
      
Creating parameters from on web-based content
----------------------------------------------
When parameters are generated, the script in the PARAMETERS tab does **not** have access to the files in the box or on the stack. To pull a random choice from a large dataset, instead of hardcoding the dataset into the script, you can use Github or some other web-based CDN.

If you choose to use Github, make sure your script has a URL that indicates the **RAW** version of the file which should look similar to:

.. code::

   https://raw.githubusercontent.com/github_user_name/repo_name/branch/folder_name/file_name.txt

To find this URL, find the file through the Github interface and click the **RAW** button:
   .. image:: /img/raw_github_button.png
      :alt: Raw button in Github interface

If it is a particularly large file, Github will present you a link instead:
   .. image:: /img/raw_github_link.png
      :alt: View raw link in Github interface

Here is an example script:

.. code:: python

   import random, string
   from urllib.request import urlopen

   codio_parameters = dict()

   codio_parameters["COUNT"] = random.randint(2, 4)

   words_file = urlopen("https://raw.githubusercontent.com/lorenbrichter/Words/master/Words/en.txt")
   words = words_file.readlines()
   codio_parameters["OUTPUT"] = words[random.randint(0,len(quotes))-1].decode('utf-8')


**Limitations:**

- We do not advise doing API calls during parameter generation due to the introduction of dependency on another system.
- Parameters are only re-generated on Publish if the PARAMETERS code has been changed. Updating to only the CDN or Github repo will **NOT** re-generate the parameters.
    * Best practice is to upload a new file with a new name -- and when you update the file name on the PARAMETERS tab, this will cause the regeneration and ensure clarity on which version of the file the assessment is using.

Accessing parameters in Auto-grading scripts
********************************************
When using parameters with assessments executing auto-grading scripts, such as with :ref:`Advanced Code Tests <advanced-code-test>`, you can access parameters from the ``CODIO_PARAMETERS`` environment variable.

To test your parameterized auto-grading script, you need to do one of the following:
  1. Within the authoring version of the assignment, click **Generate Sample Parameters** on the PARAMETERS tab and **Save** the assessment (even if you made no changes). This creates the ``CODIO_PARAMETERS`` environment variable within your authoring version of the assignment. Then you can simply click the assessment button when :ref:`previewing the Guide <preview-content-in-guides>`. (Note: ``CODIO_PARAMETERS`` environment variable is only accessible through the assessment, **not** via the command line).
  2. publish your assignment and :ref:`either Preview as a teacher or as a Test Student <preview-course>`
  3. manually create the ``CODIO_PARAMETERS`` environment variable inside the authoring version of the assignment

More examples
*************
You can find more examples of parameterized assessments in Codio:
  1. In our `blog post on parameterized assessments`_
  2. In our `Developing Evergreen Course Materials webinar`_
    
.. _blog post on parameterized assessments: https://www.codio.com/blog/individualized-student-questions-parameterized-assessments
.. _Developing Evergreen Course Materials webinar: https://www.codio.com/on-demand-webinars?wchannelid=rr05s1wyns&wmediaid=igvq1jnlwi
