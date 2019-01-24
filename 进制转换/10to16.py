#!/usr/bin/python
#encoding:utf-8

import sys
from workflow import Workflow3


def main(wf):
	query = wf.args[1]
	hex_num = hex(int(query, 10))
	hex_str= str(hex_num)[2:].upper()
	wf.add_item(
		title='10进制转16进制',
		subtitle=hex_str,
		valid=True,
		arg=hex_str
	)
	wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
