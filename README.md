# Dynamic-Date-Animation
# Voting Animation

**Fun Project Story**

This project originated as a fun experiment when my teacher tasked me with selecting the two most interesting subjects from a pool of seven. Each student was allowed to choose their two favourite subjects through a voting process.

In the end, our ECE department would offer the two subjects with the highest votes. That's when I decided to leverage the power of Matplotlib to analyze and visualize the voting data.

## Project Background

- **Data Collection:** I gathered the voting data from my fellow students.
- **Data Filtering:** With the assistance of ChatGPT and Matplotlib, I processed and filtered the data to identify the most preferred subjects.
- **Visualization:** The project uses dynamic data animation with Matplotlib to visually represent the accumulation of votes over time.

It's a lighthearted project showcasing technology's creative use to address a simple yet interesting challenge. Feel free to explore, contribute, or use the code for your own projects!

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
![Gaph image](https://github.com/hemantkrishnan4/Dynamic-Date-Animation/assets/96692095/c59875e7-bd5c-4d65-b2cf-ca445b14443c)

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

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and share!

Happy coding! 🚀



