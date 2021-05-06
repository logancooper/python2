phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

def phonenumber(myDict):
    print(phonebook_dict['Elizabeth'])

def add_to_dict(myDict):
    phonebook_dict['Kareem'] = '938-489-1234'
    print(phonebook_dict['Kareem'])

def delete_alice(myDict):
    del phonebook_dict['Alice']
    print(phonebook_dict)

def change_bob_number(myDict):
    phonebook_dict['Bob'] = '968-345-2345'

def print_all_phone_numbers(myDict):
    for key, value in phonebook_dict.items():
        print("%s's phone number is %s" % (key, value))

phonenumber(phonebook_dict)
add_to_dict(phonebook_dict)
delete_alice(phonebook_dict)
change_bob_number(phonebook_dict)
print_all_phone_numbers(phonebook_dict)
    