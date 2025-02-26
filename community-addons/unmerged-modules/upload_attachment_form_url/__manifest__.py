# -*- coding: utf-8 -*-
#################################################################################
# Author      : CFIS (<https://www.cfis.store/>)
# Copyright(c): 2017-Present CFIS.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://www.cfis.store/>
#################################################################################

{
    "name": "Attachments URL Uploader | Attachments Upload from URL | Upload URL Attachments | Attachments URL",
    "summary": "Users of Odoo can upload documents from urls to attachments with this module.",
    "version": "18.1",
    "description": """
        Users of Odoo can upload documents from urls to attachments with this module.
        Attachments URL Uploader
        Attachments Upload from URL
        Upload URL Attachments
        Attachments URL       
    """,    
    "author": "CFIS",
    "maintainer": "CFIS",
    "license" :  "Other proprietary",
    "website": "https://www.cfis.store",
    "images": ["images/upload_attachment_form_url.png"],
    "category": "Extra Tools",
    "depends": [
        "web",
        "mail",
    ],
    "data": [
    ],
    "assets": {
        "web.assets_backend": [
            "/upload_attachment_form_url/static/src/js/*.*",
        ],
    },
    "installable": True,
    "application": True,
    "price"                 :  35.00,
    "currency"              :  "EUR",
}
