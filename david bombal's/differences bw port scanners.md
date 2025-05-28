### What the Port Scanners Do:
All the port scanner scripts aim to identify open ports on a target IP address. Open ports indicate services running on the target machine, which can be useful for network diagnostics or security testing. Here's a breakdown of their functionality:

1. **Input Validation**: They validate the IP address and port range provided by the user.
2. **Port Scanning**: They attempt to connect to each port in the specified range to determine if it is open.
3. **Output**: They display the status of each scanned port (open, closed, or filtered).

---

### Differences Between the Port Scanners:

#### **`port_scanner_regex.py`**
- **Features**:
    - Uses regular expressions to validate IPv4 addresses and port ranges.
    - Implements basic socket-based scanning.
    - Does not differentiate between filtered and closed ports.
- **Complexity**: Low. Simple implementation with minimal validation.

#### **`port_scanner_ip_obj.py`**
- **Features**:
    - Uses the `ipaddress` module for IP validation.
    - Implements socket-based scanning.
    - Similar to `port_scanner_regex.py` but with stricter IP validation.
- **Complexity**: Medium. Adds better IP validation.

#### **`nmap_port_scanner.py`**
- **Features**:
    - Uses the `nmap` Python module for scanning.
    - Provides more detailed results, including port states (open, closed, filtered).
    - Requires `nmap` to be installed on the system.
- **Complexity**: High. Leverages `nmap` for advanced scanning capabilities.

#### **`nmap_port_scanner_ip_obj.py`**
- **Features**:
    - Combines `ipaddress` validation with `nmap` scanning.
    - Similar to `nmap_port_scanner.py` but with stricter IP validation.
- **Complexity**: High. Adds robust IP validation to `nmap` scanning.

---

### Key Differences:
1. **Validation**:
    - `port_scanner_regex.py` uses regex for IP validation.
    - `port_scanner_ip_obj.py` and `nmap_port_scanner_ip_obj.py` use the `ipaddress` module for stricter validation.

2. **Scanning Method**:
    - `port_scanner_regex.py` and `port_scanner_ip_obj.py` use basic socket-based scanning.
    - `nmap_port_scanner.py` and `nmap_port_scanner_ip_obj.py` use the `nmap` module for more advanced scanning.

3. **Output Detail**:
    - Socket-based scanners provide basic results (open/closed).
    - `nmap`-based scanners provide detailed results, including filtered ports and service information.

4. **Dependencies**:
    - Socket-based scanners require no external tools.
    - `nmap`-based scanners require the `nmap` tool and its Python module.