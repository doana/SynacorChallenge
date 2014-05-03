#!/usr/bin/python
import argparse, logging
from challenge import vm

def main():

    #Set up and parse command line arguments
    parser = argparse.ArgumentParser(description='Runs a synacor challenge VM binary.')
    parser.add_argument('binary', type=argparse.FileType('rb'), help='The path to a challenge VM binary.') 
    parser.add_argument('--log', type=str, choices=['info', 'debug'], help='Logging level to use')
    args = parser.parse_args()

    #Set up logging
    logging.basicConfig(filename='challenge.log')
    logger = logging.getLogger()
    if args.log:
        logger.setLevel(args.log.upper())
    else:
        logger.setLevel(logging.INFO)
    
    #Set up VM
    machine = vm.VM(args.binary, logger)
    machine.run() 

if __name__ == '__main__':
    main()
