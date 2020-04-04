<h4 align="center">This projects is part of Boston PyData Hackathon projects.</h4>

This steps will help you set up your environment so we all have the same starting point to work on the social distancing project.

Before you start, you will need to use an API key from google (Places and Maps) in order to pull real data from the API. Alternative, there is an example file you can use to load sample data and avoid making calls to the API (this helps us not depleting our budget).


### For developers
Clone the source locally:

```sh
$ git clone git@github.com:CooperData/social-distancing.git
$ cd social-distancing
```

For simplicity you might want to install 
`Anaconda`

Create environment (social-distancing:

```sh
$ make create_enviroment
```

Activate environment (social-distancing):

```sh
$ source activate social-distancing
```

Install project dependencies:

```sh
$ make requirements
```

Copy the file .env-example and renamed the copied file to .env, The file should have the variable `API_KEY` example:

```sh
`API_KEY=************************************************************`
```

You are now ready to get started with the started notebook.

```
jupyter lab
```

Use the notebook Start Here.ipynb which to test your system is working correctly.

# Important:
Make sure as you commit to the remote git repo that none of your file are including the api key.
You can do so by running the file find_key.

Author: Cesar Hernandez 
