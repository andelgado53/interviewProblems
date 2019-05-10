
meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
expected_return = [(0, 1), (3, 8), (9, 12)]

def merge_two_meetings(first_meeting, second_meeting):
	if first_meeting[1] >= second_meeting[0]:
		return (first_meeting[0], max(first_meeting[1], second_meeting[1]))
	return None

def merge_meetings(meetings):
	meetings = sorted(meetings)
	# print(meetings)
	merged_meetings  = []
	next_index = 1
	if len(meetings) <= 1:
		return meetings

	previous_meeting = meetings[0]
	while next_index < len(meetings):
		new_meeting = merge_two_meetings(previous_meeting, meetings[next_index])
		if new_meeting:
			previous_meeting = new_meeting
		else:
			merged_meetings.append(previous_meeting)
			previous_meeting = meetings[next_index]
		next_index +=1
	if previous_meeting:
		merged_meetings.append(previous_meeting)

	return merged_meetings
	

# print(merge_two_meetings((1, 3), (2, 4)))

print(merge_meetings(meetings))

print(merge_meetings([(1, 10), (2, 6), (3, 5), (7, 9)]))

# print(merge_meetings([(0,1)]))
# print(merge_meetings([(0,1), (0,1)]))