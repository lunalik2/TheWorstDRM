# TheWorstDRM

I hate DRMs just as much as you, this is just a POC. If I planned on using it, it wouldn't be open source.
Anyways, this is a very secure DRM, and was quite interesting to make. I hope you enjoy.

# Documentation

1. The first script parses an online document, and searches for a user defined activation key

2. The script then asks you what the activation key is, to verify legitimacy (this is insecure, as the activation key is the same for everyone, so I may change this. You may submit a pull request if you have an idea)

3. After the verification, the script searches for your ProductID in the registry

4. The ProductID is in binary, so it then decrypts it into a string

5. The script then takes the ProductID, and encypts it into bytes using the encryption key you defined

6. The encrypted ProductID is then saved into a file, one that cannot be read without the key

7. The second script first searches for the file we just made

8. If it exists, it goes through the process of fetching your ProductID again

9. It then decrypts the file we created earlier, using the encryption key, back into a string

10. Finally, the program validates the string. If it matches with the ProductID, it runs the code, if not, it cancels

# Requirements

- A recent version of Windows 10

- Python 3.0 - 3.6 (no 3.7 support at the moment)

# Usage

**THIS IS NOT FOR USE WITH PAID SOFTWARE, ABIDING OF THIS RULE WILL HAVE CONCEQUENCES**

1. Change the encryption key variable named "secret" in both scripts, to any 16 character string (make sure there is a "b" before the quotation marks, just as there is now)

2. Change the activation key, by changing the google docs link to your own google doc, containing the following format: "Key:**YourActivationKeyHere**:Key" (the default key is **7PBREIDSEKLG547**, and the context would be Key:**7PBREIDSEKLG547**:Key)

3. Add your own already tested code in the area provided within "DRM_Test.py" (you can find it near the bottom)

4. After saving the scripts, run the "compile.bat"

5. The compiled executables can be found in the newly created "dist" folder

6. Enjoy

# Credit

Credit for [pycryptodome](https://github.com/Legrandin/pycryptodome) goes to [Legrandin](https://github.com/Legrandin), and collaborators

Credit for [pyinstaller](https://github.com/pyinstaller/pyinstaller/) goes to the [pyinstaller](https://github.com/pyinstaller) team
