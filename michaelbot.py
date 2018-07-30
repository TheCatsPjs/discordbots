import discord

shesaid = ["it's hard", "it's very hard", "easy to get in", "hard to get it out", "impossible to rise up", "you're hardly my first", "come again", "too far in", "screw it", "getting it on", "get on", "get in", "i'm coming", "so big", "did me", "all day", "left me satisfied", "bang me", "screw it,", "screw me", "deeper", "get on this", "that straight", "touch this", "to bed", "is huge", "screwed", "get on top", "back on top", "under her", "on her", "under him", "on him", "under him", "come again", "off my chest", "you came"]

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.author.bot:
        return

#message is the thing we're searching for

    #for that's what she said
    for word in shesaid:
        if word in message.content.lower():
            msg = "That's what she said!".format(message)
            await client.send_message(message.channel, msg)
            break
#1
    if 'hey michael' in message.content.lower():
            msg = "Yes, {0.author.mention}?".format(message)
            await client.send_message(message.channel, msg)
            
#2
    elif 'hey prison mike' in message.content.lower():
            msg = "Yeah, {0.author.mention}?".format(message)
            await client.send_message(message.channel, msg)
#3
    elif 'not really appropriate' in message.content.lower():
            msg = "Why are you, the way that you are? Honestly, every time I try to do something fun, or exciting, you make it not that way. I hate so much about the things you choose to be.".format(message)
            await client.send_message(message.channel, msg)
#4
    elif 'orientation' in message.content.lower():
            msg = "Wrong, Toby, this is an orientation not a borienation.".format(message)
            await client.send_message(message.channel, msg)
#5
    elif 'scranton' in message.content.lower():
            msg = "The electric city!".format(message)
            await client.send_message(message.channel, msg)
#6
    elif 'oscar' in message.content.lower():
            msg = "Oscar is my friend, and he is gay, he is my gay friend.".format(message)
            await client.send_message(message.channel, msg)
#7
    elif 'worst thing about prison' in message.content.lower():
            msg = "The worst thing about prison, was the Dementors. They were flying all over the place and they were scary and they'd come down and they'd suck all the soul out of your body and it hurt! ".format(message)
            await client.send_message(message.channel, msg)
#8
    elif 'school' in message.content.lower():
            msg = "A boss is like a teacher. And I am like the cool teacher. Like Mr. Handell. Mr. Handell would hang out with us. And he would tell us awesome jokes. And he actually hooked up with one of the students, and then like 12 other kids came forward, it was in all the papers, really ruined 8th grade for us.".format(message)
            await client.send_message(message.channel, msg)
#9
    elif 'feeling bummed out' in message.content.lower():
            msg = "Dwight you ignorant slut!".format(message)
            await client.send_message(message.channel, msg)
#10
    elif 'salesman' in message.content.lower():
            msg = "What's the difference between a salesman and a saleswoman?".format(message)
            await client.send_message(message.channel, msg)
#11
    elif 'the fire' in message.content.lower():
            msg = "Ryan started the fire! Ryan started the fire!".format(message)
            await client.send_message(message.channel, msg)
#12
    elif 'loved' in message.content.lower():
            msg = "Would I rather be feared or loved? Easy, Both. I want people to be afraid of how much they love me.".format(message)
            await client.send_message(message.channel, msg)
#13
    elif 'best boss' in message.content.lower():
            msg = "That's me, Michael Scott, world's best boss.".format(message)
            await client.send_message(message.channel, msg)
#14
    elif 'had a gun' in message.content.lower():
            msg = "If I had a gun with two bullets and I was in a room with Hitler, Bin Laden and Toby, I would shoot Toby TWICE.".format(message)
            await client.send_message(message.channel, msg)
#15
    elif 'sentence' in message.content.lower():
            msg = "Sometimes I'll start a sentence and I don't even know where it's going. I just hope I find it along the way.".format(message)
            await client.send_message(message.channel, msg)
#16 
    elif 'wedding' in message.content.lower():
            msg = "Webster's dictionary defines wedding as: The fusing of two metals with a hot torch.".format(message)
            await client.send_message(message.channel, msg)
#17
    elif 'a solution' in message.content.lower():
            msg = "So, what is a solution? Solution is honesty, laughter, and comedy.".format(message)
            await client.send_message(message.channel, msg)
#18
    elif 'boss' in message.content.lower():
            msg = "Remember when people used to say 'boss' when they were describing something that was really cool? Like... 'Those shoulder pads are really boss, man.' 'Look at that perm. That perm is so boss.' It's what made me want to become a boss. And I looked so good in a perm and shoulder pads. But now, boss is just slang for 'jerk in charge.'".format(message)
            await client.send_message(message.channel, msg)
#19
    elif 'what to do' in message.content.lower():
            msg = "And I knew exactly what to do. But in a much more real sense, I had no idea what to do.".format(message)
            await client.send_message(message.channel, msg)
#20
    elif 'turtle' in message.content.lower():
            msg = "WHERE ARE THE TURTLES?!".format(message)
            await client.send_message(message.channel, msg)
#21
    elif 'responsibilities' in message.content.lower():
            msg = "I am running away from all my responsibilities, and it feels good.".format(message)
            await client.send_message(message.channel, msg)
#22
    elif "i'm sad" in message.content.lower():
            msg = "Society teaches us that having feelings and crying is bad and wrong. Well, that's baloney, because grief isn't wrong. There's such a thing as good grief, just ask Charlie Brown.".format(message)
            await client.send_message(message.channel, msg)
#23
    elif 'fool me' in message.content.lower():
            msg = "You know what they say, 'Fool me once, strike two, but fool me twice... strike three.'".format(message)
            await client.send_message(message.channel, msg)
#24
    elif 'to be liked' in message.content.lower():
            msg = "Do I need to be liked? Absolutely not. I like to be liked. I enjoy being liked. I have to be liked. But it's not like this, compulsive need to be liked, like my need to be praised.".format(message)
            await client.send_message(message.channel, msg)
#25
    elif 'christmas' in message.content.lower():
            msg = "Well, happy birthday Jesus, sorry that your party's so lame.".format(message)
            await client.send_message(message.channel, msg)
#26
    elif 'username' in message.content.lower():
            msg = "I need a username, and... I have a great one. 'LittleKidLover'. That way people will know exactly where my priorities are at.".format(message)
            await client.send_message(message.channel, msg)
#27
    elif 'shots' in message.content.lower():
            msg = "'You miss 100% of the shots you don't take. -Wayne Gretsky' ~Michael Scott".format(message)
            await client.send_message(message.channel, msg)
#28
    elif 'alcohol' in message.content.lower():
            msg = "Do you think that doing alcohol is cool?!".format(message)
            await client.send_message(message.channel, msg)
#29
    elif 'inside jokes' in message.content.lower():
            msg = "I love inside jokes. Love to be a part of one someday.".format(message)
            await client.send_message(message.channel, msg)
