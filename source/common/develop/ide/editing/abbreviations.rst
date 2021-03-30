
.. meta::
   :description: HTML and CSS abbreviations that expand to code in the IDE.
   
.. _abbreviations:

Abbreviations
=============

Codio offers numerous HTML and CSS abbreviations that expand to code. You simply enter the abbreviation in the Code Editor and then press the **Tab** key to expand the abbreviation. For example:

.. code:: css

    div>ul>li*3

which expands to

.. code:: html

      <div>
          <ul>
              <li></li>
              <li></li>
              <li></li>
          </ul>
      </div>

Basic HTML example
------------------

.. code:: css

    div>ul>li*3

results in

.. code:: html

    <div>
        <ul>
            <li></li>
            <li></li>
            <li></li>
        </ul>
    </div>

Juicier HTML example
--------------------

.. code:: ini

    #page>div.logo+ul#navigation>li*5>a{Item $}

results in

.. code:: html

    <div id="page">
        <div class="logo"></div>
        <ul id="navigation">
            <li><a href="">Item 1</a></li>
            <li><a href="">Item 2</a></li>
            <li><a href="">Item 3</a></li>
            <li><a href="">Item 4</a></li>
            <li><a href="">Item 5</a></li>
        </ul>
    </div>

Insertion stops/edit points
---------------------------
Some abbreviations have insertion points. For example:

.. code:: css

    a:link

inserts:

.. code:: html

    <a href="http://|"></a>

Where the ``|`` character represents the cursor after insertion. After you have entered the **href** url, press **Ctrl+Alt+right arrow** (not the **Tab** key) to jump to the next edit point.

For more HTML abbreviations, see <http://docs.emmet.io/abbreviations/>`__.

CSS examples
-------------

* **w100p** results in **width: 100%**
* **m10p30e5x** results in **margin: 10% 30em 5ex**

.. code:: css

    p100+m10e

results in

.. code:: css

    padding: 100px;
    margin: 10em;


.. code:: css

    lg(left, #fc0, 30%, red)

results in

.. code:: css

    background-image: -webkit-gradient(linear, 0 0, 100% 0, from(#fc0), color-stop(0.5, 30%), to(red));
    background-image: -webkit-linear-gradient(left, #fc0, 30%, red);
    background-image: -moz-linear-gradient(left, #fc0, 30%, red);
    background-image: -o-linear-gradient(left, #fc0, 30%, red);
    background-image: linear-gradient(left, #fc0, 30%, red);

Fuzzy search
------------

Fuzzy search logic for CSS snippets is available to make finding abbreviations easy. Every time you enter an unknown abbreviation, Emmet attempts to find the closest snippet definition. For example:

Instead of writing **ov:h** (overflow: hidden;) abbreviation, you can write **ov-h**, **ovh**, or **oh** and fuzzy search returns the correct abbreviation. 

For more details on CSS abbreviations, see the `Emmet documentation <http://docs.emmet.io/css-abbreviations/>`__.

