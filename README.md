# CYBR3220 CyberDefense Suite

**Defensive cybersecurity toolkit with multi-module security analysis capabilities**

Part of CYBR3220 Final Project (Dunwoody College of Technology)  
Instructor: Amalan Pulendran  
Student: Dalair  
Semester: Spring 2027

---

## Overview

Python-based defensive security suite consolidating pattern detection, network analysis, file integrity monitoring, and system surveillance into one unified CLI tool. Built to demonstrate blue team capabilities for the CYBR3220 final project.

**Offensive Component:** [CYBR3220-TCP-Tool](https://github.com/Dalairr/CYBR3220-TCP-Tool)

---

## Features (8 Modules)

### 1. File Pattern Scanner
YARA/regex detection engine scanning files for malicious patterns:
- Reverse shell indicators (socket connections, subprocess calls)
- Credential dumping patterns (lsass, mimikatz, SAM registry access)
- Malware signatures (common malicious file operations)
- Registry persistence mechanisms (Run keys, autostart entries)
- Packed executables (UPX, custom packers)
- Suspicious keywords (admin, privilege, bypass)

### 2. Folder Security Scanner
Recursive directory scanner for phishing and social engineering indicators:
- Scans `.txt` files for phishing keywords
- Flags files containing: urgent, verify account, suspended, unusual activity, confirm identity
- Generates detection reports with file paths

### 3. PCAP Network Analyzer
Scapy-based packet capture analysis:
- Protocol distribution (TCP/UDP/ICMP counts)
- Source/destination IP enumeration
- Suspicious traffic detection (non-standard ports, unusual protocols)
- Packet-level inspection

### 4. File Integrity Monitor
SHA256 hash-based tamper detection:
- Creates baseline hashes for monitored files
- Detects modifications via hash comparison
- Validates file integrity across directories

### 5. Process Monitor
Enumerates running processes and flags suspicious activity:
- Lists all active processes with PIDs
- Detects suspicious process names (reverse shell indicators, RATs, credential dumpers)
- Cross-platform support (Windows/Linux)

### 6. Port Connection Analyzer
Network connection surveillance via `netstat`:
- Active TCP/UDP connection enumeration
- Flags suspicious ports (4444, 8080, 31337, etc.)
- Identifies remote connections with foreign addresses

### 7. System Log Analyzer
Security event log parser:
- Failed login detection
- Privilege escalation attempts
- Authentication anomalies
- Event ID filtering for security-relevant logs

### 8. USB Device Monitor
USB device tracking and logging:
- Enumerates connected USB devices
- Logs device information with timestamps
- Detects new USB connections

---

## Requirements

### Python Version
- Python 3.8+

### Dependencies
```bash
pip install scapy
```

### Platform Support
- **Windows**: Full support (all modules)
- **Linux**: Full support (all modules)
- **macOS**: Partial support (some modules require admin privileges)

---

## Installation

```bash
# Clone the repository
git clone https://github.com/Dalairr/CYBR3220-CyberDefense-Suite.git
cd CYBR3220-CyberDefense-Suite

# Install dependencies
pip install scapy

# Run the tool
python CyberDefenseSuite.py
```

---

## Usage

### Basic Execution
```bash
python CyberDefenseSuite.py
```

### Menu Interface
```
=== CyberDefense Suite ===
1. File Pattern Scanner (YARA/Regex Detection)
2. Folder Security Scanner (Phishing Keywords)
3. PCAP Network Analyzer
4. File Integrity Monitor
5. Process Monitor
6. Port Connection Analyzer
7. System Log Analyzer
8. USB Device Monitor
9. Exit

Select an option:
```

### Module Examples

**File Pattern Scanner**
```bash
Select option: 1
Enter file or directory path: /path/to/suspicious/files
# Scans for malicious patterns using YARA-style regex rules
```

**PCAP Network Analyzer**
```bash
Select option: 3
Enter PCAP file path: /path/to/capture.pcap
# Analyzes packet capture for suspicious network activity
```

**File Integrity Monitor**
```bash
Select option: 4
Choose action: 1 (Create Baseline)
Enter directory path: /path/to/monitor
# Creates SHA256 baseline for all files in directory
```

**Process Monitor**
```bash
Select option: 5
# Enumerates running processes and flags suspicious names
```

---

## Technical Implementation

### Architecture
- **Menu-driven CLI**: User-friendly interface for module selection
- **Modular design**: Each feature isolated as independent function
- **Logging**: Results saved to `cyberdefense_log.txt`
- **Cross-platform**: Platform detection for Windows/Linux compatibility

### Detection Logic

**Pattern Matching**
```python
# Reverse shell detection
socket_pattern = r'socket\.(AF_INET|SOCK_STREAM)'
subprocess_pattern = r'subprocess\.(Popen|call|run)'
```

**Hash Verification**
```python
# SHA256 file integrity
def calculate_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        sha256.update(f.read())
    return sha256.hexdigest()
```

**Network Analysis**
```python
# Scapy packet inspection
packets = rdpcap(pcap_file)
for pkt in packets:
    if TCP in pkt:
        # Analyze TCP traffic
```

---

## Attack Scenarios Detected

### Reverse Shell Connections
- Detects socket-based reverse shells (Port Scanner, Process Monitor)
- Flags suspicious ports: 4444, 4445, 8080, 31337
- Identifies subprocess spawning patterns

### Credential Dumping
- Pattern matches: lsass.exe access, mimikatz execution, SAM registry reads
- Flags suspicious process names containing "dump", "cred", "pass"

### Registry Persistence
- Detects autorun registry key modifications
- Scans for `Run`, `RunOnce`, `Startup` registry patterns

### File Exfiltration
- Network connection monitoring for data transfer
- File integrity checks detect unauthorized modifications

---

## Course Context

**CYBR3220: Scripting for Cyber Professionals**  
Dunwoody College of Technology | Spring 2027

**Topics Applied:**
- Python scripting for security automation
- Regular expressions and pattern matching
- Network traffic analysis with Scapy
- File I/O and hash-based integrity checking
- System process enumeration
- Windows Registry interaction
- Cross-platform development

**Paired with:** [CYBR3220-TCP-Tool](https://github.com/Dalairr/CYBR3220-TCP-Tool) (offensive component)

---

## Project Structure

```
CYBR3220-CyberDefense-Suite/
│
├── CyberDefenseSuite.py       # Main unified tool
├── README.md                   # Documentation
├── requirements.txt            # Python dependencies
└── test_samples/               # Sample files for testing
    ├── malicious_script.py
    ├── phishing_email.txt
    └── test.pcap
```

---

## Testing

### Test File Pattern Scanner
```bash
# Create test malicious file
echo "import socket; s=socket.socket()" > test_reverse_shell.py
# Run scanner on test file
```

### Test PCAP Analyzer
```bash
# Use provided test.pcap or generate traffic
python CyberDefenseSuite.py
# Select option 3, provide PCAP path
```

### Test File Integrity
```bash
# Create baseline, modify file, verify
# Results show detected modifications
```

---

## Limitations

- **Process Monitor**: Requires admin/root privileges for full process visibility
- **Log Analyzer**: Windows Event Log access requires admin rights
- **USB Monitor**: Platform-dependent implementation
- **PCAP Analyzer**: Requires valid packet capture files
- **Pattern Detection**: Regex-based, may produce false positives

---

## Future Enhancements

- Real-time monitoring with continuous scanning
- Email alerting for detected threats
- Database integration for historical analysis
- Advanced ML-based anomaly detection
- Web dashboard for visualization
- Integration with SIEM platforms

---

## License

Educational project for CYBR3220 coursework.

---

## Contact

**Student:** Dalair  
**Institution:** Dunwoody College of Technology  
**Program:** Cybersecurity  
**GitHub:** [Dalairr](https://github.com/Dalairr)

---

## Acknowledgments

**Instructor:** Amalan Pulendran  
**Course:** CYBR3220 - Scripting for Cyber Professionals  
**Institution:** Dunwoody College of Technology
