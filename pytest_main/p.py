import os
work_directory = '/Users/cheongray/iras_api_clean_1/4_format_validation'
xml_file_path = work_directory + "/xml_files_for_4_Format Validation"
filename_for_csv_with_results = work_directory + '/test_results/4_Format_testing_csv_results.csv'
base_df_filepath = work_directory + '/df_full.csv'

print(filename_for_csv_with_results)
if os.path.exists(filename_for_csv_with_results):
    os.remove(filename_for_csv_with_results)
    print(f"File {filename_for_csv_with_results} removed.")