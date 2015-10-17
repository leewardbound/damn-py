
# DAMN! (Directory And Markup Notation!)

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


# That's it!
I'm tired, I'm doing to bed, got DAMN?
