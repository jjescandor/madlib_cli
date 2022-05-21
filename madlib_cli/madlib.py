"""
Make Me A Video Game!

I the majestic and purple Scott have colored JB's laughing sister and plan to steal her tickled arrows!

What are a gorilla and backpacking butterfly to do? Before you can help Betty, you'll have to collect the silly tests and striped jackets that open up the 44 worlds connected to Wilson's' Lair. There are 3 leaves and 4 swords in the game, along with hundreds of other goodies for you to find.

"""
def read_template():
    with open("../assets/dark_and_stormy_night_template.txt") as f:
        string_one=f.read()
        print(string_one.format(Adjective="beautiful", Noun="ball"))

    with open("../assets/make_me_a_video_game_template.txt") as g:
        string_two=g.read()

    for x in string_one.split():
        pass
        #print(x)

    for x in string_two.split():
        pass
        # print(x)


read_template()

# prompts = {
#     "Give me an Adjective": 2,
#     "Give me a Noun": 1
# }

# answers = {
#     "adjective" : [],
#     "noun": []
# }

# for prompt in prompts:
#     for x in range(prompts[prompt]):
#         if "Adjective" in prompt:
#             print(prompt)
#             answer = input("> ")
#             answers["adjective"].append(answer)
#         if "Noun" in prompt:
#             print(prompt)
#             answer = input("> ")
#             answers["noun"].append(answer)


