import os
import sys

def verify_config():
    required_vars = ['API_ID', 'API_HASH', 'BOT_TOKEN']
    missing_vars = []
    
    for var in required_vars:
        if not os.environ.get(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("Error: Missing required environment variables:")
        for var in missing_vars:
            print(f"- {var}")
        sys.exit(1)
    
    print("Configuration verified successfully!")
    print("Bot should be ready to run.")

if __name__ == "__main__":
    verify_config()

