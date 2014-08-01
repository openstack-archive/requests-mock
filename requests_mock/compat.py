# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import requests


def _versiontuple(v):
    return tuple(map(int, (v.split("."))))


_requests_version = _versiontuple(requests.__version__)


if _requests_version < (2, 3):
    class _FakeHTTPMessage(object):
        """A fake httplib.HTTPMessage for use when creating a Message.

        There is a problem with requests < 2.3.0 such that it needs a httplib
        message for use with cookie extraction. It has been fixed but it is
        needed until we can rely on a recent enough requests version.
        """

        def getheaders(self, name):
            return None


    class _FakeHTTPResponse(object):
        """A fake httplib.HTTPResponse for use when creating a Message.

        There is a problem with requests < 2.3.0 such that it needs a httplib
        message for use with cookie extraction. It has been fixed but it is
        needed until we can rely on a recent enough requests version.
        """

        def __init__(self):
            self.msg = _FakeHTTPMessage()

        def isclosed(self):
            # Don't let urllib try to close me
            return False

    _fake_http_response = _FakeHTTPResponse()

else:
    _fake_http_response = None
