#!/usr/bin/python
#encoding:utf-8

import sys
from workflow import Workflow3


def main(wf):
	query = wf.args[1]
	int_num = int(query, 16)
	wf.add_item(
		title='16进制转10进制',
		subtitle=int_num,
		valid=True,
		arg=int_num
	)
	wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
