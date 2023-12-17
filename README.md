﻿# Dynamic-Date-Animation
# Voting Animation

This project creates a dynamic animation that shows the accumulation of votes over time for different subjects. The data is represented using a bar chart where the x-axis represents different subjects, and the y-axis represents the percentage of votes each subject receives.

## Getting Started

To run the animation, make sure you have Python and the required libraries installed. You can install the necessary libraries using the following command:

```bash
pip install matplotlib numpy
```
After installing the dependencies, you can run the animation script:
```bash
python voting_animation.py
```
## Configuration
- The list of votes is provided in the `votes` variable.
- Subject numbers are mapped to subject names in the `subject_names` dictionary.
- The order of subjects is defined in the `ordered_subjects` list.

## Customization
You can customize the animation by adjusting parameters in the script:

- Modify the `figsize` parameter in the `plt.subplots(figsize=(8, 6))` line to change the size of the figure.
- Adjust animation parameters, such as speed and frames, based on your preferences.

## Contributing
Feel free to contribute to this project by opening issues or creating pull requests. Your feedback and improvements are welcome!

## Open Source
This project is open to all. Feel free to use, modify, and distribute the code as needed.