#30
    elif 'i went to cornell' in message.content.lower():
            msg = "Isn't that the place that Andy is always talking about?".format(message)
            await client.send_message(message.channel, msg)
#31
    elif 'about downsizing' in message.content.lower():
            msg = "No, I'm not going to tell them about downsizing. If a patient has cancer, you don't tell them.".format(message)
            await client.send_message(message.channel, msg)
#32
    elif 'forward' in message.content.lower():
            msg = "I don't come up with this stuff, I just pass it along. You wouldn't arrest a guy who was just passing drugs from one guy to another.".format(message)
            await client.send_message(message.channel, msg)
#33
    elif 'pam' in message.content.lower():
            msg = "This is our receptionist, Pam. If you think she's cute now you should have seen her a couple years ago. Rawr!".format(message)
            await client.send_message(message.channel, msg)
#34
    elif 'mexican' in message.content.lower():
            msg = "Is there something besides 'mexican' that you prefer to be called? Something less offensive?".format(message)
            await client.send_message(message.channel, msg)
#35
    elif 'reason' in message.content.lower():
            msg = "Don't ever, for any reason, do anything for anyone, for any reason, ever, no matter what. No matter where. Or who, or who you are with, or where you are going or... or where you've been... ever. For any reason, whatsoever.".format(message)
            await client.send_message(message.channel, msg)
#36
    elif 'patrick' in message.content.lower():
            msg = "It is St. Patricks Day... it is the closest that the Irish will ever get to Christmas.".format(message)
            await client.send_message(message.channel, msg)
#37
    elif 'martin luther' in message.content.lower():
            msg = "I don't understand. We have a day honoring Martin Luther King, but he didn't even work here.".format(message)
            await client.send_message(message.channel, msg)
#38
    elif 'tables turn' in message.content.lower():
            msg = "Well, well, well, how the turntables.".format(message)
            await client.send_message(message.channel, msg)
#39
    elif 'gay' in message.content.lower():
            msg = "We're all homos. Homo... Sapiens.".format(message)
            await client.send_message(message.channel, msg)
#40
    elif 'jim' in message.content.lower():
            msg = "Jim and I are great friends. We hang out a ton, mostly at work.".format(message)
            await client.send_message(message.channel, msg)
#41
    elif 'morning' in message.content.lower():
            msg = "I enjoy having breakfast in bed. I like waking up to the smell of bacon, sue me. And since I don't have a butler, I do it myself. So most nights before I go to bed, I will lay six strips of bacon out on my George Foreman Grill. Then I go to sleep. When I wake up, I plug in the grill, I go back to sleep again. Then I wake up to the smell of crackling bacon.".format(message)
            await client.send_message(message.channel, msg)
#42
    elif "pam's art" in message.content.lower():
            msg = "It is a message. It is an inspiration. It is... a source of beauty. And without paper... it could not have happened. Unless you had a camera.".format(message)
            await client.send_message(message.channel, msg)
#43
    elif 'magic' in message.content.lower():
            msg = "A lot of people think that magic camp is just for kids. And that's why a lot of other people in my class were kids.".format(message)
            await client.send_message(message.channel, msg)
#44
    elif 'the office' in message.content.lower():
            msg = "The world sends people your way. Ryan came to me through a temp agency, Andy was transferred here. No idea where Creed came from. The point is, you just have to play with the cards that you're dealt. Jim, that guy is an Ace, Dwight is the king up my sleeve, Phyllis is my old maid, Oscar is my queen. That's easy, give me a hard one. That's what Oscar said. Toby is the instruction card you throw away, Pam is a solid seven, and yeah, you know what? Ryan is probably like a two. But twos can be wild, so watch out. And I am obviously the joker, so...".format(message)
            await client.send_message(message.channel, msg)
#45
    elif 'to cry' in message.content.lower():
            msg = "I feel like I am going to cry. I feel like it, but I am not going to.".format(message)
            await client.send_message(message.channel, msg)
#46
    elif 'jan' in message.content.lower():
            msg = "A gentleman does not kiss and tell. And neither do I.".format(message)
            await client.send_message(message.channel, msg)
#47
    elif 'wikipedia' in message.content.lower():
            msg = "Wikipedia is the best thing ever. Anyone in the world can write anything they want about any subject, so you know that you are getting the best possible information.".format(message)
            await client.send_message(message.channel, msg)
#48
    elif 'meeting' in message.content.lower():
            msg = "Tactic number six, change the location of the meeting at the last second. Totally throws them off.".format(message)
            await client.send_message(message.channel, msg)
#49
    elif 'to speak' in message.content.lower():
            msg = "Number fourteen, declining to speak first. Makes them uncomfortable, puts you in control.".format(message)
            await client.send_message(message.channel, msg)
#50
    elif 'clothes' in message.content.lower():
            msg = "There were these huge bins of clothes, and everybody was rifling through them like crazy, and I grabbed one. And it fit! So I don't think that this is totally just a women's suit. At the very least it's bisexual.".format(message)
            await client.send_message(message.channel, msg)
#51
    elif 'radio' in message.content.lower():
            msg = "Don't ever touch a black man's radio!".format(message)
            await client.send_message(message.channel, msg)
#52
    elif 'phrase' in message.content.lower():
            msg = "Bippity Boppity give me the Zoppity.".format(message)
            await client.send_message(message.channel, msg)
#53
    elif 'pen' in message.content.lower():
            msg = "Why don't you just take that pen and stab me in the heart.".format(message)
            await client.send_message(message.channel, msg)
#54
    elif 'negotiation' in message.content.lower():
            msg = "Negotiation is an art. Back and forth, give and take. And today, both Darryl and I took something. Higher Salaries. Win, win, win. But you know, life is about more than just salary, it's about... perks.".format(message)
            await client.send_message(message.channel, msg)
#55
    elif 'baler' in message.content.lower():
            msg = "Bale'er? I hardly know her!".format(message)
            await client.send_message(message.channel, msg)
#56
    elif 'has the floor' in message.content.lower():
            msg = "Toby now has the floor and he is going to try not to screw this up, like everything else in his life.".format(message)
            await client.send_message(message.channel, msg)
#57
    elif 'conference room' in message.content.lower():
            msg = "All right, you know what? That's it. @everyone Conference room, five minutes.".format(message)
            await client.send_message(message.channel, msg)
#58
    elif 'appreciate women' in message.content.lower():
            msg = "Michael, how can you appreciate women so much but also dump one of them? You mean, how can I be so illogical, and flighty, and unpredictable, and emotional? Well, maybe I learned something from women after all.".format(message)
            await client.send_message(message.channel, msg)
#59
    elif 'katy' in message.content.lower():
            msg = "You're the new and improved Pam. Pam six-point-oh.".format(message)
            await client.send_message(message.channel, msg)
