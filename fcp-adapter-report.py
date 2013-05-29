#!/usr/local/python-2.7.2/bin/python
##
#
# A simple fcp adapter stats report
# Using Netapp API and Python
#
# Blake Golliher - blakegolliher@gmail.com
#
##

import sys
sys.path.append("/var/local/netapp-manageability-sdk-5.1/lib/python/NetApp")
from NaServer import *
import getpass

password = getpass.getpass()

filer_name = sys.argv[1]

filer = NaServer(filer_name,1,6)
filer.set_admin_user('root', 'password')
cmd = NaElement("fcp-adapter-stats-list-info")
ret = filer.invoke_elem(cmd)

if(ret.results_status() == "failed"):
  print "%s failed." % filer_name
	print(ret.results_reason() + "\n")
	sys.exit(2)

status = ret.child_get("fcp-adapter-stats")

if(status == None):
	print "status_children_get was empty\n"
	sys.exit(2)
else:
	result = status.children_get()

for fcpinfo in result:
	print "FCP Adapter Name : %s " % fcpinfo.child_get_string("adapter")
	print "	Adapter Resets  	: %s 		CRC Errors 		: %s " % (fcpinfo.child_get_string("adapter-resets"), fcpinfo.child_get_string("crc-errors"))
	print "	discarded-frames	: %s 		Frame Overruns 		: %s " % (fcpinfo.child_get_string("discarded-frames"), fcpinfo.child_get_string("frame-overruns"))
	print "	frame-underruns		: %s 		Invalid Xmit Words 	: %s " % (fcpinfo.child_get_string("frame-underruns"), fcpinfo.child_get_string("invalid-xmit-words"))
	print "	link-breaks		: %s 		Lip Resets		: %s " % (fcpinfo.child_get_string("link-breaks"), fcpinfo.child_get_string("lip-resets"))
	print "	protocol-errors		: %s 		Queue Depth		: %s " % (fcpinfo.child_get_string("protocol-errors"), fcpinfo.child_get_string("queue-depth"))
	print "	scsi-requests-dropped	: %s 		SFP Connector		: %s " % (fcpinfo.child_get_string("scsi-requests-dropped"), fcpinfo.child_get_string("sfp-connector"))
