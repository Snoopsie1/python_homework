import argparse
import webget as wg

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that saves an URL')
    parser.add_argument('url', type=str, help="enter an URL please")
    parser.add_argument('-d', default=None, help='The name of the file to store the url in')
    args = parser.parse_args()
    
    if args.d == None:
        args.d = args.url[:3]
    
    wg.download(args.url,args.d)
    