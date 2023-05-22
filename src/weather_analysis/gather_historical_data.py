import os
import sys
sys.path.append(os.path.join("src","constants.py"))
from constants import open_weather_key



def main():
    print(open_weather_key)


if __name__ == "__main__":
    main()