# Anime Recommendation System using Hadoop

## Project Overview
This project analyzes anime ratings using Hadoop MapReduce.

## Dataset
30 anime records with user ratings (1-10)

## Implementation
1. HDFS: Store data
2. MapReduce: Calculate average ratings per anime
3. Hive: Query and analyze results

## Files
- mapper.py: Extracts anime title and rating
- reducer.py: Calculates average rating per anime
- anime.csv: Dataset with anime records

## Technology Stack
- Hadoop HDFS
- MapReduce (Python)
- Hive
- Cloudera

## Output
Successfully calculated average ratings for multiple anime.