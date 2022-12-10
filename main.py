# Local imports
from build_stop_words import build_json

# External imports
from google.cloud import storage


def main():
    print("Building the stop word list.")
    build_json()

if __name__ == "__main__"():
    main()
