import xml.etree.ElementTree as ET

xsd = ET.parse('bookstore.xsd')
xml = ET.parse('bookstore.xml')
# root = xml.getroot()
# print(root)
# for i in root:
#     print(i.tag, i.attrib)
#     for j in i:
#         print(j)

valid_tags = [
    'all', 'annotation', 'any', 'anyAttribute', 'appInfo', 'attribute', 'attributeGroup', 'choice', 'complexContent', 'complexType', 'documentation', 'element', 'extension', 'field', 'group', 'import', 'include', 'key', 'keyref', 'list', 'notation', 'redefine', 'restriction', 'schema', 'selector', 'sequence', 'simpleContent', 'simpleType', 'union', 'unique'
]

valid_restritions = [
    'enumeration',
    'fractionDigits',
    'length',
    'maxExclusive',
    'maxInclusive',
    'maxLength',
    'minExclusive',
    'minInclusive',
    'minLength',
    'pattern',
    'totalDigits',
    'whiteSpace'
]

root = xsd.getroot()
print(root)
for i in root:
    # print(i.tag, i.attrib)
    print(i.tag)
    if i.tag == '{http://www.w3.org/2001/XMLSchema}complexType':
        print('WTF')
    # for j in i:
        # print(j)