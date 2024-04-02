
## Singelton

1. Globals are bad and singleton = global
2. You are assuming that in the future you will only ever need a single instance of your class
3. Testing is hard



### Singelton

Doesn't mean that it will live trough the whole lifecycle of a program.

    some_global_var = 123
    
    def reset():
        global some_global_var
        del some_global_var
     
     reset()
