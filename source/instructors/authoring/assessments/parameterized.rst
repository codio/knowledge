.. meta::
   :description: Parameterized assessments
   
.. _parameterized:

Parameterized assessments
=========================
For all assessment types except Gradebook and Random, you can set up parameterized assessments by writing **python** code on the Parameters tab.

   .. image:: /img/guides/parameterized.png
      :alt: Parameterized Assessment

For more information and to get started, see `Prairielearn <https://prairielearn.readthedocs.io/en/latest/getStarted/>`_ for the popular implementation.

Setting up parameters
*********************

To set up your parameters, create them using **codio_parameters["parameter name"] = yourparamevalue** on the **Parameters** tab and you can then refer to them throughout the assessment within double curly brackets.

e.g. creating a parameter of **codio_parameters["parameter name"] = random_int**, you can then refer to **{{parameter name}}** in your assessment. This can be in the instructions on the **General** tab, in fields on the **Execution** tab as well as in the rationale on the **Grading** tab.

   .. image:: /img/guides/setupparams.png
      :alt: Setting up parameters

   .. image:: /img/guides/param_instructions.png
      :alt: Parameters in instructions

   .. image:: /img/guides/param_commands.png
      :alt: Parameters in commands

Parameter variables
*******************

We are not using global variables but explicitly storing parameter values in a dictionary. Here is an example:

.. code:: ini

  import random
  import uuid

  # init codio_parameters dictionary
  codio_parameters = dict()

  # generate random values
  random_int = random.randint(0, 100)
  random_string = str(uuid.uuid4())
  random_boolean = random.choice([True, False])
  random_float = float(random.randint(0, 1000)/100)
  random_array = []
  random_array.append(random.randint(0, 100))
  random_array.append(str(uuid.uuid4()))
  random_dict = dict()
  random_dict["int"] = random.randint(0, 100)
  random_dict["str"] = str(uuid.uuid4())
  random_dict["boolean"] = random.choice([True, False])

  # add random values to codio_parameters dictionary
  codio_parameters["int"] = random_int
  codio_parameters["str"] = random_string
  codio_parameters["boolean"] = random_boolean
  codio_parameters["float"] = random_float
  codio_parameters["array"] = random_array
  codio_parameters["dict"] = random_dict