import hyperloglog, pickle, base64

blocks_log = None
def hyperloglog_init():
	global blocks_log
	try:
		print("Loading HLL from file")
		blocks_log_f = open("blocks_log.hll", "r")
		blocks_log = pickle.load(blocks_log_f)
	except (IOError, EOFError):
		print("Creating HLL")
		blocks_log_f = open("blocks_log.hll", "w")
		blocks_log = hyperloglog.HyperLogLog(0.01)
	blocks_log_f.close()

def hyperloglog_check(value):
	global blocks_log
	before = len(blocks_log)
	blocks_log.add(str(value))
	after = len(blocks_log)
	print "bef %s after %s" %(before, after)
	return before < after
def hyperloglog_save():
	blocks_log_f = open("blocks_log.hll", "w")
	pickle.dump(blocks_log, blocks_log_f)


hyperloglog_init()

print (hyperloglog_check(122314))

hyperloglog_save()

#blocks_already_processed = HyperLogLog(0.01)

# blocks_log.add("1232")
# print len(blocks_log)
#print base64.b64encode(pickle.dumps(hll))

# blocks_log_f.close()
# blocks_log_f = open("blocks_log.hll", "w")
# pickle.dump(blocks_log, blocks_log_f) #save HLL