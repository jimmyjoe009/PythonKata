# Convert a 10 digit array into phone number format

def create_phone_number(n):
    pn=""
    # Convert the array to string
    for c in n: pn=pn+str(c)
    return("("+pn[0:3]+") "+pn[3:6]+"-"+pn[6:10])
