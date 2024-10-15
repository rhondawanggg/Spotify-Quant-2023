# -*- coding: utf-8 -*-
"""DS2001 Final Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZvjSzAI-wRVIOC5yVE18hhmKFhjGY9mj

###Group Members

- Wattakarn Lamsam: lamsam.w@northeastern.edu
- Siqi Cai: cai.siq@northeastern.edu
- Jasmyn Loelke: loelke.ja@northeastern.edu
- Shaoxian Wang: wang.shaox@northeastern.edu

# Quantitative Analysis of Spotify Top 50 Tracks 2023

### Problem Statement and Background

#### Objective

In the world of music streaming, it's important to understand which types of music are most popular. This can help musicians, record companies, and streaming platforms like Spotify know what people like to listen to nowadays. We found a dataset with a bunch of informations about the top 50 songs on Spotify in 2023, which we got from a website called Kaggle. We want to use this information to figure out which genre of music is the most popular, and see if there are any patterns we can spot.

Music is something that people from anywhere and any background enjoy and connect with. Nowadays, we can listen to music easily through apps like Spotify, which has a huge number of collection of songs. This data includes things like the song's name, the artist, when it was released, what genres of music it is, and how many times people listened to it. By looking at this data, we can learn which types of music are liked the most by Spotify users.

#### Data Source

We sourced our data from the Kaggle website and compiled it into a CSV file to facilitate analysis. This dataset contains a comprehensive collection of tracks from Spotify's official "Top Tracks of 2023" playlist, showcasing the most popular and influential music of the year as determined by Spotify's streaming data. It encompasses a diverse range of genres, artists, and musical styles that have shaped the musical landscape of 2023.

This dataset serves as a fundamental resource for music enthusiasts, data analysts, and researchers interested in exploring music trends or developing recommendation systems, offering insights into the dynamics of the music industry and its evolving trends.

https://www.kaggle.com/datasets/yukawithdata/spotify-top-tracks-2023/data - Data for Spotify Top 50 Tracks 2023

### Introduction & Description of the Data

#### Motivation

Our whole team is really passionate about music. We all have memories of listening to our favorite songs over and over again since we were kids. We also love discovering new artists and genres of music. Music isn't just background noise for us but also brings us joy, inspires us, and helps us connect with each others. When we were thinking of ideas for our project, it was clear that our shared love for music would be a good topic for us. We decided to focus on the Top 50 Tracks on Spotify for 2023 because we wanted to explore the different kinds of music people enjoy listening to. We want to understand why people listen to certain songs and how music influences their lives.

As we work on this project, our goal is to tell the stories behind the data. We want to uncover the emotions, experiences, and cultural influences that shape people's music preferences. This journey is driven by our genuine love for music, our curiosity, and our belief in the power of music to bring people together.

#### Importance

Understanding the popularity of different types of music is really important to us. By looking at the Top 50 Tracks on Spotify for 2023, we can learn which music genres are the most liked by people. This information is valuable for musicians, record labels, and music streaming platforms because it helps them know what kind of music people want to listen to.

For us, it's not just about analyzing numbers or datas. We want to dig deeper and understand why certain songs or genres of songs are popular. By doing this, we can uncover the stories behind the data like the emotions, experiences, and cultural influences that shape people's music choices. This understanding can help us appreciate the power of music to bring people together and inspire us in our own lives.

#### Dataset Details

Our dataset includes datas like the artist's name, the title of the track, when it was released, the type of music it is, and various measures of how the music sounds, like how danceable or energetic it is. Before we start analyzing the data, we made sure to clean and organize it well to make sure it's accurate and reliable. This sets the stage for a thorough and helpful exploration. We also looked at using averages or percentages where it makes sense to better understand and compare the different characteristics of the tracks.

Data Key Table:
- Track_name
- Is_explicit
- Album_release_date
- Genres
- Danceability
- Valence
- Energy
- Loudness
- Acousticness
- Instrumentalness
- Liveness
- Speechiness
- Key
- Tempo
- Mode
- Duration_ms
- Time_signature
- Popularity

Data Points Actually Used:
- Genres
- Danceability
- Popularity
- Amount of genres

### Methods

#### Data Cleaning and Preperation

##### We started off our analysis by cleaning the data, ensuring all the data was clear and easy to use. We created functions to illustrate the data in different ways. Through the use of variables, loops, dictionaries, and the pandas library, we were able to read the data and prepare it to be used in our visualizations.

#### Visualization Techniques

We used matplotlib to create a bar graph and different scatter plots to illustrate the data. We examined the relationship between popularity and three of the other variables given. We also highlighted the most and least popular songs to clearly define whether or not there was a clear correlation.
"""

