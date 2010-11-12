# Copyright (c) 2010 by John Anderson <sontek@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import urllib2
import weechat

SCRIPT_NAME    = "whatismyip"
SCRIPT_AUTHOR  = "John Anderson <sontek@gmail.com>"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "GPL3"
SCRIPT_DESC    = "Get your current external ip"


def what_is_my_ip(buffer):
    url = 'http://www.whatismyip.com/automation/n09230945.asp'

    if buffer:
        shortenurl_hook_process = weechat.hook_process(
                    "python -c \"import urllib2; print urllib2.urlopen('" + url + "').readlines()[0]\"",
                    10 * 1000, "process_complete", buffer)
    else:
        return urllib2.urlopen(url).readlines()[0]

def process_complete(data, command, rc, stdout, stderr):
    url = stdout.strip()
    if url:
        weechat.prnt(data, '[%s]' % (url))

    return weechat.WEECHAT_RC_OK

def command_input_callback(data, buffer, args):
    """ Function called when a command "/input xxxx" is run """
    what_is_my_ip(buffer)

    return weechat.WEECHAT_RC_OK

if weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE,
                    SCRIPT_DESC, "", ""):

    weechat.hook_command("whatismyip", SCRIPT_DESC, "", "", "", "command_input_callback", "")
