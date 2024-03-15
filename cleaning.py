import re

# Function to process each statement
def process_statement(statement):
    # Extract the conversation from the statement
    #statement2 = statement.replace("\n", "")
    #print(statement2)
    # statement2=statement.replace("\\nCustomer:", "")
    #print(statement2)
    #con=re.compile(r'Actual Conversation:\'\'\'\\nCustomer: (.*)?\'\'\'')
    #conversation_match = re.search(r'Actual Conversation:\'\'\'(.*)?\'\'\'',con, re.DOTALL)
    conversation_match = re.search(r'declared by the customer(.*)?nInformation',statement, re.DOTALL)
    #conversation_match=con.search(statement)
    if conversation_match:
        actual_conversation = conversation_match.group().strip()
    else:
        actual_conversation = ""
    #print(actual_conversation)

    # Extract the response content from the statement
    response_match = re.search(r'response: content=\'(.*?)\'', statement)
    if response_match:
        response_content = response_match.group(1).strip()
    else:
        response_content = ""

    # Construct the desired output
    output = f"<s>[INST] {actual_conversation} [/INST] Content='{response_content}'</s>"

    return output

# Input and output file paths
input_file_path = "uf_extractor.log"  # Replace with the actual path to your input file
output_file_path = "output.txt"  # Replace with the desired path for the output file

# Read statements from the input file
with open(input_file_path, "r", encoding="utf-8") as input_file:
    statements = input_file.read().split("===END=====user_field_extractor=====")

# Process each statement and store the results in a list
processed_results = [process_statement(statement) for statement in statements]

# Write the results to the output file
with open(output_file_path, "w", encoding="utf-8") as output_file:
    for result in processed_results:
        output_file.write(result + "\n")
