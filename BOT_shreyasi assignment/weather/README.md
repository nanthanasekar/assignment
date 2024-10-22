
# Weather Data Aggregation Application

## Description
This application processes a list of weather records and aggregates temperature and humidity data for various cities. It calculates the average temperature and humidity for each city, handling missing data gracefully.

## Prerequisites
- Python 3.x installed on your system.
- Basic understanding of Python programming.

## Setup Instructions

1. **Clone the Repository (if applicable)**  
   If you have the code in a repository, clone it using:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a Python File**  
   Create a new Python file, e.g., `weather_aggregator.py`, and copy the following code into it:
   ```python
   def aggregate_weather_data(records):
       city_data_store = {}

       for entry in records:
           location_name = entry.get('city')
           location_temp = entry.get('temperature')
           location_humidity = entry.get('humidity')

           if location_name not in city_data_store:
               city_data_store[location_name] = {
                   'temperature_sum': 0,
                   'temperature_entries': 0,
                   'humidity_sum': 0,
                   'humidity_entries': 0
               }

           if location_temp is not None:
               city_data_store[location_name]['temperature_sum'] += location_temp
               city_data_store[location_name]['temperature_entries'] += 1

           if location_humidity is not None:
               city_data_store[location_name]['humidity_sum'] += location_humidity
               city_data_store[location_name]['humidity_entries'] += 1

       location_averages = {}
       for location_name, stats in city_data_store.items():
           temp_count = stats['temperature_entries']
           humidity_count = stats['humidity_entries']

           avg_temperature = (stats['temperature_sum'] / temp_count) if temp_count > 0 else None
           avg_humidity = (stats['humidity_sum'] / humidity_count) if humidity_count > 0 else None

           location_averages[location_name] = {
               'average_temperature': avg_temperature,
               'average_humidity': avg_humidity
           }

       return location_averages
   ```

3. **Prepare Sample Data**  
   Create a list of weather records (as dictionaries) in your Python file or in a separate JSON file. For example:
   ```python
   weather_records = [
       {'city': 'City A', 'temperature': 25, 'humidity': 60},
       {'city': 'City A', 'temperature': None, 'humidity': 65},
       {'city': 'City B', 'temperature': 30, 'humidity': 55},
       {'city': 'City B', 'temperature': 28, 'humidity': None},
       {'city': 'City C', 'temperature': None, 'humidity': 70}
   ]
   ```

4. **Run the Application**  
   Call the `aggregate_weather_data` function with the sample data and print the results:
   ```python
   if __name__ == "__main__":
       results = aggregate_weather_data(weather_records)
       print(results)
   ```

## Running the Application
- Run the Python file using the command:
   ```bash
   python weather_aggregator.py
   ```
- The output will display the average temperature and humidity for each city based on the provided records.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thank you for using this application!
