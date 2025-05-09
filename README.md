# Creating Python programs in Codio

## One time setup

### Stack
If using Codio, put on the certified Python stack `Python Ubuntu 22.04 (pyenv)`. 

### Install

```
pip install sphinx==4.2.0 sphinx-sitemap sphinx_code_tabs recommonmark git+https://github.com/codio/pydata-sphinx-theme.git@master
```

Due to some versions being outdated, temporarily you will need to use this command to install dependencies:

```
pip install sphinxcontrib-applehelp==1.0.4 sphinxcontrib-devhelp==1.0.2 sphinxcontrib-htmlhelp==2.0.1 sphinxcontrib-qthelp==1.0.3 sphinxcontrib-serializinghtml==1.1.5 sphinx==4.2.0 sphinx-sitemap sphinx_code_tabs recommonmark git+https://github.com/codio/pydata-sphinx-theme.git@master
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
If inside Codio, you can use the Make button on the Codio menu (Next to Preview)

### Preview

Navigate using a web-browser to: **https://{{domain}}/build/html/index.html**

If inside Codio, you can use the Preview play button on the Codio menu.
