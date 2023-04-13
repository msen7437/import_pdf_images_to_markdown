# Script to automatically paste pdf pages as images to a markdown file

### Dependencies:

- Python 3

- `pdf2image` module

  ```shel
  $ pip install pdf2image
  ```

- Poppler PDF-Engine

  ```shell
  $ sudo apt-get install poppler-utils
  ```

  - Put bin to environment path

    - change `/etc/environment` file

      ```
      PATH="/usr/bin:/some/other/path:/usr/lib/poppler-utils"
      ```

      

### Parameters:

`-i` -> path to the pdf file

`-o` -> output directory where the images and the markdown file will be dumped in

`-f` -> filename of the markdown file



### Run:

```shell
$ python3 import.py -i path/to/file.pdf -o path/to/output/ -f example.md
```



### Disclaimer:

- All images will be dumped into the `images` folder inside the `output` directory
- I was to lazy to do error handling, so make sure all the directories exist
- Every output file will be generated on its own.
- Delete all the images in the `images` folder before running the script again using the same parameters