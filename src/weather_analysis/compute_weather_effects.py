import os
import pickle
import datetime

def main():
    weather_pickle_path = os.path.join('dataset', 'weather_data_by_day.pkl')
    weather_data = None

    with open(weather_pickle_path, 'rb') as f:
        weather_data = pickle.load(f)
    # date_to_retrieve = datetime.date(2020, 9, 1)  
    # data = weather_data[date_to_retrieve]  
    # print(data)  


if __name__ == "__main__":
    main()