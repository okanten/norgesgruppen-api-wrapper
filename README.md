# NorgesGruppen API Wrapper
An unofficial API-wrapper for the API used by various NorgesGruppens' stores (Spar, Joker, Meny).
Something I made for personal projects, but I figured I might as well release it to the public.

## Usage
Import the module and classes, instantiate the Store class with a store code (will default to Spar if none is given), create a new Product with a search term (e.g. "Cola" or "5000112636864").
Every getter will default to index 0 in the search results, but it can be user-defined.

### No user-defined store or index.
```
    spar = Store()
    cola = Product(spar, 'Cola')

    print('content_type:')
    print(cola.get_content_type())

```

### User-defined store and index for item results.
```
    meny = Store(1300)
    cola = Product(meny, 'Cola')

    print('content_type:')
    print(cola.get_content_type(1))

```

### Store codes:
```
    ID:
     1210 - Spar
     1220 - Joker
     1300 - Meny
```

See examples.py for more examples. Its pretty self-explanatory.


