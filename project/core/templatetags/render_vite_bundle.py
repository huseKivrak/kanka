# This template tag is needed for production

import json

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def render_vite_bundle():
    """
    Template tag to render a vite bundle in production.
    """

    try:
        fd = open(f"{settings.VITE_APP_DIR}/dist/manifest.json", "r")
        manifest = json.load(fd)
    except FileNotFoundError:
        raise Exception(
            f"Vite manifest file not found or invalid. Maybe your {settings.VITE_APP_DIR}/dist/manifest.json file is empty?"
        )

    imports_files = "".join(
        [
            f'<script type="module" src="/static/{manifest[file]["file"]}"></script>'
            for file in manifest["index.html"]["imports"]
        ]
    )

    return mark_safe(
        f"""<script type="module" src="/static/{manifest['index.html']['file']}"></script>
        <link rel="stylesheet" type="text/css" href="/static/{manifest['index.html']['css'][0]}" />
        {imports_files}"""
    )