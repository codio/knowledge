.. meta::
   :description: Markdown content

## Markdown content editing
### Cheat Sheet
Please refer to the **Callout** section of the Cheat Sheet. If you have not done so already, copy [this starter pack](https://codio.com/home/starter-packs/cb114a27-d88e-4b74-a2a0-518ccb30dc44/) into your own account. You should select the **Use Pack** option to create the project.

Content can be written in

- **Markdown** - the recommended option and described on this page
- **HTML** allowing more detailed control but requiring more time; described on the next page.

When you are in edit mode, you can select a section by

- using the navigation buttons in the header area
- selecting a section from the section list

![editnav](/img/guides/editnav.png)


### Renaming the Section
You can rename your section by clicking on the section title in the header area.

### Writing content
You can then start writing your content in the main content area.

### Markdown
For those of you not familiar with Markdown, it is an extremely easy way of writing content without having to worry about HTML.

When in Play Mode or as you preview, your content is rendered as students will see it. You can also override the default CSS styling if you wish. Go to **Tools->Guide->Add Custom CSS**

![Guide CSS](/img/guides/guidecss.png)

'Reset Custom CSS' will restore the default CSS styling

Click here for details on how to insert [images, videos and hyperlinks](/courses/authoring/#adding-media).

Here is a summary of the Markdown formatting codes

### Headers/Titles
To display a header or title, you can use the `#` character at the start of the line. The more `#` characters you add, the smaller the font.

```markdown
# Big title
## Smaller title
# Even smaller title
## etc.
```

### Bold and Italic
To create bold or italic text, you use `**` and `*` either side of the respective words.

```markdown
I want to say that **this is really important**, you know
I *really* like chocolate
```

### Bullet Lists
To create a list of bullet points, you start the line with a `-`

```markdown
- Bullet 1
- Bullet 2
- Bullet 3
- etc
```

### Numbered Lists
To create a numbered list, you start the line with a `1.` The numbers are automatically calculated for you.

```markdown
1. Item 1
1. Item 2
1. Item 3
1. etc
```

### Code Blocks
If you want to show some code, styled with the courier font, in a box and with syntax highlighting applied you surround your code block with three backticks `` ``` ``. For example, the following javascript snippet

```js
var i;
for(i = 0; i < 10; i++) {
   document.write(i);
}
```

is written with the first line as

`` ```js``

then your code, and the last line as

`` ``` ``

Note that you can specify a language type after the top 3 back ticks. Entering `python ` after the backticks would apply syntax highlighting for python. Many languages are supported. [See a full list of supported languages here](https://github.com/github/linguist/blob/master/lib/linguist/languages.yml). You should search for your language and then use the `alias` shown.

The Code block also includes a 'copy to clipboard' button to allow students to easily copy the code to their clipboard where you may want them to run this code in the assignment

![copy to clipboard](/img/guides/copyclipboard.png)



### Code Segments
If you want to insert a piece of code inline with the rest of your text, then you use a single \` (backtick) character either side of the text. For example,

We can define a variable `var x;` if we like

... is written in markdown as

We can define a variable \`var x;\` if we like


### Indented Lists
If you want to indent a list, then indent just 2 spaces and it will indent.

```markdown
  - Bullet 1
  - Bullet 2
  - Bullet 3
  - etc
```

### Callout Blocks
If you want to show a callout block a number of options are available and others can be easily added if required

  - important
  - info
  - warning
  - topic
  - definition
  - challenge
  - guidance
  - meetup
  - hackathon
  - create
  - calendar
  - growthhack
  - xdiscipline
  - debugging

e.g.

```
|||info
# My Title

Some text

|||
```

![calloutinfo](/img/guides/callout_info.png)

The **Guidance** callout block is only visible in play mode to designated teachers within a course. It is not visible for students.


### Hyperlinks, Images, Videos & iframes
We describe these in [this section](/courses/authoring/#adding-media).

### HTML
You can include HTML tags

### Latex / MathJax

Latex is supported using [MathJax](http://www.mathjax.org/). For example

```markdown
When $a \ne 0$ there are two solutions to $(ax^2 + bx + c = 0)$ and they are $x = {-b \pm \sqrt{b^2-4ac} \over 2a}$

and for multiple lines we do the following

$$
y=x^2
y=\frac{x^2}{x+1}
$$
```

[Click here](/courses/authoring/#latex-for-math-expressions) for more details on Latex and Mathjax.

![MathJax](/img/guides/mathjax.png)

Inline math equations are encapsulated in a single `$` like this: $\omega = d\phi / dt$.

### Collapsible Content
In writing content, it is sometimes useful to provide information for the student, but to keep this hidden until they are ready.

This can be achieved with collapsible content and the `<details> <summary>` elements. The content is treated as HTML and as such a mix of HTML and Markdown can be required.
#### Notes
- If including code blocks, ensure you have an empty line after the closing ``</summary>`` tag.
- All code block starter lines, e.g. ` ```js ` must be preceded by a blank line. 
- The closing block ` ``` ` tag must be followed by a newline. 
- If you have multiple collapsible sections, ensure you have an empty line after the closing ``</details>`` tag.
- If you wish to have the content showing by default, use `<details  open>`.

**Example**

![CollapsibleContent](/img/guides/collapsible.png)

To achieve this result, the code is comprised below (in 3 code blocks to ensure all presents correctly here)

```markdown
## Example Collapsible Content

<details><summary>
	There are some <b>Special Numeric Values</b> which are part of the number data type. For each of the variables <code>a</code> <code>b</code>and <code>c</code> print out their data types and values.
</summary><hr>

The result of any mathematical operation will produce a value of type `number`.

1. Variable `a` contains a value of `infinity` which represents mathematical infinity.
2. Variable `b` is assigned a value where the left-hand operator looks like a `string` however JavaScript tries to convert it into a number which is successful.
3. In the case of variable `c`, the string can't be converted and the operation returns the value of `NaN` which means _not a number_. If this is then used in susequent operations the value cascades and the result will also be `NaN`.
```
```
<h6>Code Block</h6>

```js `
const name = {
		first: 'John',
		'last name': 'Doe',
		dob: {
			year: 1970,
			month: 'January'
	}
}
```
```
</details>
```

### Cheat Sheet

Check out our [Cheat Sheet](https://codio.com/home/starter-packs/cb114a27-d88e-4b74-a2a0-518ccb30dc44/) and **Use Pack** to create the Cheet Sheet project in your Codio account.
## Previewing content
### Preview mode
You will regularly want to switch from editing your page content to preview it as users will see it. The best way to do this is to press the preview button in the top right of the content window. When the guide renders, it would open at the current page you were editing.

![authtoken](/img/guides/preview-button.png)

To return to the edit mode, press the **Editor** button and you will be returned to edit mode on the page that you were viewing in Play mode.

![authtoken](/img/guides/editor-button.png)


### Split screen
Another approach that works for the current page is to switch layout mode to split view mode by selecting the 2nd from left button in the header bar.

![authtoken](/img/guides/split-button.png)

### Play
You can start the Guide player from the **Tools->Guide->Play** menu or selecting the '>' icon in the file tree
## HTML content editing
We do not recommend this setting unless you have very specific reasons. It is much harder to use and maintain than markdown but for those who want ultimate control over appearance it is a good option.

### Setting HTML
You can specify that an individual page be authored using HTML from the content **Settings**. You will find the **Content type** dropdown where you can switch between HTML and markdown.

### CSS header and footer
In order to style your content properly, you should use the **Edit HTML header** and **Edit HTML footer** settings. These can be found in the main **Settings** area on the **Global** tab.

The header and footer information wrap the HTML content for your page. Below is a typical example of a header.

```html
<html>
<head>
  <meta charset="UTF-8">
		<title>bjlo2e_ch04-1</title>
		<link href=".guides/content/css/my-style.css" rel="stylesheet" type="text/css" />
		<script src="https://codio.com/codio-client.js" type="text/javascript"></script>
		<script src=".guides/content/script/my-script.js" type="text/javascript"></script>
	</head>

<body>
```

And here is the footer.

```html
</body>
</html>
```

### Support functions
In a page authored using Markdown, you are able to create buttons and other actions. We provide some javascript functions that support the same functionality.

**Important** : if you use any of the functions listed below then you must load `https://codio.com/codio-client.js`in the HTML Header as shown in the example above.


- `codio.run(command, callback)` - Run a command on the box. `callback` will fire once executed and should be used to communicate back to the user.
- `codio.runAndShow(command, outputElementId)` - Run a command on the box. All `stdout` will be displayed in `outputElementId`.
- `codio.open('file', path, panel_num)` - Opens a file located in `path` in the `panel_num` panel, where `0` is the first panel from top left
- `codio.open('terminal', command, panel_num)`-  Opens a terminal window and executes `command`. `panel_num` specifies the location of the panel, where `0` is the first panel from top left.
- `codio.open('preview', url, panel_num)` - Opens a preview window at `url`. `panel_num` specifies the location of the panel, where `0` is the first panel from top left.
- `codio.goToNextSection()` - Moves to the next page in the guide.
- `codio.goToPreviousSection()` - Moves to the previous page in the guide.
- `codio.switchUnit(unitId)` - Changes to a different assignment. The assignment ID is found by opening the assignment and getting the ID from the URL.
- `codio.goToSectionTitled('Section Title')` - Switches to the page whose title is "Section Title'.
- `codio.assessments.check(assessmentId)` - Executes the assessment
- `codio.assessments.reset(assessmentId)` - Resets any response and score that the user may have already provided for `assessmentId`.
- `codio.assessments.get(assessmentId, callback)` - Gets the result data for a completed assessment
- `codio.assessments.send(assessmentId, answer, points, callback)` - Sends result data for a custom assessment. `answer` contains the custom result data for `assessment` and will be stored in Codio. You can use `codio.assessments.get()` to reconstruct the output for an already answered question.
- `codio.resetCurrentFiles()` - Allows students to restore current files in guides within your content.
