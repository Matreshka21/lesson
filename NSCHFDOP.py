import xml.etree.ElementTree as ET

f = ET.parse("123.xml").getroot()
xpath = f.find('Документ/СвСчФакт')
print(xpath.get('НомерСчФ'))

xpath.set('НомерСчФ', 2)

print(xpath.get('НомерСчФ'))

