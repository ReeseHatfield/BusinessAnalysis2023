from src.parsing.DataReader import DataReader
import os
import pickle
import datetime


def main():
    # Load weather data
    weather_pickle_path = os.path.join('dataset', 'weather_data_by_day.pkl')
    weather_data = load_weather_data_from_pickle(weather_pickle_path)

    # Load sales data
    reader = DataReader(os.path.join('dataset', 'dataSet.csv'))

    # Process each month
    for i in range(1, 13):
        current_month: int = i
        avg_sales_on_normal_day = reader.get_avg_sales_per_day_in_month(current_month)

        # Calculate average temperature for the current month
        avg_temp = calculate_avg_temp_for_month(current_month, weather_data)
        print(f"Average Temperature for month {current_month}: {avg_temp}")

        # Calculate sales percentage effects for each weather condition for the current month
        month_effects = calculate_sales_percentage_effects(reader, weather_data, current_month)
        print(f"Sales effects for month {current_month}: {month_effects}")


def calculate_sales_percentage_effects(reader, weather_data, month):
    NORMAL_TEMP_DIFF = 10

    avg_month_temp = calculate_avg_temp_for_month(month, weather_data)

    hot_upper_bound = avg_month_temp + NORMAL_TEMP_DIFF
    cold_lower_bound = avg_month_temp - NORMAL_TEMP_DIFF

    avg_sales_on_normal_day = reader.get_avg_sales_per_day_in_month(month)

    weather_condition_sales = {
        "Precipitating_Hot": [],
        "Precipitating_Normal": [],
        "Precipitating_Cold": [],
        "Not_Precipitating_Hot": [],
        "Not_Precipitating_Normal": [],
        "Not_Precipitating_Cold": [],
    }

    date_sales_dict = reader.get_sales_by_day()

    for date, sales in date_sales_dict.items():
        if date.month == month:
            precipitation, temp = weather_data[date.date()]

            condition = "Precipitating" if precipitation > 0.5 else "Not_Precipitating"
            if temp > hot_upper_bound:
                condition += "_Hot"
            elif temp < cold_lower_bound:
                condition += "_Cold"
            else:
                condition += "_Normal"

            weather_condition_sales[condition].append(sales)

    # Calculate average sales under each weather condition and convert it to percentage
    weather_condition_effects = {}
    for condition, sales in weather_condition_sales.items():
        avg_sales = sum(sales) / len(sales) if sales else 0
        effect = (avg_sales - avg_sales_on_normal_day) / avg_sales_on_normal_day * 100
        weather_condition_effects[condition] = effect

    return weather_condition_effects
def calculate_avg_temp_for_month(month: int, weather_data: dict):
    total_temp = 0
    total_days = 0
    for date, weather in weather_data.items():
        if date.month == month:
            total_temp += weather[1]  # Assuming the second element of the tuple is temperature
            total_days += 1

    if total_days == 0:
        return None

    avg_temp = total_temp / total_days
    return avg_temp



def load_weather_data_from_pickle(weather_pickle_path: str):
    weather_data = None

    if not os.path.exists(weather_pickle_path):
        print(f"File does not exist: {weather_pickle_path}")
        raise FileNotFoundError

    try:
        with open(weather_pickle_path, 'rb') as f:
            weather_data = pickle.load(f)
    except (pickle.UnpicklingError, EOFError) as e:
        print(f"Error while reading the pickle file: {str(e)}")
        weather_data = None

    return weather_data


if __name__ == "__main__":
    main()
