# This program prompts for user to enter US phone number, US Social Security Number, and ZIP code, then
# validates the standard format for a US phone number includes a three-digit area code followed by a seven-digit local
# number, the US Social Security number (SSN) is a nine-digit number formatted as XXX-XX-XXXX, where the hyphens
# separate the number into three parts: the area number (first three digits), the group number (middle two digits),
# and the serial number (last four digits), and US ZIP codes are formatted as either a 5-digit number or
# a 5-digit number followed by a hyphen and a 4-digit number (ZIP+4 format).

import re

def verify_phone_number(phone_number):

    phone_format = r'\d{3}-\d{3}-\d{4}'
    is_valid_phone = re.fullmatch(phone_format, phone_number)

    while True:
        if is_valid_phone:        
            return is_valid_phone.group()
        else:
            return False


def verify_ssn(ssn):
    
    ssn_format = re.compile(r"\d{3}-\d{2}-\d{4}")
    is_valid_ssn = re.fullmatch(ssn_format, ssn)

    while True:
        if is_valid_ssn:
            return is_valid_ssn.group()
        else:
            return False

    

def verify_zip_code(zip_code):

   zip_code_format = re.compile(r"\d{5}|\d{5}-\d{4}")
   is_valid_zip_code = re.fullmatch(zip_code_format, zip_code)

   while True:
        if is_valid_zip_code:
            return is_valid_zip_code.group()
        else:
            return False


    
def main():
    while True:
        phone_number = input("Enter a phone # (format: 941-752-5504):")
        if verify_phone_number(phone_number):
            break
        else:
            print("You've entered an invalid phone number.")

    while True:
        ssn = input("Enter a social security # (format: 732-52-1199): ")
        if verify_ssn(ssn):
            break
        else:
            print("You've entered an invalid SSN.")

    while True:
        zip_code = input("Enter a ZIP code: (format: 34209 or 34209-1234): ")
        if verify_zip_code(zip_code):
            break
        else:
            print("You've entered an invalid ZIP code.")


    divider = '*' * 30
    print()
    print(divider)
    print("\tInput Summary")
    print(divider)
    print(f"Phone Number: {phone_number}")
    print(f"Social Security #: {ssn}")
    print(f"ZIP code: {zip_code}")
    
if __name__ =="__main__":
    main()
