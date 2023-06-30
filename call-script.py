import pjsua2  # Import the pjsua2 library
import time
import argparse

ip = '127.0.0.1' #Put your PABX IP here

def parse_arguments():
    # Create an argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--ramal', action='store', dest='ramal_number', help='Extension for the call')
    parser.add_argument('--num', action='store', dest='number', help='Number to call')
    args = parser.parse_args()

    if args.ramal_number is not None:
        ramal = "sip:" + args.ramal_number + "@" + ip  # Format the extension for the call
    else:
        parser.error("The '--ramal' argument is required. Please specify the extension for the call.")

    if args.number is not None:
        num = "sip:" + args.number + "@" + ip  # Format the number to call
    else:
        parser.error("The '--num' argument is required. Please specify the number to call.")
    
    return ramal, num

class Account(pjsua2.Account):
    ep_cfg = pjsua2.EpConfig()
    ep = pjsua2.Endpoint()
    ep.libCreate()
    ep.libInit(ep_cfg)

    sipTpConfig = pjsua2.TransportConfig()
    sipTpConfig.port = 5060  # Set the port for the transport
    ep.transportCreate(pjsua2.PJSIP_TRANSPORT_UDP, sipTpConfig)
    ep.libStart()

def make_call(ramal, num):
    acfg = pjsua2.AccountConfig()
    acfg.idUri = num  # Set the identity URI for the account
    acfg.regConfig.registrarUri = "sip" + ip  # Set the registrar URI for the account

    creds = pjsua2.AuthCredInfo("digest", "ccmsipline", "user", 0, "12345")  # Set authentication credentials
    acfg.sipConfig.authCreds.append(creds)

    acc = Account()  # Create an instance of the Account class
    acc.create(acfg)  # Create the account

    call = pjsua2.Call(acc)  # Create a call instance

    prm = pjsua2.CallOpParam()  # Create a call operation parameter instance

    call.makeCall(ramal, prm)  # Initiate the call to the specified extension/number

    time.sleep(300)  # Sleep for 300 seconds (placeholder for call duration)
    acc.ep.libDestroy()  # Destroy the library endpoint

    print("Call ended")  # Print a message indicating the call has ended

def main():
    ramal, num = parse_arguments()
    make_call(ramal, num)

if __name__ == "__main__":
    main()
