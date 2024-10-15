# Spotify-Quant-2023
## Objective:

In the world of music streaming, it's important to understand which types of music are most popular. This can help musicians, record companies, and streaming platforms like Spotify know what people like to listen to nowadays. We found a dataset with a bunch of informations about the top 50 songs on Spotify in 2023, which we got from a website called Kaggle. We want to use this information to figure out which genre of music is the most popular, and see if there are any patterns we can spot. Music is something that people from anywhere and any background enjoy and connect with. Nowadays, we can listen to music easily through apps like Spotify, which has a huge number of collection of songs. This data includes things like the song's name, the artist, when it was released, what genres of music it is, and how many times people listened to it. By looking at this data, we can learn which types of music are liked the most by Spotify users.

## Data Source:

We sourced our data from the Kaggle website and compiled it into a CSV file to facilitate analysis. This dataset contains a comprehensive collection of tracks from Spotify's official "Top Tracks of 2023" playlist, showcasing the most popular and influential music of the year as determined by Spotify's streaming data. It encompasses a diverse range of genres, artists, and musical styles that have shaped the musical landscape of 2023. This dataset serves as a fundamental resource for music enthusiasts, data analysts, and researchers interested in exploring music trends or developing recommendation systems, offering insights into the dynamics of the music industry and its evolving trends. 
- https://www.kaggle.com/datasets/yukawithdata/spotify-top-tracks-2023/data - Data for Spotify Top 50 Tracks 2023

## Motivation:

Our whole team is really passionate about music. We all have memories of listening to our favorite songs over and over again since we were kids. We also love discovering new artists and genres of music. Music isn't just background noise for us but also brings us joy, inspires us, and helps us connect with each others. When we were thinking of ideas for our project, it was clear that our shared love for music would be a good topic for us. We decided to focus on the Top 50 Tracks on Spotify for 2023 because we wanted to explore the different kinds of music people enjoy listening to. We want to understand why people listen to certain songs and how music influences their lives. As we work on this project, our goal is to tell the stories behind the data. We want to uncover the emotions, experiences, and cultural influences that shape people's music preferences. This journey is driven by our genuine love for music, our curiosity, and our belief in the power of music to bring people together.

## Importance:

Understanding the popularity of different types of music is really important to us. By looking at the Top 50 Tracks on Spotify for 2023, we can learn which music genres are the most liked by people. This information is valuable for musicians, record labels, and music streaming platforms because it helps them know what kind of music people want to listen to. For us, it's not just about analyzing numbers or datas. We want to dig deeper and understand why certain songs or genres of songs are popular. By doing this, we can uncover the stories behind the data like the emotions, experiences, and cultural influences that shape people's music choices. This understanding can help us appreciate the power of music to bring people together and inspire us in our own lives.

## Dataset Details:

Our dataset includes datas like the artist's name, the title of the track, when it was released, the type of music it is, and various measures of how the music sounds, like how danceable or energetic it is. Before we start analyzing the data, we made sure to clean and organize it well to make sure it's accurate and reliable. This sets the stage for a thorough and helpful exploration. We also looked at using averages or percentages where it makes sense to better understand and compare the different characteristics of the tracks.

**Data Key Table**:
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
  
**Data Points Actually Used**:
- Genres
- Danceability
- Popularity
- Amount of genres
