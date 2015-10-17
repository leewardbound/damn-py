from collections import OrderedDict
import yaml, json, os, glob
join = os.path.join

DAMN_EXTENSIONS={
    'damn': lambda d: load_file(d),
    'yml': lambda fn: yaml.load(open(fn, 'r')),
    'yaml': lambda fn: yaml.load(open(fn, 'r')),
    'json': lambda fn: json.load(open(fn, 'r')),
}
DAMN_FILE_GLOB='*.(%s)'%'|'.join(DAMN_EXTENSIONS.keys())

def any_exists(fn, extensions=None):
    if not extensions: extensions = DAMN_EXTENSIONS
    for ext in extensions:
        f_x = fn + '.' + ext
        if os.path.isfile(f_x):
            return f_x
    return None

def load_file(fn):
    print 'FILE', fn
    with open(fn, 'r') as fh:
        return Damn(yaml.load(fh.read()) or {})

def load(path, match=DAMN_FILE_GLOB):
    print 'loading path',path
    exists = False
    if os.path.isdir(path):
        # check for {path}/__.yml
        exists = any_exists(os.path.join(path, '__'))
        data = exists and load_file(exists) or Damn()
        children = glob.glob(os.path.join(path, '*/'))
        for ext in DAMN_EXTENSIONS:
            children += glob.glob(os.path.join(path, '*.%s'%ext))
        for full_child in children:
            child = full_child[len(path):].strip('/')
            if not child or full_child == exists: continue
            if '.' in child:
                child_dotted = child.split('.')
                child_base = '.'.join(child_dotted[:-1])
                child_ext = child_dotted[-1]
            else:
                child_base = child
                child_ext = ''
            if os.path.isdir(full_child):
                data[child_base] = load(full_child)
            elif child_ext in DAMN_EXTENSIONS:
                data[child_base] = load_file(full_child)
        return data
    elif os.path.exists(path):
        # check for {path}
        return load_file(path)
    else:
        # check for {path}.{ext}
        return load_file(any_exists(path))

def loads(data):
    return Damn()

def dumps(data):
    pass

class Damn(dict):
    def __init__(self, *args, **kwargs):
        super(Damn, self).__init__(*args, **kwargs)
        for k,v in self.items():
            if isinstance(v, dict):
                self[k] = Damn(v)

    def __getattribute__(self, name):
        try: return super(Damn, self).__getattribute__(name)
        except:
            if name in self: return self[name]
            raise

    def __str__(self):
        return json.dumps(self, indent=2)
