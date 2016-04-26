VAL_IDX = 0
INCR_IDX = 1
DECR_IDX = 2
TREND_INC = 1
TREND_DEC = 2

def upvote(votes, n, k):
	result = []
	icount = dcount = 0

	candidate = []
	candidate.append([votes[0], 0, 0])
	for i in range(1,k):
		inc = 0
		dec = 0
		if votes[i]>votes[i-1]:
			inc=1+candidate[i-1][INCR_IDX]
			icount+=inc
		elif votes[i]<votes[i-1]:
			dec=1+candidate[i-1][DECR_IDX]
			dcount+=dec
		else:
			dec=1+candidate[i-1][DECR_IDX]
			dcount+=dec
			inc=1+candidate[i-1][INCR_IDX]
			icount+=inc

		candidate.append([votes[i], inc, dec])
	result.append(icount-dcount)
	#print 'result:',result
	i=k
	while i<n:
		#eliminating the first record from the candidate array.
		#print '\nidx:',i,' val:',votes[i] 
		trend = TREND_DEC
		if candidate[1]>candidate[0]:
			trend = TREND_INC
		count = get_count(candidate, trend, k)

		if trend==TREND_INC:
			icount-=count
		else:
			dcount-=count
		#print 'count:',count,' icount:',icount, ' dcount:',dcount
		inc = 0
		dec = 0
		candidate.pop(0)
		if votes[i]>votes[i-1]:
			inc=1+candidate[-1][INCR_IDX]
			icount+=inc
		elif votes[i]<votes[i-1]:
			dec=1+candidate[-1][DECR_IDX]
			dcount+=dec
		else:
			inc=1+candidate[-1][INCR_IDX]
			icount+=inc
			dec=1+candidate[-1][DECR_IDX]
			dcount+=dec
			
		candidate.append([votes[i], inc, dec])
		#print_candidate(candidate)
		#print 'icount',icount, ' dcount',dcount
		result.append(icount-dcount)
		i+=1
	return result

def print_candidate(can):
	for c in can:
		print c

def get_count(candidate, req_trend, k):
	count = 0
	for i in range(k-1):
		if candidate[i+1][VAL_IDX]-candidate[i][VAL_IDX]>0:
			trend = TREND_INC
		else:
			trend = TREND_DEC
		if not trend==req_trend:
			break
		count+=1
		candidate[i+1][req_trend]-=1
	return count

if __name__=="__main__":
	votes = [3,4,2,1,5,7,8,6]
	n = len(votes)
	k = 3
	res = upvote(votes, n, k)
	print res

