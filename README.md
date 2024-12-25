# crunchy

### The Next-Gen Wordlist Generator  

<br>

**crunchy** is a powerful and customizable wordlist generator for penetration testers, security researchers, and hobbyists. Inspired by the legendary *crunch*, crunchy is designed to make crafting tailored wordlists more flexible. Whether you're working on brute-force attacks, password cracking, or creative projects, crunchy is your go-to tool for generating dynamic wordlists.  

<br>

---

<br>

## Features  
- **Dynamic Input Handling**: Combine company names, dates, and years seamlessly.  
- **Advanced Casing and Normalization**: Automatically handles numbers, special characters, and casing for diverse results.  
- **Intuitive CLI**: A user-friendly command-line interface, ideal for scripting and automation.  
- **Blazing Fast**: Generates wordlists in seconds.  

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
   <br>
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```  
   <br>
3. Run the program:
   ```bash
   python3 crunchy.py --help
   ```

<br>

---

<br>

## Usage

<br>

Generate a wordlist by providing a company name and year range:  

### Basic Usage:
```bash
python3 crunchy.py --company <company> --start-year <year> --end-year <year> --output <company.txt>

### Options:  
| Option             | Description                                             | Example                    |  
|--------------------|---------------------------------------------------------|----------------------------|  
| `--company`        | Company name, including numbers or special characters  | `TechNova`                |  
| `--start-year`     | Start year for generating year combinations            | `2023`                    |  
| `--end-year`       | Optional end year for a range of years                 | `2025`                    |  
| `--output`         | File to save the generated wordlist                   | `output.txt`              |  

<br>

---

<br>

## Examples

<br>

### 1. Generate a Wordlist for a Company Name with Year Range:
```bash
python3 crunchy.py --company TechNova --start-year 2023 --end-year 2025 --output TechNova.txt
```
Output example:
```
TechNova
technova
TECHNOVA
2023TechNova
2024TechNova
2025TechNova
TechNova2023
TechNova2024
TechNova2025
TechNova-2023
TechNova-2024
TechNova-2025
```

### 2. Generate for a Single Year:
```bash
python3 crunchy.py --company TechNova --start-year 2022 --output TechNova2022.txt
```

<br>

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

