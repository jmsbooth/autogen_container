# File: autogen_container.py
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import json
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class AutoGenContainer:

    def __init__(self, config_file):
        logging.info(f'Initializing AutoGenContainer with config file: {config_file}')

        # Load the main configuration from the specified file
        config = None  # Define config outside of the with block
        with open(config_file, 'r') as file:
            config = json.load(file)
        
        # Load environment-specific configurations
        env_config_file = config.get('config_file', 'local_config.json')
        with open(env_config_file, 'r') as file:
            self.env_config = json.load(file)
        
        # Set the OpenAI API key as an environment variable
        os.environ['OPENAI_API_KEY'] = self.env_config['OPENAI_API_KEY']
        logging.info('OpenAI API key set successfully')
        
        # Create agents based on the configuration
        self.agents = {}
        for agent_name, agent_config in config['agents'].items():
            AgentClass = UserProxyAgent if agent_config['type'] == 'UserProxyAgent' else AssistantAgent
            self.agents[agent_name] = AgentClass(
                agent_name, 
                llm_config=agent_config['llm_config'],
                system_message=agent_config['description']  # Using description as system_message
            )
        logging.info(f'{len(self.agents)} agents created successfully')

    def initiate_chat(self, agent_name, message):
        logging.info(f'Initiating chat with agent: {agent_name}')
        # Initiate a chat with the specified agent
        response = self.agents[agent_name].process_message(message)
        logging.info(f'Received response from agent: {agent_name}')
        return response

# If you need a main block to test or run the script independently
#if __name__ == '__main__':
#    # Example usage
#    container = AutoGenContainer('config.json')
#    response = container.initiate_chat('admin', 'Hello, Admin!')
#    print(response)
