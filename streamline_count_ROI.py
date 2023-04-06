import csv
import numpy as np
import nibabel as nib
from dipy.tracking import utils
from dipy.io.streamline import load_trk

# List of all .trk file names in your folder
trk_files = [
    'AnterioFrontalCC.trk',
    'ForcepsMajor.trk',
    'ForcepsMinor.trk',
    'LeftAnterioFrontoCerebellar.trk',  
    'RightAnterioFrontoCerebellar.trk'
]
#Path to your ROI, DWI, and the folder where your trk files respectfully
roi_file = '/Users/nando/Desktop/HCP_PMC/Subject_286650/pmc_seed.nii.gz'
ref_file = '/Users/nando/Desktop/HCP_PMC/Subject_286650/dwi/dwi.nii.gz'
trk_folder = '/Users/nando/Desktop/HCP_PMC/Subject_286650/'

roi_img = nib.load(roi_file)
roi_data = roi_img.get_fdata()
affine = np.linalg.inv(roi_img.affine)

# Function to process each .trk file
def process_trk_file(trk_file):
    streams = load_trk(trk_file, ref_file)

    selected_streams = []
    for sl in streams.streamlines:
        start = np.round(utils.apply_affine(affine, sl[0])).astype(np.int32)
        end = np.round(utils.apply_affine(affine, sl[-1])).astype(np.int32)

        if roi_data[tuple(start)] > 0 or roi_data[tuple(end)] > 0:
            selected_streams.append(sl)

    return len(selected_streams)

# Create a list to store the results
results = []

# Process each .trk file and add the results to the list
for trk_file in trk_files:
    trk_path = trk_folder + trk_file
    track_count = process_trk_file(trk_path)
    results.append((trk_file, track_count))

# Write the results to a CSV file
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['File', 'Track Count'])
    writer.writerows(results)
