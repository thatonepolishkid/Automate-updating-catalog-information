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
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    report("/tmp/fruit.pdf", "Fruit Report", body, fruit_dict_to_table(data))
    message = email_generate("automation@example.com", "username@example.com", "Upload Completed - Online Fruit Store", body, "/tmp/fruit.pdf")
    email_send(message)

if __name__ == "__main__":
    main(sys.argv)

