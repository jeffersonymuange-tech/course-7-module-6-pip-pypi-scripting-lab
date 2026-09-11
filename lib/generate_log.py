from datetime import datetime


def generate_log(data):
    """Writes each entry in `data` to a timestamped log file
    (log_YYYYMMDD.txt) and returns the filename.

    Raises:
        ValueError: if `data` is not a list.
    """
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)