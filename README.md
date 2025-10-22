# Creating Python programs in Codio

## One time setup

### Stack
If using Codio, put on the certified Python stack `Python Ubuntu 22.04 (pyenv)`. 

### Install

```
pip install sphinx==8.2.0 sphinxawesome-theme==5.3.2 sphinx-docsearch==0.1.0 sphinx-sitemap==2.9.0 sphinx_code_tabs==0.5.5 recommonmark==0.7.1
```

### Build

```
python3 -m sphinx source build
```

## Every time you make an edit

### Make

```
make html
# or
make html TYPE=instructor
# or 
make html TYPE=student
```
If inside Codio, you can use the Make button on the Codio menu (Next to Preview)

### Preview

Navigate using a web-browser to: **https://{{domain}}/build/html/index.html**

If inside Codio, you can use the Preview play button on the Codio menu.
