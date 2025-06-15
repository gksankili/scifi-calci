# 🧮 SciFi Calculator – `scifi-calci`

A web-based scientific calculator built using **Python Flask**, supporting both basic arithmetic and advanced functions like `sin()`, `log()`, `sqrt()` and more. The app includes a clean web UI and is fully containerized using **Docker**.

---

## 🚀 Features

- Basic arithmetic: `+`, `-`, `*`, `/`, `**`
- Scientific functions: `sin`, `cos`, `tan`, `sqrt`, `log`, `log10`, `pi`, `e`
- User-friendly web interface
- Built with Flask (Python)
- Dockerized for easy deployment
- Runs on port `5011`

---

## 📸 Demo

![Calculator UI Screenshot](docs/demo.png) <!-- Replace with actual screenshot when available -->

---

## 🛠️ Tech Stack

- **Backend:** Python 3, Flask  
- **Frontend:** HTML5, CSS3  
- **Containerization:** Docker  

---

## 🧑‍💻 Getting Started

### 📥 1. Clone the Repository
```bash
git clone https://github.com/gksankili/scifi-calci.git
cd scifi-calci
```

### 🧪 2. Run Locally (without Docker)
```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Then open your browser at: http://localhost:5011

## 🐳 Run with Docker
### 🔨 Build the Docker Image
```bash
docker build -t scifi-calci .
```
### ▶️ Run the Container
```bash
docker run -d -p 5011:5011 --name scifi-calci-app scifi-calci
```
## 🐳 Docker Commands
| Task             | Command                                                         |
| ---------------- | --------------------------------------------------------------- |
| Build image      | `docker build -t scifi-calci .`                                 |
| Run container    | `docker run -d -p 5011:5011 --name scifi-calci-app scifi-calci` |
| Stop container   | `docker stop scifi-calci-app`                                   |
| Start container  | `docker start scifi-calci-app`                                  |
| Remove container | `docker rm -f scifi-calci-app`                                  |
| View containers  | `docker ps`                                                     |

## 🧮 Supported Expressions
You can safely use these functions in the calculator:

sin(x), cos(x), tan(x)

log(x), log(x, base), log10(x)

sqrt(x), abs(x)

Constants like pi, e

Expressions like sin(pi / 2) + log(100, 10)

⚠️ Expressions are evaluated using Python's math module in a sandboxed environment.

## 📁 Project Structure
```csharp
scifi-calci/
├── app.py                 # Flask application logic
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker build config
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
├── static/
│   └── styles.css         # Optional styling
└── templates/
    └── index.html         # Web UI for calculator
```

## 📝 License
This project is open source and available under the MIT License.

##🙋‍♂️ Author
Made by gksankili

```yaml
---

Let me know if you'd like:
- A GitHub Actions workflow to auto-build Docker images
- Deployment guide for Render, Railway, or fly.io
- Keyboard input or mobile optimization

You're off to a great start 🚀
```