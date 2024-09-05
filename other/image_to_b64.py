def image_to_base64(image_file, output_file):
    # need base 64
    import base64
    import sys

    # open the image
    image = open(image_file, "rb")
    # read it
    image_read = image.read()
    # encode it as base 64
    # after python>=3.9, use `encodebytes` instead of `encodestring`
    image_64_encode = (
        base64.encodestring(image_read)
        if sys.version_info < (3, 9)
        else base64.encodebytes(image_read)
    )
    # convert the image base 64 to a string
    image_string = str(image_64_encode)
    # replace the newline characters
    image_string = image_string.replace("\\n", "")
    # replace the initial binary
    image_string = image_string.replace("b'", "")
    # replace the final question mark
    image_string = image_string.replace("'", "")
    # add the image tags
    image_string = '<p><img src="data:image/png;base64,' + image_string + '"></p>'
    # write it out
    image_result = open(output_file, "w")
    image_result.write(image_string)
    image_result.close()


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("img_file", type=str)
    parser.add_argument("-o", "--output", type=str, required=False)
    args = parser.parse_args()
    output_file = args.output
    if output_file is None:
        output_file = args.img_file.split(".")[0] + ".txt"
    image_to_base64(args.img_file, output_file)


if __name__ == "__main__":
    main()
