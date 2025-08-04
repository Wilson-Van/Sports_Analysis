# Sports_Analysis

## Description:

This is a simple program that will show real time stats and odds for multiple sports including football, basketball, soccer, hockey, and baseball. 

## Purpose/Reasoning:

I decided to make this as I wanted to improve my skills with APIs and wanted more experience with developing both the backend and frontend. I chose this specific topic because I wanted to make a tool that I would actually use. At the time of making this my friends and I are about to start fantasy football and the NFL season is about to begin so I would like a tool that allows me to analyze trends of players and see whether or not they are worth the fantasy draft pick and/or betting on.

## Tools:

I will be using the api-sports api which allows me to find real time stats of all sports and also has information of betting odds. 

## Resources:

I will be using the documentation of the api-sports api found at https://api-sports.io/#apis. This page has multiple sports available each with separate documentation.

## Output:

As a finished product the program should be able to display a webpage which allows the user to select between tabs of sports and allows the user to select a team/player for certain stats about them. 

## Issues:

After doing a bit of research this api only allows for 100 api calls a day which could be an issue if this program was for commercial use, however this is for personal use and I don't believe myself or anyone I would allow to use my api key would call the api 100 times a day. If 100 api calls are too little I could call the api once and store the stats/odds into variables and display those variables instead of the actual api call. I could then recall the api after certain intervals of time and update the variables at that time.

After some experimentation I found that with the free version of the api 