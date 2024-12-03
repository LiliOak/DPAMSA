import os
import csv

dataset_folder = "unaligned_sequences_csv_mini_60_8_10"

def load_sequences(file_name):
    sequences = []
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            sequences.append(row[0])  # Assuming each row has one sequence
    return sequences

datasets = []
for filename in os.listdir(dataset_folder):
    if filename.endswith(".csv"):
        dataset_name = filename.split("_")[0]
        file_path = os.path.join(dataset_folder, filename)
        
        datasets.append([dataset_name, load_sequences(file_path)])

file_name = "Human EvolveAGene Dataset"  


