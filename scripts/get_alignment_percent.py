'''This is a script to get the alignment rates for each sample from bowtie2 standard output

@authors: Adam Koller
@date: 3-22-2024
'''

import pandas as pd
import csv

def get_alignment_percent(alignment_file: str, maps_script_file: str, output_file: str):
    
    # Order of sample ID's as appeared in the `maps` file
    ids = [line.split(' ')[10].split('.')[0] for line in open(maps_script_file, 'r').readlines()]
    
    # Initialize dictionary
    alignment_dict = dict()
    for id in ids:
        alignment_dict[id] = {'reads': None,
                             'unpaired': None,
                             'aligned 0 times': None,
                             'aligned exactly 1 time': None,
                              'aligned >1 times': None,
                              'overall alignment rate': None
                             }
    
    # counter to ID
    counter_to_id = dict(zip(range(len(ids)), ids))
    
    # Specify the file name
    csv_file = './data/meta/bamID_to_sampleID.csv'

    # Writing to CSV
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for key, value in counter_to_id.items():
            writer.writerow([key, value])


    alignment = open(alignment_file, 'r')
    
    id_counter = 0
    field_count = 0
    
    for line in alignment.read().splitlines():
        
        id = counter_to_id[int(id_counter)]
        if field_count == 0:
            reads = line.split(' ')[0]
            alignment_dict[id]['reads'] = reads
        elif field_count == 1:
            unpaired = line.split(' ')[2]
            alignment_dict[id]['unpaired'] = int(unpaired)
        elif field_count == 2:
            aligned_0_times = line.split(' ')[5][1:-2]
            alignment_dict[id]['aligned 0 times'] = float(aligned_0_times)
        elif field_count == 3: 
            aligned_1_times = line.split(' ')[5][1:-2]
            alignment_dict[id]['aligned exactly 1 time'] = float(aligned_1_times)
        elif field_count == 4: 
            aligned_1plus_times = line.split(' ')[5][1:-2]
            alignment_dict[id]['aligned >1 times'] = float(aligned_1plus_times)
        elif field_count == 5: 
            overall = line.split(' ')[0][0:-1]
            alignment_dict[id]['overall alignment rate'] = float(overall)
        field_count = (field_count + 1) % 6
        id_counter += 1/6
        
    pd.DataFrame.from_dict(alignment_dict, orient='index').to_csv(output_file)
    
    
if __name__ == '__main__':
    
    
    
    get_alignment_percent('./data/results/alignment.txt', './data/raw/merged/maps', './data/results/alignment_rates.csv')
    