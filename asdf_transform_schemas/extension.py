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
            "tag:stsci.edu:asdf/transform/",
            "http://stsci.edu/schemas/asdf/transform/{tag_suffix}"
        )]

    @property
    def url_mapping(self):
        transform_root = os.path.join(SCHEMAS_ROOT, "transform")
        transform_root_url = urljoin("file:", pathname2url(transform_root))

        return [(
            "http://stsci.edu/schemas/asdf/transform/",
            transform_root_url + "/{url_suffix}.yaml"
        )]
