import gooey
import sys

@gooey.Gooey(program_name="VCard 生成器")
def main():
    import argparse

    parser = argparse.ArgumentParser(description="生成 Vcard 文件")
    parser.add_argument("--content", type=str, help="填写需要在 Vcard 中插入的字符")
    parser.add_argument("--number", type=int, help="需要生成的联系人数量")
    args = parser.parse_args()

    vcard_content = args.content
    number_of_entries = args.number
    vcard = "BEGIN:VCARD\nVERSION:2.1\n"

    for i in range(number_of_entries):
        vcard += "N:{0};{0};;;\n".format(vcard_content)
        vcard += "FN:{0} {0}\n".format(vcard_content)
        vcard += "TEL;CELL:0\n"
        vcard += "EMAIL;HOME:{}\n".format(vcard_content)
        vcard += "ADR;HOME:;;{};;;;\n".format(vcard_content)
        vcard += "URL:{}\n".format(vcard_content)
        vcard += "URL:{}\n".format(vcard_content)
        vcard += "URL:{}\n".format(vcard_content)
        vcard += "URL:{}\n".format(vcard_content)
        vcard += "NOTE:{}\n".format(vcard_content)
        vcard += "X-AIM:{}\n".format(vcard_content)
        vcard += "X-MSN:{}\n".format(vcard_content)
        vcard += "X-YAHOO:{}\n".format(vcard_content)
        vcard += "X-SKYPE-USERNAME:{}\n".format(vcard_content)
        vcard += "END:VCARD\n"

    with open("vcard.vcf", "w") as f:
        f.write(vcard)

if __name__ == '__main__':
    main()
