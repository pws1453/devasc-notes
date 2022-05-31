#   Data Formats
Files following these formats generally have extensions that contain the name
*   xml - `.xml`
*   json - `.json`
*   yaml - `.yaml` OR `.yml`

##  XML
*   Looks a ton like HTML
*   Not HTML
*   XML Version and Encoding are required in prologue
*   Structure of body - tree
*   Tag names are user-defined
    *   Can be repeated for many items
*   Encoding - HARD
    *   XSS can **still** be done if XML is used in web
    *   Sometimes, use the numerical representation of the character
    *   [Reference Material for Character References]
*   Attributes
    *   Can add attributes to the tag to include metadata
    *   Values must be in single of double quotes
*   Namespaces
    *   Some documents must include namespaces to specify specific tags and purposes
    *   Use the `xmlns` attribute to denote this
*   Comments - `<!-- surround comments here-->`


##  JSON
*   Looks like a python dictionary
*   JSON DOES NOT SUPPORT COMMENTS
*   Lists can be written similarly to python lists or javascript arrays


##  YAML
*   Becoming increasingly common
*   YAML is a type of JSON made to be read by humans
*   JSON can be embedded in YAML
    *   Escape quotes with `\"`
*   Data Types
    *   Strings
    *   Booleans
    *   Nulls
    *   Floats
    *   Doubles
*   Indentation denotes hierarchy
    *   A tag indented within another tag is an attribute of that tag
    *   UNLESS Prefixed by a `-`, then it denotes a part of a list used as a value

##  Fun Examples
### XML
```
<?xml version="1.0" encoding="UTF-8"?>
<!-- Instance list -->
<vms>
  <vm vmid="0101af9811012" type="t1.nano" />
  <vm vmid="0102bg8908023" type="t1.micro"/>
</vms>
```
### JSON

```
{
  "edit-config":
  {
    "default-operation": "merge",
    "test-operation": "set",
    "some-integers": [2,3,5,7,9],
    "a-boolean": true,
    "more-numbers": [2.25E+2,-1.0735],
  }
}
```

### YAML

```
edit-config:
  a-boolean: true
  default-operation: merge
  more-numbers:
  - 225.0
  - -1.0735
  some-integers:
  - 2
  - 3
  - 5
  - 7
  - 9
  test-operation: set`
```
<!-- LINKS -->
[Reference Material for Character References]:<https://dev.w3.org/html5/html-author/charref>