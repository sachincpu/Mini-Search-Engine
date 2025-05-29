# Interactive Dictionary Application

## Description

This application is a command-line interactive dictionary that allows users to look up definitions of English words. It provides definitions for known words, suggests corrections for common misspellings, and handles cases where a word is not found.

The application is built in Python and uses a JSON file (`data.json`) to store dictionary data.

## Running the Application

To run the application, navigate to the directory containing the script and execute the following command in your terminal:

```bash
python dictionary.py
```

The script will then prompt you to "Enter a word:".

## Usage Examples

### 1. Word Found

If you enter a word that exists in the dictionary:

```
Enter a word: apple
A fruit
```

*(The exact definition will depend on the content of `data.json`)*

### 2. Word Not Found (No Suggestions)

If you enter a word that does not exist and has no close matches:

```
Enter a word: xyzxyz
The word does not exist.Please double check it
```

### 3. Word Not Found (With Suggestion)

If you enter a word that is not found directly but has a close match, the application will suggest a correction:

```
Enter a word: apel
Did you mean apple instead ?Enter 'Y' for yes or 'N' for no: Y
A fruit
```

If you enter 'N' to the suggestion:

```
Enter a word: apel
Did you mean apple instead ?Enter 'Y' for yes or 'N' for no: N
The word does not exist.Please double check it
```

If you provide an invalid response to the suggestion:

```
Enter a word: apel
Did you mean apple instead ?Enter 'Y' for yes or 'N' for no: maybe
Sorry we didn't understand your entry
```

## Data File

**Important Note:** The current `data.json` file included in this repository is a **dummy file** with a very limited set of example words (e.g., "apple", "banana"). This is for demonstration and testing purposes.

For full functionality, this dummy `data.json` should be replaced with the actual, comprehensive data file (originally named `1.2 data.json.json`). The application expects the data file to be named `data.json` and be in the same directory as `dictionary.py`.

## Testing

Unit tests for the dictionary logic are available in `test_dictionary.py`. You can run them using:

```bash
python -m unittest test_dictionary.py
```
