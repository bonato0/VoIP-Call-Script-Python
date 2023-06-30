# VoIP Call Script Documentation
This script utilizes the pjsua2 library to initiate a VoIP call using the PJSIP library. It accepts command-line arguments to specify the extension (--ramal) and the number to call (--num).

## Prerequisites
Before running the script, make sure you have the following prerequisites:

Python 3 installed on your system.
The pjsua2 library and its dependencies installed.
To install the requirements, please refer to the [PJSUA2-High Level API Documentation](https://www.pjsip.org/docs/book-latest/html/intro_pjsua2.html#building-pjsua2).

## Usage
To use the script, follow the steps below:

In call-script.py file, change the <IP> for your PABX IP.

Open a terminal or command prompt.

Run the script with the desired command-line arguments:

```shell
python3 call-script.py --ramal <extension> --num <number>
```
Replace <extension> with the extension for the call and <number> with the number to call.

The script will initiate the VoIP call to the specified extension/number and will keep the call active for 300 seconds or until terminated (adjustable in the code). After the call, it will print a message indicating that the call has ended.

This will creates an empty call with no audio. If necessary, it can be included directly in the PABX

## Command-line Arguments
The script accepts the following command-line arguments:

--ramal: Specifies the extension for the call. It is a required argument. Example usage: --ramal 1001

--num: Specifies the number to call. It is a required argument. Example usage: --num 123456789

## Code Overview
The code consists of the following main components:

parse_arguments(): This function parses the command-line arguments using the argparse module. It retrieves the values of --ramal and --num, performs validation, and returns the formatted extension and number.

Account class: This class represents the SIP account for making the VoIP call. It configures the Endpoint, initializes it, creates a transport for UDP communication, and starts the library.

make_call(ramal, num): This function creates an instance of the Account class, configures it with the provided extension and number, creates a call instance, initiates the call, and waits for the specified duration. Finally, it destroys the library endpoint and prints a message indicating the call has ended.

main(): This function serves as the entry point of the script. It calls parse_arguments() to retrieve the extension and number, and then calls make_call(ramal, num) to initiate the VoIP call.

## Library Documentation
For detailed documentation on the pjsua2 library and its classes, methods, and configuration options, please refer to the following resources:

Official PJSUA2 Documentation: https://www.pjsip.org/docs/book-latest/html/
