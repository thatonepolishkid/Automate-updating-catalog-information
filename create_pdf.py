#!/usr/bin/env python3
import sys
from reports import generate as report
from emails import generate as email_generate
from emails import send as email_send





def fruit_dict_to_table(fruit_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["name",  "weight"]]
  table_data.extend([item['name'], item['weight']] for item in fruit_data['fruit'])
  return table_data

def main(argv):
    data = load_data('file location')
    summary = process_data(data)
    new_summary = ''.join(summary)
    print(summary)
    report("/tmp/cars.pdf", "Cars Report", new_summary, fruit_dict_to_table(data))
    message = email_generate("automation@example.com", "username@example.com", "sales summary for last month", new_summary, "/tmp/cars.pdf")
    email_send(message)

if __name__ == "__main__":
    main(sys.argv)

