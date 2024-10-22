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