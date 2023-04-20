import zipfile as zf


def extract_archive(archive_path, dest_dir):
    with zf.ZipFile(archive_path, "r") as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("../journal/dest/compressed.zip", "../journal/dest")