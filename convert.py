import csv

# Input and output file paths
input_file_path = 'output.txt'
output_file_path = 'output1.csv'

# Open input and output files with 'utf-8' encoding
with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
    # Create a CSV writer
    csv_writer = csv.writer(output_file)

    # Write header to the CSV file
    csv_writer.writerow(['Text', 'Content'])

    # Process each line in the input file
    for line in input_file:
        # Split the line into two parts using "Content=" as the separator
        parts = line.split('Content=')

        # Check if the line has the expected structure
        if len(parts) == 2:
            text_part = parts[0].strip()
            content_part = 'Content=' + parts[1].strip()

            # Write the two parts as separate rows to the CSV file
            csv_writer.writerow([text_part, content_part])

print(f'Conversion complete. CSV file written to: {output_file_path}')

