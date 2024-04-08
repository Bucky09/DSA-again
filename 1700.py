from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        dq_st, dq_sa = deque(students), deque(sandwiches)
        counter = 0
        while dq_st:
            if counter == len(dq_st):
                break

            cur_st = dq_st.popleft()
            if cur_st == dq_sa[0]:
                dq_sa.popleft()
                counter = 0
            else:
                dq_st.append(cur_st)
                counter += 1
        return len(dq_st)
