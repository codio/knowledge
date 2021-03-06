.. meta::
   :description: The Grade weights settings are used to enable and disable the grading model to be used: Teachers Grading, Assessments Grading, or Script Grading.


.. _grade-weights:

Grade Weights
=============
The **Grade Weights** settings are used to enable and disable the grading model to be used: Teachers Grading, Assessments Grading, or Script Grading, and to manage the grading weight.

.. image:: /img/gradingweights.png
   :alt: Grade Weights

View this video to learn more.

.. raw:: html

    <script src="https://fast.wistia.com/embed/medias/5xp528jt6x.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_5xp528jt6x videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/5xp528jt6x/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

You can enable all of the grading options and set grading weights for each. The total grade is based on the grading weight assigned to each option. For example, if Teachers Grading has a grading weight of 2 and Assessments Grading has a grading weight of 1, the final grade is calculated as Teachers Grading points * 2 + Assessments Grading points * 1 /3).

If only one option is enabled, 100 percent of the points of the enabled grading option go to the final grade.

To specify Grade Weights, follow these steps:

1. Open the assignment **Settings**.
2. In the **Grade Weights** area, click the grading options you want to enable and assign the grading weights to each option:

  - **Teachers Grading** - This option allows you to specify a [Grading Rubric Template](/courses/classes/#grading-rubric-templates) to use with an assignment and specify the grading weight.

    - Click **Teachers Grading** and enter a value in the **Grading Weight** field.
    - Click **Rubics** to assign a grading rubic template to the assignment and then choose the rubic template from the drop-down list.

  - **Assessments Grading** - If your assignment includes [assessments](/courses/assessments/), this option is enabled by default. If you do not want the results of the assessments to be included in the grading, disable this option.

    - Click **Assessments Grading** and enter a value in the **Grading Weight** field.

  - **Script Grading** - This option allows you to specify an auto-grade script that runs when the assignment is :ref:`marked as complete <mark-assignment-complete>`. The default setting ensures that any grades generated from auto-graded assessments and grades from free text assessments are automatically transferred into the grading field.

   - Click **Script Grading** and enter a value in the **Grading Weight** field.
   - Click **Set Custom Script Path** and choose the path from the drop-down list.

   For more information about auto-grade scripts, see :ref:`Using Auto-Grade Scripts <auto-grade-scripts>`.
   
