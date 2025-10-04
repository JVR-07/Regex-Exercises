# Python Regex library

This small repository is a compilation of exercises I created for one of my classes. The objective is to learn about regular expressions and how to use them in Python.

# Files explained

## Test.py
This is the first exercise, and I used the `re` library for the first time in Python. This code has a regex to check if the input is a valid phone number with one of these two formats  **XXX-XXX-XXXX** & **XXX XXX XXXX**.
The regex used is: `^\d{3}[-\s]\d{3}[-\s]\d{4}$`

## Regex-Decimales.py
For this exercise, I used a regular expression to check if the input is a valid integer or decimal number. I used two different regex patterns for this:
- **Integer:**`'^[-+]?\d+$'`
- **Decimal:**`^[-+]?(\d+)?\.(\d+)?([eE]\^?[-+]?\d+)?$`

## Regex-Correo-o-Url.py
In this exercise, I used regular expressions to evaluate whether the input is a valid email address or a valid URL (without the path). I used two different regex patterns:
- **Email:**`^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$`
- **URL:**`^(https?://)?(www\.)?[\w.-]+\.[a-zA-Z]{2,}$` 

## Verificar-Entradas.py
This exercise is a bit more complex because I merged all the regex patterns into a single program. I also used a new regular expression to check if the input is a valid variable name: `^[a-zA-Z_][a-zA-Z0-9_]*$`

## EscanearArchivo.py
This exercise is similar to the previous one, but it implements the necessary logic to read a .txt file and scan the entire content to search for valid and invalid words.

**Entrada.txt** is the example file I used for this exercise.