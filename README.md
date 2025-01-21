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
```

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
2023TECHNOVA
2023TechNova
2023technova
2024TECHNOVA
2024TechNova
2024technova
2025TECHNOVA
2025TechNova
2025technova
TECHNOVA
TECHNOVA-2023
TECHNOVA-2024
TECHNOVA-2025
TECHNOVA01!
TECHNOVA123
TECHNOVA2023
TECHNOVA2024
TECHNOVA2025
TECHNOVA_2023
TECHNOVA_2024
TECHNOVA_2025
TechNova
TechNova-2023
TechNova-2024
TechNova-2025
TechNova01!
TechNova123
TechNova2023
TechNova2024
TechNova2025
TechNova_2023
TechNova_2024
TechNova_2025
password123
technova
technova-2023
technova-2024
technova-2025
technova01!
technova123
technova2023
technova2024
technova2025
technova_2023
technova_2024
technova_2025
```

<br>

### 2. Generate for a Single Year:
```bash
python3 crunchy.py --company TechNova --start-year 2022 --output TechNova2022.txt
```

Output example:
```
2022TECHNOVA
2022TechNova
2022technova
TECHNOVA
TECHNOVA-2022
TECHNOVA01!
TECHNOVA123
TECHNOVA2022
TECHNOVA_2022
TechNova
TechNova-2022
TechNova01!
TechNova123
TechNova2022
TechNova_2022
password123
technova
technova-2022
technova01!
technova123
technova2022
technova_2022
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

