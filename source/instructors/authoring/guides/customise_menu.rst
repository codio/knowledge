.. meta::
   :description: Customising IDE menu
   
### Customizing IDE menu
To simplify the educational process for students, the top menu can be customized to remove options from students that they cannot override. 

**Please note that only students will see this. Teachers previewing the assignment will not see the customization. If you wish to check this, the [test student](/courses/classes/#test-students) accounts can be used**

Through a `.codio-menu` file, a teacher can specify what menu items should be hidden.
Example:

```json
{
    "Logo": false, // hides the Codio logo
	"Codio": false, // hides the Codio menu dropdown
    "Project": {
         "Permissions": false // hides the Permissions option in the Project menu dropdown
    },
    "Help": false, // hides the Help menu dropdown
    "Run": false, // hides the Run menu dropdown
    "Preview": false, // hides the Preview menu dropdown
    "Debugger": false, // hides the Debugger menu dropdown
    "Status": false // hides the Status icon, user Avatar, user name and exit button
}
```

**Be aware that if setting Status=false, students will need to use the 'Back to Dashboard' button shown on the last page of the guides to return to their dashboard area**

Setting up .codio-menu file:

![EditorMode](/img/guides/codiomenu.png)

Menu items that the student will see:

![PreviewMode](/img/guides/codiomenupreview.png)

Students will not see the .codio-menu file to be able to edit/change it.