#60
    elif 'regional manager' in message.content.lower():
            msg = "I'm Michael Scott, regional manager at Dunder-Mifflin Scranton.".format(message)
            await client.send_message(message.channel, msg)
#61
    elif "chili's" in message.content.lower():
            msg = "Chili's babyback ribs...".format(message)
            await client.send_message(message.channel, msg)
#62
    elif '*punch*' in message.content.lower():
            msg = "Faaaaaaaaaaaaaaaaaaaaaa-".format(message)
            await client.send_message(message.channel, msg)
#63
    elif 'improv' in message.content.lower():
            msg = "Boom! Detective Michael Scott! I'm with the FBI!".format(message)
            await client.send_message(message.channel, msg)
#64
    elif 'the discord' in message.content.lower():
            msg = "I am going nowhere. This place is like... the hospital, where I was born. My house, my old age home, and my graveyard, for my bones.".format(message)
            await client.send_message(message.channel, msg)
#65
    elif 'shot dwight' in message.content.lower():
            msg = "No, that is not funny. I love my employees. Even though I hit one of you with my car. For which, I take full responsibility.".format(message)
            await client.send_message(message.channel, msg)
#66
    elif 'flaws' in message.content.lower():
            msg = "Guess what, I have flaws. What are they? Oh, I don't know. I sing in the shower. Sometimes I spend too much time volunteering. Occasionally I'll hit somebody with my car. So sue me.".format(message)
            await client.send_message(message.channel, msg)
#67
    elif 'cat died' in message.content.lower():
            msg = "Sprinkles? *Sighs.* Oh sh.... I'm sorry, Angela. Man, what a day, huh? How could it get any worse?".format(message)
            await client.send_message(message.channel, msg)
#68
    elif 'the curse' in message.content.lower():
            msg = "Oh, I am taking responsibility. And it is up to me get rid of the curse that hit Meredith with my car. I'm not superstitious, but... I-I am a little stitious.".format(message)
            await client.send_message(message.channel, msg)
#69
    elif 'religion' in message.content.lower():
            msg = "I would like now to talk about each of your religious beliefs. Satan is a master of lies. Everything he says is the opposite. All right, let's just go around the room and-and tell me what you believe in.".format(message)
            await client.send_message(message.channel, msg)
#70           
    elif 'a god' in message.content.lower():
            msg = "Is there a god? If not, then what are all these churches for? And who is Jesus's dad?".format(message)
            await client.send_message(message.channel, msg)
#71
    elif 'rabies' in message.content.lower():
            msg = "A woman shouldn't have to be hit by a car, to learn that she may have rabies. But that is where we are in America. And that does not sit right with me. And that is why I am hosting a Fun Run Race for the Cure for Rabies--to raise awareness of the fact that there is a cure for rabies. A disease that has largely been eradicated in the U.S. But not very many people know that.".format(message)
            await client.send_message(message.channel, msg)
#72
    elif "i'm fat" in message.content.lower():
            msg = "I know that you're probably scared of someone seeing your fat legs in shorts. Well, back in olden times, a large, fat person like this was a person of power. A person who had money, who could buy food, a person of respect, like the regional manager of the day. Whereas someone athletic and trim like myself was somebody who worked in the fields, and I was a peasant. ".format(message)
            await client.send_message(message.channel, msg)
#73
    elif 'olden times' in message.content.lower():
            msg = "It is not olden times anymore.".format(message)
            await client.send_message(message.channel, msg)
#74
    elif 'naked' in message.content.lower():
            msg = "European offices are naked all the time. Besides, my shirttail covered most of it, so-".format(message)
            await client.send_message(message.channel, msg)
#75
    elif 'where it ended' in message.content.lower():
            msg = "That's not gross! It is the human body. What is your problem? Pam, you're an artist, right? Think of me as one of your models.".format(message)
            await client.send_message(message.channel, msg)
#76
    elif 'stretching' in message.content.lower():
            msg = "Check that out. *Look at me, I'm Toby! I'm stretching. I know what I'm doing.* Why is he even here?".format(message)
            await client.send_message(message.channel, msg)
#77
    elif 'myth' in message.content.lower():
            msg = "Myth: three Americans every year die from rabies. Fact: four Americans every year die from rabies. How many of you, know someone who has been afflicted or affected by rabies?".format(message)
            await client.send_message(message.channel, msg)
#78
    elif 'fast' in message.content.lower():
            msg = "I'm fast. I'm very fast. I'm like Forest Gump. Except, I am not an idiot.".format(message)
            await client.send_message(message.channel, msg)
#79
    elif 'water' in message.content.lower():
            msg = "No, no water for me. Not while rabies causes fear of water. Solidarity!".format(message)
            await client.send_message(message.channel, msg)
#80
    elif 'i know you michael' in message.content.lower():
            msg = "You don't--You don't know me. You've just seen my penis.".format(message)
            await client.send_message(message.channel, msg)
#81
    elif 'ryan' in message.content.lower():
            msg = "Yeah, Ryan snapped at me. But there was this twinkle in his eye that I picked up on which said, 'Dude, we're friends. I'm doing this for appearances. I am the big boss now. And I have to seem like an ogre. But you know me and you trust me. And we like each other. And we'll always be friends. And I would never take you for granted in a million years. And I miss you, man. And I love you.' His words.".format(message)
            await client.send_message(message.channel, msg)
#82
    elif 'ageism' in message.content.lower():
            msg = "What is that word?".format(message)
            await client.send_message(message.channel, msg)
#83
    elif "can't do things" in message.content.lower():
            msg = "Ever since I was a kid, people have been telling me that I can't do things. You can't be on the team. You can't move on to second grade. Well, now they're telling me that I can't win back clients using old fashioned business methods. We'll see about that. And FYI, I eventually aced second grade. And I was the biggest kid in class.".format(message)
            await client.send_message(message.channel, msg)
#84
    elif 'emily' in message.content.lower():
            msg = "She gonna be, like, 11... This winter? Wow, they grow up so fast. I have a few of my own that I want someday.".format(message)
            await client.send_message(message.channel, msg)
#85
    elif 'gift basket' in message.content.lower():
            msg = "Don't let Emily have any of the Cajun almonds, she's allergic.".format(message)
            await client.send_message(message.channel, msg)
#86
    elif 'technology' in message.content.lower():
            msg = "May I have your attention, please? This office will not be using an new technology ever, starting now. Ryan thinks that technology is the answer. Well, guess what? I just drove my car into a lake. I drove my car... into a [*bleep*]ing lake. Why, you may ask, did I do this? Well, because of a machine. A machine told me to drive into the lake. And I did it. I did it because I trusted Ryan's precious technology. And look where it got me.".format(message)
            await client.send_message(message.channel, msg)
