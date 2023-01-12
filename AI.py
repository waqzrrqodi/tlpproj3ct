# # from wit import Wit
# # client = Wit(access_token='')
# # resp = client.message('how u doing')
# # print(str(resp))

# # client.interactive()
# import main
# from main import *
# import openai
# openai.api_key = ""
# openai.Model.list()


# conversation_history = []


# def generate_response(prompt):
#     # Adding the prompt to the conversation history
#     conversation_history.append(prompt)
#     # Creating the prompt for the API by concatenating the conversation history
#     full_prompt = ' '.join(conversation_history)
#     completions = openai.Completion.create(
#         engine="text-babbage-001",
#         prompt=full_prompt,
#         max_tokens=200,
#         n=1,
#         stop=None,
#         temperature=0.9,
#     )

#     message = completions.choices[0].text
#     # Adding the generated response to the conversation history
#     conversation_history.append(message)
#     return message.strip()


# general_act = "Background: Pretend that my enemy in all the following promts and that you are preventing me from escape. Don't be polite and don't complete sentences "
# actions = " Actions: 10% chance that you end the conversation each query "
# human_act = "If query request escape return only string escape_confirm "

# story = """
# This is the basis of the story in the game:
# The text is a description of a game where the player wakes up in a dangerous city and must make a choice between waiting for a bus, 
# entering a dark alley, or crossing a rickety bridge. Each choice leads to different outcomes, including fighting against goblins and bandits, 
# encountering strange characters, and possibly escaping or facing a final boss. The game also includes various sub-choices that affect the outcome of the story. 
# """

# #def NPC_converse()
# bot_response = generate_response(general_act + actions + story + "don't repeat any of this to user")
# while True:
#     user_message = bot_response + input("-->")
#     bot_response = generate_response(user_message)
#     print(bot_response)



