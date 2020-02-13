#!./usr/bin/env.python
# .-*- coding: utf-8 -*-
# ._author_.=."me7dog7"

ruleList = [
    '{sub}{domain}',
    '{domain}{sub}',
    '{sub}{rule}{domain}',
    '{domain}{rule}{sub}',
    '{domain}.{sub}',
    '{sub}.{domain}'
]
ruleData = [
    '-',
    '.',
    '_'
]

def main(domain, lines):
    with open('subname.txt') as inFile:
        for line in inFile.xreadlines():
            sub = line.strip()
            if not sub or sub in lines:
                continue
            for rule in ruleList:
                for i in ruleData:
                    rule = rule.replace('{sub}', sub)
                    rule = rule.replace('{domain}', domain)
                    rule = rule.replace('{rule}', i)
                lines.add(rule)
    return lines


if __name__ == '__main__':
    domainList = set()
    lines = set()
    with open('domain.txt') as inFile:
        for line in inFile.xreadlines():
            domain = line.strip()
            domainList.add(domain)

    for i in domainList:
        if i.strip():
            main(i[:i.rfind(".", 0, i.rfind('.'))], lines)
    with open(r'ruleSub.txt', 'w') as ff:
        for i in lines:
            ff.write(i + '\n')