import pandas as pd
import matplotlib.pyplot as plt

def plot_frequencies(file_name):
    """
    This function reads the CSV file, counts the frequency of each genre,
    and uses the counts to create a bar graph illustrating how common/popular
    each genre is.

    """
    # Read the data
    top_50_2023 = pd.read_csv(file_name)

    # Create a dictionary to count the genres
    genre_count = {}

    # Loop through each row
    for genre in top_50_2023['genres']:
        # Remove brackets and split by comma to get individual genres
        genres = genre.strip("[]").replace("'", "").split(", ")
        for genre in genres:
            if genre in genre_count:
                genre_count[genre] += 1
            else:
                genre_count[genre] = 1

    # Plot the results
    plt.figure(figsize=(10, 8))
    # Create bars for each genre with their count
    plt.bar(genre_count.keys(), genre_count.values())
    plt.title('Genre Frequency in Top 50 Songs of 2023')
    plt.xlabel('Genre')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.show()


file_name = 'top_50_2023.csv'
plot_frequencies(file_name)

# The bar chart "Genre Frequency in Top 50 Songs of 2023" provides valuable insights into Spotify music trends.
# This graph visually presents how often each genre appears in Spotify's top 50 songs of 2023, as a clear indicator of genre popularity.
# Pop music emerges as the most dominant, with over 16 appearances, highlighting its strong commercial performance.
# Additionally, Latin genres like "Trap Latino" and "Urbano Latino," each appearing 10 times, along with "Reggaeton" with 9 appearances, demonstrate the global influence of Latin music during 2023.
# This graph directly addresses the problem statement by enabling an analysis of music popularity based on genre, which is crucial for artists, record labels, and streaming services aiming to understand current musical preferences.
# This also enables industry stakeholders to discover patterns and make informed decisions that foster the development of diverse music genres.

import pandas as pd
import matplotlib.pyplot as plt

def plot_genre_popularity_correlation(file_name, highlight_songs=None):
    """
    Plots the correlation between the number of genres in a song and
    the song's popularity. The most popular song and least popular song are
    also highlighted to help see if there is a correlation.

    """
    # Read the data
    top_50_songs = pd.read_csv(file_name)

    # Get the number of genres per song
    num_genres_list = []
    for genres_string in top_50_songs['genres']:
        genres = genres_string.strip("[]").replace("'", "").split(", ")
        num_genres_list.append(len(genres))
    top_50_songs['num_genres'] = num_genres_list

    # Create plot
    plt.figure(figsize=(10, 6))
    plt.scatter(top_50_songs['num_genres'], top_50_songs['popularity'], alpha=0.5, label='All Songs')

    # Highligh most and least popular song
    if highlight_songs:
        for index, (color, label) in highlight_songs.items():
            plt.scatter(top_50_songs.at[index, 'num_genres'], top_50_songs.at[index, 'popularity'],
                        color=color, s=100, edgecolors='black', label=label)

    # Plot
    plt.title('Correlation Between Number of Genres and Song Popularity')
    plt.xlabel('Number of Genres')
    plt.ylabel('Popularity')
    plt.xticks(range(1, max(top_50_songs['num_genres']) + 1))
    plt.grid(True)
    plt.legend()
    plt.show()

# Call the function
file_name = 'top_50_2023.csv'
highlight_songs = {
    5: ('red', 'Cruel Summer by Taylor Swift'),
    20: ('green', 'Another Love by Tom Odell')
}
plot_genre_popularity_correlation(file_name, highlight_songs=highlight_songs)

