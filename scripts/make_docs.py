import json
from os.path import join
from functools import partial
from io import StringIO

CORPORA = './corpora.txt'

with open(CORPORA, 'r') as f:
    for line in f:
        corpus = line.strip()

        with open(join(corpus, 'README.template.md')) as tf, \
             open(join(corpus, 'README.md'), 'w') as of, \
             open(join(corpus, 'datapackage.json')) as dpf:

            template = tf.read()
            pkg = json.load(dpf)

            summary = StringIO()
            body = StringIO()

            ps = partial(print, file=summary)
            pb = partial(print, file=body)

            ps('## Summary')
            ps()
            ps('*Resources*')
            ps()

            for resource in pkg['resources']:
                ps('* [%s](#%s)' % (resource['title'], resource['name']))

                pb('<h2 id="%s">%s</h2>' % (resource['name'], resource['title']))
                pb()
                pb('File: [%s](./%s)' % (resource['path'], resource['path']))
                pb()
                pb(resource['description'])
                pb()
                pb('*Fields*')
                pb()

            for field in resource['schema']['fields']:
                pb('* **%(name)s** (*%(type)s*): %(description)s' % field)

            contents = summary.getvalue() + '\n' + body.getvalue()
            of.write(template.format(contents=contents.strip()))
