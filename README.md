# Luma-AI-Scripts
Helper scripts for batch processing Luma AI NeRFs written by ChatGPT and Github Copilot with a little input from rhickman

My main goal is to batch upload multiple Insta360 MP4 files from my desktop instead of using the web uploader. Running UploadDirectory.py will prompt you for a directory path or default to the current location. You can also add text as a naming prefix if all the scans are part of a related batch (e.g. "Museum Artifacts") in front of their file names.

I initially neglected to include the command to trigger new captures to be processed (ooops). So I added a script called GetCaptures.py to fetch a list of captures that includes the "slug" key that Luma assigns to each capture. You can then run ManualTrigger.py and paste in the slug name to kick off processing for it.
