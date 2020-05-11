import os
from urllib.request import pathname2url, urljoin

from .common import SCHEMAS_ROOT


class AsdfTransformSchemasExtension:
    @property
    def types(self):
        return []

    @property
    def tag_mapping(self):
        return [(
            "tag:astroasdf.org:transform/",
            "http://astroasdf.org/schemas/transform/{tag_suffix}"
        )]

    @property
    def url_mapping(self):
        transform_root = os.path.join(SCHEMAS_ROOT, "transform")
        transform_root_url = urljoin("file:", pathname2url(transform_root))

        return [(
            "http://astroasdf.org/schemas/transform/",
            transform_root_url + "/{url_suffix}.yaml"
        )]

