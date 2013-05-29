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
	print "	Adapter Resets  : %s " % fcpinfo.child_get_string("adapter-resets")
	print "	CRC Error Count : %s " % fcpinfo.child_get_string("crc-errors")
	print "	discarded-frames: %s " % fcpinfo.child_get_string("discarded-frames")
	print "	frame-overruns: %s " % fcpinfo.child_get_string("frame-overruns")
	print "	frame-underruns: %s " % fcpinfo.child_get_string("frame-underruns")
	print "	initiators-connected: %s " % fcpinfo.child_get_string("initiators-connected")
	print "	invalid-xmit-words: %s " % fcpinfo.child_get_string("invalid-xmit-words")
	print "	is-sfp-diagnostics-internally-calibrated: %s " % fcpinfo.child_get_string("is-sfp-diagnostics-internally-calibrated")
	print "	is-sfp-optical-transceiver-valid: %s " % fcpinfo.child_get_string("is-sfp-optical-transceiver-valid")
	print "	is-sfp-rx-power-in-range: %s " % fcpinfo.child_get_string("is-sfp-rx-power-in-range")
	print "	is-sfp-tx-power-in-range: %s " % fcpinfo.child_get_string("is-sfp-tx-power-in-range")
	print "	link-breaks: %s " % fcpinfo.child_get_string("link-breaks")
	print "	lip-resets: %s " % fcpinfo.child_get_string("lip-resets")
	print "	lr-received: %s " % fcpinfo.child_get_string("lr-received")
	print "	lr-sent: %s " % fcpinfo.child_get_string("lr-sent")
	print "	nos-received: %s " % fcpinfo.child_get_string("nos-received")
	print "	ols-received: %s " % fcpinfo.child_get_string("ols-received")
	print "	protocol-errors: %s " % fcpinfo.child_get_string("protocol-errors")
	print "	queue-depth: %s " % fcpinfo.child_get_string("queue-depth")
	print "	scsi-requests-dropped: %s " % fcpinfo.child_get_string("scsi-requests-dropped")
	print "	sfp-connector: %s " % fcpinfo.child_get_string("sfp-connector")
	print "	sfp-date-code: %s " % fcpinfo.child_get_string("sfp-date-code")
	print "	sfp-encoding: %s " % fcpinfo.child_get_string("sfp-encoding")
	print "	sfp-fc-speed-capabilties: %s " % fcpinfo.child_get_string("sfp-fc-speed-capabilties")
	print "	sfp-formfactor: %s " % fcpinfo.child_get_string("sfp-formfactor")
	print "	sfp-part-number: %s " % fcpinfo.child_get_string("sfp-part-number")
	print "	sfp-rev: %s " % fcpinfo.child_get_string("sfp-rev")
	print "	sfp-rx-power: %s " % fcpinfo.child_get_string("sfp-rx-power")
	print "	sfp-serial-number: %s " % fcpinfo.child_get_string("sfp-serial-number")
	print "	sfp-tx-power: %s " % fcpinfo.child_get_string("sfp-tx-power")
	print "	sfp-vendor-name: %s " % fcpinfo.child_get_string("sfp-vendor-name")
	print "	sfp-vendor-oui: %s " % fcpinfo.child_get_string("sfp-vendor-oui")
	print "	sfp-wavelength: %s " % fcpinfo.child_get_string("sfp-wavelength")
	print "	spurious-interrupts: %s " % fcpinfo.child_get_string("spurious-interrupts")
	print "	total-logins: %s " % fcpinfo.child_get_string("total-logins")
	print "	total-logouts: %s " % fcpinfo.child_get_string("total-logouts")
