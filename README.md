# Creating Python programs in Codio

## One time setup

### Stack
If using Codio, put on the certified Python stack.

### Install

```
pip install sphinx==4.2.0 sphinx-sitemap sphinx_code_tabs recommonmark git+https://github.com/codio/pydata-sphinx-theme.git@master
```

### Build

```
python3 -m sphinx source build
```

## Every time you make an edit

### Make

```
make html
```
If inside Codio, you can use the Make rocketship button on the Codio menu

### Preview

Navigate using a web-browser to: **https://{{domain}}/build/html/index.html**

If inside Codio, you can use the Preview play button on the Codio menu.