'''This is a script to count the number restriction enzyme cutsites in a genome. Requires the `re` module.

@authors: Adam Koller
@date: 2-16-2024
'''


import re


# Define a function to extract information and build a dictionary
def extract_info(block):
    # Use regular expressions to extract relevant information
    reads = int(re.search(r'(\d+) reads;', block).group(1))
    print(reads)
    
    print(re.search(r'(\d+) \(.*%\) aligned 0 times', block))
    aligned_0_times = int(re.search(r'(\d+) \(.*%\) aligned 0 times', block).group(1)
    
    print(re.search(r'(\d+\.\d+)% aligned 0 times', block))
    
    percent_aligned_0_times = float(re.search(r'(\d+\.\d+)% aligned 0 times', block).group(1))
    aligned_1_time = int(re.search(r'(\d+) \(.*%\) aligned exactly 1 time', block).group(1))
    percent_aligned_1_time = float(re.search(r'(\d+\.\d+)% aligned exactly 1 time', block).group(1))
    aligned_gt_1_time = int(re.search(r'(\d+) \(.*%\) aligned >1 times', block).group(1))
    percent_aligned_gt_1_time = float(re.search(r'(\d+\.\d+)% aligned >1 times', block).group(1))
    overall_alignment_rate = float(re.search(r'(\d+\.\d+)% overall alignment rate', block).group(1))

    # Build a dictionary with the extracted information
    result_dict = {
        'reads': reads,
        'aligned_0_times': aligned_0_times,
        'percent_aligned_0_times': percent_aligned_0_times,
        'aligned_1_time': aligned_1_time,
        'percent_aligned_1_time': percent_aligned_1_time,
        'aligned_gt_1_time': aligned_gt_1_time,
        'percent_aligned_gt_1_time': percent_aligned_gt_1_time,
        'overall_alignment_rate': overall_alignment_rate
    }

    return result_dict







def get_alignment_percent(alignment_file: str, maps_script_file: str, output_file: str):
    ids = []
    for line in open(maps_script_file):
        id = line[line.index('-U')+3: line.index('-S')-1].split('.')[0]
        ids.append(id)
    
    with open(alignment_file, 'r') as file:
        file_content = file.read()

    # Split the content into blocks using a regular expression
    blocks = re.split(r'\n(?=\d+ reads;)', file_content.strip())

    # Initialize an empty list to store dictionaries for each block
    result_list = []
    
    # Iterate through each block, extract information, and append to the result list
    for block in blocks:
        print(block)
        result_list.append(extract_info(block))

    # Print the resulting list of dictionaries
    for result in result_list:
        print(result)

        
        
            
    
    
if __name__ == '__main__':
    
    
    
    get_alignment_percent('./data/results/alignment.txt', './data/raw/merged/maps', './data/results/alignment_rates.csv/')
    