#!/usr/bin/env python3

import click

@click.command()
@click.argument("action", required=True)
@click.option("-m", "--model-file", default=None)

def main(action, model_file):
    print(action, model_file)
    
if __name__=="__main__":
    main()
    
