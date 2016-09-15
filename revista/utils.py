# -*- coding: UTF-8 -*-
import os
import re

p = re.compile(r'[^0-9a-zA-Z\._]+')

def repl(match):
    chars = {u'á': u'a', u'Á': u'A', u'é': u'e', u'É': u'E', u'í': u'i', u'Í': u'I', u'ó': u'o',
             u'Ó': 'O', u'ú': u'u', u'Ú': 'U', u'ñ': u'n', u'ü': u'u', }
    a = ''
    for i in match.group():
        if i in chars:
            a = a + chars[i]
        else:
            a += '_'
    return a


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    nombre = p.sub(repl, filename.replace('.' + filename.split('.')[-1], ''))
    filename = "%s.%s" % (nombre, ext)
    return os.path.join(instance.fileDir, filename)
