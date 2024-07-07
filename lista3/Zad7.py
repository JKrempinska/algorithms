import re

def check_tags(path):
    with open('unpaired_tags.txt') as u:
        unpaired = u.readlines()
    for i in range(len(unpaired)):
        unpaired[i] = unpaired[i].replace('\n','')

    with open(path) as f:
        content = f.readlines()

    tags_pattern = "<(\"[^\"]*\"|'[^']*'|[^'\">])*>"
    tag_match = re.compile(tags_pattern)
    errors = 0
    for i in range(len(content)):
        match = re.search(tag_match,content[i])
        if match:
            if re.findall(unpaired[0], match.group()):
                i += 1
            else:
                unpaired_tags = 0
                for j in range(1,len(unpaired)):
                    is_unpaired = re.findall(unpaired[j], match.group())
                    if is_unpaired:
                        unpaired_tags += 1
                if unpaired_tags != 0:
                    i += 1
                else:
                    tag = match.group()
                    if tag[1] == '/':
                        tag = tag.replace('/','')
                        tag = tag.replace('>','')
                        tag = tag.lower()
                        counter = 0
                        for k in range(i):
                            content[k] = content[k].lower()
                            is_tag_open = re.findall(tag, content[k])
                            if is_tag_open:
                                counter += 1
                        if counter == 0:
                            print(content[i])
                            errors += 1
                    else:
                        tag = tag.replace('=',' ')
                        head, sep, tail = tag.partition(' ')
                        head = head.replace('<','')
                        head = head.replace('>','')
                        head = head.lower()
                        tag = '</' + head + '>'
                        counter = 0
                        for k in range(i,len(content)):
                            content[k] = content[k].lower()
                            is_tag_closed = re.findall(tag, content[k])
                            if is_tag_closed:
                                counter += 1
                        if counter == 0:
                            print('Brak zamknięcia tagu:',content[i])
                            errors += 1
        else:
            i += 1
    print(errors)
    if errors != 0:
        pass
    else:
        print('Wszystko dobrze')
            
check_tags('sample2.txt')
