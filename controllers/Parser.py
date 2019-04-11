import configparser, sys

## NOTE - TODO - FIX - filename is weird and not really based off function of code within

class FakeSecHead(object):
    def __init__(self, fp):
        self.fp = fp
        self.sechead = '[asection]\n'

    def readline(self):
        if self.sechead:
            try: 
                return self.sechead
            finally: 
                self.sechead = None
        else: 
            return self.fp.readline()

def add_section_header(properties_file):
    # configparser.ConfigParser requires at least one section header in a properties file.
    # Our properties file doesn't have one, so add a header to it on the fly.
    yield '[{}]\n'.format("asection")
    for line in properties_file:
        yield line



cp = configparser.SafeConfigParser()
cp.read_file(add_section_header(open("config.properties")))
port_dic = dict(cp.items('asection'))
cmd_port = int(port_dic['cmd_port'])
