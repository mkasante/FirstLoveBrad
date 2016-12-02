# -*- coding: utf-8 -*-

import codecs, cStringIO, csv, json
import sys, requests, os
from collections import OrderedDict


def flatten(l):
    '''
    flattens a list, dict or tuple
    '''
    ret = []
    for i in l:
        if isinstance(i, list) or isinstance(i, tuple):
            ret.extend(flatten(i))
        elif isinstance(i, dict):
            ret.extend(flatten(i.values()))
        else:
            ret.append(i)
    return ret

def convertJsonCsv(appname):
    path = "templates/fixtures"
    try:
        if not os.path.exists(path): os.makedirs(path)

        file_json = "http://localhost:8000/api/%s/?format=json" % appname
        data = requests.get(file_json, auth=("firstloveleeds", "14leeds20")).json(object_pairs_hook=OrderedDict)
        file_csv = "%s/%s.csv" % (path, appname)

        data = data['results']
        fields = data[0].keys()

        with open(file_csv, 'wb') as fo:
            writer = csv.DictWriter(fo, fieldnames=fields)
            o = UnicodeWriter(fo)
            o.writerow(fields)

            for record in data:
                o.writerow(flatten(record.values()))
    except:
        pass
        

class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")


class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self


class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([unicode(s).encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)