#87
    elif 'game over' in message.content.lower():
            msg = "Game, set, match. Point. Scott. Game over. End of game.".format(message)
            await client.send_message(message.channel, msg)
#88
    elif 'witness protection' in message.content.lower():
            msg = "I always wanted to be in the Witness Protection program. Fresh start: no debts, no baggage. I've already got my name picked out: 'Lord Rupert Everton.' I'm a, uh a shipping merchant who raises fancy dogs. That's the life.".format(message)
            await client.send_message(message.channel, msg)
#89
    elif 'money problem' in message.content.lower():
            msg = "I, declare, bankruptcy!!!".format(message)
            await client.send_message(message.channel, msg)
#90
    elif 'debt consolidator' in message.content.lower():
            msg = "No. No. We are going to leave Jan out of this. We will find another way. We'll ask powerpoint.".format(message)
            await client.send_message(message.channel, msg)
#91
    elif 'presentation tool' in message.content.lower():
            msg = "You're a presentation tool... if you think I'm going to tell Jan about this.".format(message)
            await client.send_message(message.channel, msg)
#92
    elif 'you know that' in message.content.lower():
            msg = "I don't know that.".format(message)
            await client.send_message(message.channel, msg)
#93
    elif 'not that bad' in message.content.lower():
            msg = "Yeah it is. It is. I really messed up.".format(message)
            await client.send_message(message.channel, msg)
#94
    elif 'where is this train taking us' in message.content.lower():
            msg = "I don't--I think the engineer left.".format(message)
            await client.send_message(message.channel, msg)
#95
    elif 'dancing babies' in message.content.lower():
            msg = "Dancing babies. I love it!".format(message)
            await client.send_message(message.channel, msg)
#96
    elif 'paper' in message.content.lower():
            msg = "We can't overestimate the value of computers. Yes, they are great for playing games and forwarding funny emails. But real business is done on paper. Okay? Write that down.".format(message)
            await client.send_message(message.channel, msg)
#97
    elif 'dunder mifflin ad' in message.content.lower():
            msg = "Little girl in a field holding a flower. We zoom back to find that she's in the desert and the field is an oasis. We zoom back further. The desert is a sandbox in the world's largest resort hotel. Zoom back further. The hotel is actually the playground of the world's largest prison.".format(message)
            await client.send_message(message.channel, msg)
#98
    elif 'not creative' in message.content.lower():
            msg = "All right, let me ask you this. Tell me if you think this is creative. When I was five... I imagined that there was such a thing as a unicorn. And this is before I had ever heard of one, or seen one. I just drew a picture of a horse that could fly over rainbows and had a huge spike in it's head. I was five. Five years old. couldn't even talk yet. ".format(message)
            await client.send_message(message.channel, msg)
#99
    elif 'dismissing the ad people' in message.content.lower():
            msg = "Yeah, I'm glad you called. Ryan is being a little bitch again. Listen, David. I would like to do this ad in-house. I want to use only the creativity that we have right here in the office. And I will send it to you tomorrow morning. Take a look at it. If you do not think that it's ready to air, send the ad agency back here and we'll do it on my dime. I am willing to stake my entire reputation on it.".format(message)
            await client.send_message(message.channel, msg)
#100
    elif "what's rap" in message.content.lower():
            msg = "OK, Darryl, wow. You need to learn a lot about your own culture. I'll make you a mix.".format(message)
            await client.send_message(message.channel, msg)
#101
    elif 'you hate' in message.content.lower():
            msg = "I don't hate it. I just don't like it at all. And it's terrible.".format(message)
            await client.send_message(message.channel, msg)
#102
    elif 'dunder mifflin' in message.content.lower():
            msg = "Limitless paper in a paperless world.".format(message)
            await client.send_message(message.channel, msg)
#103
    elif 'more money' in message.content.lower():
            msg = "Mo' money mo' problems Stanley, you of all people should know that.".format(message)
            await client.send_message(message.channel, msg)
#104
    elif 'is leaving' in message.content.lower():
            msg = "Wanted... Middle-aged black man with sass. Big butt. Bigger heart.".format(message)
            await client.send_message(message.channel, msg)
#105
    elif 'wilderness adventure retreat' in message.content.lower():
            msg = "Hey! Nobody cares. Nobody cares.".format(message)
            await client.send_message(message.channel, msg)
#106
    elif 'donating blood' in message.content.lower():
            msg = "How often can you actually donate blood? Your body only has a certain amount.".format(message)
            await client.send_message(message.channel, msg)
#107
    elif 'woods' in message.content.lower():
            msg = "Now, these woods are full of creatures that can sustain human life. Things like, uh, squirrels. A nice, juicy rabbit would be delicious.".format(message)
            await client.send_message(message.channel, msg)
#108
    elif 'civil' in message.content.lower():
            msg = "Man became civilized for a reason. He decided that he like to have food to have warmth and clothing and television and hamburgers and to walk upright. And to have a soft futon at the end of the day. He didn't want to have to struggle to survive. I don't need the woods. I have a nice wood desk. I don't need fresh air because I have the freshest air around: A.C. And I don't need wide open spaces.".format(message)
            await client.send_message(message.channel, msg)
#109
    elif 'in ten years' in message.content.lower():
            msg = "That's what I said. That's what she said! *Chewing loudly.*".format(message)
            await client.send_message(message.channel, msg)
#110
    elif 'what who said' in message.content.lower():
            msg = "I never know. I just say it. I say stuff like that, you know, to lighten the tension when things sort of get hard.".format(message)
            await client.send_message(message.channel, msg)
#111
    elif "that's what she said" in message.content.lower():
            msg = "*Snorting* Hey! Nice! Really good. Bravo, my young ward.".format(message)
            await client.send_message(message.channel, msg)
#112
    elif "boys club" in message.content.lower():
            msg = "Yeah, I hate that.".format(message)
            await client.send_message(message.channel, msg)
#113
    elif "million dollars" in message.content.lower():
            msg = "Man! That is a lot of guacamole. Lot of the green. Lotta green.".format(message)
            await client.send_message(message.channel, msg)
#114
    elif "as friends" in message.content.lower():
            msg = "I would love that.".format(message)
            await client.send_message(message.channel, msg)
#115
    elif "don't have plans" in message.content.lower():
            msg = "I think we should celebrate. How about you, Pam, mi casa--a little dinner, dancing, drinks? You said you didn't have plans. That's what you said.".format(message)
            await client.send_message(message.channel, msg)
#116
    elif "whatever you want" in message.content.lower():
            msg = "Whatever I want? It's never whatever I want. When I wanted to see *Stomp,* and you wanted to see *Wicked* what did we see? When I said that I wanted to have kids, and you said that you wanted me to have a vasectomy, what did I do? And then, when you said that you might want to have kids, and I wasn't so sure, who had the vasectomy reversed? And then when you said you definitely didn't want to have kids. Who had it reversed back? Snip, snap! Snip, snap! Snip, Snap! I did! You have no idea the physical toll that three vasectomies have on a person!".format(message)
            await client.send_message(message.channel, msg)
