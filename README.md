# 🛡️ ShieldRate: Automated Cyber Insurance Underwriter

### 🚀 Project Overview
**ShieldRate** is an actuarial engine that bridges the gap between **technical vulnerability management** and **financial risk assessment**. It demonstrates a **dynamic pricing model** that ingests live vulnerability data (CVEs) and adjusts insurance premiums based on security posture.

### ⚙️ How It Works
1.  **Ingestion:** Parses `.CSV` exports from Tenable Nessus.
2.  **Risk Scoring:** Applies a weighted algorithm (Criticals = +$5k, Defender = -20%).
3.  **Quoting:** Outputs a financial "Policy Quote".

### 🛠️ Tech Stack
* **Language:** Python 3.9+ (Pandas)
* **Infrastructure:** Microsoft Azure (Windows Server 2019)
* **Security:** Tenable Nessus, Microsoft Defender for Endpoint
