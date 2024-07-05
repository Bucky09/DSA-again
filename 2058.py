class Solution:

	def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
		critical_idx, idx, a, b, c = [], 0, -1, -1, -1
		while head:
			idx += 1
			a, b, c = b, c, head.val
			if idx >= 3 and (a < b > c or a > b < c):
				critical_idx.append(idx)
			head = head.next

		if len(critical_idx) < 2:
			return [-1, -1]

		min_dist = inf
		for a, b in zip(critical_idx, critical_idx[1:]):
			if (d:= b - a) < min_dist:
				min_dist = d
		return [min_dist, critical_idx[-1] - critical_idx[0]]
