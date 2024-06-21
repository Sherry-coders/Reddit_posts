import csv
import os
import subprocess

base_csv_path = r"C:\Users\ntu-s\OneDrive - Nanyang Technological University\sherry\reddit output\outputs csv reddit"
base_output_path = r"C:\Users\ntu-s\OneDrive - Nanyang Technological University\sherry\reddit output\final outputs reddit (posts and comments)"
reddit_archiver_directory = r"C:\Users\ntu-s\RedditArchiver-standalone-main\RedditArchiver-standalone-main"
reddit_archiver_path = os.path.join(reddit_archiver_directory, 'RedditArchiver.py')

for month in range(1, 13):
    month_str = f"{month:02}"  
    csv_file_path = os.path.join(base_csv_path, f"filtered_posts_{month_str}.csv")
    output_folder = os.path.join(base_output_path, f"reddits_{month_str}")

    os.makedirs(output_folder, exist_ok=True)

    post_ids = []
    if os.path.exists(csv_file_path):
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                post_ids.append(row['id'])

        for post_id in post_ids:
            try:
                command = ['py', '-3', reddit_archiver_path, '-i', post_id, '-o', output_folder]
                subprocess.run(command, check=True, capture_output=True, text=True)

                for filename in os.listdir(output_folder):
                    if filename.endswith('.html') and post_id in filename:  
                        new_filename = f"{post_id}_{filename}"
                        old_path = os.path.join(output_folder, filename)
                        new_path = os.path.join(output_folder, new_filename)
                        os.rename(old_path, new_path)
                        break

            except subprocess.CalledProcessError as e:
                print(f"Error processing post ID {post_id} in month {month_str}: {e}")
            except Exception as e:
                print(f"An unexpected error occurred for month {month_str}: {e}")

        print(f"All HTML files for month {month_str} have been saved to {output_folder}")
    else:
        print(f"No CSV file found for month {month_str}")
