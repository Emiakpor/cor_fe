import requests
import plot_chart
import json

def fetch_data_from_api(api_url):
    try:
        response = requests.get(api_url)
        # Check if request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    

def main():
    api_url = "http://127.0.0.1:8000/detect_corrosion/"  # Replace this with the actual API URL
    data_json = fetch_data_from_api(api_url)
    if data_json:
        data = json.loads(data_json)

        print('_classification_report')
        print(data['_classification_report'])
        print('_confusion_matrix')
        print(data['_confusion_matrix'])
        
        plot_chart.plot(data['loss_history'], data['val_loss_history'], data['accuracy_history'], data['val_accuracys_history'],
               data['x_test_prop_class_count'], data['pred_digits_prop_class_count_pre_label'], data['y_test_prop_class_count_actual_label'],
                data['x_test_mis_class_count'], data['pred_digits_mis_class_count_pre_label'], data['y_test_mis_class_count_actual_label'],
            data['labels'], data['_confusion_matrix'])
        
        
    else:
        print("Failed to fetch data from the API.")

if __name__ == "__main__":
    main()