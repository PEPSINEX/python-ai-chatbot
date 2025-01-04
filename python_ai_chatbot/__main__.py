import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    SAMPLE_KEY = os.getenv("SAMPLE_KEY")

    print(SAMPLE_KEY)

if __name__ == "__main__":
    main()
