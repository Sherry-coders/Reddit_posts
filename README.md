# Mental Health Reddit Analysis
This repository contains scripts and data for analyzing Reddit posts related to mental health issues among Singaporean youth. The project utilizes keyword expansion techniques and specific subreddit targeting to gather and analyze relevant data.

## Description
This project aims to identify and analyze Reddit posts discussing mental health concerns particularly relevant to Singaporean youth. Using keyword expansion models like Word2Vec and Transformers (BERT), we've enhanced the scope of our search terms to include a broader array of related keywords. The project filters posts from specific subreddits known to engage Singaporean youth, providing insights into their mental health discussions and concerns.

## Tools and Libraries Used
Word2Vec: For semantic similarity and keyword expansion.

Transformers (BERT): For contextual keyword expansion.

RedditArchiver-standalone: Tool for downloading post data (https://github.com/Ailothaen/RedditArchiver-standalone)).

## Process Overview
### Step 1: Keyword Identification and Expansion
- Initial keywords related to mental health were manually selected based on common terminology.
- Word2vec_keywordslist.ipynb and Transformers_keywordslist.ipynb were used to expand these keywords using Word2Vec and BERT models respectively, capturing a wider range of related terms.

### Step 2: Filtering Reddit Posts
-  Seven subreddits were targeted: 'askSingapore', 'NTU', 'nus', 'SGExams', 'singapore', 'SingaporeRaw', and 'NationalServiceSG'.
-  Final_filter_reddit_posts.ipynb processes the complete Reddit posts dataset to filter posts containing the expanded keywords in the specified subreddits.
-  Filtered posts are exported monthly into CSV files for easy access and review, available in 2023_reddit_outputs_csv.zip.

### Step 3: Data Extraction and Visualization
-  For a detailed review, RedditArchiver-standalone-main.zip was used to download post content and comments based on identified post IDs.
-  Final_reddit_posts_comments_html.py utilizes these IDs from csv files to generate HTML files for each month, facilitating an interactive review of the content.




