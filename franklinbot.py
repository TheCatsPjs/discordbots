import discord
import random

#if anyone types any of these words the franklinbot will be triggered to tell a fact.
facttrigger = ["fact", "frank", "ben",]


#bot will choose a random string from this list
answer = ["I invented the lightning rod, the Franklin stove, and bifocals.", "Did you know I founded Philadelphia's fire department and the University of Pennsylvania?",
          "I was a once a successful newspaper editor and printer in Philadelphia, publishing the *Pennsylvania Gazette* and *Poor Richard's Almanac,* this made me quite wealthy.",
           "I was once the governer of Pennsylvania, the first United States ambassador to France and Sweden, and I was also the first Postmaster General in the United States. However, I was never the president.",
          "Playing Chess was something of a talent of mine, I wrote an essay titled 'The Morals of Chess' that went over some of the rules of conduct. I helped make Chess a popular sport in the United States, and I was inducted into the United States Chess Hall of Fame in 1999.",
          "I once invented a fictional character named Silence Dogood to write for the New England Courant newspaper. When Ms. Dogood started to get proposed to by readers, I thought I should put an end to it.",
          "I spoke five different languages, including French, Latin, Spanish, Italian, and of course, English.",
          "I came up with the phrase 'Early to bed, early to rise makes a man healthy, wealthy and wise.'", "Nobody knows exactly who invented the glass harmonica, but I perfected it! My design was so innovative that Beethoven, Strauss, and Mozart composed pieces for it.", "Pssst, most of these facts come from www.bostonteapartyship.com/benjamin-franklin-facts. Go there to learn more about me.",
          "I only had two years of formal schooling in my life. School is for nerds.", "I was born on January 17, 1706. I died on April 17, 1790 aged 84. Over 20,000 people attended my funeral.",
          "I was one of the founding fathers of the United States, I was also an author, printer, political theorist, politician, freemason, postmaster, scientist, inventor, civic activist, statesman, and a diplomat. Whew.",
          "'Fart Proudly' is an essay I wrote about farts. It is also called 'A Letter to the Royal Academy of Farting.' The essay included an idea to create a type of drug that could be mixed with foods to not only make flatulence inoffensive, but agreeable.",
          "My face has been on the $100 bill since 1928, I and Alexander Hamilton are the only two non-presidents to be on US dollars.",
          "Swimming was something I enjoyed a great deal, I once invented fins for my hands to help me swim. I tried them on my feet but they were far too bulky.",
          "I never once patented an invention, my inventions were practical and designed to make life easier, and I considered them a gift to the public.", "I assisted in making the first library in Philadelphia, the Library Company of Philadelphia.",
          "I witnessed the first hydrogen balloon flight in 1783 on the 27th of August, quite a sight.", "I am the only founding father that signed all three documents freeing the United States from Britain, the Declaration of Independance, The Treaty of Paris and the United States Constitution.",
          "Late in my life I embraced the abolition of slavery, and became the president of the first abolition organization, the Philadelphia Abolition Society. In 1790, I petitioned congress to abolish slavery, two months before my death.",
          "I suffered from obesity throughout the later years of my life, this caused me multiple health problems and I was in poor health during the signing of the US Constitution in 1787.",
          "When I was 22 I wrote what I hoped would be my own epitaph.", "When I died the French National Assembly announced a day of mourning.", "I am sometimes called 'The only President of the United States who was never the President of the United States.'"]

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

#message is the thing we're searching for

    #if message.content.lower().startswith('heck'):
    for word in facttrigger:
        if word in message.content.lower():
            msg = (random.choice(answer)).format(message) #(random.choice(answer)) chooses a random answer
            await client.send_message(message.channel, msg)
            break

@client.event
async def on_ready():
    print('Greetings, I am Benjamin Franklin, do you require my services?')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('')
