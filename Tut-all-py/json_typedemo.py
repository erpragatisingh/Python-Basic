print("JSON (JavaScript Object Notation), specified by RFC 7159 (which obsoletes RFC 4627) \nand by ECMA-404, is a lightweight data interchange format inspired by JavaScript object literal syntax (although it is not a strict subset of JavaScript [1] ).\njson exposes an API familiar to users of the standard library marshal and pickle modules.\nEncoding basic Python object hierarchies:")
import json
print(json.dumps([1, 'simple', 'list']))
print("test")
j=json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(j)
print(json.dumps("\"foo\bar"))
print(json.dumps('\u1234'))
print(json.dumps('\\'))
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))



from io import StringIO

io = StringIO()
json.dump(['streaming API'], io)
print(io.getvalue())

#compact encoding

print(json.dumps([1,2,3,{'4': 5, '6': 7}], separators=(',', ':')))
# formated printing
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