#117
    elif "have a kid" in message.content.lower():
            msg = "Do you mean it? You want to have a kid?".format(message)
            await client.send_message(message.channel, msg)
#118
    elif "friend who's single" in message.content.lower():
            msg = "Is she a dress-wearer or a pants-wearer? Could we share a rowboat? Could a rowboat support her? I think I'm being very clear what I'm asking. Would an average-sized rowboat support her without capsizing? It bothers me that you're not answering the question.".format(message)
            await client.send_message(message.channel, msg)
#119
    elif "meredith" in message.content.lower():
            msg = "Jim, it's not the horniness, okay? It's the loneliness.".format(message)
            await client.send_message(message.channel, msg)
#120
    elif "did i stutter" in message.content.lower():
            msg = ".....".format(message)
            await client.send_message(message.channel, msg)
#121
    elif "didn't seem like he was joking" in message.content.lower():
            msg = "Well, you don't get it. Because Stanley is a beautiful, sassy, powerful black man, and you're you. If you had any friends, you would understand. Friends joke with one another. 'Hey, um, you're poor.' 'Well, hey your mama's dead.' That's what friends do. It's--you're so white.".format(message)
            await client.send_message(message.channel, msg)
#123
    elif "stomach hurts" in message.content.lower():
            msg = "Well, sometimes my stomach hurts when you come into my office. So it's probably psychological.".format(message)
            await client.send_message(message.channel, msg)
#124
    elif "apologize to you" in message.content.lower():
            msg = "Friends do not need to apologize to friends, so we are cool.".format(message)
            await client.send_message(message.channel, msg)
#125
    elif "are you serious" in message.content.lower():
            msg = "I am serious. We are all serious.".format(message)
            await client.send_message(message.channel, msg)
#126
    elif "professional idiot" in message.content.lower():
            msg = "Hey, stop it! Okay, everybody out. Yeah, everybody except Stanley. I don't understand why you keep picking on me. You just do and I don't know why. So... please help me understand.".format(message)
            await client.send_message(message.channel, msg)
#127        
    elif 'stanley' in message.content.lower():
            msg = "Now this gentleman right here is the key to our urban vibe. Stanley is hilarious.".format(message)
            await client.send_message(message.channel, msg)
#128
    elif 'job fair' in message.content.lower():
            msg = "Today I'm headed over to the job fair at Valley View High school to find some new interns. Wanna get some fresh blood, uh, euthanize this place.".format(message)
            await client.send_message(message.channel, msg)
#129
    elif '*smooch*' in message.content.lower():
            msg = "Yeah, kiss her. Kiss her good.".format(message)
            await client.send_message(message.channel, msg)
#130
    elif "'s last day" in message.content.lower():
            msg = "Today is Toby Flenderson's last day. I couldn't sleep last night. I came in extra early. So much energy. There are certain days that you know you will remember for the rest of your life. And I just have a feeling that today is one of those days.".format(message)
            await client.send_message(message.channel, msg)
#131
    elif "not enough cash" in message.content.lower():
            msg = "Every year, my sweet, sweet grandmother sends me a check on my birthday for $50. And lately, she has been sending me, like, nine or ten checks a year. Uh, as Nana starts to--but I knew I should be saving it for something. I just didn't know what I should be saving it for. And then I had an awakening. Michael, buy a motorcycle. So I put the money in my shoe, and then I forgot about it until now.".format(message)
            await client.send_message(message.channel, msg)
#132
    elif "this is holly" in message.content.lower():
            msg = "Hi. Hi, yeah, right. Okay, well, they hired a female Toby. Good for the world. Thank you, God, for creating two of you. Here's how things work here. My job is to make the office fun. Your job is to make the office lame. And we have an eternal struggle, you and I. And only one of us can be the winner. Spoiler alert--I'm gonna win.".format(message)
            await client.send_message(message.channel, msg)
#133
    elif "someone doesn't like h.r." in message.content.lower():
            msg = "Yeah.".format(message)
            await client.send_message(message.channel, msg)
#134
    elif "what did you do to him" in message.content.lower():
            msg = "He tortured me... with his awfulness.".format(message)
            await client.send_message(message.channel, msg)
#135
    elif "h.r." in message.content.lower():
            msg = "Thanks to Toby, I have a very strong prejudice against human resources. I believe that the department is a breeding ground for monsters. What I failed to consider, though, is that not all monsters are bad. Like E.T. Is Holly our extraterrestrial? Maybe. Or maybe she's just an awesome woman from this planet.".format(message)
            await client.send_message(message.channel, msg)
#136
    elif "you don't love holly" in message.content.lower():
            msg = "I think I do.".format(message)
            await client.send_message(message.channel, msg)
#137
    elif "you just met her" in message.content.lower():
            msg = "Well, it was love at first sight. Actually, it was--no it was when I heard her voice. It was love at first see with my ears.".format(message)
            await client.send_message(message.channel, msg)
#138
    elif "it doesn't work like that" in message.content.lower():
            msg = "Well, you're not romantic.".format(message)
            await client.send_message(message.channel, msg)
#139
    elif "exit interview" in message.content.lower():
            msg = "I'll let you in on a little secret. I've been very much looking forward to this moment. Very, very much. I--I have been steeped in anticipation. Toby has been cruisin' for a bruisin' for 12 years, and I am now his cruise director. And my name is Captain Bruisin'.".format(message)
            await client.send_message(message.channel, msg)
#140
    elif "baker" in message.content.lower():
            msg = "Holly is sweet and simple. Like a lady baker. I would not be surprised to find out that she had worked in a bakery before coming here. She has that kind of warmth. I'm pretty sure she's baked on a professional level".format(message)
            await client.send_message(message.channel, msg)
#141
    elif "cool you hired kevin" in message.content.lower():
            msg = "Thanks.".format(message)
            await client.send_message(message.channel, msg)
#142
    elif "i'm toby" in message.content.lower():
            msg = "Why are you the way that you are? Honestly, everytime I try to do something fun or exciting, you make it not that way. I hate so much about the things that you choose to be.".format(message)
            await client.send_message(message.channel, msg)
#143
    elif "good luck" in message.content.lower():
            msg = "Hh, holly doesn't need luck, everyone that meets her instantly loves her.".format(message)
            await client.send_message(message.channel, msg)
#144
    elif "society" in message.content.lower():
            msg = "There is something wrong with society. Not me. If it's me, then society made me that way.".format(message)
            await client.send_message(message.channel, msg)
#145
    elif "got engaged" in message.content.lower():
            msg = "To be married? *Hug.*".format(message)
            await client.send_message(message.channel, msg)
