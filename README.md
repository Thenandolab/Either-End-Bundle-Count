# Tractography ROI Analysis

This Python script loads a list of tractography (.trk) files, applies a region of interest (ROI) mask to them, and counts the number of streamlines that intersect the ROI. The results are then written to a CSV file.

## Requirements
- Python 3
- `numpy`
- `nibabel`
- `dipy`

## Usage
1. Clone or download the repository to your local machine.
2. Open a terminal and navigate to the directory containing the script and input data.
3. Modify the file paths in the script to match the location of your input files.
4. Run the script by typing `python tractography_ROI_analysis.py` in the terminal.
5. The script will generate a CSV file named `output.csv` containing the results.

## Input Data
The script requires the following input data:
- A list of `.trk` files to analyze.
- An ROI mask in NIfTI format (`.nii.gz`) defining the region of interest.
- A reference diffusion-weighted image in NIfTI format (`.nii.gz`) matching the resolution and orientation of the `.trk` files.

## Output Data
The script generates a CSV file named `output.csv` containing the results of the analysis. Each row of the CSV file corresponds to one of the input `.trk` files and includes the following columns:
- `File`: the name of the input `.trk` file.
- `Track Count`: the number of streamlines that intersect the ROI.

## License
This script is released under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgements
This script was created by Fernando Aguilar Ortega as part of research conducted at the Sarah Heilbronner Lab. If you use this script in your research, please cite [relevant publications] and acknowledge the [funding sources].
