import discord
import random

#if anyone types any of these words the franklinbot will be triggered to tell a fact.
facttrigger = ["fact", "frank", "ben" ]


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
          "When I was 22 I wrote what I hoped would be my own epitaph.", "When I died the French National Assembly announced a day of mourning.", "I am sometimes called 'The only President of the United States who was never the President of the United States.'",
          "*Well done is better than well said.* ~Me.", "An investment in knowledge pays the best interest.", "They who can give up essential liberty to obtain a temporary safety deserve neither liberty or safety.",
          "Never leave that till tomorrow which you can do today, piece of advice.", "You may delay, but time will not.", "Either write something worth reading or do something worth writing. ~Benjamin Franklin (Me.)",
          "I helped negotiate the 1783 Treaty of Paris, which ended the Revolutionary War.", "We are all born ignorant, but one must work hard to remain stupid.", "Do not fear mistakes. You will know failure. Continue to reach out.",
          "From a child I was fond of reading, and all the little money that came into my hands was ever laid out in books.",
          "In reality, there is, perhaps, no one of our natural passions so hard to subdue as pride. Disguise it, struggle with it, beat it down, stifle it, mortify it as much as it pleases, it is still alive, and will every now and then peep out and show itself; you will see it, perhaps, often in this history; for, even if I could conceive that I had completely overcome it, I should be proud of my humility.",
          "There was never a good war or a bad peace.", "The Franklin stove, my first invention made sometime around 1740, cost less fuel but provided far more heat.",
          "I once proposed a new scheme for the alphabet that would make the letters C, J, Q, W, X, and Y redundant.",
          "I coined the terms battery, charge, conductor and electrify.", "At 12-years-old, I was apprenticed in a print shop run by my brother James, eventually, I grew tired of my brother's tyrannical and abusive behavior. I fled Boston in 1723, and although I had a few years remaining on the legally binding contract of my apprenticeship, I eventually found my way to Philadelphia, which became my home for the rest of my life.",
          "In 1725 I published my first pamphlet, *A Dissertation upon Liberty and Necessity, Pleasure and Pain.* that argued humans lacked free will and are not morally responsible for their actions. I later repudiated this and burned all but one copy of the pamphlet in my possession.",
          "By 1748, my printing business had made me one of the richest men in Pennsylvania, and I became a soldier in the local militia. I turned my business over to a partner to give myself more time to conduct scientific experiments.", "In 1748, I acquired slaves to work in my home and print shop, however, my views on slavery evolved over time, and, convinced it was evil, I freed my slaves in the 1760s."]

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.author.bot:
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
