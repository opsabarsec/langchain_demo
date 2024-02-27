# LangChain Demo
![LangChain logo](/langchain.png)

This repository allows using the [LangChain library](https://python.langchain.com/docs/get_started/introduction) for building powerful applications with large language models (LLMs). By following the instructions below you will be able to connect large language models (LLMs) like OpenAI's GPT-3.5 Turbo throug an APIs and run them from command line.
This approach is much more versatile than having to enter prompts manually using web interfaces. 
And you can build your own code upon it. LangChain is designed to allow training of LLMs on your own data. It also seamlessly integrates into several platforms such as MS Azure, Amazon Web Services, Google cloud...

### How to install it and run it on your PC
---- Video tutorial can be found [here](https://www.youtube.com/watch?v=DhFfw04QDHw) -----

I assume that you have Python and Anaconda installed. The second is not mandatory but recommended.

- Optional step: Create a conda environment to run this package.
Get to your terminal and run:

conda create -n langchain_demo python=3.11.4

conda activate langchain_demo

- STEP 1: Get the package and install dependencies in your environment.

git clone {address of this github repo}

pip install -r requirements.txt

- STEP 2: Add your API key to connect to OPEN AI.
  
You are almost done. But you need to connect to OPENAI API with your own key. 
You can create one easily if you have a Chat-GPT account that you will use for the [OpenAI website](https://platform.openai.com/account/api-keys).

[Check out this tutorial if you do for the first time.](https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/)

Copy it and store it in a safe place. 
You will have to paste it into the .env file that you find in this repository.
You cannot go wrong, as there is written OPENAI_API_KEY = "paste value here".
Save and close.

- STEP 3: Enjoy!
Now you are ready to go. You can even run the jupyter notebook in this repo and play with your own prompts.

### Augmented Chat-GPT with Langchain Agents
![bike logo](/cyberbike.jpg)

Location-related advice for bike tourist example. ![code in this notebook](demo_touradvice.ipynb)

Using the Langchain Agent library you can prompt the openweather_API to obtain the current local weather.
This information is fed to OpenAI LLMs to obtain an advice for bike tourist visiting the given city.

