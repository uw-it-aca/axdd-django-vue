# Copyright 2022 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

import os
import json
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
from django.templatetags.static import static

register = template.Library()


def vite_manifest(entries_names):

    # path to the manifest.json (relative if localdev, /static if not)
    manifest_filepath = getattr(
        settings,
        "VITE_MANIFEST_PATH",
        os.path.join(os.sep, "static", ".vite", "manifest.json"),
    )

    with open(manifest_filepath) as fp:
        manifest = json.load(fp)
    _processed = set()

    def _process_entries(names):
        scripts = []
        styles = []

        for name in names:
            if name in _processed:
                continue

            chunk = manifest[name]

            import_scripts, import_styles = _process_entries(
                chunk.get("imports", [])
            )
            scripts += import_scripts
            styles += import_styles

            scripts += [chunk["file"]]
            styles += [css for css in chunk.get("css", [])]

            _processed.add(name)

        return scripts, styles

    return _process_entries(entries_names)


@register.simple_tag(name="vite_styles")
def vite_styles(*entries_names):
    """
    Populate an html template with styles generated by vite

    Usage::

        {% vite_styles 'main.js' 'other-entry.js' %}

    Examples::
        <head>
            ...
            {% vite_styles 'main.js' 'other-entry.js' %}
        </head>
    """
    _, styles = vite_manifest(entries_names)
    styles = map(lambda href: static(href), styles)

    def as_link_tag(href):
        return f'<link rel="stylesheet" href="{href}" />'

    return mark_safe("\n".join(map(as_link_tag, styles)))


@register.simple_tag(name="vite_scripts")
def vite_scripts(*entries_names):
    """
    Populate an html template with script tags generated by vite

    Usage::

        {% vite_scripts 'main.js' 'other-entry.js' %}

    Examples::
        <body>
            <!-- Your HTML -->
            {% vite_scripts 'main.js' 'other-entry.js' %}
        </body>
    """
    scripts, _ = vite_manifest(entries_names)
    scripts = map(lambda src: static(src), scripts)

    def as_script_tag(src):
        return f'<script type="module" src="{src}"></script>'

    return mark_safe("\n".join(map(as_script_tag, scripts)))
