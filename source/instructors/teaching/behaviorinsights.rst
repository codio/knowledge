.. meta::
   :description: Enable and view behavior insights which combine different IDE logs to identify potential plagiarism.

.. _behavior-insights:

Behavior Insights
=================

All teachers have access to Codio's Behavior Insights which combines different IDE logs into understandable measures to detect cases of potential plagarism.


Enable Behavior Insights for your Course
----------------------------------------
**Behavior Insights** is enabled at the course-level. Navigate to the **Courses** page and select the course to open it. Then choose **Basic Settings** under **Grading** in the left hand menu.

  .. image:: /img/insights/BehaviorInsightsToggle.png
     :alt: Select: Course, Basic Settings, Enable behavioral insights, Save Changes

Toggle on the **Enable Behavioral Insights** setting and click **Save Changes**.

Viewing Behavior Insights
-------------------------
When you go to the Student progress page of an assignment in that course, you should now see a **Behavior** column and be able to filter and sort based on the behavior indicator.

  .. image:: /img/insights/BehaviorInsightsStudentProgressIndicator.png
     :alt: A Behavior column on the assignment progress dashboard can be filtered and sorted
     
Click on an indicator under the **Behavior** column to see the Behavior Insights Dashboard.

  .. image:: /img/insights/BehaviorInsightsDashboard.png
     :alt: Five tiles showing numeric metrics with text descriptions under each
     
There should be between 1 and 5 tiles displayed. Tiles are only displayed if the student value is outside of a given threshold (indicated by dashed lines or red on the tile). Each tile has a textual description directly below it to help teachers interpret the numerical date presented in graphical form on the tile.

Click the **Ignore** button at the bottom of the dashboard to remove the behavior indicator for that student on that assignment. This action cannot be undone.

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
    
