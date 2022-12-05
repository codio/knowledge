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

   .. image:: /img/guides/parameterSyntax.png
      :alt: Syntax for parameters in Codio

See the first image on this page for an example of creating parameters. Once created, you can then refer to parameters throughout the other fields in your assessment (e.g. instructions on the **General** tab, fields on the **Execution** tab, rationale on the **Grading** tab).

   .. image:: /img/guides/param_instructions2.png
      :alt: Parameters in question field

   .. image:: /img/guides/param_execution.png
      :alt: Parameters in fields of multiple choice assessment

Accessing parameters in Auto-grading scripts
********************************************
When using parameters with assessments executing auto-grading scripts, such as with :ref:`Advanced Code Tests <advanced-code-test>`, you can access parameters from the ``CODIO_PARAMETERS`` environment variable.

To test your auto-grading script, you need to either:
  1. publish your assignment and :ref:`either Preview as a teacher or as a Test Student <preview-course>` since the ``CODIO_PARAMETERS`` environment variable does not exist in the authoring version of the assignment
  2. manually create the ``CODIO_PARAMETERS`` environment variable inside the authoring version of the assignment

More examples
*************
You can find more examples of parameterized assessments in Codio:
  1. In our `blog post on parameterized assessments`_
  2. In our `Developing Evergreen Course Materials webinar`_
    
.. _blog post on parameterized assessments: https://www.codio.com/blog/individualized-student-questions-parameterized-assessments
.. _Developing Evergreen Course Materials webinar: https://www.codio.com/on-demand-webinars?wchannelid=rr05s1wyns&wmediaid=igvq1jnlwi
