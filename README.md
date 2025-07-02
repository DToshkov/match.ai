# match.ai
Matching Algorithm normalizing 4 attributes using greedy and optimization-based weighted pairing to match mantees to best-fit mentors 
# match.ai - Mentor-Mentee Matching Algorithm

## Overview

`match.ai` is a lightweight, customizable algorithm to match mentors and mentees using weighted attribute scoring. Built for internal mentoring programs, the system evaluates compatibility across criteria like university, hobbies, professional interests, and location proximity.

## Features

- Attribute-based matching using weighted scores
- Hungarian algorithm for optimal assignments
- Cosine similarity for nuanced matching (e.g., outside role interests)
- Easily configurable weights and fields
- Sample data and test cases provided

## Matching Criteria

Each mentor-mentee pair is scored based on:
- 🎓 University
- 🧘 Hobbies
- 🌎 Outside Role / Engagement
- 📍 Proximity (home hub)
- 🧠 Key Interests (current function)

Weights can be adjusted in `WEIGHTS` dict.

## Project Structure

