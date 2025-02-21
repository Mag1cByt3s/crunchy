#!/usr/bin/env python3

import argparse
import itertools
import re

# Function to generate wordlists based on inputs, length range, and patterns
def generate_wordlist(company, start_year, end_year=None):
    wordlist = set()

    # Generate years if end_year is provided
    years = [str(year) for year in range(start_year, end_year + 1)] if end_year else [str(start_year)]

    # Normalize company name: remove special characters and numbers, and handle different casing
    base_company = re.sub(r'[^a-zA-Z]', '', company)  # Remove non-alphabetic characters
    variations = {company, base_company, company.lower(), base_company.lower(), company.upper(), base_company.upper()}

    # Combine company name with years and other variations
    for variation in variations:
        wordlist.add(variation)
        for year in years:
            wordlist.add(f"{variation}{year}")
            wordlist.add(f"{year}{variation}")
            wordlist.add(f"{variation}-{year}")
            wordlist.add(f"{variation}_{year}")

        # Add custom patterns
        wordlist.add(f"{variation}123")
        wordlist.add(f"{variation}01!")

    # Add a universal pattern
    wordlist.add("password123")
    wordlist.add("password123!")
    wordlist.add("welcome123")
    wordlist.add("welcome123!")
    wordlist.add("Password123")
    wordlist.add("Password123!")
    wordlist.add("Welcome123")
    wordlist.add("Welcome123!")
    wordlist.add("welcome1")
    wordlist.add("Welcome1")
    wordlist.add("passw0rd")
    wordlist.add("Passw0rd")
    wordlist.add("123")
    wordlist.add("123!")
    wordlist.add("1234!")
    wordlist.add("1234")
    wordlist.add("12345")
    wordlist.add("12345!")
    wordlist.add("123456")
    wordlist.add("123456!")
    wordlist.add("1234567")
    wordlist.add("1234567!")
    wordlist.add("12345678")
    wordlist.add("12345678!")
    wordlist.add("123456789")
    wordlist.add("123456789!")
    wordlist.add("1234567890")
    wordlist.add("1234567890!")
    wordlist.add("123123")
    wordlist.add("1231234")
    wordlist.add("1231234!")
    wordlist.add("12312345")
    wordlist.add("12312345!")
    wordlist.add("123123456")
    wordlist.add("123123456!")

    return wordlist

# Function to write the wordlist to a file
def save_to_file(wordlist, output_file):
    with open(output_file, 'w') as f:
        for word in sorted(wordlist):
            f.write(word + '\n')

# Main function to handle CLI arguments
def main():
    parser = argparse.ArgumentParser(description="Crunchy: The Next-Gen Wordlist Generator")
    parser.add_argument('--company', required=True, help="Company name (e.g., ExampleCorp)")
    parser.add_argument('--start-year', type=int, required=True, help="Start year (e.g., 2020)")
    parser.add_argument('--end-year', type=int, help="End year (e.g., 2025)")
    parser.add_argument('--output', required=True, help="File to save the generated wordlist")

    args = parser.parse_args()

    # Generate wordlist
    wordlist = generate_wordlist(args.company, args.start_year, args.end_year)

    # Save to file
    save_to_file(wordlist, args.output)
    print(f"Wordlist saved to {args.output} with {len(wordlist)} entries.")

if __name__ == "__main__":
    main()
