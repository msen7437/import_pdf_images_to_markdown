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
parser.add_argument("-n", "--namescheme", help="namescheme for images")
parser.add_argument(
    "-r", "--resolution", help="resolution of the images default 200"
)
args = parser.parse_args()


def main():
    if args.resolution == None:
        args.resolution = 200
    if args.namescheme == None:
        args.namescheme = "image"
    pdf_to_image(args.input, args.output, args.namescheme, args.resolution)
    write_images_to_markdown(args.output, args.output, args.filename)


def pdf_to_image(
    pdf_path, image_path, image_name_scheme="image", resolution=200
):
    pages = convert_from_path(pdf_path, resolution)
    index = 1
    for page in pages:
        print(page)
        page.save(
            os.path.join(
                image_path, "images", image_name_scheme + str(index) + ".jpg"
            ),
            "JPEG",
        )
        index += 1


def write_images_to_markdown(markdown_directory, image_directory, filename):
    images = os.path.join(image_directory, "images")
    with open(os.path.join(markdown_directory, filename), "w") as f:
        for image in os.listdir(images):
            if image.endswith(".jpg"):
                f.write("![%s](%s)\n" % (image, os.path.join("images", image)))


if __name__ == "__main__":
    main()