# The scatter plot "Correlation Between Number of Genres and Song Popularity" offers insights into how the diversity of genres in a song influences its popularity.
# By examining Spotify's top 50 songs of 2023, the plot indicates that there isn't a clear pattern of increased popularity with a higher number of genres.
# Instead, popularity appears to be distributed across songs with varying genre counts.
# We can observe this trend by considering two specific songs as examples: "Cruel Summer" by Taylor Swift and "Another Love" by Tom Odell.
# "Cruel Summer," marked in red, sticks to a single genre appears to be the most popular, while "Another Love," highlighted in green, is also associated with one genre but is shown to be the least popular.
# The widely scattered data points further support this observation, indicating a lack of strong correlation between the number of genres and a song's popularity score.
# This implies that factors other than genre diversity may have a more significant impact on a song's popularity.
# This correlation also benefits stakeholders to understand these dynamics and help develop strategies to maximize the appeal of songs and expand their reach in the highly competitive music market.

import pandas as pd
import matplotlib.pyplot as plt

def plot_danceability_popularity_correlation(file_name, highlight_songs=None):
    """
    Plots the correlation between a song's danceability and its popularity. It
    also highlights the most and least popular songs to make it clear whether
    or not there is a correlation.

    """
    # Read the data
    top_50_songs = pd.read_csv(file_name)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(top_50_songs['danceability'], top_50_songs['popularity'], alpha=0.5, label='All Songs')

    # Highlighting specific songs
    if highlight_songs:
        for index, (color, label) in highlight_songs.items():
            plt.scatter(top_50_songs.at[index, 'danceability'], top_50_songs.at[index, 'popularity'],
                        color=color, s=100, edgecolors='black', label=label)

    # Finalize  plot
    plt.title('Correlation Between Danceability and Popularity')
    plt.xlabel('Danceability')
    plt.ylabel('Popularity')
    plt.legend()
    plt.grid(True)
    plt.show()

# Call the function
file_name = 'top_50_2023.csv'
highlight_songs = {
    5: ('red', 'Cruel Summer by Taylor Swift'),
    20: ('green', 'Another Love by Tom Odell')
}
plot_danceability_popularity_correlation(file_name, highlight_songs=highlight_songs)

# The scatter plot "Correlation Between Danceability and Popularity" provides valuable insights into the potential relationship between a song's danceability and its popularity.
# The plot demonstrates a spread of popularity ratings across various danceability scores, suggesting no strong direct correlation between the two variables for Spotify's top 50 songs of 2023.
# One notable observation is the highlighted song "Cruel Summer" by Taylor Swift, marked in red, which enjoys high popularity despite having a danceability score around the mid-range.
# Conversely, "Another Love" by Tom Odell, highlighted in green, has both a lower danceability score and lower popularity, indicating that songs with lower danceability might not achieve the highest levels of popularity.
# This visualization implies that while danceability may contribute to a song's appeal, it is not the sole determinant of its popularity.
# Other factors such as genre, artist recognition, and cultural trends could also play significant roles.
# By analyzing the relationship between danceability and popularity, stakeholders can develop more targeted and effective marketing strategies, leading to increased visibility and engagement for artists and their music.

import pandas as pd
import matplotlib.pyplot as plt

def plot_duration_popularity_correlation(file_name, highlight_songs=None):
    """
    Plots the correlation between song duration (in milliseconds) and popularity.
    It also highlights the most and least popular songs to make it clear whether
    or not there is a correlation.

    """
    # Read the data
    top_50_songs = pd.read_csv(file_name)

    # Plotting the general scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(top_50_songs['duration_ms'], top_50_songs['popularity'], alpha=0.5, label='All Songs')

    # Highlighting specific songs
    if highlight_songs:
        for index, (color, label) in highlight_songs.items():
            plt.scatter(top_50_songs.at[index, 'duration_ms'], top_50_songs.at[index, 'popularity'],
                        color=color, s=100, edgecolors='black', label=label)

    # Finalizing the plot
    plt.title('Correlation Between Duration (ms) and Popularity')
    plt.xlabel('Duration (ms)')
    plt.ylabel('Popularity')
    plt.legend()
    plt.grid(True)
    plt.show()

# Call the function
file_name = 'top_50_2023.csv'
highlight_songs = {
    5: ('red', 'Cruel Summer by Taylor Swift'),
    20: ('green', 'Another Love by Tom Odell')
}
plot_duration_popularity_correlation(file_name, highlight_songs=highlight_songs)

