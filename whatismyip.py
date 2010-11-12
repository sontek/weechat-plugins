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

def command_input_callback(data, buffer, command):
    """ Function called when a command "/input xxxx" is run """
    if command == '/whatismyip return':
        what_is_my_ip()

        weechat.buffer_set(buffer, 'input', input)

    return weechat.WEECHAT_RC_OK

if weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE,
                    SCRIPT_DESC, "", ""):

    # Hooks we want to hook
    hook_command_run = {
        "input" : ("/whatismyip return",  "command_input_callback"),
    }

