import time

def log_error(message):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")  
    report = f"[{ts}] ERROR: {message}\n"
    
    # Append to error.log
    with open("error.log", "a") as f:
        f.write(report)

for i in range(5):
    log_error(f"Run time Error {i+1}")
