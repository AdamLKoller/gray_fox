'''This is a script to count the number restriction enzyme cutsites in a genome. Requires the `re` module.

@authors: Adam Koller
@date: 2-16-2024
'''


import re

def count_cutsites(filepath: str, target_regex: str, cut_length: int) -> int:
    '''
    Counts the number of cutsites of inputted enzyme found in a genome
    
    param str filepath: filepath to the genome file (.fna or .fasta)
    param str target_regex: regex pattern for the enzyme ex. Bcg1 =  'GCA.{6}TCG|CGA.{6}TGC'
    param str cut_length: length of the fragment (bp)
    '''
    
    file = open(filepath, 'r')
    print('Storing genome...')
    genome = ''.join([line.rstrip() for line in open(filepath)])
    pattern = re.compile(target_regex, re.IGNORECASE)
    print('Finding sites... (this may take 2-5 minutes)')
    matches = re.findall(pattern, genome)
    print(f'{len(matches)} instances of the {target_regex} pattern covering {round(len(matches)*cut_length/len(genome)*100, 4)}% of the genome')
    return len(matches)
    
    
if __name__ == '__main__':
    
    filepath = './data/genome/ncbi_dataset/data/GCA_032313775.1/GCA_032313775.1_UCinereo1.0_genomic.fna'
    #filepath = '../DeerProject/genome/genome.fasta'
    target_regex = '.[GA].{10}GCA.{6}TCG.{10}C.|.[GA].{10}CGA.{6}TGC.{10}C.' 
    #target_regex = 'GCA.{6}TCG|CGA.{6}TGC'
    cut_length = 36
    
    count_cutsites(filepath, target_regex, cut_length)