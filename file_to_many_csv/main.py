#for the manual addition of Enteries, we need lookup files
#each file has a key  : the name
#                value: the column
#add a csv file containing new enteries and their enrichement data
#in the same directory as the script
#baiscally turns one large csv into little ones
import csv
import os

def split_csv(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True) #create output dir if not existant

    with open(input_file, mode='r', newline='', encoding='unicode_escape') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Read the header row

        # Ensure there are at least two columns
        if len(headers) < 2:
            print("The CSV file must have at least two columns.")
            return

        # Create a writer for each column (except the first column)
        writers = {}
        files = {}
        for i, header in enumerate(headers[1:], start=1):
            output_file = os.path.join(output_dir, f"{header.replace('�','').replace('#','').strip().replace(' ','_')}_Enrich_Lookup.csv")
            files[header] = open(output_file, mode='w', newline='', encoding='utf-8')
            writers[header] = csv.writer(files[header])

            writers[header].writerow(["key", "value"])

        # Write rows to the corresponding files
        for row in reader:
            key = row[0]
            for i, header in enumerate(headers[1:], start=1):
                writers[header].writerow([key, row[i]])

        for file in files.values():
            file.close()

input_csv = 'input.csv'  
output_directory = 'output_files'  
split_csv(input_csv, output_directory)

