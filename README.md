# 22I2072_BD_Assignment2
# Members:
Muhammad Subhan 22i-2024
Hamza Asad   22i-1908
Emad Iqbal 22i-2072

The objective of this project is to develop a basic search engine using Apache Hadoop's MapReduce framework. The project aims to address the challenges of handling large amounts of textual data efficiently while ensuring low-latency responses to user queries. The report provides a comprehensive overview of the development process, including data preprocessing, indexing, and query processing, along with the technologies used and the rationale behind design decisions.
# Libraries used:
import sys
import re
from collections import Counter
import math
    • import sys: This statement imports the sys module, which provides access to system-specific parameters and functions. It is commonly used for interacting with the Python interpreter and the system environment.
    • import re: This statement imports the re module, which provides support for regular expressions in Python. Regular expressions are used for pattern matching and text manipulation.
    • from collections import Counter: This statement imports the Counter class from the collection’s module. Counter is a specialized container data type in Python used for counting the occurrences of elements in an iterable.
    • import math: This statement imports the math module, which provides mathematical functions and constants. It is commonly used for mathematical operations in Python.
Search Engine Development utilizing MapReduce

   # 1. Load reducer function/file
    1. def load_reducer_output(file_path): This line defines a function named load_reducer_output that takes a file path (file_path) as an argument.
    2. out_data = {}: Initializes an empty dictionary out_data to store the data read from the file.
    3. with open(file_path, 'r') as out_file:: Opens the specified file (file_path) in read mode ('r') using a context manager. The context manager ensures that the file is properly closed after its suite finishes, even if an exception occurs.
    4. for line in out_file: Iterates over each line in the opened file.
    5. parts = line.strip().split('\t'): Strips leading and trailing whitespace from the line and splits it into parts using the tab ('\t') character as the delimiter. This assumes that each line contains two parts separated by a tab.
    6. if len(parts) == 2 : Checks if the line contains exactly two parts.
    7. out_data[parts[0]] = parts[1]: Assigns the first part as the key and the second part as the value in the out_data dictionary.
    8. return out_data: Returns the out_data dictionary containing the parsed data from the file.
    9. word_enumeration = load_reducer_output('en_out.txt'): Calls the load_reducer_output function with the file path 'en_out.txt' and stores the returned dictionary in word_enumeration.
    10. document_count = load_reducer_output('idf_out.txt'): Calls the load_reducer_output function with the file path 'idf_out.txt' and stores the returned dictionary in document_count.
# Merging into a single structure:
vocabulary = {}: Initializes an empty dictionary vocabulary to store the merged data.
for word, unique_id in word_enumeration.items():: Iterates over each key-value pair in the word_enumeration dictionary.
document_count_value = document_count.get(word, 0): Retrieves the value corresponding to the current word from the document_count dictionary. If the word is not found, it defaults to 0.
vocabulary[word] = {'ID': unique_id, 'DocumentCount': document_count_value}: Creates a new entry in the vocabulary dictionary with the word as the key and a dictionary containing 'ID' (from word_enumeration) and 'DocumentCount' (from document_count) as the value.
# Printing the output:
for word, info in list(vocabulary.items()):: Iterates over each key-value pair in the vocabulary dictionary.
print(f'ID: {info["ID"]}, Document Count: {info["DocumentCount"]}'): Prints the 'ID' and 'DocumentCount' associated with each word in the vocabulary dictionary.
Overall, this code parses data from two files, combines the information into a single structure (vocabulary), and then prints the merged data.

  # 2. Enumeration
  # • Mapper – Enumeration
# Input Reading:
Reads input from standard input (stdin), typically in the form of text data.
# Text Processing:
Extracts words from the input text using a regular expression.
Converts each word to lowercase and filters out stopwords.
# Output Emission:
Emits each significant word along with a count of 1 as a key-value pair.
The key is the word, and the value is 1, indicating that this word has been encountered once.
Outputs key-value pairs to standard output (stdout), separated by a tab character.
  # • Reducer- enumeration
The reducer receives the key-value pairs emitted by the mapper and performs aggregation or computation based on the keys. 
In the provided code:
# Input Reading:
Reads key-value pairs from standard input (stdin), typically produced by the mapper.
# Aggregation:
Groups together key-value pairs with the same key.
Computes the total count for each unique key (word) by summing up the values associated with it.
# Output Emission:
Emits the aggregated results, usually as key-value pairs.
The key is typically the word, and the value is the total count of occurrences of that word across the input data.
Outputs the final results to standard output (stdout), ready for further processing or analysis.
In summary, the reducer aggregates the intermediate results produced by the mapper, performing any necessary computation or summarization, and produces the final output data. In the context of word counting or enumeration, the reducer would produce a list of unique words along with their respective counts or identifiers.
  # 3. IDF
  # • Mapper – IDF
