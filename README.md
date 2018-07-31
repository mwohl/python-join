# python-join
Join lines from two files on common key

## Requirements:
Python >= 3.5

## Installation/Configuration:
Clone the GitHub repository:

``` 
git clone https://github.com/mwohl/python-join.git
```

Add the installation directory to your $PATH environment variable.  
  On Linux/Unix systems, add the following line to your ~/.profile or ~/.bashrc file:

    ``` 
    export PATH="$PATH:/path/to/installation"
    ```

    then reload your profile:

    ` source ~/.profile` or `source ~/.bashrc`
  On Windows systems, modify the user's PATH environment variable through **Control Panel** > **System** > **Advanced system settings** > **Environment Variables**.

## Usage:
``` 
python-join [-h] [--left-key LEFT_KEY] [--right-key RIGHT_KEY]
                   left_file right_file

positional arguments:
  left_file             name of file to be used as left file in key join
  right_file            name of file to be used as right file in key join

optional arguments:
  -h, --help            show this help message and exit
  --left-key LEFT_KEY   index to use as key in left file
  --right-key RIGHT_KEY
                        index to use as key in right file
```

## Example:
``` 
python-join a.txt b.txt
```

## Accepted Input Files:
Text files with whitespace-separated values, containing 7-bit ascii bytes only, with lines ending in newline character.
