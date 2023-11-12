import os
import pydoc
import shutil

from dotenv import load_dotenv

from logger import Log

log = Log(module_name="initialization")

load_dotenv()


def move_html_to_directory():
    """
    Move created HTML files to the ./docs/ directory
    """
    if os.getenv("IS_DEBUG_MODE") == "False":
        return

    file_extension = ".html"
    source_directory = "./"

    destination_directory = os.path.join(source_directory, "..", "docs")

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    for filename in os.listdir(source_directory):
        if filename.endswith(file_extension):
            source_path = os.path.join(source_directory, filename)
            destination_path = os.path.join(destination_directory, filename)

            shutil.move(source_path, destination_path)
            log.info(f"Moved {filename} to {destination_directory}")


def combine_html_files():
    """
    Combine all the html files in the directory to create a new file with all docs in one
    """
    # Directory containing HTML files
    html_directory = "./"

    # Initialize an empty string to store the combined HTML content
    combined_html = ""

    # List all HTML files in the directory
    for filename in os.listdir(html_directory):
        if filename.endswith(".html"):
            file_path = os.path.join(html_directory, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                file_content = file.read()
                combined_html += file_content

    # Specify the name of the output HTML file
    output_file = "documentation.html"

    # Write the combined content to the output HTML file
    with open(output_file, "w", encoding="utf-8") as output:
        output.write(combined_html)

    log.info(f"Combined HTML saved to {output_file}")


def write_pydoc_to_docs():
    """
    if IS_DEBUG_MODE == True
    Write pydoc html files for all python files in ./api/ and move to ./docs/
    """
    debug = os.getenv("IS_DEBUG_MODE")

    if debug == "True":
        log.info(f"Writing documentation. Please wait...")

        pydoc.writedocs("./")
        combine_html_files()
        move_html_to_directory()

        log.info(f"Completed writing documentation")
    else:
        log.error(f"Cannot write logs when IS_DEBUG_MODE is not True")


if __name__ == "__main__":
    write_pydoc_to_docs()
