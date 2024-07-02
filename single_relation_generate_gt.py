import csv

# Paths of the CSV files
input_file_path = r'D:\TA\coba 3\Grountruth_BussApp.csv'
output_file_path = r'D:\TA\coba 3\ProcessedGroundTruthBussApp.csv'

def remove_space(text):
    return text.replace(' ', '')

def notation_relation(notation):
    relationships = {
        'a': "AccessRelationship",
        'c': "CompositionRelationship",
        'f': "FlowRelationship",
        'g': "AggregationRelationship",
        'i': "AssignmentRelationship",
        'n': "InfluenceRelationship",
        'o': "AssociationRelationship",
        'r': "RealizationRelationship",
        's': "SpecializationRelationship",
        't': "TriggeringRelationship",
        'v': "ServingRelationship"
    }
    return relationships.get(notation, 'Unknown notation')

try:
    # Read the input CSV with semicolon delimiter
    with open(input_file_path, mode='r', newline='') as infile:
        reader = csv.reader(infile, delimiter=';')
        head = next(reader)  # Read the header
        print(head)  # Print the header

        output_data = [head]

        # Process each row
        for row in reader:
            print("Original row:", row)  # Print the original row
            source, relation, target = row

            source = remove_space(source)
            target = remove_space(target)

            print("Processed source:", source)  # Print the processed source
            print("Processed target:", target)  # Print the processed target
            for char in relation:
                char = notation_relation(char)
                output_data.append([source, char, target])

    # Write the output CSV
    with open(output_file_path, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(output_data)

    print(f"Success: {output_file_path} is generated")

except Exception as e:
    print(f"Error: {e}")
