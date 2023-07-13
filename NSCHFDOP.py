import xml.etree.ElementTree as ET

f = ET.parse("123.xml").getroot()
xpath = f.find('Документ/СвСчФакт')
print(xpath.get('НомерСчФ'))

xpath.set('НомерСчФ', '2')
xpath.set('ДатаСчФ', '10.10.2010')
xpath.set('КодОКВ', '123')

xpath1 = f.find('Адрес/Индекс')
xpath.set('Индекс', '214013')

xpath1 = f.find('Документ/СвСчФакт/СвПрод/Адрес/АдрРФ')
xpath1.set('Индекс', '214013')

print(xpath.get('НомерСчФ'))

f = ET.ElementTree(f)
f.write('new_nschfdop.xml', encoding='utf-8')

