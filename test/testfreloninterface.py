import lima


print "Creating Espia.Dev"
edev = lima.Espia.Dev(0)

print "Creating Espia.Acq"
acq = lima.Espia.Acq(edev)

acqstat = acq.getStatus()
print "Whether the Acquisition is running : ", acqstat.running

print "Creating Espia.BufferMgr"
buffer_cb_mgr = lima.Espia.BufferMgr(acq)

print "Creating Espia.SerialLine"
espia_sl = lima.Espia.SerialLine(edev)


print "This is the End..."