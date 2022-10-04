.. meta::
   :description: Freezing Code
 
.. _freezecode:

Freezing Code
=============

If you wish to freeze code in a code file that students can't edit/change you can write code within tags (**FREEZE CODE BEGIN** and **FREEZE CODE END** using the usual commenting out characters for the language being used). The section of code will be highlighted to the students along with a padlock icon at the top right of the code block.

Example Python solution file:

.. code:: python

    def main:
        # FREEZE CODE BEGIN
        print('Hello world!')
        # FREEZE CODE END

will then show to students as:

  .. image:: /img/guides/freezecode.png
     :alt: Frozen Code


Supported language files
------------------------

.c .cpp .java .py .html .css .r .rb .js .ts .sql .h .hpp .ocaml .ml .php .pas .yml .xml .cs .coffescript .fs .go .kt .kts .less .lua .m .h .pl .scala .vb .swift .sh .scss .sass .md .yaml .hs .rkt .ss .scm .lisp .erl .ex .exs .elm .asm .s .rs .rlib .dart .jl