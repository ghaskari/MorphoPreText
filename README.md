# MorphoPreText

MorphoPreText is a Python package designed for preprocessing English and Persian text. This library provides tools for text normalization, tokenization, cleaning, and other preprocessing tasks that are essential for Natural Language Processing (NLP) applications. The package supports both English and Persian languages with specific modules tailored to the linguistic nuances of each language.

---

## Features

- **Multilingual Support**: Handles preprocessing for both English and Persian text.
- **Text Normalization**: Includes dictionaries for standardizing characters, punctuation, and text structure.
- **Stopword Removal**: Integrated with customizable stopword lists for both languages.
- **Spelling Correction**: Automatically corrects misspelled words (English only).
- **Emoji Handling**: Options to remove, replace, or analyze emoji sentiments.
- **Date Handling**: Converts Persian dates to the Gregorian calendar format.
- **Customizable Tasks**: Configurations for different NLP use cases such as sentiment analysis, named entity recognition (NER), and more.
- **Predefined Task Configurations**: Provides task-specific preprocessing setups for translation, summarization, topic modeling, and more.
- **Task-Specific Preprocessing**:
  - Supports tasks like `translation`, `sentiment`, `ner`, `spam_detection`, `topic_modeling`, and `summarization`.
- **Language-Specific Preprocessing**:
  - **Persian**: Diacritic removal, numeral normalization, punctuation handling, Persian stopword removal, half-space handling.
  - **English**: Spelling correction, contractions expansion, lemmatization, stemming, and punctuation cleaning.
- **Text Cleaning**:
  - Removes URLs, HTML tags, emails, hashtags, mentions, and extra spaces.
- **Custom Dictionary Support**:
  - Includes dictionaries for standardizing text, handling special characters, and expanding contractions.
- **Flexible Emoji Processing**:
  - Provides options to analyze emoji sentiment, replace emojis with placeholders, or remove them entirely.
- **Efficient Column-Wide Processing**:
  - Capable of processing entire pandas DataFrame columns for large-scale text datasets.
- **Persian-Specific Date Handling**:
  - Converts Persian calendar dates into the Gregorian calendar format seamlessly.

---

## Installation

MorphoPreText is available on PyPI and can be installed using pip:

```bash
pip install morphopretext
```

Alternatively, you can install the package from the source:

```bash
# Clone the repository
$ git clone https://github.com/ghaskari/MorphoPreText.git

# Navigate to the project directory
$ cd MorphoPreText

# Install the package
$ pip install .

# Install dependencies
$ pip install -r requirements.txt
```

---

## Usage

### What Can You Do With MorphoPreText?

MorphoPreText provides robust preprocessing tools for handling diverse text preprocessing needs:

- **Clean and Normalize Text**: Standardize characters, remove extra spaces, and handle punctuation.
- **Handle Emojis**: Remove, replace, or analyze sentiment based on emojis.
- **Convert Dates**: Process Persian calendar dates into standard Gregorian format.
- **Remove Unwanted Elements**: Strip out URLs, HTML tags, mentions, hashtags, and email addresses.
- **Custom Task Configurations**: Use predefined configurations for tasks like sentiment analysis, translation, and topic modeling.
- **Tokenization and Stopword Removal**: Tokenize text and remove language-specific stopwords.
- **Language-Specific Enhancements**: Handle unique linguistic features such as Persian half-spaces or English contractions.

### English Text Preprocessing

```python
from morphopretext import EnglishTextPreprocessor

# Initialize the preprocessor
english_preprocessor = EnglishTextPreprocessor(task="default")

# Preprocess text example 1
text = "This is a sample text with emojis 😊 and a URL: https://example.com"
cleaned_text = english_preprocessor.clean_punctuation(text)
print(cleaned_text)  # Output: This is a sample text with emojis 😊 and a URL https example com

# Preprocess text example 2
text_with_html = "This is a <b>bold</b> statement."
cleaned_html_text = english_preprocessor.remove_url_and_html(text_with_html)
print(cleaned_html_text)  # Output: This is a bold statement.

# Preprocess text example 3
text_with_emojis = "I love programming! 😊"
emoji_handled_text = english_preprocessor.handle_emojis(text_with_emojis, strategy="replace")
print(emoji_handled_text)  # Output: I love programming! EMOJI

# Preprocess text example 4
spelling_text = "Ths is a smple txt with erors."
corrected_text = english_preprocessor.correct_spelling(spelling_text)
print(corrected_text)  # Output: This is a sample text with errors.
```

### Persian Text Preprocessing

```python
from morphopretext import PersianTextPreprocessor

# Initialize the preprocessor with a custom stopword file
persian_preprocessor = PersianTextPreprocessor(stopword_file="stopwords.txt", task="default")

# Preprocess text example 1
persian_text = "این یک متن نمونه است که شامل تاریخ ۱۴۰۲/۰۳/۱۵ و علائم نگارشی است."
cleaned_text = persian_preprocessor.remove_stopwords(persian_text)
print(cleaned_text)  # Output: این متن نمونه شامل تاریخ ۱۴۰۲/۰۳/۱۵ علائم نگارشی است.

# Preprocess text example 2
persian_text_with_emojis = "این یک متن 😊 تست است"
emoji_removed_text = persian_preprocessor.handle_emojis(persian_text_with_emojis, "remove")
print(emoji_removed_text)  # Output: این یک متن تست است

# Preprocess text example 3
persian_text_with_half_space = "این‌ متن‌ تست‌ است"
cleaned_half_space_text = persian_preprocessor.remove_half_space(persian_text_with_half_space)
print(cleaned_half_space_text)  # Output: این متن تست است

# Preprocess text example 4
persian_date_text = "تاریخ امروز ۱۴۰۲/۰۵/۲۰ است"
converted_date_text = persian_preprocessor.date_converter().handle_persian_dates(persian_date_text, convert_to_standard=True)
print(converted_date_text)  # Output: تاریخ امروز 2023-08-11 است
```

---

## Project Structure

```
MorphoPreText/
├── morphotext/                    # Package directory
│   ├── __init__.py                # Initialize the package
│   ├── english_text_preprocessor.py
│   ├── persian_text_preprocessor.py
│   ├── Dictionaries_En.py
│   ├── Dictionaries_Fa.py
│   ├── stopwords.txt
├── README.md                      # Project description
├── setup.py                       # Packaging configuration
├── requirements.txt               # Dependencies
├── LICENSE                        # License information
```

---

## Contributions

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes.

---

## License

This project is licensed under the terms of the MIT License. See the `LICENSE` file for details.

---

## Repository

For more details, visit: https://github.com/ghaskari/MorphoPreText

