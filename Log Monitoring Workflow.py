import os  # For accessing files and directories
import re  # For using regular expressions to analyze log data
import smtplib  # For sending email alerts
from email.mime.text import MIMEText  # To format email content
import datetime  # For checking if it's Sunday for weekly reporting

# Path to shared folder where logs are stored (adjust as needed)
SHARED_FOLDER = r"Z:\"

# List of Linux log files to analyze
linux_log_files = ["auth.log", "syslog", "apache_access.log", "apache_error.log", "weekly_logs.txt"]

# List of Windows log files to analyze (exported as .txt or .csv from Event Viewer)
windows_log_files = ["Application.txt", "Security.txt", "System.txt"]

# Regex patterns to identify issues in logs based on structure, not keywords
patterns = {
    "failed_login": r"\b(?:Failed|Invalid)\b.*\b(?:login|authentication)\b",  # Matches failed login attempts
    "unauthorized_access": r"\b(?:Unauthorized|Access Denied|403)\b",         # Matches unauthorized access attempts
    "system_error": r"\b(?:ERROR|CRITICAL|PANIC|FAILURE)\b.*",                # Matches system errors
    "ip_suspicious": r"(?:\d{1,3}\.){3}\d{1,3}",                             # Matches IP addresses (e.g., for brute force detection)
}

# Email configuration for sending alerts and reports
SMTP_SERVER = "smtp.gmail.com"    # Replace with your SMTP server address
SMTP_PORT = 587                   # SMTP port (587 for TLS)
EMAIL_ADDRESS = os.EMAIL_ADDRESS  # My email address (stored in an env file)
EMAIL_PASSWORD = os.EMAIL_PASSWORD# My email password (stored in an env file)

# Function to analyze a single log file using regex patterns
def analyze_log(file_path):
    """
    Analyzes a log file for specific patterns using regex.
    
    Args:
        file_path (str): Path to the log file.
    
    Returns:
        dict: A dictionary with issue types as keys and their occurrence counts as values.
    """
    issues_found = {}  # Dictionary to store counts of each issue type
    
    try:
        with open(file_path, "r") as file:  # Open the log file in read mode
            for line in file:  # Read each line in the file
                for issue, pattern in patterns.items():  # Check each regex pattern against the line
                    if re.search(pattern, line):  # Search for the pattern in the line
                        issues_found[issue] = issues_found.get(issue, 0) + 1  # Increment count for matched issue type
    except FileNotFoundError:
        print(f"Log file not found: {file_path}")
    
    return issues_found

# Function to generate explanations based on analysis results
def generate_explanations(results):
    """
    Generates human-readable explanations for detected issues.
    
    Args:
        results (dict): Dictionary of detected issues and their counts.
    
    Returns:
        list: A list of explanations for the detected issues.
    """
    explanations = []  # List to store explanations
    
    if results.get("failed_login", 0) > 0:  # Check if failed login attempts were detected
        explanations.append(f"{results['failed_login']} failed login attempts detected.")
    
    if results.get("unauthorized_access", 0) > 0:  # Check if unauthorized access attempts were detected
        explanations.append(f"{results['unauthorized_access']} unauthorized access attempts detected.")
    
    if results.get("system_error", 0) > 0:  # Check if system errors were detected
        explanations.append(f"{results['system_error']} system errors detected.")
    
    if results.get("ip_suspicious", 0) > 0:  # Check if suspicious IP addresses were detected
        explanations.append(f"{results['ip_suspicious']} suspicious IP addresses found.")
    
    return explanations

# Function to send an email alert or report
def send_email(subject, body):
    """
    Sends an email with a given subject and body.
    
    Args:
        subject (str): Email subject.
        body (str): Email body content.
    """
    msg = MIMEText(body)  # Format the email body as plain text
    msg["Subject"] = subject  # Set the email subject
    msg["From"] = EMAIL_ADDRESS  # Sender's email address
    msg["To"] = EMAIL_ADDRESS  # Recipient's email address (can be modified)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:  # Connect to SMTP server
            server.starttls()  # Start TLS encryption for secure communication
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Log in to the SMTP server
            server.send_message(msg)  # Send the email message
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Main script logic

# Analyze Linux logs in the shared folder
for log_file in linux_log_files:
    log_path = os.path.join(SHARED_FOLDER, log_file)  # Construct full path to the log file
    
    if os.path.exists(log_path):  # Check if the log file exists in the shared folder
        print(f"Analyzing Linux log: {log_file}")
        
        results = analyze_log(log_path)  # Analyze the log file using regex patterns
        
        explanations = generate_explanations(results)  # Generate explanations for detected issues
        
        if explanations:  # If any issues were found, print them and send an alert email
            print(f"Issues found in {log_file}:")
            for explanation in explanations:
                print(f"- {explanation}")
            
            body = "\n".join(explanations)  # Combine all explanations into a single string for the email body
            
            send_email(f"Alert: Issues Detected in {log_file}", body)  # Send an alert email

# Analyze Windows logs in the shared folder (exported from Event Viewer)
for log_file in windows_log_files:
    log_path = os.path.join(SHARED_FOLDER, log_file)  # Construct full path to the Windows log file
    
    if os.path.exists(log_path):  # Check if the Windows log file exists in the shared folder
        print(f"Analyzing Windows log: {log_file}")
        
        results = analyze_log(log_path)  # Analyze the Windows log file using regex patterns
        
        explanations = generate_explanations(results)  # Generate explanations for detected issues
        
        if explanations:  # If any issues were found, print them and send an alert email
            print(f"Issues found in {log_file}:")
            for explanation in explanations:
                print(f"- {explanation}")
            
            body = "\n".join(explanations)  # Combine all explanations into a single string for the email body
            
            send_email(f"Alert: Issues Detected in {log_file}", body)  # Send an alert email

# Weekly report generation (runs on Sunday)
if datetime.datetime.now().weekday() == 6:  # Check if today is Sunday (weekday() returns 6 for Sunday)
    print("Generating weekly report...")
    
    report_lines = []  # List to store report content
    
    for log_file in linux_log_files + windows_log_files:
        log_path = os.path.join(SHARED_FOLDER, log_file)
        
        if os.path.exists(log_path):
            results = analyze_log(log_path)  # Analyze each log file
            
            explanations = generate_explanations(results)  # Generate explanations
            
            report_lines.append(f"--- {log_file} ---")  # Add a header for each log file in the report
            
            report_lines.extend(explanations)  # Add explanations to the report
    
    report_body = "\n".join(report_lines)  # Combine all report lines into a single string
    
    send_email("Weekly Log Report", report_body)  # Send the weekly report via email

print("Log analysis completed.")