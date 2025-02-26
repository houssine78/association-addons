import os
import requests
import base64

from urllib.parse import urlparse
from odoo import http, _

import logging
_logger = logging.getLogger(__name__)

try:
    import base64
except ImportError:
    _logger.debug('Cannot `import base64`.')

class ImageFromURL(http.Controller):

    @http.route('/upload_attachment_form_url/get_base64_attachment_data', type="json", auth="public")
    def get_base64_attachment_data(self, url):
        result = {
            'base64': False,
            'file_name': None,
            'mime_type': None
        }
        if url: 
            try:
                # Check the URL and get the headers
                response = requests.head(url)
                if response.status_code != 200:
                    return result
                
                content_type = response.headers.get('Content-Type')
                if content_type:
                    # Download the image
                    image_response = requests.get(url)
                    if image_response.status_code != 200:
                        return result
                    
                    # Encode image content to Base64
                    result['base64'] = base64.b64encode(image_response.content).decode('utf-8')
                    result['mime_type'] = content_type
                    
                    # Extract the file name from the URL
                    parsed_url = urlparse(url)
                    result['file_name'] = os.path.basename(parsed_url.path)
                    
                    return result
                else:
                    return result
            except Exception as e:
                print(f"An error occurred: {e}")
                return result
        return result
