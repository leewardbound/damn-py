
# DAMN! (Directory And Markup Nesting!)

DAMN is not-your-dad's structured file storage. It is a superset of YAML, and therefore JSON. If you are using YAML and JSON already, there is probably no reason to switch, but you can do so seamlessly. Use DAMN next time you get a headache.

DAMN is good for managing complex configurations that would get too-big-to-manage in other markups and object notations. It does this by allowing you to use directories and filenames all whilly-nilly to organize all your data.

For example, let's redunantly store the same data twice, like this --
```bash
$ echo "{nested: {message: {hi: mom}}}" > ./__.json
$ echo "{message: {hi: mom}}" > ./nested/__.damn
```

Now we can retrieve it like this --


```python
# Load from a string
damn.loads("{nested: {message: {hi: mom} } }")

# Or a flatfile
damn.load('__.json')

# Guess a valid extension (.json|.yml|.yaml|.damn)
damn.load('__')

# Or load from nested directories, automagically
damn.load('.') == {'nested': damn.load('nested/')}
damn.load('__.json') == {'nested': damn.load('nested/__.damn')}
```

In other words, any time nested dictionaries are too much for you to handle, you can fall back to using directories full of files.

A file named 'a/b/c.yml' will populate into a dictionary called `data['a']['b']['c']`, just like that, easy-peasy.

Need more examples? I HAVE FIVE.

```python

# Look, it might as well be YAML!
yaml_abc = yaml.load(yml)
damn_abc = damnit.load(FIXT('abc'))
self.assertEqual(damn_abc, yaml_abc)

# Check the tests/ directory to see how these files are structured
mom = {'hi': 'mom'}
self.assertEqual(damnit.load(FIXT('dir/and/markup/nest')), mom)

# Or you can probably figure this out
self.assertEqual(damnit.load(FIXT('dir')), {'and': {'markup': {'nest': mom}}})

# It's not a science rocket
self.assertEqual(damnit.load(FIXT('foo')), {'bar': damnit.load(FIXT('bar'))})

# if 'bar.yml' and 'bar/__.yml' both exist, directories take precedence over files
self.assertEqual(damnit.load(FIXT('foo/bar')), damnit.load(FIXT('bar')))

```

# Was another markup notation really necessary?
Hey shut up, structuring my config files like this drastically saved me a ton of
time and effort in one of my recent projects, is anything that makes us happy ever really necessary?

# That's it!
I'm tired, I'm doing to bed, got DAMN?
