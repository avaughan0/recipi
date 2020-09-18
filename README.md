# recipi

This is my repo for my project to create a virtual assistant that can do the following:
1. take pictures of my recipes in my cookbooks
2. ingest recipes from pictures of my cookbooks using OCR
3. store and retrieve recipes on command
4. be able to take voice commands and respond with voice output

Currently, I have written scripts to take the pictures and move them to a computer with more processing power to prep for OCR (not currently shared) and a rudimentary interface for searching and retrieving recipes.

The intent is to run all of this (except the OCR) on two Raspberry Pis.  One is a Raspberry Pi Zero which is just a camera, and the other is a Raspberry Pi 3 B+ with the Google AIY Voice Kit. 
