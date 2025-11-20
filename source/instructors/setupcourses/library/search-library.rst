.. meta::
   :description: You can search the Assessment's Library and filter by tags such as programming language.
.. _search-library:

Search Assessments Library
==========================

Searching an assessment library works the same way whether you're using Codio's :ref:`Global Assessment Library <global-library>` or your :ref:`organization assessment library <org-library>`. To search a library, follow these steps:

1. From the course dashboard navigate to **Edit Assignments**. 

2. Click and Open an Assignment. 

3. Click **Edit**. 

4. In the Guide Editor, click the **Assessments** button and choose **Assessment** from the **Add from Library** area.
 
5. Click the **Library Name** drop-down and choose the assessments library you want to search.

   .. image:: /img/selectLib.png
      :alt: Select Library


6. To narrow the displayed assessments, enter a tag and value pair. For example, select **Programming Language** as the tag and **Python** as the value. The search is not case sensitive, and Codio provides auto-complete suggestions as you type.

   .. image:: /img/autoComplete.png
      :alt: Autocomplete

   
.. tab-set::

   .. tab-item:: Filter Categories

      .. list-table:: Filter Categories and Inputs
         :widths: 30 70
         :header-rows: 1

         * - Category
           - Available Inputs & Description
         * - Bloom's Taxonomy Level
           - .. tab-set::

                .. tab-item:: Levels I-III
                
                   * Level I - Remembering
                   * Level II - Understanding
                   * Level III - Applying

                .. tab-item:: Levels IV-VI
                
                   * Level IV - Analyzing
                   * Level V - Evaluating
                   * Level VI - Creating
         * - Assessment Type (auto-detected)
           - .. tab-set::

                .. tab-item:: Code-Based
                
                   * Standard Code Test 
                   * Advanced Code Test 
                   * Parsons Puzzle 

                .. tab-item:: Text-Based
                
                   * Multiple Choice 
                   * Fill in the Blanks 
                   * Free Text Autograde 
         * - Programming Language
           - Select the programming language for code-based assessments (e.g., Python, Java, C++, JavaScript)
         * - Category (topic-level)
           - Broad subject area or topic category for filtering assessments (e.g., variables, functions, loops).
         * - Content (sub-topic level)
           - Specific subtopic or concept within the category (e.g., modifying variables, creating functions, nesting for loops).
         * - Learning Objective (SWBAT form)
           - Define what "Students Will Be Able To..." accomplish after completing the assessment
             
             Example: "Students will be able to implement binary search algorithms efficiently"

   .. tab-item:: Using Multiple Filters

      **Adding multiple filters:**
      
      - Click any tag field in the results to automatically add it to your search query
      - Click the **+** button to add a new row for additional tag and value pairs
      - Add as many tag and value pairs as needed to refine your search

      .. image:: /img/doubleTags.png
         :alt: Add Tags

      The results update automatically based on your selected filters.

      .. image:: /img/searchResults.png
         :alt: Search Results




Managing Saved Searches
-----------------------

.. tab-set::

   .. tab-item:: Saving Searches

      If you want to save search parameters, follow these steps:

      1. Click the **Save** button to the right of the tags and values.

      2. On the **Save Search** dialog, enter a **Search Name** and click **OK**.

         .. image:: /img/nameSearch.png
            :alt: Search Name

   .. tab-item:: Using Saved Searches

      To use a saved search, click the **Saved** drop-down list and choose the saved search.

      You can edit these search parameters without changing your saved search.

   .. tab-item:: Deleting Saved Searches

      To remove a saved search, click the **Saved** drop-down list and click the red **x** next to the name.

      .. image:: /img/savedSearchDelete.png
         :alt: Delete Saved Search