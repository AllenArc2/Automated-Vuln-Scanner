import nmap
from scanner import scan_target

def test_scan():
    target = '127.0.0.1'  # Localhost for testing
    results = scan_target(target)
    print(results)

if __name__ == "__main__":
    test_scan()
