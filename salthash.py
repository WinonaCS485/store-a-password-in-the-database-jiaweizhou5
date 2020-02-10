from passlib.hash import sha512_crypt
import bcrypt

# Connect to database
connection = pymysql.connect(host='mrbartucz.com',
                             user='cl8355ps',
                             password='Winona',
                             db='cl8355ps_password',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
	with connection.cursor() as cursor:

	# Ask user to store a password
    psw = input("Create your password: ")

    # Generate salt and hash the password
    # Use salt generator from bcrypt crypto library
    salt = bcrypt.gensalt()
    hashed = hashPsw(psw, salt)

	# Insert the created pssword into database
	# Stores the salt and hash in database - NOT the password
    sql = "INSERT INTO User_Password(salt, hash) VALUES(%s, %s)"
    cursor.execute(sql, (salt,hashed))
    connection.commit()

    # Ask the user to enter it again
    check = input("Check your password: ")

    # Check if password in file
    sql = "SELECT * FROM User_Password"
    cursor.execute(sql)
    
    for row in cursor:
        salt = row['Salt']
        hashed = row['Hash']
        
        hashedCheck = hashPsw(check, salt)
        
        if hashedCheck == hashed:
            print("[Y] Entered password found")
        else:
            print("[N] Entered password not found")

finally:
    connection.close()


# Hash the salted password
def hashPsw(password, salt):
	saltedPsw = password + salt
    return hashed = hashlib.sha512(str.encode()).hexdigest()