# The scatter plot "Correlation Between Duration (ms) and Popularity" examines whether the length of a song, measured in milliseconds, has any bearing on its popularity.
# The data points are spread across various song durations for Spotify's top 50 songs of 2023, from around 140,000 ms to over 260,000 ms.
# There is no apparent trend that suggests a strong correlation between song duration and popularity.
# The song "Cruel Summer" by Taylor Swift, highlighted in red, is the most popular and is on the shorter side of the duration spectrum. This indicates that a shorter duration does not hinder a song's potential to achieve high popularity.
# While "Another Love" by Tom Odell, marked in green, is among the least popular and has a longer duration.
# However, there are other songs with similar or longer durations that have higher popularity, suggesting that length is not a primary factor in popularity.
# There is a cluster of songs with durations around 200,000 ms that have varying levels of popularity, which further supports the idea that duration alone is not a decisive factor in a song's success.
# This scatter plot analysis suggests that song duration has a negligible impact on popularity within the top 50 songs of 2023, which could be valuable for artists who may be considering the optimal length for a song, as it implies that they should perhaps focus more on the quality and content of the music rather than its duration.

"""#### Statistical Analysis"""

import pandas as pd

def print_popularity_correlations(file_name):
    """
    Calculates the correlation between various musical features
    and the songs' popularity, and prints the correlation coefficients, excluding the self-correlation
    of popularity.
    """
    # Load the data
    top_50_songs = pd.read_csv(file_name)

    # Select the relevant columns and calculate the correlation matrix
    correlation = top_50_songs[['danceability', 'valence', 'energy', 'loudness',
                                 'acousticness', 'instrumentalness', 'liveness', 'speechiness', 'key' , 'tempo', 'duration_ms', 'popularity']].corr()

    # Print the correlation coefficients between popularity and other features
    print(correlation['popularity'].drop('popularity'))  # Exclude self-correlation of popularity

# Example usage
file_name = 'top_50_2023.csv'
print_popularity_correlations(file_name)

"""The list of correlation coefficients describes the linear relationship between our selected musical features and the popularity of songs. Here’s an explanation of what each of these correlations implies:

- **Danceability (-0.157372):** Indicates a slight negative correlation with popularity. Songs with higher danceability might slightly decrease in popularity, but the relationship is weak.

- **Duration_ms (-0.112414):** A weak negative correlation with popularity implies that longer songs tend to be slightly less popular. This could suggest a preference for shorter, more concise songs in popular music.

Overall, all the selected and unused correlation coefficients reveal only weak relationships between these musical features and song popularity. The presence of both negative and positive correlations suggests that no single feature is a strong predictor of popularity. The slight preferences indicated by these correlations (e.g., for more speechiness or a faster tempo) highlight the complex nature of musical popularity, which is likely influenced by a broad range of factors beyond these features. It can be concluded that the popularity of a song can depend on many aspects beyond these measured attributes.

### Results, Conclusions & Future Work

#### Results

Our study looked at the top 50 songs on Spotify in 2023 to see what genre of music people like. First, we found out that pop music was the most popular genre, followed by Latin genres like Trap Latino and Urbano Latino. This means that these types of music were listened to the most during the year of 2023. We showed this information using a bar chart, which is a type of graph that helps us see data more easily.

Next, we looked at whether having more types of music in a song made it more popular. Surprisingly, we didn't find a clear link or connection between having more genres in a song and how popular it was. Some songs with just one genre were very popular, while others with many genres were not as popular. This was shown using a graph called a scatter plot.

We also checked if the length of a song had anything to do with how popular it was. Surprisingly, we found that the length of a song didn't really matter when it came to popularity. We used another scatter plot to show this.

Lastly, we wanted to see if how easy a song was to dance to affected how popular it was. Again, we found that there wasn't a strong connection between danceability and popularity. Some songs that were easy to dance to were very popular, but others were not. We used another scatter plot to show this.

#### Conclusions

We conclude that pop was indeed the most popular genre of 2023. Our analysis also revealed that there is little to no correlation with any of the other given variables. The lack of correlation between popularity and the other variables supports the idea that music is an art form and art is subjective. Because of this, it is hard to measure and predict what music is most popular. The results of our project are important to all music listeners because it proves that any type of music with a range of different characteristics can be popular.

#### Future Work

> Add blockquote


Even though we learned a lot from our project, there's still a lot more to explore. We could look at other music platforms besides Spotify, or look at different types of music to see if our findings are the same. We could also use more advanced techniques to analyze the data better. And it might be helpful to weigh certain factors more than others to get a clearer picture of how they affect a song's popularity. This way, we can keep learning more about why people like the music they do.
"""