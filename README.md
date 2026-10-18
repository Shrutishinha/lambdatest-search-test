# 🌐 WEBSITE TESTING AUTOMATION ON LAMBDATEST
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=900&size=34&pause=700&color=00F5FF&center=true&vCenter=true&width=1100&lines=Website+Testing+on+LambdaTest;Cross-Browser+Cloud+Execution;HyperExecute+Parallel+Runs;Screenshot+%26+Log+Evidence+Capture;CI%2FCD+Integrated+Pipeline;Automated+Bug+Reporting" />
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=blur&color=0:00F5FF,50:7C4DFF,100:FF6D00&height=200&section=header&text=LAMBDATEST%20AUTOMATION&fontSize=40&fontColor=ffffff&animation=fadeIn"/>
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Platform-LambdaTest-00E676?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Execution-HyperExecute%20Parallel-FF9100?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Cloud-Cross%20Browser-00B0FF?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Language-Python-7C4DFF?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/CI%2FCD-Ready-00C853?style=for-the-badge&logo=githubactions&logoColor=white"/>
</p>

---

# ⚡ PROJECT OVERVIEW

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:141E30,100:243B55&height=4"/>
</p>

An automated website testing project that runs entirely on the **LambdaTest cloud**.
Tests are written in Python, executed in parallel with **HyperExecute**, and validated across multiple browsers and operating systems without any local browser setup.

## 🚀 What This Project Does

```
✔ Runs website tests on the LambdaTest cloud
✔ Validates forms, navigation and key user flows
✔ Executes tests in parallel with HyperExecute
✔ Covers multiple browsers and operating systems
✔ Captures screenshots and logs on failure
✔ Reviews results on the LambdaTest dashboard
✔ Stores structured reports in /reports/
```

---

# 🔁 LAMBDATEST EXECUTION FLOW

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=soft&color=0:00F5FF,100:7C4DFF&height=140&section=header&text=TEST%20FLOW&fontColor=ffffff&fontSize=30&animation=fadeIn"/>
</p>

```text
Write Test Cases (Python)
      │
      ▼
Set LambdaTest Credentials
      │
      ▼
Run via HyperExecute (hyperexecute.yaml)
      │
      ▼
Parallel Cloud Sessions
      │
      ▼
Cross-Browser / OS Validation
      │
      ▼
Assertions + Screenshot & Log Capture
      │
      ▼
LambdaTest Dashboard + /reports/
```

---

# 🌍 CROSS-BROWSER & OS COVERAGE

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:1D2B64,100:F8CDDA&height=140&section=header&text=CLOUD%20COMPATIBILITY&fontColor=ffffff&fontSize=28&animation=fadeIn"/>
</p>

| Browser | Windows | macOS | Linux |
|---------|:-------:|:-----:|:-----:|
| Chrome  | ✅ | ✅ | ✅ |
| Firefox | ✅ | ✅ | ✅ |
| Edge    | ✅ | ✅ | – |
| Safari  | – | ✅ | – |

> Browsers and OS versions are chosen per run in the LambdaTest configuration.
> Adjust the table to match what you actually executed.

⚡ Parallel execution reduces total runtime.

---

# 🧪 TEST SCENARIO FLOW

```
Start LambdaTest Session
      ↓
Open Website Under Test
      ↓
Locate Elements
      ↓
Enter Test Data
      ↓
Perform UI Actions
      ↓
Validate Expected Result
      ↓
Capture Screenshot + Logs
      ↓
PASS / FAIL
```

Handled in the tests:

• Dynamic page content  
• Wait strategies for slow-loading elements  
• Form validation  
• Navigation checks  
• Retry for flaky tests  

---

# 📊 REPORTING

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:000428,100:004e92&height=4"/>
</p>

After every run:

✔ Pass/fail status for each test on the LambdaTest dashboard  
✔ Video recording and logs for each session  
✔ Screenshots captured on failures  
✔ Browser and OS details recorded  
✔ Local report files saved in `/reports/`  

```bash
/reports/
```

---

# ⚙️ SETUP & RUN

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set LambdaTest credentials

Find your username and access key in the LambdaTest dashboard under **Profile → Account Settings**.

**Windows (Command Prompt):**

```bash
setx LT_USERNAME "your_username"
setx LT_ACCESS_KEY "your_access_key"
```

**macOS / Linux:**

```bash
export LT_USERNAME="your_username"
export LT_ACCESS_KEY="your_access_key"
```

> Restart the terminal after using `setx` so the variables load.

### 3. Run on LambdaTest (HyperExecute, parallel)

```bash
hyperexecute --config hyperexecute.yaml
```

### 4. Run a single test file

```bash
python tests/main_test.py
```

---

# 📄 HYPEREXECUTE CONFIG (hyperexecute.yaml)

```yaml
version: 0.1
runson: win
concurrency: 2
autosplit: true
retryOnFailure: true
maxRetries: 1

pre:
  - pip install -r requirements.txt

testSuites:
  - python tests/main_test.py

report: true
```

> Adjust `runson`, `concurrency` and the test command to match your setup.

---

# 🔐 SECURITY

• Credentials stored as environment variables  
• No hardcoded username or access key  
• `.env` and key files excluded via `.gitignore`  

---

# 🚀 CI/CD INTEGRATION

```
Commit → Build → Test on LambdaTest → Validate → Deploy
                      │
                      └── If Failed → Deployment Blocked
```

Can be wired into:

• GitHub Actions  
• Jenkins  
• GitLab CI  
• Azure DevOps  

Store `LT_USERNAME` and `LT_ACCESS_KEY` as secrets in your CI tool.

---

# 🏗 PROJECT STRUCTURE

```
website-testing/
│
├── tests/
├── config/
├── utils/
├── reports/
├── hyperexecute.yaml
└── requirements.txt
```

---

# 💎 HIGHLIGHTS

✨ Fully cloud-based execution on LambdaTest  
✨ Parallel runs with HyperExecute  
✨ Cross-browser and cross-OS validation  
✨ Screenshot and log evidence for every failure  
✨ Secure, environment-based credentials  
✨ CI/CD ready  

---

# 👩‍💻 AUTHOR

Shruti Sinha  
QA Automation | LambdaTest | Python  

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00F5FF,100:7C4DFF&height=180&section=footer&animation=fadeIn"/>
</p>
