import csv


def get_year(book):
    return book["Year"]


# Add to library should add a book to our library saved to disk.
def add_to_library():
    title = input("Title: ")
    author = input("Author: ")
    year = input("Year: ")
    series = input("Series: ")

    with open("library.csv", "a") as library:
        fieldnames = ["Author", "Title", "Year", "Series"]
        writer = csv.DictWriter(library, fieldnames=fieldnames)
        writer.writerow(
            {"Title": title, "Series": series, "Author": author, "Year": year}
        )


# View library should let us view our library in the terminal.
def view_library():
    grouped_by_author = {}

    with open("library.csv", "r") as library:
        reader = csv.DictReader(library)
        for row in reader:
            title = row["Title"]
            author = row["Author"]
            year = row["Year"]
            series = row["Series"]

            if author in grouped_by_author:
                if series in grouped_by_author[author]:
                    grouped_by_author[author][series].append(
                        {"Title": title, "Year": year}
                    )
                else:
                    grouped_by_author[author][series] = [{"Title": title, "Year": year}]
            else:
                grouped_by_author[author] = {series: [{"Title": title, "Year": year}]}

    for author in grouped_by_author:
        print()
        print(author)
        for series in grouped_by_author[author]:
            if series is not None:
                print(f"  {series}")
            grouped_by_author[author][series].sort(key=get_year)
            for book in grouped_by_author[author][series]:
                print(f"""    {book["Title"]}, {book["Year"]}""")
        print()


def get_option(options):
    while True:
        try:
            number_input = int(input("What would you like to do?: "))
            if number_input not in options:
                raise ValueError
            return number_input
        except ValueError:
            print("  Invalid option")


def print_header():
    print("PYBIB")
    print("=====")
    print("Options:")
    print("  1. View library")
    print("  2. Add to library")
    print()


# Entry point to our program.
def main():
    print_header()
    option = get_option([1, 2])
    if option == 1:
        view_library()
    elif option == 2:
        add_to_library()


if __name__ == "__main__":
    main()
