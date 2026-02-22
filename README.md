# Borderpass CAPTCHA Solver

High-performance OCR-based solver for numeric CAPTCHA challenges from borderpass.ir.  
Supports both direct image PATH input and Base64 image data.

---

## Description

Borderpass CAPTCHA Solver is a lightweight and automation-ready tool designed to detect and extract numeric CAPTCHA text with high accuracy and speed.

Main goals:

- Clean numeric CAPTCHA recognition
- Mathematical expression extraction
- Fast inference time
- Simple integration into bots or backend services

---

## Features

- Automatic CAPTCHA text detection
- High-speed OCR processing
- Supports image PATH input
- Supports Base64 image input
- Extracts numbers and simple math expressions
- Optional expression evaluation
- Minimal preprocessing required
- Lightweight and production-ready

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mhmalimhm/captcha_borderpass.git
cd captcha_borderpass
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Solve from Image PATH

```python
from main import solve

result = solve(path,"path")
print(result)
```

---

### Solve from Base64

```python
from main import solve

result = solve(data,"bs64")
print(result)
```

---

## Example

Input:

```
3 + 4 =
```

Detected Output:

```
3 + 4 =
```

Optional evaluated result:

```
7
```

---

## How It Works

1. Receives image (PATH or Base64)
2. Converts image to array format
3. Processes image through OCR engine
4. Extracts text
5. Cleans and returns final result
6. eval result

---

## Project Structure

```
├── main.py
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.8+
- OpenCV
- EasyOCR (or configured OCR engine)

---

## Disclaimer

This project is provided for educational, research, and automation testing purposes.  
Users are responsible for complying with the terms of service of any target website.

---

## License

MIT License
