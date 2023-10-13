.. meta::
   :description: Enable and view behavior insights which combine different IDE logs to identify potential plagiarism.

.. _behavior-insights:

Behavior Insights
=================

All teachers have access to Codio's Behavior Insights which combines different IDE logs into understandable measures to detect cases of potential plagarism.


Enable Behavior Insights for your Course
----------------------------------------
**Behavior Insights** is enabled at the course-level. Navigate to the **Courses** page and select the course to open it. Then choose **Basic Settings** under **Grading** in the left hand menu.

  .. image:: /img/insights/BehaviorInsightsToggleV2.png
     :alt: Select: Course, Basic Settings, Enable behavioral insights, Save Changes

Toggle on the **Enable Behavioral Insights** setting and click **Save Changes**.

Configure Behavior Insights Options
-----------------------------------

You can configure the individual Behavior Insights options and set minimum and maximum values for a particular option. Values less than the minimum or greater than the maximum will trigger an indicator and show up in the Behavior column for that respective student.

  .. image:: /img/insights/BehaviorInsightsOptions.png
     :alt: Behavior Insights Options
 

- **Time Spent** - You can monitor the amount of time the student spent on the assignment in the middle. You can set minimum and maximum values (in minutes), values less than the minimum or greater than the maximum will trigger an indicator. You can disable the minimum or the maximum or both as per your requirement.

- **Rate of Edits** - You can monitor Rate of Edits (Characters per Second) of students. Based on thousands of student submissions, we determined a generalized threshold of submissions created with a pace of more than 4 characters edited (inserted or deleted) per second had a high likelihood of being plagiarized so we set the default value for Maximum to 4 but you can change the minimum and maximum values ​​as per your requirement or disable minimum or maximum or both.

- **Coding vs Debugging Time** - You can monitor the percent of active time students spent in an error state (debugging) vs a non-error state (coding). In the context of detecting plagiarism, it would be odd for students to never have errors or spend time trying to resolve them. Based on thousands of student submissions, we determined a generalized threshold of less then 4% of the time in an error state (i.e. “debugging”) had a high likelihood of being plagiarized so we set the default value for Minimum to 4% but you can change the minimum and maximum values ​​as per your requirement or disable minimum or maximum or both.

- **Insertions vs Deletions** - You can monitor the percent of characters inserted vs characters deleted across assignment code files for the student. you can set the minimum and maximum percentage of deletions ​​as per your requirement or disable minimum or maximum or both.

- **External Pastes** - You can monitor each occurrence of a paste that did not come from an assignment code file or the Guide. You can set Minimum lines to count as occurrence and Minimum number of occurrences. You can disable this option if you don’t want to use it in your course.


Viewing Behavior Insights
-------------------------

When you go to the Student progress page of an assignment in that course, you will now see a **Behavior** column and be able to filter and sort based on the behavior indicator.

  .. image:: /img/insights/BehaviorInsightsStudentProgressIndicator.png
     :alt: A Behavior column on the assignment progress dashboard can be filtered and sorted

.. Note:: Behavior Insights will only appear once an assignment is marked as complete. A lack of indicator means no behavior thresholds have been met - the student has no indications of the specified behavior.

Click on an indicator under the **Behavior** column to see the Behavior Insights Dashboard.

  .. image:: /img/insights/BehaviorInsightsDashboard.png
     :alt: Five tiles showing numeric metrics with text descriptions under each
     
There will be between 1 and 5 tiles displayed. Tiles are only displayed if the student value is outside of a given threshold (indicated by dashed lines or red on the tile). Each tile has a textual description directly below it to help teachers interpret the numerical date presented in graphical form on the tile.

Click the **Ignore** button at the bottom of the dashboard to remove the behavior indicator for that student on that assignment. This action cannot be undone.

Behavioral Player
-----------------

You can also view students activity for all files in the assignment going to **Education > Behavioral Player** menu option.

History of External Pastes and CodePlayback
-------------------------------------------
If you click on a bar in the **History of External Pastes** tile, you will be presented with that paste in Codio's Code Playback feature.

  .. image:: /img/insights/BehaviorInsightsPlayback.png
     :alt: Code playback with code changes on top and a timeline underneath with file name and pastes indicated

The top pane shows the contents of the modified file with the change higlighted in green (inserted characters) or red (deleted characters).

The timeline at the bottom indicates all detected pastes, and clicking on the paste will bring you to that point in the timeline.

No Data
-------
Behavior Insights is built on Codio's IDE instrumentation. This means if your students work on their local IDE and simply upload their work to Codio, or you have them working on a 3rd party IDE inside Codio (e.g. VSCode, Jupyter, RStudio, vim, nano), you might see that some tiles are being shown to indicate lack of data:

  .. image:: /img/insights/BehaviorInsightsNoData.png
     :alt: No data displayed on Coding vs Debugging and Insertions vs Deletions tiles
    