#146
    elif "youtube" in message.content.lower():
            msg = "When I discovered Youtube, I didn't work for five days. I did nothing. I viewed *Cookie Monster Sings Chocolate Rain* about 1,000 times.".format(message)
            await client.send_message(message.channel, msg)
#147
    elif "what was the dilemma" in message.content.lower():
            msg = "To tell you or not. And I'm glad I did. I feel very, very good and 'catharctic.'".format(message)
            await client.send_message(message.channel, msg)
#148
    elif "told you so" in message.content.lower():
            msg = "How do you tell somebody that you care about deeply, 'I told you so'? Gently? With a rose? In a funny way, like it's a hilarious joke? Or do you just let it go because saying it would just make things worse? Probably the funny way.".format(message)
            await client.send_message(message.channel, msg)
#149
    elif "babies" in message.content.lower():
            msg = "I love babies. I think they are beautiful in all sorts of different ways. I try yo pick up and hold a baby every day, if possible, because it nourishes me. It feeds my soul. Babies are drawn to me. And I think it's because they see me as one of them. But cooler. And with my life put together a little bit. If a baby were president, there would be no taxes, there would be no war. There would be no government. And... Things could get terrible, and actually, probably, it would be a better screenplay idea than a serious suggestion.".format(message)
            await client.send_message(message.channel, msg)
#150
    elif "i'll bid on a hug" in message.content.lower():
            msg = "She's your wife, you idiot.".format(message)
            await client.send_message(message.channel, msg)
#151
    elif "i was raped" in message.content.lower():
            msg = "You cannot say 'I was raped' and expect all your problems to go away, Kelly. Not again. Don't keep doing that.".format(message)
            await client.send_message(message.channel, msg)
#152
    elif "guacamole" in message.content.lower():
            msg = "I can't tell you how much leftover guacamole I have ended up eating over the years. I don't even know why I make it in such great quantities.".format(message)
            await client.send_message(message.channel, msg)
#153
    elif "japan" in message.content.lower():
            msg = "In Japan, you must always commit suicide to avoid embarrassment.".format(message)
            await client.send_message(message.channel, msg)
#154
    elif "morocco" in message.content.lower():
            msg = "Did you know that in Morocco it is common to exchange a small gift when meeting somebody for the first time?".format(message)
            await client.send_message(message.channel, msg)
#155
    elif "italy" in message.content.lower():
            msg = "In Italy you must always wash your hands after going to the bathroom. This is considered to be polite.".format(message)
            await client.send_message(message.channel, msg)
#156
    elif "where you going?" in message.content.lower():
            msg = "To Can-a-da.".format(message)
            await client.send_message(message.channel, msg)
#157
    elif "what's respect" in message.content.lower():
            msg = "A boss that will not fire you even though you just tell him off right to his face over the phone--that's respect.".format(message)
            await client.send_message(message.channel, msg)
#158
    elif "toby works here again" in message.content.lower():
            msg = "NO! GOD! NO, GOD, PLEASE NO! NO! NO! NOOOOOO!".format(message)
            await client.send_message(message.channel, msg)
#159
    elif "without cause" in message.content.lower():
            msg = "I have cause. It is because I hate him.".format(message)
            await client.send_message(message.channel, msg)
#160
    elif "talk to toby and be friends" in message.content.lower():
            msg = "I tried. I tried. I tried to talk to Toby and be his friend, but that is like trying to be a friend with and evil... snail.".format(message)
            await client.send_message(message.channel, msg)
#161
    elif "men find me desirable" in message.content.lower():
            msg = "Yes. Sure they do Dwight.".format(message)
            await client.send_message(message.channel, msg)
#162
    elif "seems awfull mean" in message.content.lower():
            msg = "Sometimes the ends justify the mean".format(message)
            await client.send_message(message.channel, msg)
#163
    elif "silent killers" in message.content.lower():
            msg = "You are the silent killer. Go back to the annex.".format(message)
            await client.send_message(message.channel, msg)
#164
    elif "should we just do it then" in message.content.lower():
            msg = "We cannot do it then. Monthyl dental appointment. Soft teeth.".format(message)
            await client.send_message(message.channel, msg)
#165
    elif "i'm not an alcoholic" in message.content.lower():
            msg = "Yeah, obviously you are. Okay, everybody who thinks that Meredith is an alcoholic please raise your hands.".format(message)
            await client.send_message(message.channel, msg)
#166
    elif "did the best you could" in message.content.lower():
            msg = "Enabler. Enabler. Enabler. Enabler. Enabler. Enabler. It's Christmas and we are turning our back on somebody who's asking for help.".format(message)
            await client.send_message(message.channel, msg)
#167
    elif "sense of what that is" in message.content.lower():
            msg = "David, here it is. My philosophy is basically this. And this is something that I live by. And I always have, and I always will. Don't ever for any reason do anything to anyone for any reason, ever, no matter what. No matter wh--where, or who, or who you are with, or--or where you are going, or--or where you've been... ever... for any reason whatsoever.".format(message)
            await client.send_message(message.channel, msg)
#168
    elif "improv conversation" in message.content.lower():
            msg = "Improversation.".format(message)
            await client.send_message(message.channel, msg)
#169
    elif "tweed" in message.content.lower():
            msg = "I feel the need. The need for tweed.".format(message)
            await client.send_message(message.channel, msg)
#170
    elif "michael how are you" in message.content.lower():
            msg = "I'm good, how are you?".format(message)
            await client.send_message(message.channel, msg)
#171
    elif "fax" in message.content.lower():
            msg = "Fax? Why don't you just send it over on a dinosaur?".format(message)
            await client.send_message(message.channel, msg)
#172
    elif "this is important michael" in message.content.lower():
            msg = "Oh, well, then E-mail it David.".format(message)
            await client.send_message(message.channel, msg)
#173
    elif "denny's" in message.content.lower():
            msg = "No, I never said Denny's. IHOP. IHOP. We're going to IHOP.".format(message)
            await client.send_message(message.channel, msg)
#174
    elif "you'll fall in love with her" in message.content.lower():
            msg = "Yeah, so what if I did? That would take precedence, and I would expect your support.".format(message)
            await client.send_message(message.channel, msg)
#175
    elif "i'll have a cup of coffee" in message.content.lower():
            msg = "You will have pancakes, and you'll like it.".format(message)
            await client.send_message(message.channel, msg)
#176
    elif "vietnam" in message.content.lower():
            msg = "Ah, Vietnam, I hear it's lovely.".format(message)
            await client.send_message(message.channel, msg)
#177
    elif "what is your job" in message.content.lower():
            msg = "Laughter is my job. Tears are my game. Law is my profession.".format(message)
            await client.send_message(message.channel, msg)
#178
    elif "what's the procedure" in message.content.lower():
            msg = "Stay [bleep]ing calm!".format(message)
            await client.send_message(message.channel, msg)
