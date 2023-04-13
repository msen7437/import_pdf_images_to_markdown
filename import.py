# convert pdf to image
from pdf2image import convert_from_path
import argparse
import os

# receive arguments -i for input and -o for output

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input pdf file")
parser.add_argument("-o", "--output", help="output directory")
# add filename
parser.add_argument("-f", "--filename", help="output markdown file")
args = parser.parse_args()


def main():
    pdf_to_image(args.input, args.output)
    print("--------------------------")
    write_images_to_markdown(args.output, args.output, args.filename)


def pdf_to_image(pdf_path, image_path):
    pages = convert_from_path(pdf_path, 500)
    index = 1
    for page in pages:
        page.save(
            os.path.join(image_path, "images", str(index) + ".jpg"), "JPEG"
        )
        index += 1


def write_images_to_markdown(markdown_directory, image_directory, filename):
    images = os.path.join(image_directory, "images")
    with open(os.path.join(markdown_directory, filename), "w") as f:
        for image in os.listdir(images):
            f.write("![%s](%s)\n" % (image, os.path.join("images", image)))


if __name__ == "__main__":
    main()
