# crunchy

### The Next-Gen Wordlist Generator  

<br>

**crunchy** is a powerful and customizable wordlist generator for penetration testers, security researchers, and hobbyists. Inspired by the legendary *crunch*, crunchy is designed to make crafting tailored wordlists more flexible. Whether you're working on brute-force attacks, password cracking, or creative projects, crunchy is your go-to tool for generating dynamic wordlists.  

<br>

---

<br>

## Features  
- **Dynamic Input Handling**: Combine names, dates, company names, patterns, and more.  
- **Advanced Permutation Engine**: Precise control over combinations, lengths, and repetitions.  
- **Intuitive CLI**: A user-friendly command-line interface, ideal for scripting and automation.  
- **Customizable Rulesets**: Create and apply rules to fine-tune your output.  

<br>

---

<br>

## Installation  

<br>

### Prerequisites  
- Python 3.8+  
- `pip`  

<br>

### Installation Steps  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Mag1cByt3s/crunchy.git
   cd crunchy
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the program::
   ```bash
   python3 crunchy.py --help
   ```

<br>

---

<br>

## Usage

<br>

Generate a wordlist by providing inputs like names, years, and patterns:
Basic Usage:
```bash
python3 crunchy.py --inputs "John,2024,Secure" --length 6-12 --output mywordlist.txt
```

<br>

---

<br>

## Examples

<br>

Generate a Wordlist Based on Names and Years
```bash
python3 crunchy.py --inputs "Alice,Bob,2024" --length 8-16 --output names_years.txt
```

Generate Using Patterns
```bash
python3 crunchy.py --inputs "admin,root,secure" --pattern "@n@d!" --output admin_list.txt
```

Extend with Dictionaries
```bash
python3 crunchy.py --inputs "CompanyName" --append-dictionary /usr/share/wordlists/rockyou.txt --output extended_list.txt
```

---

<br>

## Contribution

Contributions are welcome! Please feel free to submit issues or pull requests.

1. Fork the repository
2. Create a new branch:
```bash
git checkout -b feature/my-feature
```
3. Commit your changes:
```bash
git commit -m "Add my feature"
```
4. Push to the branch:
```bash
git push origin feature/my-feature
```
5. Submit a pull request

<br>

---

<br>

## License

This project is licensed under the GPL3 License.

<br>

---

<br>

## Acknowledgments

crunchy is inspired by crunch and aims to modernize wordlist generation with enhanced flexibility and features.
