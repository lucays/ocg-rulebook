# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sphinx_typlog_theme
import datetime
# from jupyter_sphinx_theme import *
# init_theme()

# -- Project information -----------------------------------------------------

project = 'ocg-rulebook'
copyright = f'2018-{(datetime.datetime.now() + datetime.timedelta(hours=8)).strftime("%Y")}, 碎冰'
author = '碎冰'

# The short X.Y version
version = '2020.4'
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_search.extension',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html.static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = "sphinx_rtd_theme"
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_theme = 'sphinx_typlog_theme'
html_theme_path = [sphinx_typlog_theme.get_path()]
html_theme_options = {
    'logo': 'logo.webp',
    'color': 'rgba(3, 172, 244, 0.8)',
    'description': 'OCG完全规则书 by 碎冰',
    'github_user': 'lucays',
    'github_repo': 'ocg-rulebook',
    'canonical_url': 'https://ocg-rulebook.readthedocs.io',
    'analytics_id': 'UA-131764005-1',
    'last_updated': (datetime.datetime.now() + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S"),
}
html_sidebars = {
    '**': [
        'logo.html',
        'docstatus.html',
        'github.html',
        'searchbox.html',
        'globaltoc.html',
    ]
}

html_static_path = ['.static']
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
html_favicon = '.static/favicon.ico'

# html_logo = '.static/logo.webp'

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ocg-rulebookdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_logo = '.static/pdf_cover.png'
font_path = os.path.join(os.getcwd(), 'fonts') + '/'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'sphinxsetup': 'attentionBorderColor={rgb}{0.012,0.663,0.957}, noteBorderColor={rgb}{0.012,0.663,0.957}, tipBorderColor={rgb}{1,0.412,0.706}',
    'papersize': 'a4paper',
    'figure_align': 'H',
    'extraclassoptions': 'openany,oneside',
    'preamble': r'''
        \usepackage[UTF8]{ctex}
        \usepackage{ulem}
        \newcommand*{\DUrolestrike}{\sout}
        \xeCJKsetup{CJKspace=true}
        \xeCJKDeclareCharClass{CJK}{`①,`②,`③,`④,`⑤,`⇄}
        \setCJKmainfont[Path=%s,BoldFont={NotoSerifCJKsc-Bold.otf},ItalicFont={NotoSerifCJKsc-Light.otf}]{NotoSansCJKsc-Light.otf}
        \setCJKsansfont[Path=%s,BoldFont={NotoSansCJKsc-Bold.otf},ItalicFont={NotoSerifCJKsc-Light.otf}]{NotoSansCJKsc-Light.otf}
        \setCJKmonofont[Path=%s,BoldFont={NotoSansMonoCJKsc-Bold.otf},ItalicFont={NotoSansMonoCJKsc-Regular.otf}]{NotoSansMonoCJKsc-Regular.otf}
    ''' % (font_path, font_path, font_path),
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('pdf_index', 'ocg-rulebook.tex', 'ocg-rulebook Documentation',
     '碎冰', 'manual'),
]

latex_show_pagerefs = True

latex_show_urls = 'footnote'

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ocg-rulebook', 'ocg-rulebook Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ocg-rulebook', 'ocg-rulebook Documentation',
     author, 'ocg-rulebook', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''
epub_show_urls = 'no'
epub_cover = ('_static/epub_cover.png', 'epub-cover.html')
