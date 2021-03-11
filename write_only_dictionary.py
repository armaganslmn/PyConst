"""
    Copyright info can be found in LICENSE.txt or
    at the end of this document.
"""

import copy

class WriteOnlyDictionary:
    """
    Python2.7+
    
    Write keys once key-value store.
    Main purpose is to provide constant variable semantics present
    in static languages.
    
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    Requirement & specification
    
    Requires a key-value store that has
        store_creation_func = Function that creates an empty store.
        add(key, value)
        does_contain(key) # Returns True if it contains the key.
        get_value(key) # Returns value associated with key.
        get_all_keys() # Returns an iterable of keys.
        get_all_values() # Returns an iterable of values.
        get_all_mappings() # Returns an iterable of mappings.
    functionality.
    
    TODO(armaganslmn):
        Add functions to WriteOnlyDictionary
            + create_keeper_from_mappings(iterable)
                Elements must be of 2 dimensions.
                First one is key, second is value.
                (key, value)
                [key, value]
                etc.
                
            + does_contain(key)
            + get_value(key) # Returns value associated with key.
            + get_all_keys() # Returns an iterable of keys.
            + get_all_values() # Returns an iterable of values.
            + get_all_mappings() # Returns an iterable of mappings.
            + fix_key(old_key, new_key) # returns a new store
            + fix_value(key, new_value) # returns a new store
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    """
    
    class KeyExists(Exception): pass
    class KeyNotFound(Exception): pass
    
    def __init__(self, store_creation_func):
        self.store_func = store_creation_func
        self.STORE = store_creation_func() # Returns an empty key-value store.
    #
    
    def does_contain(self, key):
        return self.STORE.does_contain(key)
    #
    
    def put_key_value(self, key, value):
        if self.does_contain(key):
            t = type(key)
            raise self.KeyExists("`{}` of {} can't be added again to constant store.".format(key, t))
        #
        self.STORE.add(key,value) # Put if it's a new key.
    #
    
    def put_pair(self, pair):
        self.put_key_value(pair[0], pair[1])
    #
    
    def get_value(self, key):
        if self.does_contain(key):
            return copy.deepcopy(self.STORE.get_value(key))
        #
        else: # Can't find the key in store.
            t = type(key)
            raise self.KeyNotFound("`{}` of {} is not in constant store.".format(key, t))
        #
    #
    
    def get_all_keys(self):
        return copy.deepcopy(self.STORE.get_all_keys())
    #
    
    def get_all_values(self):
        return copy.deepcopy(self.STORE.get_all_values())
    #
    
    def get_all_mappings(self):
        return copy.deepcopy(self.STORE.get_all_mappings())
    #
    
    def fix_key(self, old_key, new_key):
        """
        Creates a new keeper instance by copying mappings except `old_key`.
        value mapped by `old_key` will be mapped by `new_key`.
        """
        if not self.does_contain(old_key):
            t = type(old_key)
            raise self.KeyNotFound("`{}` of {} is not in constant store.".format(old_key, t))
        
        
        value = self.STORE.get_value(old_key)
        
        new_keeper = WriteOnlyDictionary(self.store_func)
        
        old_keys = self.STORE.get_all_keys()
        
        for key in old_keys:
            if key == old_key:
                """ TODO(armaganslmn): double equals might cause problems.
                    Use .equals() maybe?"""
                new_keeper.put_key_value(new_key, value)
            #
            else:
                new_keeper.put_key_value(key, self.STORE.get_value(key))
            #
        #
        return new_keeper
    #
    
    def fix_value(self, KEY, new_value):
        """
        Creates a new keeper instance by copying mappings except `key`.
        value mapped by `key` will be changed to new_value.
        """
        #value = self.STORE.get_value(KEY)
        
        if not self.does_contain(KEY):
            t = type(KEY)
            raise self.KeyNotFound("`{}` of {} is not in constant store.".format(KEY, t))
        #
        
        new_keeper = WriteOnlyDictionary(self.store_func)
        
        old_keys = self.STORE.get_all_keys()
        
        for ky in old_keys:
            if ky == KEY:
                """ TODO(armaganslmn): double equals might cause problems.
                    Use .equals() maybe?"""
                new_keeper.put_key_value(ky, new_value)
            #
            else:
                new_keeper.put_key_value(ky, self.STORE.get_value(ky))
            #
        #
        return new_keeper
    #
    
    def create_keeper_from_mappings(self, iterable_of_mappings):
        new_keeper = WriteOnlyDictionary(self.store_func)
        
        for pair in iterable_of_mappings:
            new_keeper.put_pair(pair)
        #
        return new_keeper
    #
#

class KVStore:
    """
    This KVStore is for demonstration. You should choose how to implement
    the functions below according to your needs.
    For example, you can use a binary tree, array, linked list,
    custom hashmap etc.
    """
    def __init__(self):
        self.kv = dict()
    #
    
    def add(self, key, value):
        self.kv[key] = value
    #
    
    def does_contain(self, key):
        return key in self.kv
    #
    
    def get_all_mappings(self):
        return self.kv
    #
    
    def get_value(self, key):
        return self.kv.get(key)
    #
    
    def get_all_keys(self):
        return self.kv.keys()
    #
    
    def get_all_values(self):
        return self.kv.values()
    #
#

"""
MIT License

Copyright (c) 2021 Armağan Salman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