#179
    elif "hilary swank" in message.content.lower():
            msg = "Oh, she's hot.".format(message)
            await client.send_message(message.channel, msg)
#180
    elif "biofeedback machine" in message.content.lower():
            msg = "I think that thing is on the fritz. Ah, Oscar. Would you reach over and touch his thing? That's what he said. Right, guys? 'Cause of gay.".format(message)
            await client.send_message(message.channel, msg)
#181
    elif "you're the killer" in message.content.lower():
            msg = "You never expect that you're the killer. It's a great twist. Great twist.".format(message)
            await client.send_message(message.channel, msg)
#182
    elif "perspective" in message.content.lower():
            msg = "You know, sometimes to get perspective I like to think about a spaceman on a star incredibly far away. And our problems don't matter to him because we're just a distant point of light. But he feels sorry for me. Because he has an incredibly powerful microscope and he can see my face.".format(message)
            await client.send_message(message.channel, msg)
#183
    elif "roast" in message.content.lower():
            msg = "Jim, you're 6' 11'' and you weigh 90 pounds. Gumby has a better body than you. Boom. Roasted. Dwight, you're a kiss-ass. Boom. Roasted. Pam, you failed art school. Boom. Roasted. Meredith, you've slept with so many guys, you're starting to look like one. Boom. Roasted. Kevin, I can't decide between a fat joke and a dumb joke. Boom. Roasted. Creed, your teeth called, your breath stinks. Boom. Roasted. Angela. Where's Angela? Well, there you are. I didn't see you behind that grain of rice. Boom. Roasted. Stanley, you crush your wife during sex and your heart sucks. Boom. Roasted. Oscar, you are--Oscar, you're gay. Andy, Cornell called. They think you suck. And you're gayer than Oscar. Boom. Roasted.".format(message)
            await client.send_message(message.channel, msg)
#184
    elif "honesty" in message.content.lower():
            msg = "I fear that people are afraid to be honest with me. Because I am their boss. I would rather that someone be honest with me than be a good worker. Than be a good... employee. Because if he was honest, I could say 'Hey, can you handle this job?' and he would say, 'I don't--no, I can't.' And then I would say, 'Well, then I'm not gonna hire you. No offense. You seem like a really nice guy. But you're not qualified. You admitted it yourself.' That's how it works.".format(message)
            await client.send_message(message.channel, msg)
#185
    elif "unique thing" in message.content.lower():
            msg = "I have an amazing mnemonic device by which I have now memorized all of your names. Shirty. Mole. Lazy eye. Mexico. Baldy. Sugar Boobs. Black Woman. I have taken a unique part of who you are, and I have used that to memorize your name. Baldy. Your head is bald. It is hairless. It is shiny. It is reflective. Like a mirror. 'M.' Your name is Mark.".format(message)
            await client.send_message(message.channel, msg)
#186
    elif "it's very insulting" in message.content.lower():
            msg = "But it works.".format(message)
            await client.send_message(message.channel, msg)
#187
    elif "my husband impregnated me" in message.content.lower():
            msg = "Oh, great.".format(message)
            await client.send_message(message.channel, msg)
#188
    elif "it's really sweet" in message.content.lower():
            msg = "No, it's really dorky. You were right the first time.".format(message)
            await client.send_message(message.channel, msg)
#189
    elif "remember holly" in message.content.lower():
            msg = "Blonde hair. Nice boobs. Not too big, not too small. She was the love of my life.".format(message)
            await client.send_message(message.channel, msg)
#190
    elif "tony" in message.content.lower():
            msg = "Man was he fat. So, so fat. Too fat. Big fat fatty.".format(message)
            await client.send_message(message.channel, msg)
#191
    elif "answer the door" in message.content.lower():
            msg = "I'm not gonna answer it it's the KGB!".format(message)
            await client.send_message(message.channel, msg)
#192
    elif "jelly beans" in message.content.lower():
            msg = "These are extraordinary jelly beans!".format(message)
            await client.send_message(message.channel, msg)
#193
    elif "these aren't announcements" in message.content.lower():
            msg = "Yes they are you just don't care about the information.".format(message)
            await client.send_message(message.channel, msg)
#194
    elif "no, it is not" in message.content.lower():
            msg = "No, it is not.".format(message)
            await client.send_message(message.channel, msg)
#195
    elif "okay, so we're on the same page, great" in message.content.lower():
            msg = "Okay, so we're on the same page, great.".format(message)
            await client.send_message(message.channel, msg)
#196
    elif "okay, michael" in message.content.lower():
            msg = "Okay, Michael...".format(message)
            await client.send_message(message.channel, msg)
#197
    elif "no, seriously" in message.content.lower():
            msg = "No, seriously.".format(message)
            await client.send_message(message.channel, msg)
#198
    elif "how old are you" in message.content.lower():
            msg = "How old are you?".format(message)
            await client.send_message(message.channel, msg)
#199
    elif "five-years-old" in message.content.lower():
            msg = "Five-years-old.".format(message)
            await client.send_message(message.channel, msg)
#200
    elif "im going to walk away" in message.content.lower():
            msg = "I'm going to walk away.".format(message)
            await client.send_message(message.channel, msg)
#201
    elif "paper in a furnace" in message.content.lower():
            msg = "If you put paper in a furnace do you know what would happen? You'd ruin it.".format(message)
            await client.send_message(message.channel, msg)
#202
    elif "15th anniversary" in message.content.lower():
            msg = "Cancelled my 15th anniversary party. Just pulled the rug out from under me. He said, 'No figs.' I've already bought them. And I don't have a place to store them. So I feel like I've been sort of boned. Did you talk to him about this? You've talked to him all day, obviously. Did you talk to him about this? Okay, then I don't get it. It doesn't make any sense to me. Because I thought in the new system, that I was supposed to talk to Charles, and then Charles was supposed to talk to you, then that will dilute any need for me to ever talk to you again. Clearly, that's what you wanted. 15 years... I've been here, and I have sacrificed a lot. I've put having a family on hold. And I've never gone hang-gliding. And I've never driven my car to the top of mount Washington. I don't understand, that after 15 years of service here, I have to get in the car and drive to New York in order to talk to you. That doesn't seem right to me. That doesn't seem fair. And I think... That I've earned more... than that. ".format(message)
            await client.send_message(message.channel, msg)
#203
    elif "i quit" in message.content.lower():
            msg = "You have no idea how high I can fly.".format(message)
            await client.send_message(message.channel, msg)
#204
    elif "the industry is in decline" in message.content.lower():
            msg = "I practically invented decline.".format(message)
            await client.send_message(message.channel, msg)
#205
    elif "no, michael" in message.content.lower():
            msg = "You know what? I had a great time at prom. And no-one said yes to that either.".format(message)
            await client.send_message(message.channel, msg)