Input Reading: Reads input lines from standard input (stdin), typically produced by another script or process.
Parsing: Parses each input line into a term and a document ID.
Term Counting: Counts the occurrences of each term across documents by maintaining a set of document IDs for each term.
Output Emission: Emits key-value pairs where the key is the term and the value is the count of unique documents containing that term.
  # • Reducer – IDF
Input Reading: Reads key-value pairs from standard input (stdin), typically produced by the Mapper.
Aggregation: Aggregates the counts of documents containing each term.
IDF Calculation: Calculates the IDF (Inverse Document Frequency) for each term using the formula :
idf = 1 + log(total_documents / (1 + doc_count)).
Output Emission: Emits key-value pairs where the key is the term and the value is its IDF.
In summary, the Reducer calculates the IDF for each term based on the document frequencies (DF) obtained from the Mapper's output.
  # 4. Indexer
  # • Mapper – Indexer
# Function Definition: load_vocabulary:
This function reads a vocabulary file (vocab_out.txt) and creates a dictionary containing the unique IDs and document counts for each term.
It returns the vocabulary dictionary.
# Loading Vocabulary:
The load_vocabulary function is called to load the vocabulary from the vocab_out.txt file.
# Function Definition: calculate_normalized_tf:
This function calculates the normalized term frequency (TF) for each term in a given text.
It returns a dictionary where keys are terms and values are their normalized TF scores.
# Reading Input:
The script reads input from standard input (stdin), which typically comes from another process or file.
Each line is split into columns using a comma (,) as the delimiter.
The article ID and text section are extracted from the columns.
# Processing Text:
The text section is cleaned by removing punctuation and splitting it into individual words using regular expressions.
Each word is converted to lowercase and checked against the stopwords list.
If the word is not a stopword, its normalized TF score is calculated using calculate_normalized_tf.
# Output:
For each term in the text with a non-zero TF score, the corresponding term ID and article ID are printed to stdout, along with the TF score.
This script essentially preprocesses text data by calculating the TF scores for each term in each article, considering only non-stopwords. The TF scores are normalized to handle sparse vectors, and the results are emitted for further processing, such as calculating TF-IDF values.
  # • Reducer -indexer
This script is a Reducer in a MapReduce job for calculating TF-IDF (Term Frequency-Inverse Document Frequency). 
# 1. Vocabulary Loading Function (`load_vocabulary`): 
   - This function loads the vocabulary from a text file.
   - It opens the specified file (`vocabulary_path`) and reads it line by line.
   - Each line is stripped of leading and trailing whitespaces and then split by the tab character (`'\t'`) to extract the unique ID and document count.
   - These extracted values are stored in a dictionary called `vocabulary`, where the unique ID serves as the key, and a dictionary containing the document count is the value.
   - The function returns the loaded vocabulary dictionary.
# 2. Mapper Output Parsing Function (`read_mapper_output`): 
   - This function parses the output generated by the Mapper.
   - It takes a file object (`file`) and an optional separator (defaulting to `'\t'`).
   - It iterates over each line in the file, stripping trailing whitespace and splitting the line by the specified separator, resulting in a key-value pair.
   - It yields each key-value pair as a tuple.
# 3. Main Function:
   - The `main` function is the entry point of the Reducer script.
   - It initializes an empty dictionary called `term_frequencies` to store term frequencies.
   - It processes each line output by the Mapper using the `read_mapper_output` function.
   - For each key-value pair (`term_article, tf`), it splits the `term_article` to extract the term ID and article ID.
   - It converts the term frequency (`tf`) to a float.
   - If the term ID is not already present in the `term_frequencies` dictionary, a new entry is created.
   - It increments the term frequency for the corresponding article ID.
   - After processing all input, it calculates the total number of documents using the sum of document counts from the vocabulary.
   - It calculates IDF (Inverse Document Frequency) for each term using the formula
`idf = log((total_documents / (1 + df)) + 1)`,
 where `total_documents` is the sum of document counts and `df` is the document frequency obtained from the vocabulary.
   - Finally, it calculates TF-IDF for each article and term combination and prints the result in the format `article_id <separator> tf_idf`.
This Reducer script effectively computes the TF-IDF score for each term in each document based on the data emitted by the Mapper.

# Future Enhancements
Implement query processing algorithms to enable users to search for documents based on their queries more effectively.
Enhance the efficiency and scalability of the search engine by optimizing MapReduce jobs and exploring distributed computing techniques.
