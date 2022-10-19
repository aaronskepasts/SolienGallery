# Solien Gallery

View live project on Heroku here: http://sol333.herokuapp.com/


## The Project
 
There is a lot of excitement around non-fungible tokens (NFTs). People love to buy digital art and show them off to their friends, particularly on Twitter. Prior to Twitter's integration of nfts, users would display a screenshot of their favorite NFT on their Twitter banner (i.e., a large image on their profile). The issue with this is that it is difficult to display multiple NFTs. People want to avoid the work of merging images together, and so many users just choose a single token to exhibit, even if they have several items that they want to show off.
 
Solien Gallery provides a simple GUI that allows users to easily create a gallery of their NFTs and upload these galleries to Twitter, solving the current issues with showcasing one’s NFTs. For our project, we will restrict ourselves to Solien NFTs on the Solana blockchain.
 
To learn more about this project, please read further in the documentation folder.
 
If you're interested in the project at large checkout the ProjectOverview. If you're interested in the system and design, take a look at the ProgrammersGuide.
 
## Depreciations
 
Heroku no longer supports redis in the capacity of this project. As a result, the deployed version has been stripped of caching features: loading pages have been removed and longer load times when searching the blockchain and rendering gallery images can be expected. The example case has been hardcoded to avoid a tedious search of the blockchain allowing for a smoother demonstration of the project. Documentation should be consulted to view the full list of project features. The code has been left unchanged from the caching version in this repo.


## Instructions to run `runserver.py`

### Install Python with the default settings:
https://www.python.org/downloads/

### Download the latest version of Redis:
https://redis.io/ <br />

Windows users should follow this tutorial: https://redis.com/blog/redis-on-windows-10/. Unfortunately, it's a little tedious and requires WSL. 

### Run the following commands in terminal:
`pip install cloudinary` <br />
`pip install flask` <br />
`pip install imageio` <br />
`pip install pillow` <br />
`pip install rq` <br />
`pip install theblockchainapi`

### Run the server:
`redis-server`
`python worker.py`
`python runserver.py 8080`

The server should be on port 8080.
