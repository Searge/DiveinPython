"""
Weather API Python sample code

Copyright 2019 Oath Inc. Licensed under the terms of the zLib license see https://opensource.org/licenses/Zlib for terms.

$ python --version
Python 2.7.10

"""
import time
import uuid
import urllib.request
import urllib.parse
import hmac
import hashlib
from base64 import b64encode

import json
import ast

"""
Basic info
"""
app_id = 'eHMyyJ4m'
consumer_key = 'dj0yJmk9QnFRblJUckFBenNKJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTVl'
consumer_secret = 'bc99df9b9724f7e0ce029969868b8fd658dcb820'
query = {'location': 'kyiv,ua', 'format': 'json', 'u': 'c'}

url = 'https://weather-ydn-yql.media.yahoo.com/forecastrss'
method = 'GET'
concat = '&'

oauth = {
    'oauth_consumer_key': consumer_key,
    'oauth_nonce': uuid.uuid4().hex,
    'oauth_signature_method': 'HMAC-SHA1',
    'oauth_timestamp': str(int(time.time())),
    'oauth_version': '1.0'
}

"""
Prepare signature string (merge all params and SORT them)
"""
merged_params = query.copy()
merged_params.update(oauth)
sorted_params = [k + '=' + urllib.parse.quote(merged_params[k], safe='')
                 for k in sorted(merged_params.keys())]
signature_base_str = method + concat + urllib.parse.quote(
    url, safe='') + concat + urllib.parse.quote(concat.join(sorted_params), safe='')


"""
Generate signature
"""
composite_key = urllib.parse.quote(consumer_secret, safe='') + concat
oauth_signature = b64encode(hmac.new(composite_key.encode(
    'utf-8'), signature_base_str.encode('utf-8'), hashlib.sha1).digest())


"""
Prepare Authorization header
"""
oauth['oauth_signature'] = oauth_signature.decode('utf-8')
auth_header = 'OAuth ' + \
    ', '.join(['{}="{}"'.format(k, v) for k, v in oauth.items()])
"""
Send request
"""
url = url + '?' + urllib.parse.urlencode(query)

request = urllib.request.Request(url)
request.headers['Authorization'] = auth_header
request.headers['X-Yahoo-App-Id'] = app_id

response = urllib.request.urlopen(request).read()

res_dict = ast.literal_eval(response.decode('utf-8'))
res = json.dumps(res_dict)

print(json.loads(res))
