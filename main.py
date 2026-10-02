
from cleaner import DataCleaner
from converter import read_csv,write_csv,write_json

def main():
    """Run the full data - cleaning pipeline."""

    file_input = input("enter the input csv filename: ")
    if not file_input :
        file_input = "sample_data.csv"

    rows = read_csv(file_input)
    if not rows:
        print("file not found: exiting program")
        return 
    print(f"[OK] Read {len(rows)} row (s).")

    cleaner = DataCleaner(rows)
    cleaner.cleaner_text_fields(["name","email","city","occupation","company"]).duplicates_remove().validate()

    fieldnames = list(rows[0].keys()) if rows else []
    
    write_csv("clean_data.csv",cleaner.valid_rows,fieldnames)
    write_csv("invalid_data.csv",cleaner.invalid_rows,fieldnames)
    write_json("valid_data.json",cleaner.valid_rows)

    report = cleaner.summary()
    for key,value in report.items():
        print(f"key: {key},value: {value}")

    print("=========REPORT==========")

    print("-clean_data.csv: valid_data")
    print("- invalid_data: problem_data with reasons")
    print("-valid_data.json: json_of_valid_data")


if __name__== "__main__":
    main()
