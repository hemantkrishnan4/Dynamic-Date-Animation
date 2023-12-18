import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Your list of votes
votes = [312, 312, 342, 322, 342, 342, 312, 312, 342, 312,
 372, 322, 362, 312, 342, 342, 362, 312, 372, 322, 342, 322,
  342, 322, 332, 362, 372, 332, 372, 312, 372, 312, 342, 342,
   362, 362, 372, 312, 372, 342, 322, 342, 312, 342, 332, 372,
    342, 372, 312, 322, 322, 372, 322, 342, 312, 342, 312, 332,
     342, 362, 312, 342, 322, 372, 312, 322, 312, 372, 312, 362
     , 312, 372, 322, 372, 322, 342, 312, 372, 342, 362, 312, 372,
      322, 362, 332, 372, 342, 362, 352, 372, 312, 332, 332, 342,
       322, 342, 342, 362, 322, 362]

# Unique numbers in the list
unique_numbers = list(set(votes))

# Map subject numbers to subject names
subject_names = {
    312: 'Digital System Design',
    322: 'Power Electronics',
    332: 'Data Analysis',
    342: 'Embedded Systems',
    352: 'Digital Image Processing',
    362: 'Introduction to MEMS',
    372: 'Quantum Computing'
}

# Order subjects based on the provided order
ordered_subjects = [subject_names[num] for num in unique_numbers]

# Decrease the size of the figure window by adjusting figsize
fig, ax = plt.subplots(figsize=(9, 6))
bars = ax.bar(ordered_subjects, [0] * len(unique_numbers))

# Set the y-axis limit to 100
ax.set_ylim(0, 50)

# Function to update the animation
def update(frame):
    votes_so_far = votes[:frame+1]
    vote_percentages = [votes_so_far.count(num) / len(votes_so_far) * 100 for num in unique_numbers]

    for bar, percentage in zip(bars, vote_percentages):
        bar.set_height(percentage)

    # Update x-axis ticks dynamically with improved layout
current_subjects = [subject_names[num] for num in unique_numbers]
ax.set_xticks(np.arange(len(current_subjects)))
ax.set_xticklabels(current_subjects, rotation=45, ha='right', va='top')

# Create the animation
animation = FuncAnimation(fig, update, frames=len(votes),repeat=False)

# Use the subplot configuration tool to adjust the bottom margin interactively
plt.subplots_adjust(bottom=0.241)

# Show the plot
plt.xlabel('Subjects')
plt.ylabel('Percentage of Votes (%)')
plt.title('Accumulation of Votes Over Time')
plt.tight_layout()
plt.show()
