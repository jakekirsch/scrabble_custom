##### Goals

- [ ] create a 3d scrabble game with different types of computers 'brains' to play against
- [ ] solidy python learnings from 6.001, 6.002 and others in this process
- [ ] learn Git and GitHub
- [ ] practice documenting learnings on website


##### Note to Future Self
This is going to be hard. At the start of this you were excited about the prospects of diving in because it seemed like an elegant way to work on becoming very good at Python. However, to become very good at Python takes a **lot** of time and learning is **hard**. You're going to be frustrated and want to change projects a lot or move onto other things because you're stuck.

Remember, the purpose of this project is to **learn**. If it's coming along easily then you're not learning. *There are no royal roads to geometry* or in the words of Bon Scott, *it's a long way to the top if you wanna rock n' roll*

If you're feeling frustrated or stuck - throw [this on](https://www.youtube.com/watch?v=-sUXMzkh-jI) and remember why you're doing this.


##### Log
Working on `class bag`, need to finish writing the removal piece and then
start making some unit tests. I'm not sure making a `letter` (i.e. tiles) class is necessary, might be over-engineered since the information of a tile sits within the game_rules and the tiles themselves don't change value state. Although that would be interesting in the future...maybe as time goes on you can change the value of tiles?? 







##### Learnings
*group these once there are three of a kind*

##### Virtual Env
[How to create a virtualenv with the right version](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)

[How to delete a virtualenv when you don't need it](https://stackoverflow.com/questions/11005457/how-do-i-remove-delete-a-virtualenv)

Activate and deactivate a virtualenv
	`source envname/bin/activate`
	`deactivate`


##### Git
How to initialize a new git repo in your [project](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/)
1. creates a local git repository in working directory
		`git init` 
2. stages all the files/folders in repository
		`git add .` 
3. commit the files that are staged
		`git commit -m "Commit Message"`
4. Go to Github and create a new repository, copy the remote repo URL
5. Add the URL for the remote repository, basically where the local repository is pushed to.
		`git remote add origin remote repositoryURL`
6. Verify the remote URL with
		`git remote -v`
7. push the changes in local repository to github, which means the github repository will have the same state as local repository
		`git push -u origin master`
