"""
    Copyright info can be found in LICENSE.txt or
    at the end of this document.
"""

import write_only_dictionary as WRD

k = WRD.WriteOnlyDictionary(WRD.KVStore)
k.put_key_value("ok", 555)
k.put_key_value("settt", {2,3,4,5,5,5,6})
k.put_key_value(571, ("new", "power"))
#k.put_key_value(571, ("new", "power"))
#k.add_key_value("ok", True)
print(k.get_value("ok"))
print(k.get_all_mappings())
print(WRD.WriteOnlyDictionary.KeyExists)

l = k.fix_key("ok", "pk")

print("All mappings: {}".format(k.get_all_mappings()))
print("All keys: {}".format(k.get_all_keys()))
print("All values: {}".format(k.get_all_values()))

print("\nAll mappings: {}".format(l.get_all_mappings()))
print("All keys: {}".format(l.get_all_keys()))
print("All values: {}".format(l.get_all_values()))

l = l.fix_value("pk", 666)

print("\nAll mappings: {}".format(l.get_all_mappings()))
print("All keys: {}".format(l.get_all_keys()))
print("All values: {}".format(l.get_all_values()))

l = l.create_keeper_from_mappings(l.get_all_mappings().items())
M = l

print("\nAll mappings: {}".format(l.get_all_mappings()))
print("All keys: {}".format(l.get_all_keys()))
print("All values: {}".format(l.get_all_values()))



l = l.create_keeper_from_mappings([(1,2), (2,3), (3,4)])

DC = l.get_all_mappings()

DC["pk"] = None

print("\nAll mappings: {}".format(M.get_all_mappings()))
print("All keys: {}".format(M.get_all_keys()))
print("All values: {}".format(M.get_all_values()))

print("\nAll mappings: {}".format(l.get_all_mappings()))
print("All keys: {}".format(l.get_all_keys()))
print("All values: {}".format(l.get_all_values()))

print("\nAll is well.")

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
