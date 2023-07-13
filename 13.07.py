import xml.etree.ElementTree as ET

root = ET.Element('Страна')
appt = ET.Element('Город')
root.append(appt)

begin = ET.SubElement(appt, 'Индекс')
begin.text = '214000'

name = ET.SubElement(appt, 'Название_города')
name.text = 'Смоленск'

street = ET.SubElement(appt, 'Улица')
street.text = 'Ленина'

tree=ET.ElementTree(root)
ET.indent(tree)
tree.write ('new.xml', encoding='utf-8')