#206
    elif "i had a real job" in message.content.lower():
            msg = "I want you to listen to me. Because I want to tell you the situation that we are both in right now. Okay? You quit your job. I quit my job. We both quit. Those are the facts. That's what happened. Now what are our choices right now? Because, you know what, kiddo? You quit. So what are our options? Well... We can start this paper company. We can try. Or that's it. That's our only option. Because we quit. Pam, I do my best work when people don't believe in me. I remember in High school, my math teacher told me I was gonna flunk out, and know what I did? The very next day, I went out, and I scored more goals than anyone in the history of the Hockey team. See what I mean? I thrive on this. I thrive on it. So I'm gonna go inside. I'm going to make some calls. I'm gonna get us an office space, and I'm going to show you why you joined this company, all right?".format(message)
            await client.send_message(message.channel, msg)
#207
    elif "average" in message.content.lower():
            msg = "My mom used to say that average people are the most special people in the world, and that's why God made so many.".format(message)
            await client.send_message(message.channel, msg)
#208
    elif "we don't have anything" in message.content.lower():
            msg = "Well, we should make a list. List's are good. Lists are good. Lists are good.".format(message)
            await client.send_message(message.channel, msg)
#209
    elif "keep your friends close" in message.content.lower():
            msg = "You know what they say. 'Keep your friends close.'".format(message)
            await client.send_message(message.channel, msg)
#210
    elif "charles" in message.content.lower():
            msg = "If I were you, Charles Miner, I would watch your step. Because the Michael Scott paper company is about to open a big old can of Whoop-ass on Dunder Mifflin. Actually, a six-pack. We're gonna open a six-pack of Whoop-ass.".format(message)
            await client.send_message(message.channel, msg)

    elif "britney" in message.content.lower():
            msg = "It's Britney, bitch.".format(message)
            await client.send_message(message.channel, msg)

    elif "hire" in message.content.lower():
            msg = "They always say that it is a mistake to hire your friends. And they are right. So I hired my best friends. And this is what I get?".format(message)
            await client.send_message(message.channel, msg)

    elif "corner idea" in message.content.lower():
            msg = "No, you're supposed to say 'Rock the house!'".format(message)
            await client.send_message(message.channel, msg)

    elif "dibs" in message.content.lower():
            msg = "You respect dibs don't you?".format(message)
            await client.send_message(message.channel, msg)

    elif "i'm not a barbarian" in message.content.lower():
            msg = "Good.".format(message)
            await client.send_message(message.channel, msg)

    elif "do you understand" in message.content.lower():
            msg = "I understand nothing.".format(message)
            await client.send_message(message.channel, msg)

    elif "buyout" in message.content.lower():
            msg = "These are our demands.".format(message)
            await client.send_message(message.channel, msg)

    elif "company cannot be worth" in message.content.lower():
            msg = "Our company is worth nothing. That's the difference between you and I. Business isn't about money to me, David. If tomorrow my company goes under, I will just start another paper company. And then another and another and another. I have no shortage of company names. These are our demands. This is what we want. Our balls are in your court.".format(message)
            await client.send_message(message.channel, msg)

    elif "who could it be" in message.content.lower():
            msg = "Someone is returning! He started his own company, and now he's back. Who could it be? I'll give you a hint. He is a man. A man you have missed with all your heart. A man who has ruined all other men for you. Who is it? Who is it? Who is it? It's Michael Scott.".format(message)
            await client.send_message(message.channel, msg)

    elif "stolen clients" in message.content.lower():
            msg = "Okay, Dwight, let me explain something to you. I set the rules and you follow them. Blindly. Okay? And if you have a problem with that, then you can talk to our complaint department. It's a trash can. ".format(message)
            await client.send_message(message.channel, msg)

    elif "in the wrong" in message.content.lower():
            msg = "No matter how I look at this, I am in the wrong. And I have looked at this thing, like, a hundred different ways. From my point of view, from their point of view... 98 others. And the bottom line, I am in the wrong. I'm the bad guy.".format(message)
            await client.send_message(message.channel, msg)

    elif "she can be shrill" in message.content.lower():
            msg = "Oh, wow! Whoa! Ho-ho, man! Wow. *Honey! I want you to bring the garbage out. 'Cause I'm not going to have sex with you unless you bring out the garbage.*".format(message)
            await client.send_message(message.channel, msg)

    elif "kevin, come" in message.content.lower():
            msg = "Kevin, stay.".format(message)
            await client.send_message(message.channel, msg)

    elif "is there a cookie" in message.content.lower():
            msg = "Mm hmm.".format(message)
            await client.send_message(message.channel, msg)

    elif "to work" in message.content.lower():
            msg = "Sorry, this is a no work-zone. please respect the Lei.".format(message)
            await client.send_message(message.channel, msg)

    elif "walls could talk" in message.content.lower():
            msg = "If these walls could talk, they would say, 'This is a magical place. You are safe here. We are talking walls. We're not going to eat you.'".format(message)
            await client.send_message(message.channel, msg)

    elif "left out" in message.content.lower():
            msg = "I hate, hate, hate being left out. Whether it's not being picked for a team or being picked for a team and then showing up and realizing that the team doesn't exist. Or that the sport doesn't exist. I should have known. Poopball?".format(message)
            await client.send_message(message.channel, msg)

    elif "out of the loop" in message.content.lower():
            msg = "Stanley's having an affair, did you hear?".format(message)
            await client.send_message(message.channel, msg)

    elif "untell something" in message.content.lower():
            msg = "You can't. You can't put words back in your mouth. What you can do is spread false gossip. So that people think that everything that's been said is untrue. Including Stanley is having an affair. It's like the end of 'Spartacus.' I have seen that movie a half-dozen times and I still don't know who the real Spartacus is. And that is what makes that movie a classic Whodunit.".format(message)
            await client.send_message(message.channel, msg)

    elif "what about jim" in message.content.lower():
            msg = "Jim is like Big Bird. He is tall and yellow and very nice. But would I put him in charge, no. I don't think so. He--Big Bird doesn't make the tough decisions. I--if I was going to put someone in charge, I would put Bert in charge. Or I would put one of the real grown-ups in charge, like Maria. Or Gordon, maybe.".format(message)
            await client.send_message(message.channel, msg)

    elif "you are responsible" in message.content.lower():
            msg = "I can't help but feel partially responsible.".format(message)
            await client.send_message(message.channel, msg)

    elif "i have an announcement" in message.content.lower():
            msg = "Whoa... do you have an announcement?".format(message)
            await client.send_message(message.channel, msg)

    elif "jimothy" in message.content.lower():
            msg = "Jimothy... to be fair, Jimothy, the--ah, that sounds weird. Are you okay with being called Jim?".format(message)
            await client.send_message(message.channel, msg)

    

@client.event
async def on_ready():
    print("Ready to get to work. That's what she said.")
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('')
