import re
import io
import os

regex = r"<rec>(?P<Action>\t\t\t<.+)<[\/]rec>"
path = r'C:\Users\gutsko_i\Desktop\code'

xml_list = []
for file in os.listdir(path):
    if file.endswith(".xml"):
        xml_list.append(os.path.join(path, file))

processed_list_path = path + '\processed.list'

if 'processed.list' not in os.listdir(path):
    processed_list = open(processed_list_path, 'w+')
    processed_list.close    

processed_list = open(processed_list_path, 'r')
processed_list.seek(0)
xml_processed_list = processed_list.read().splitlines()
processed_list.close


for xml in xml_list:
    if xml not in xml_processed_list:
        file = io.open(xml, encoding='utf-8')
        file.seek(0)
        test_str = file.read()
        file.close
        test_str = test_str.replace('\n', '').replace('</rec>', '</rec>\n')
        matches = re.finditer(regex, test_str, re.MULTILINE)
        result = ""
        for matchNum, match in enumerate(matches, start=1):
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                result += ("{group}\n".format(group = match.group(groupNum)))                           

        result = result.replace('\t\t\t', '')

        file = open(xml, 'w')
        file.seek(0)
        file.write(result)
        file.close

        processed_list = open(processed_list_path, 'a')
        processed_list.seek(0)
        processed_list.write(xml + "\n")
        processed_list.close