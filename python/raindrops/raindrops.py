def convert(number):
    nu_string = ''
    if number % 3 == 0:
        nu_string += 'Pling'
    if number % 5 == 0:
        nu_string += 'Plang'
    if number % 7 == 0:
        nu_string += 'Plong'
    if nu_string == '': 
        nu_string = str(number)
    return nu_string 
 
