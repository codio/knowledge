.. meta::
   :description: Solution File templating
 
.. _solutionfile:

Solution File Templating
========================

To help you test/check solutions for students prior to publishing, you can write your solution code within tags (**CODIO SOLUTION BEGIN** and **CODIO SOLUTION END** using the usual commenting out characters for the language being used) that will be visible to the teacher when editing the assignment and allow the code to be executed but will not be available to the student when the assignment is published. 

Example Python solution file:

.. code:: python

    def main:
        # CODIO SOLUTION BEGIN
        print('Hello world!')
        # CODIO SOLUTION END

will then show to students as:

.. code:: python

    def main:
        # WRITE YOUR CODE HERE 

.. Note:: In order that other teachers working with the assignment in a course can also see the solution information to help their students, it is recommended that the solution information is also included within the guidance code block `|||guidance ..... |||` on the guides page or in a specific :ref:`Teacher Only <teacher-only>` page.

Supported language files
------------------------

.c .cpp .java .py .html .css .r .rb .js .ts .sql .h .hpp .ocaml .ml .php .pas .yml .xml .cs .coffescript .fs .go .kt .kts .less .lua .m .h .pl .scala .vb .swift .sh .scss .sass .md .yaml .hs .rkt .ss .scm .lisp .erl .ex .exs .elm .asm .s .rs .rlib .dart .jl