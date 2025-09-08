import secret
import os



print("enter secret code: ")
code = input()

if code != secret.mon_code_super_secret:
    print("wrong code entered.")

elif code == secret.mon_code_super_secret:

    # check if file exist
    if os.path.exists(secret.secret_file_path):
        # read the file
        print("secret file content:")
        with open(secret.secret_file_path, "r") as f:
            print(f.read())
        # propose to update the file
        print("\nOverride new text? (n/y): ")
        a = input()
        if a == "y" or a == "Y":
            print("enter new text:")
            text = input()
            with open(secret.secret_file_path, "w") as f:
                f.write(text)
    
    # create the file
    else:
        print("no secret file found, enter text to secret file:")
        text = input()
        with open(secret.secret_file_path, "w") as f:
            f.write(text)