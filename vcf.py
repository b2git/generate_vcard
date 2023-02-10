import sys

num_contacts = int(input("请输入要生成多少个联系人："))
content = input("请输入要在vcf文件中生成的内容：")

vcard_template = """BEGIN:VCARD
VERSION:2.1
N:{};{};;;
FN:{} {}
TEL;CELL:0
EMAIL;HOME:{}
ADR;HOME:;;{};;;;
URL:{}
URL:{}
NOTE:{}
X-AIM:{}
X-MSN:{}
X-YAHOO:{}
X-SKYPE-USERNAME:{}
END:VCARD"""

with open("contacts.vcf", "w") as f:
    for i in range(num_contacts):
        vcard = vcard_template.format(content, content, content, content, content, content, content, content, content, content, content, content, content)
        f.write(vcard)
