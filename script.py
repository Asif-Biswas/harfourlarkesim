import pandas as pd
import os

# set the path of the big CSV file
big_file = "npidata_pfile_20050523-20230212.csv"

# set the chunksize for reading the big file
chunksize = 10000

# set the name of the output folder for the split files
output_folder = "split"

# create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# read the big file in chunks and write each chunk to a separate CSV file
for i, chunk in enumerate(pd.read_csv(big_file, chunksize=chunksize)):
    # set the name of the output file for this chunk
    output_file = os.path.join(output_folder, f"split_{i+1:03d}.csv")
    # write the chunk to the output file
    chunk.to_csv(output_file, index=False)
