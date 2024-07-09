class Solution:
    def averageWaitingTime(self, cust: List[List[int]]) -> float:
        n = len(cust)
        wait = 0
        e= -maxsize
        for val in cust:
            arrive , time = val
            if arrive < e: # no one shows up at -9gazillion
            # so we use this to determine if this is their first time or not
                wait +=e -arrive +time
                e+= time
            else:
                wait += time
                e = arrive + time
        return wait/n
