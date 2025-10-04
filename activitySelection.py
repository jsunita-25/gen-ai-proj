def activity_selection(activities):
    # Sort activities based on their finish time
    activities.sort(key=lambda x: x[1])
    
    # The first activity is always selected
    selected_activities = [activities[0]]
    
    # Iterate over the activities to select non-overlapping ones
    for i in range(1, len(activities)):
        if activities[i][0] >= selected_activities[-1][1]:
            selected_activities.append(activities[i])
    
    return selected_activities

# Example usage:
activities = [(1, 3), (2, 5), (4, 6), (6, 7)]
result = activity_selection(activities)
print(f"Selected Activities: {result}")
