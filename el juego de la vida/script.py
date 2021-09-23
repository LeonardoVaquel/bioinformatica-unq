import random
import functools
# DESAFIO II
codigo_de_aminos = {
    'A': 'Ala',
    'T': 'Thr',
    'H': 'His',
    'R': 'Arg',
    'Y': 'Tyr',
    'F': 'Phe',
    'C': 'Cys',
    'G': 'Gly',
    'Q': 'Gly',
    'E': 'Glu',
    'D': 'Asp',
    'K': 'Lys',
    'L': 'Leu',
    'M': 'Met',
    'N': 'Asn',
    'S': 'Ser',
    'I': 'Iso',
    'W': 'Trp',
    'P': 'Pro',
    'V': 'Val'
}

codigo_genetico = {
    'Phe': ['UUU', 'UUC'],
    'Leu': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'Iso': ['AUU', 'AUC', 'AUA'],
    'Met': ['AUG'],
    'Val': ['GUU', 'GUC', 'GUA', 'GUG'],
    'Ser': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'Pro': ['CCU', 'CCC', 'CCA', 'CCG'],
    'Thr': ['ACU', 'ACC', 'ACA', 'ACG'],
    'Ala': ['GCU', 'GCC', 'GCA', 'GCG'],
    'Tyr': ['UAU', 'UAC'],
    'His': ['CAU', 'CAC', 'CAA', 'CAG'],
    'Asn': ['AAU', 'AAC'],
    'Lys': ['AAA', 'AAG'],
    'Asp': ['GAU', 'GAC'],
    'Glu': ['GAA', 'GAG'],
    'Cys': ['UGU', 'UGC'],
    'Try': ['UGG'],
    'Arg': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly': ['GGU', 'GGC', 'GGA', 'GGG']
}

def decodificar_a_amino(proteina):
    result = ''
    for amino in proteina:
        result = result + codigo_de_aminos[amino] + '_'
    return result.split('_')[:-1]


def decodificar_a_ARN(sec):
    result = ''
    for amino in sec:
        result = result + random.choice(codigo_genetico[amino]) + '_'
    return result.split('_')[:-1]


def decodificar(proteina):
    sec2 = decodificar_a_amino(proteina)
    sec3 = decodificar_a_ARN(sec2)
    return functools.reduce(lambda arn,codigo: arn + codigo, sec3, '')


sec1 = 'ATVEKGGKHKTGPNEKGKKIFVQKCSQCHTVLHGLFGRKTGQA'

print(decodificar(sec1))