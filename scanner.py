import nmap

def scan_target(target):
    """
    Scans a given target for open ports and vulnerabilities using Nmap.
    
    :param target: IP address or domain to scan.
    :return: Dictionary with scan results.
    """
    nm = nmap.PortScanner()
    scan_results = {}

    try:
        # Perform a scan with Nmap
        nm.scan(target, arguments="--script=vuln -Pn")

        for host in nm.all_hosts():
            scan_results[host] = {
                "host": host,
                "status": nm[host].state(),
                "ports": []
            }

            for proto in nm[host].all_protocols():
                for port in nm[host][proto].keys():
                    port_info = nm[host][proto][port]
                    scan_results[host]["ports"].append({
                        "port": port,
                        "state": port_info["state"],
                        "service": port_info.get("name", "unknown"),
                        "vulnerabilities": port_info.get("script", {})
                    })

    except Exception as e:
        return {"error": str(e)}

    return scan_results
