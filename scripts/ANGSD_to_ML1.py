"""This is a script to transform a genotype matrix into one that can be used for machine learning

@authors: Adam Koller
@date: 3-5-2024
"""


import pandas as pd
from collections import Counter
import numpy as np
from sklearn.impute import SimpleImputer


def bases_to_number(bases: str, major_allele: str) -> int:
    if bases == "NN":
        return np.nan
    else:
        return (2 - bases.count(major_allele))


def ANGSD_to_ML1(filepath: str):
    """
    Transforms ANGSD genotype data to a matrix with 0s, 1s, and 2s
    based on recessive vs heterozygous vs dominant alleles

    param str filepath: filepath to the genotypes file (.csv)
    param pandas dataframe bamID_to_sampleID: dataframe linking bam IDs to sample IDs
    """
    df = pd.read_table(filepath, header=None)
    df = df.drop([0,1,458], axis=1).T
    df_meta = pd.read_csv('./data/results/counts_master.csv')
    replicates = ['105LC', '109LC','120RE','131LC', '806replicate','935replicate',
             'ucin024replicate','ucin236replicate','ucin261replicate','ucin279concreplicate',
             'ucin413replicate']
    df.index = df_meta['id']
    df = df.drop(replicates, axis='index')
    
    
    #df = pd.read_csv(filepath, index_col="id")
    major_alleles = []
    for column_name in df.columns:
        column = df[column_name].to_list()
        bases = "".join(column)
        allele_frequencies = dict(Counter(bases))
        major_allele = max(zip(allele_frequencies.values(), allele_frequencies.keys()))[
            1
        ]
        major_alleles.append(major_allele)

    for column_name, index in zip(df.columns, range(len(df.columns))):
        df[column_name] = df[column_name].apply(
            bases_to_number, major_allele=major_alleles[index]
        )

    mean_imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
    mat = mean_imputer.fit_transform(df)
    df_transformed = pd.DataFrame(mat)
    df_transformed.index = df.index

    return df_transformed


if __name__ == "__main__":

    # filepath = './data/genome/ncbi_dataset/data/GCA_032313775.1/GCA_032313775.1_UCinereo1.0_genomic.fna'
    df = ANGSD_to_ML1("./data/genotypes.csv")
    print(df)
