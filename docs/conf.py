# -*- coding: utf-8 -*-
from sphinx_celery import conf
import sys

sys.path.append('.')

globals().update(conf.build_config(
    'faust', __file__,
    project='Faust',
    # version_dev='2.0',
    # version_stable='1.4',
    canonical_url='http://faust.readthedocs.org',
    webdomain='',
    github_project='robinhoodmarkets/faust',
    copyright='2017',
    html_logo='images/logo.png',
    html_favicon='images/favicon.ico',
    html_prepend_sidebars=[],
    include_intersphinx={'python', 'sphinx'},
    extra_extensions=[
        'sphinx.ext.napoleon',
        'sphinx_autodoc_annotation',
        'sphinxcontrib.asyncio',
        'alabaster',
        'faustdocs',
    ],
    extra_intersphinx_mapping={
        'aiohttp': ('https://aiohttp.readthedocs.io/en/stable/', None),
        'aiokafka': ('https://aiokafka.readthedocs.io/en/stable/', None),
    },
    # django_settings='testproj.settings',
    # from pathlib import Path
    # path_additions=[Path.cwd().parent / 'testproj']
    apicheck_ignore_modules=[
        'faust.__main__',
        'faust.assignor',
        'faust.bin',
        'faust.models',
        'faust.serializers',
        'faust.streams',
        'faust.streams._coroutines',
        'faust.transport.confluent',
        'faust.types._coroutines',
        'faust.types',
        'faust.utils',
        'faust.utils.avro',
        r'faust.utils.kafka.*',
        'faust.utils.types',
        'faust.utils.graphs.graph',
        'faust.utils.graphs.formatter',
        'faust.web',
        r'faust.web.apps*',
        'faust.web.apps.stats.app',
        'faust.web.drivers',
    ],
))

html_theme = 'alabaster'
html_sidebars = {}
templates_path = ['_templates']

autodoc_member_order = 'bysource'

# This option is deprecated and raises an error.
try:
    del(html_use_smartypants)  # noqa
except NameError:
    pass
