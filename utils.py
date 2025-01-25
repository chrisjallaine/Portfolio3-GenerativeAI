import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.tools import DuckDuckGoSearchRun

def generate_script(prompt, video_length, creativity, api_key):
    # Setup OpenAI
    llm = OpenAI(temperature=creativity, openai_api_key=api_key)
    
    # Prompt template for generating video title
    title_template = PromptTemplate(input_variables=["topic"], template="Generate a YouTube video title about {topic}.")
    title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)

    # Prompt template for generating video script
    script_template = PromptTemplate(input_variables=["title", "duration", "search_data"],
                                     template="Create a YouTube script with the title '{title}' that lasts for {duration} minutes, using the following information: {search_data}.")
    script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True)

    # Get search data from DuckDuckGo
    search_tool = DuckDuckGoSearchRun()
    search_data = search_tool.run(prompt)

    # Generate the title
    title = title_chain.run({"topic": prompt})

    # Generate the script
    script = script_chain.run({
        "title": title,
        "duration": video_length,
        "search_data": search_data
    })

    return title, script, search_data


    