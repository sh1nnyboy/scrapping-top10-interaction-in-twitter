# Twitter Top Interactions

A simple Python script that analyzes a Twitter user's timeline to find their top 10 most frequently mentioned users.

## Features

- Fetches up to 1000 recent tweets from a specified user
- Analyzes mentions within these tweets
- Shows the top 10 most frequently mentioned users
- Displays the number of mentions for each user
- Dynamic user input - analyze any Twitter handle without editing the code

## Requirements

- Python 3.6+
- Tweepy library

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/sh1nnyboy/twitter-top-interactions.git
   cd twitter-top-interactions
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Twitter API credentials:
   - Create a Twitter Developer account at https://developer.twitter.com/
   - Create a new app to get your API credentials
   - Add your credentials to the `interaction.py` file

## Usage

1. Edit the `interaction.py` file to add your Twitter API credentials.
2. Run the script:
   ```
   python interaction.py
   ```
3. When prompted, enter the Twitter handle you want to analyze (with or without the @ symbol)
4. The script will fetch and analyze the tweets, then print the top 10 users mentioned by the specified account, along with the number of mentions.

## Example Output

```
Enter the Twitter handle to analyze (without @): elonmusk

Analyzing @elonmusk's recent tweets. This may take a moment...

Top 10 accounts mentioned by @elonmusk:
Tesla: 42 mentions
SpaceX: 36 mentions
Twitter: 29 mentions
...
```

## Error Handling

The script includes error handling for:
- Invalid Twitter handles
- Protected accounts
- Twitter API errors
- Empty or non-existent accounts

## License

MIT License 